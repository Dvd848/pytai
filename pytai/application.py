"""The 'Controller' module, connecting between the 'View' and 'Model'.

The application module acts as the 'Controller' and is responsible for
connecting between the 'View' and the 'Model' in the MVC pattern.

It receives user-triggered events from the View via callbacks, translates
them to operations which need to be performed by the Model, and updates
the View when the operations are completed.

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
from pathlib import Path
from collections import namedtuple
from typing import Union, Dict, Optional

from . import view as v
from . import model as m

from . import utils

from .common import *

class Application():
    def __init__(self, file: Optional[str], format: Dict[str, Optional[str]], *args, **kwargs):

        # These callbacks are used to notify the application
        #  of events from the view
        callbacks = {
            v.Events.REFRESH:             self.cb_refresh,
            v.Events.STRUCTURE_SELECTED:  self.cb_structure_selected,
            v.Events.GOTO:                self.cb_goto,
            v.Events.OPEN:                self.cb_open,
            v.Events.GET_CWD:             self.cb_get_cwd,
        }

        self.current_file_path = None
        self.format = None

        self.view = v.View(title = "pytai", callbacks = callbacks)
        self.model = m.Model()

        if (file is not None):
            self.populate_view(file, format)

    def run(self) -> None:
        """Runs the application."""
        self.view.mainloop()

    def populate_view(self, path_file: Union[str, Path], format: Dict[str, str]) -> None:
        """Populates the View for the given file.
        
        Args:
            path_file:
                Path to the file to be parsed.
            format:
                Dictionary containing the type of format to use for parsing the file.
                The file will be parsed based on the format type.
                Dictionary should contain one of the following pairs:
                    (-) kaitai_format -> Name of Kaitai format module from format folder
        """
        with utils.memory_map(path_file) as f:
            self.view.populate_hex_view(f)
        self._populate_structure_tree(path_file, format)

    def _populate_structure_tree(self, path_file: Union[str, Path], format: Dict[str, str]) -> None:
        """Populates the View's structure tree for the given file.
        
        Args:
            path_file:
                Path to the file to be parsed.
            format:
                See description under populate_view().
        """

        self.current_file_path = path_file
        self.format = format

        try:
            parser = self.model.get_parser(**format)
            with parser.parse(self.current_file_path) as parsed_file:

                # W/A for Kaitai struct behavior:
                # In some cases (e.g. if of the structures within a Kaitai struct is imported), Kaitai will populate
                # the debug offsets with a relative value to the internal struct instead of an absolute value from the start
                # of the external structure.
                # We rely on the offset to highlight the selected bytes in the hex view, and can't use relative offsets.
                # Therefore, as a W/A, we're currently maintaining an "add_offset" variable to transform a relative offset into
                # an absolute one.

                NodeAttributes = namedtuple("NodeAttributes", "parent name value start_offset end_offset is_metavar is_array add_offset")

                # Build the structure tree by iterating the parsed file (BFS)

                queue = []
        
                queue.append(NodeAttributes(parent = '', name = 'root', value = parsed_file, start_offset = 0, end_offset = 0, 
                                            is_metavar = False, is_array = False, add_offset = 0))
        
                while queue:
                    node_attr = queue.pop(0)

                    handle = self.view.add_tree_item(node_attr.parent, name = node_attr.name, 
                                                    extra_info = parser.get_item_description(node_attr.value), 
                                                    start_offset = node_attr.start_offset, end_offset = node_attr.end_offset, 
                                                    is_metavar = node_attr.is_metavar)
                    
                    if node_attr.is_array:
                        for i, (arr_attr) in enumerate(node_attr.value):

                            start_offset = arr_attr.start_offset
                            end_offset = arr_attr.end_offset
                            if node_attr.start_offset is not None:
                                start_offset += node_attr.add_offset
                                end_offset += node_attr.add_offset

                            queue.append( NodeAttributes(parent = handle, name = f"[{i}]", value = arr_attr.value, 
                                                        start_offset = start_offset, 
                                                        end_offset = end_offset, 
                                                        is_metavar = False, is_array = False, 
                                                        add_offset = start_offset if arr_attr.relative_offset else node_attr.add_offset) )
                    else:
                        for child_attr in parser.get_children(node_attr.value):

                            start_offset = child_attr.start_offset
                            end_offset = child_attr.end_offset
                            if child_attr.start_offset is not None:
                                start_offset += node_attr.add_offset
                                end_offset += node_attr.add_offset

                            queue.append( NodeAttributes(parent = handle, name = child_attr.name, value = child_attr.value, 
                                                        start_offset = start_offset, 
                                                        end_offset = end_offset, 
                                                        is_metavar = child_attr.is_metavar, 
                                                        is_array = child_attr.is_array, 
                                                        add_offset = start_offset if child_attr.relative_offset else node_attr.add_offset) )

                self.view.set_status("Loaded")
        except PyTaiException as e:
            self.view.display_error(str(e))
        except Exception:
            raise

    def cb_refresh(self) -> None:
        """Callback for an event where the user refreshes the view."""
        self.view.reset()
        self.view.set_status("Refreshing...")
        if self.current_file_path is not None:
            self.populate_view(self.current_file_path, self.format)

    def cb_structure_selected(self, path: str, start_offset: int, end_offset: int) -> None:
        """Callback for an event where the user selects a structure from the tree."""
        self.view.mark_range(start_offset, end_offset)
        self.view.make_visible(start_offset)

    def cb_goto(self, offset: int) -> None:
        """Callback for an event where the user wants to jump to a given offset."""
        self.view.make_visible(offset, highlight = True)
        self.view.set_status(f"Jumping to offset {hex(offset)} ({offset})")

    def cb_open(self, path: str, format: Dict[str, str]) -> None:
        """Callback for an event where the user wants to open a new file."""
        self.view.reset()
        self.populate_view(path, format)
        self.view.set_status(f"Opened {path}")

    def cb_get_cwd(self) -> str:
        """Callback for getting the current working directory.
        The CWD is defined as the parent directory of the last file opened,
        or the current directory if no file was previously opened.
        """
        if self.current_file_path is not None:
            return Path(self.current_file_path).parent

        return "."