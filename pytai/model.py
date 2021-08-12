from enum import Enum
import sys
import importlib
import inspect

from pathlib import Path
from typing import Union, Any, Tuple
from collections import namedtuple

from .common import *
from . import utils


class Parser(object):
    ChildAttr = namedtuple("ParserChildAttr", "name value start_offset end_offset is_metavar is_array")
    ArrayAttr = namedtuple("ArrayAttr", "value start_offset end_offset")

    def __init__(self) -> None:
        pass
    

    def parse(self, path_file: Union[str, Path]) -> Any:
        """Parse the given file.
        
        Args:
            path_file:
                The path to the file to be parsed.
        
        Returns:
            A parser-specific object that can be used to iterate the internal structure of the
            file using get_children().
        """
        raise NotImplementedError("Inheriting classes must implement this method")

    def get_children(self, parent: Any) -> "Parser.ChildAttr":
        """An iterator over the name and value of the children of the given parent.
        
        Args:
            parent: 
                An object as returned by parse() or get_children()

        Returns:
            A generator serving tuples containing the:
             * Name of the child (str)
             * Value of the child (arbitrary object)
               The value can either be a parser-specific object representing a structure
               or an integral type such as a list, string, integer, enum etc.
             * Start and end offsets of the structure in the file
             * Whether the child is actually in the file or an inferred metavar. 
               An inferred metavar is a variable that does not exist as-is in the file, 
               but is somehow transformmed from an existing variable to provide a 
               user-friendly representation of the existing variable.
             * Whether the value is an array of values, each with their own offsets
        """
        raise NotImplementedError("Inheriting classes must implement this method")

    def get_item_description(self, item: Any) -> str:
        if isinstance(item, (bytes, bytearray)):
            return f"Byte Array (Length: {len(item)})"
        elif isinstance(item, str):
            return item
        elif isinstance(item, int):
            return f"{item} ({hex(item)})"
        elif isinstance(item, Enum):
            return item.name
        else:
            return ""

class KaitaiParser(Parser):

    def __init__(self, format: str) -> None:
        """Create a Kaitai Parser.
        
        Args:
            format:
                Format of the file.
                Must match a *.py file under "SUBFOLDER_FORMATS/SUBFOLDER_FORMATS".
        """
        super().__init__()

        try:
            import kaitaistruct
        except ImportError:
            sys.path.append(str(KAITAI_DIR.resolve()))
            #import kaitaistruct
            self.kaitaistruct = importlib.import_module("kaitaistruct")
            
        self._load_parser(format)

    def _load_parser(self, format: str) -> None:
        """Load and return a Kaitai parser matching the given Kaitai Struct language definition.
        
        Args:
            format:
                Format of the file.
                Must match a *.py file under "SUBFOLDER_FORMATS/SUBFOLDER_FORMATS".
        """
        try:
            format_dir = str(KAITAI_FORMAT_DIR.resolve())
            if format_dir not in sys.path:
                sys.path.append(format_dir)
            parser_module = importlib.import_module(f'..{SUBFOLDER_KAITAI}.{SUBFOLDER_FORMATS}.{format}', __name__)
            module_classes = [m[0] for m in inspect.getmembers(parser_module, inspect.isclass) if m[1].__module__ == parser_module.__name__]
            if len(module_classes) != 1:
                raise RuntimeError("Can't determine class name using introspection")
            main_class_name: str = module_classes[0]
        except (ImportError, RuntimeError):
            raise # TODO

        self.parser = getattr(parser_module, main_class_name)
        self.format = format

    def parse(self, path_file: Union[str, Path]) -> "KaitaiStruct":
        try:
            parsed_file = self.parser.from_file(path_file)
            parsed_file._read()
        except self.kaitaistruct.ValidationNotEqualError as e:
            raise PyTaiException(f"Can't parse file as '{self.format}': {str(e)}") from e
        except Exception:
            raise

        return parsed_file

    def get_children(self, parent: "KaitaiStruct") -> Parser.ChildAttr:
        if hasattr(parent, "SEQ_FIELDS"):
            for child in parent.SEQ_FIELDS:
                if not hasattr(parent, child):
                    continue
                debug_dict = getattr(parent, "_debug")
                value = getattr(parent, child)
                is_array = False
                if 'arr' in debug_dict[child]:
                    value = [Parser.ArrayAttr(v, debug_dict[child]['arr'][i]['start'], debug_dict[child]['arr'][i]['end']) for i, v in enumerate(value)]
                    is_array = True
                
                yield Parser.ChildAttr(name = child, value = value, start_offset = debug_dict[child]['start'], 
                                       end_offset = debug_dict[child]['end'], is_metavar = False, is_array = is_array)

        for name, value in utils.getproperties(parent):
            if value is not None:
                yield Parser.ChildAttr(name = name, value = value, start_offset = None, end_offset = None, is_metavar = True, is_array = False)
        



class Model(object):

    def __init__(self):
        self.parsers = {}

    def get_parser(self, **kwargs) -> Parser:
        """Return a parser to parse the required files.

        Keyword Args:
            kaitai_format:
                Path to a compiled Kaitai Structure definition 
                (*.py generated from *.ksy file).
                Given this parameter, the returned parser will be 
                a KaitaiParser instance.

        Returns:
            The appropriate parser based on the keyword args.       
        """
        if "kaitai_format" in kwargs:
            try:
                parser = self.parsers[kwargs["kaitai_format"]]
            except KeyError:
                parser = KaitaiParser(kwargs["kaitai_format"])
                self.parsers[kwargs["kaitai_format"]] = parser
            
            return parser
        
        raise RuntimeError("Can't identify appropriate parser type")

        


        