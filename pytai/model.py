from enum import Enum
import sys
import importlib
import inspect

from pathlib import Path
from typing import Union, Any, Tuple

from .common import *

class Parser(object):
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

    def get_children(self, parent: Any) -> Tuple[str, Any, int, int]:
        """An iterator over the name and value of the children of the given parent.
        
        Args:
            parent: 
                An object as returned by parse() or get_children()

        Returns:
            A generator serving tuples containing the name of the child (str),  
            the value of the child (arbitrary object) and the start and end offsets of
            the structure in the file.
            The value can either be a parser-specific object representing a structure
            or an integral type such as a list, string, integer, enum etc.
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
            #parser_module = importlib.import_module(f'..{SUBFOLDER_KAITAI}.{SUBFOLDER_FORMATS}.{format}', __name__)
            format_dir = str(KAITAI_FORMAT_DIR.resolve())
            if format_dir not in sys.path:
                sys.path.append(format_dir)
            parser_module = importlib.import_module(format)
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

    def get_children(self, parent: "KaitaiStruct") -> Tuple[str, Any, int, int]:
        if hasattr(parent, "SEQ_FIELDS"):
            for child in parent.SEQ_FIELDS:
                debug_dict = getattr(parent, "_debug")
                value = getattr(parent, child)
                if isinstance(value, list):
                    value = ((v, debug_dict[child]['arr'][i]['start'], debug_dict[child]['arr'][i]['end']) for i, v in enumerate(value))
                
                yield (child, value, debug_dict[child]['start'], debug_dict[child]['end'] )


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

        


        