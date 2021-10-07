"""The Model of the application, handling the file parsing via Kaitai.

License:
    MIT License

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
from enum import Enum
import sys
import importlib
import inspect

from pathlib import Path
from typing import Union, Any, Dict, Tuple
from collections import namedtuple
from contextlib import contextmanager

from .common import *
from . import utils

class PytaiUnparsedAccessException(Exception):
    """The parser tried to access an element that hasn't been parsed yet.
    
    This can happen when the file format defines cross-references between
    structures, i.e. one structure contains an element that isn't relative to 
    itself, but to another structure.

    Upon catching such an exception, the caller can choose to raise a flag
    and continue parsing the file. After proceeding with the parsing until the end,
    the caller can restart the parsing (if the flag is raised) in hope that that 
    the cross reference has been resolved (i.e. the referenced element has been parsed). 
    The caller should set a limit to the amount of reparse attempts.
    """

class Parser(object):
    ChildAttr = namedtuple("ParserChildAttr", "name value start_offset end_offset is_metavar is_array")

    def __init__(self) -> None:
        pass
    
    @contextmanager
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

        self.kaitaistruct = importlib.import_module(f"..{SUBFOLDER_KAITAI}.kaitaistruct", __name__)
            
        self._load_parser(format)

    def _load_parser(self, format: str) -> None:
        """Load and return a Kaitai parser matching the given Kaitai Struct language definition.
        
        Args:
            format:
                Format of the file.
                Must match a *.py file under "SUBFOLDER_KAITAI/SUBFOLDER_FORMATS".
        """
        try:
            format_dir = str(KAITAI_FORMAT_DIR.resolve())
            if format_dir not in sys.path:
                sys.path.append(format_dir)
            sys.modules['kaitaistruct'] = self.kaitaistruct

            class PseudoInt(int):
                def __new__(cls, x, data, *args, **kwargs):
                    instance = int.__new__(cls, x, *args, **kwargs)
                    instance.data = data
                    return instance

            class KaitaiStreamWrapper(self.kaitaistruct.KaitaiStream):
                def pos(self):
                    return PseudoInt(super().pos(), self)
            
            self.kaitaistruct.KaitaiStream = KaitaiStreamWrapper

            parser_module = importlib.import_module(f'..{SUBFOLDER_KAITAI}.{SUBFOLDER_FORMATS}.{format}', __name__)

            module_classes = [m[0] for m in inspect.getmembers(parser_module, inspect.isclass) if m[1].__module__ == parser_module.__name__]
            if len(module_classes) != 1:
                raise RuntimeError("Can't determine class name using introspection")
            main_class_name: str = module_classes[0]
        except (RuntimeError):
            raise # TODO Is there any other way to determine class name?

        self.parser = getattr(parser_module, main_class_name)
        self.format = format

    @contextmanager
    def parse(self, path_file: Union[str, Path]) -> "KaitaiStruct":
        parsed_file = None
        try:
            parsed_file = self.parser.from_file(path_file)
            parsed_file._read()
            parsed_file._io._base_offset = 0
            yield parsed_file
        except self.kaitaistruct.ValidationNotEqualError as e:
            raise PyTaiException(f"Can't parse file as '{self.format}': {str(e)}") from e
        except Exception:
            raise
        finally:
            if parsed_file is not None:
                parsed_file.close()

    def _has_relative_offset(self, obj: Any) -> bool:
        """Returns true if the object has a relative offset in the Kaitai _debug dictionary, false otherwise."""
        if not isinstance(obj, self.kaitaistruct.KaitaiStruct):
            return False
        return (obj._parent is None or obj._io != obj._parent._io)
        
    def _add_base_offset(self, value: Any, start_offset: int, base_offset: int) -> None:
        """Add the _base_offset attribute to a KaitaiStream based on whether the offset is relative or not."""
        if isinstance(value, self.kaitaistruct.KaitaiStruct) and not hasattr(value._io, "_base_offset"): 
            if not self._has_relative_offset(value):
                value._io._base_offset = base_offset
            else:
                value._io._base_offset = start_offset

    def _get_details(self, debug_dict: Dict[str, Dict[str, int]], parent: "KaitaiStruct", child_name: str, value: Any) -> Tuple[int, int, bool, Any]:
        """Extract some details about parent.child_name.
        
        Args:
            debug_dict: 
                Kaitai's _debug dictionary for the parent.

            parent:
               KaitaiStruct parent object. 

            child_name:
                Name of child attribute.

            value:
                Value of child as received from Kaitai.

        Returns:
            A tuple containing the following information:
                - Start offset: Start offset of the object as captured in the debug_dict.
                - End offset: End offset of the object as captured in the debug_dict.
                - Is array: True if the given object is in fact a list of objects.
                - Value: Value of the object. For arrays, will be expanded to a list of ParserChildAttr, 
                         otherwise same as value sent to it
            
        """
        start_offset = end_offset = None
        is_array = False
        
        try:
            base_offset = parent._io._base_offset

            # Note: debug_dict[child_name] might not exist
            start_offset = debug_dict[child_name]['start'] + debug_dict[child_name]['start'].data._base_offset 
            end_offset = debug_dict[child_name]['end'] + debug_dict[child_name]['end'].data._base_offset       

            real_value = getattr(parent, child_name)

            self._add_base_offset(real_value, start_offset, base_offset)
            
            if 'arr' in debug_dict[child_name]:
                new_value = []
                for i, v in enumerate(value):
                    self._add_base_offset(v, debug_dict[child_name]['arr'][i]['start'] + debug_dict[child_name]['start'].data._base_offset, base_offset)
                    new_value.append(Parser.ChildAttr(name = f"[{i}]",
                                                value = v, 
                                                start_offset = debug_dict[child_name]['arr'][i]['start'] + debug_dict[child_name]['start'].data._base_offset, 
                                                end_offset = debug_dict[child_name]['arr'][i]['end'] + debug_dict[child_name]['end'].data._base_offset, 
                                                is_metavar = False,
                                                is_array = False))
                value = new_value
                is_array = True
        except KeyError:
            pass
        except AttributeError:
            raise PytaiUnparsedAccessException(f"Unparsed access during parsing of '{child_name}' ")

        return start_offset, end_offset, is_array, value

    def get_children(self, parent: "KaitaiStruct") -> Parser.ChildAttr:
        if not isinstance(parent, self.kaitaistruct.KaitaiStruct):
            return

        debug_dict = getattr(parent, "_debug")

        for child in parent.SEQ_FIELDS:
            if not hasattr(parent, child):
                continue

            start_offset, end_offset, is_array, value = self._get_details(debug_dict, parent, child, getattr(parent, child))

            yield Parser.ChildAttr(name = child, value = value, start_offset = start_offset, 
                                    end_offset = end_offset, is_metavar = False, 
                                    is_array = is_array)

        for name, value in utils.getproperties(parent):
            if value is None:
                continue
            
            start_offset, end_offset, is_array, value = self._get_details(debug_dict, parent, f"_m_{name}", value)

            yield Parser.ChildAttr(name = name, value = value, start_offset = start_offset, 
                                   end_offset = end_offset, is_metavar = True, 
                                   is_array = is_array)


class Model(object):

    def __init__(self):
        self.parsers = {}

    def get_parser(self, **kwargs) -> Parser:
        """Return a parser to parse the required files.

        Keyword Args:
            kaitai_format:
                Path to a compiled Kaitai Structure definition 
                (*.py generated from *.ksy file), relative to KAITAI_FORMAT_DIR.
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

        


        