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
import mmap
import queue
import bisect

from pathlib import Path
from typing import Callable, Union, Any, Dict, Tuple, Generator, Optional
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

    def get_children(self, parent: Any) -> Generator[Optional["Parser.ChildAttr"], None, None]:
        """An iterator over the name and value of the children of the given parent.
        
        Args:
            parent: 
                An object as returned by parse() or get_children()

        Returns:
            A generator serving either: 
                (-) Tuples containing the:
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
                OR:
                (-) "None", which indicates that the currect child has some unresolved dependency.
                        * In such a case, the caller can choose to continue traversing the tree for the 
                        sake of resolving the dependency, while marking for itself that a subsequent traversal
                        will later be needed.
        """
        raise NotImplementedError("Inheriting classes must implement this method")

    def get_item_description(self, item: Any) -> str:
        if isinstance(item, (bytes, bytearray)):
            return f"Byte Array (Length: {len(item)})"
        elif isinstance(item, str):
            return item
        elif isinstance(item, int):
            return f"{item} ({hex(item)})"
        elif isinstance(item, float):
            return f"{item}"
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

        Raises:
            PytaiUnparsedAccessException:
                In case there is some cross-dependency between this child attribute and an unparsed section of the binary.
                This can happen when the current element references an element which hasn't been parsed yet.
            
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
            # data._base_offset doesn't exist - meaning the Kaitai Stream which this element is referring to hasn't been handled by this function yet.
            # This can happen in case of a cross-reference to a different stream.
            raise PytaiUnparsedAccessException(f"Unparsed access during parsing of '{child_name}' ")

        return start_offset, end_offset, is_array, value

    def get_children(self, parent: "KaitaiStruct") -> Generator[Optional[Parser.ChildAttr], None, None]:
        if not isinstance(parent, self.kaitaistruct.KaitaiStruct):
            return

        debug_dict = getattr(parent, "_debug")

        for child in parent.SEQ_FIELDS:
            if not hasattr(parent, child):
                continue

            try:
                start_offset, end_offset, is_array, value = self._get_details(debug_dict, parent, child, getattr(parent, child))

                yield Parser.ChildAttr(name = child, value = value, start_offset = start_offset, 
                                        end_offset = end_offset, is_metavar = False, 
                                        is_array = is_array)
            except PytaiUnparsedAccessException:
                yield None

        for name, value in utils.getproperties(parent):
            if value is None:
                continue
            
            try:
                start_offset, end_offset, is_array, value = self._get_details(debug_dict, parent, f"_m_{name}", value)

                yield Parser.ChildAttr(name = name, value = value, start_offset = start_offset, 
                                       end_offset = end_offset, is_metavar = True, 
                                       is_array = is_array)
            except PytaiUnparsedAccessException:
                yield None

class Model(object):

    def __init__(self):
        self.parsers = {}
        self.highlight_context = {ht: set() for ht in HighlightType if HighlightType.is_custom(ht)}

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

    def build_structure_tree(self, path_file: Union[str, Path], parser: Any, comm_queue: queue.Queue, abort_cb: Callable[[None], bool]) -> None:
        """Build the structure tree for the given file.

        This function is expected to run in a dedicated thread. 
        It communicates with the caller via a provided thread-safe queue.
        
        Args:
            path_file:
                Path to the file to be parsed.
            parser:
                A parser as returned by get_parser().
            comm_queue:
                A thread-safe queue to pass results to.
            abort_cb:
                A callback to determine if the function should abort.
        """

        try:
            with parser.parse(path_file) as parsed_file:
                NodeAttributes = namedtuple("NodeAttributes", "parent name value start_offset end_offset is_metavar is_array")

                # Build the structure tree by iterating the parsed file (BFS)

                # For some files, due to a cross-dependency, we might first try to process an element without processing its 
                # dependency. The solution is to raise a flag in such a case (reparse_needed), continue parsing the file
                # until the dependency is parsed, and then repeat the parsing process with the dependency already resolved.
                max_parse_retries = 5

                for retry_num in range(max_parse_retries):

                    reparse_needed = False

                    work_queue = []
            
                    work_queue.append(NodeAttributes(parent = None, name = 'root', value = parsed_file, start_offset = 0, end_offset = 0, 
                                                is_metavar = False, is_array = False))

                    i = 0
                    while work_queue:
                        if abort_cb():
                            break

                        node_attr = work_queue.pop(0)

                        if not reparse_needed:
                            comm_queue.put(dict(current = i, parent = node_attr.parent, name = node_attr.name, 
                                                            extra_info = parser.get_item_description(node_attr.value), 
                                                            start_offset = node_attr.start_offset, end_offset = node_attr.end_offset, 
                                                            is_metavar = node_attr.is_metavar))
                        # else: We're just parsing for the sake of resolved a dependency, no point in adding to the GUI

                        if node_attr.is_array:
                            values = node_attr.value
                        else:
                            values = parser.get_children(node_attr.value)

                        for child_attr in values:
                            if child_attr is not None:
                                work_queue.append( NodeAttributes(parent = i, name = child_attr.name, value = child_attr.value, 
                                                        start_offset = child_attr.start_offset, 
                                                        end_offset = child_attr.end_offset, 
                                                        is_metavar = child_attr.is_metavar, is_array = child_attr.is_array) )
                            else:
                                # There is some unresolved dependency which should be resolved later
                                reparse_needed = True
                        i += 1

                    if not reparse_needed or abort_cb():
                        # We are done
                        comm_queue.put(None)
                        break
                    else:
                        # We need to reparse, so empty the GUI queue and try again
                        try:
                            while True:
                                comm_queue.get_nowait()
                        except queue.Empty:
                            pass
                        comm_queue.put(PyTaiReparseException(f"Reparse Needed, attempt #{retry_num}"))
                else:
                    raise PyTaiException("Unable to parse file!")

        except PyTaiException as e:
            comm_queue.put(e)
        except Exception as e:
            comm_queue.put(PyTaiException(f"Error while parsing file:\n'{str(e)}'"))

    def get_byte_range(self, mmap: mmap.mmap, start_offset: int, end_offset: int, byte_representation: ByteRepresentation):
        """Retrieve a byte range according to a given representation

        This function returns the byte array in the given range formatted according to the given
        representation.
        
        Args:
            mmap:
                Memory map of the file to extract the byte array from.
            start_offset:
                Start offset of the given range.
            end_offset:
                End offset of the given range.
            byte_representation:
                The byte representation to return.
        """
        if byte_representation == ByteRepresentation.HEX_STREAM:
            return mmap[start_offset:end_offset].hex()
        elif byte_representation == ByteRepresentation.HEX:
            return mmap[start_offset:end_offset].hex(" ")
        elif byte_representation == ByteRepresentation.RAW_BYTES:
            return mmap[start_offset:end_offset]

    @staticmethod    
    def _s1_contains_s2(s1: Tuple[int, int], s2: Tuple[int, int]):
        """Returns whether the range in s1 is contained withing the range in s2"""
        return s1[0] <= s2[0] and s1[1] >= s2[1]
        
    def process_highlight(self, start_offset: int, end_offset: int, mark: bool, highlight_type: HighlightType) -> bool:       
        """Handle a highlight/un-highlight request.

        If the request is to highlight a range:
            Iterate all existing highlighted ranges. 
            If the requested range is already within a previously-highlighted range: Nothing to do.
            If the requested range contains a previously-highlighted range: Remove the old one in 
            favor of the new one.
            If the requested range does not overlap an existing range: Just add the new one.
        If the request is to remove a range:
            Just remove it, since we make sure during addition that there's no overlap between
            added ranges.

        Args:
            start_offset:
                The start offset for the requested range.

            end_offset:
                The end offset for the requested range.

            mark:
                True if the request is to highlight the range, False to un-highlight

            highlight_type:
                The highlight type

        Returns:
            False if no action was needed, True otherwise.
        
        """
        this_segment = (start_offset, end_offset)
        if mark:
            new_set = set()
            for segment in self.highlight_context[highlight_type]:
                if self._s1_contains_s2(segment, this_segment):
                    return False
                elif not self._s1_contains_s2(this_segment, segment):
                    new_set.add(segment)
            new_set.add(this_segment)
            self.highlight_context[highlight_type] = new_set
            return True
        else:
            res = this_segment in self.highlight_context[highlight_type]
            if res:
                self.highlight_context[highlight_type].remove(this_segment)
            return res

    def get_highlighted_colors(self, start_offset: int, end_offset: int) -> Dict[HighlightType, HighlightDetails]:
        """Return the highlighted colors for the given range.

        Args:
            start_offset:
                The start offset for the requested range.

            end_offset:
                The end offset for the requested range

        Returns:
            A mapping between highlight types and the following information:
                - Whether the given highlighter is active for the range
                - If it is active, whether the range was explicitly highlighted itself,
                  or whether it is highlighted as a result of being included in a larger
                  highlighted range.

        """
        res = {}
        this_segment = (start_offset, end_offset)
        for ht in HighlightType:
            if not HighlightType.is_custom(ht):
                continue
            
            is_active = False
            is_exact_match = False

            for segment in self.highlight_context[ht]:
                if segment == this_segment:
                    is_active = True
                    is_exact_match = True
                    break
                elif self._s1_contains_s2(segment, this_segment):
                    is_active = True
                    break
            
            res[ht] = HighlightDetails(is_active = is_active, is_exact_match = is_exact_match)
        return res
    
        
class SearchContext(object):
    """Context for searching within a given binary.
    
    Supports a single search term and allows searching forward and backwards for it.
    The context remembers the previous occurrance of the term and the next search request
    continues from the previous one.
    """
    def __init__(self, mmap: mmap.mmap, term: bytes):
        """Instansiate the object.

        Args:
            mmap:
                Memory mapped object representing the binary.

            term:
                Search term for this context.(as bytes)
        
        """
        self._mmap = mmap
        self._mmap_len = len(mmap)
        self._offset = -1
        self._term = term

    def find_next(self, reverse: bool = False) -> int:
        """Find the next occurrence of the term (forwards or backwards).
        
        Args:
            reverse:
                True if the request is to search backwards.
        
        Returns:
            The offset of the next term in the binary, or -1 if not found.
        """
        if not reverse:
            self._offset = self._mmap.find(self.term, self._offset + 1)
        else:
            end = self._offset if self._offset >= 0 else self._mmap_len
            self._offset = self._mmap.rfind(self.term, 0, end + len(self.term) - 1)
        
        return self._offset

    @property
    def term(self) -> str:
        """The given search term."""
        return self._term

    
class XRefManager(object):
    """Class to manage cross-referencing: From a hex offset in the file to a structure."""

    XRefAttr = namedtuple("XRefAttr", "start_offset end_offset tree_handle")

    def __init__(self) -> None:
        self.xref_offset_map = []
        self.xref_offset_map_start = []

    def add_range(self, start_offset: int, end_offset: int, tree_handle: Any) -> None:
        """Register a range of (start, end) to a given tree handle.
        
        Args:
            start_offset:
                Start offset of the range.
            end_offset:
                End offset of the range.
            tree_handle:
                Handle in the structure tree which can later be used to mark the structure
                associated with the given offset
        """
        self.xref_offset_map.append(self.XRefAttr(start_offset, end_offset, tree_handle))

    def finalize(self) -> None:
        """Perform any post-processing needed after all ranges have been added."""
        self.xref_offset_map.sort()
        self.xref_offset_map_start = [x.start_offset for x in self.xref_offset_map]

    def get_xref_handle(self, offset: int) -> Optional[Any]:
        """Given an offset, return the tree handle for the inner-most range to which the offset belongs to.
        
        Args:
            offset:
                An offset in the binary.

        Returns:
            A tree handle associated with the inner-most (deepest) range containing the offset, or None if 
            no such range was found.
        """

        # Example: 
        # [(0, 100, h1), (0, 10, h2), (10, 15, h4), (10, 20, h3), (15, 20, h5), (20, 100, h6)]
        # We will search for offset 12.
        
        # Get the index of the tuple to the right of the right-most tuple which has a start offset
        # under the given offset. In the example: 4 [(15, 20, h5)].
        index = bisect.bisect_right(self.xref_offset_map_start, offset)

        match = None
        
        try:
            # Move left to the right-most tuple which has a start offset under the given offset.
            # Int the example: 3 [(10, 20, h3)].
            index -= 1
            start_offset = self.xref_offset_map[index].start_offset
        except IndexError:
            return

        while index >= 0:
            # Continue moving left while the start offset is equal and the end offset is after the given offset.
            # In the example: Stop at 2 [(10, 15, h4)]. This is the inner-most (deepest) structure for 12.
            t = self.xref_offset_map[index]
            if t.start_offset == start_offset and offset <= t.end_offset and t.start_offset != t.end_offset:
                match = t
                index -= 1
            else:
                break

        if match is not None:
            assert(match.start_offset <= offset <= match.end_offset)

        return match.tree_handle if match is not None else None