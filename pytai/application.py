from pathlib import Path
from collections import namedtuple
from typing import Union, Dict
import inspect

from . import view as v
from . import model as m

from . import utils

from .common import *

class Application():
    def __init__(self, file, format, *args, **kwargs):

        # These callbacks are used to notify the application
        #  of events from the view
        callbacks = {
            v.Events.REFRESH:             self.cb_refresh,
            v.Events.STRUCTURE_SELECTED:  self.cb_structure_selected,
        }

        self.view = v.View(title = "PyTai", callbacks = callbacks)
        self.model = m.Model()

        self.populate_view(file, format)

    def run(self) -> None:
        """Run the application."""
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
            parsed_file = parser.parse(self.current_file_path)

            # W/A for Kaitai struct behavior:
            # In some cases (e.g. if of the structures within a Kaitai struct is imported), Kaitai will populate
            # the debug offsets with a relative value to the internal struct instead of an absolute value from the start
            # of the external structure.
            # We rely on the offset to highlight the selected bytes in the hex view, and can't use relative offsets.
            # Therefore, as a W/A, we're currently disabling offsets for any children and siblings that appear to
            # be relative (i.e. the first sibling has an offset of 0 and the parent has an offset larger than zero).
            # This is done using "invalidate_offsets" and is propagated to all siblings and children.

            NodeAttributes = namedtuple("NodeAttributes", "parent name value start_offset end_offset is_metavar invalidate_offsets")

            # Build the structure tree by iterating the parsed file (BFS)

            queue = []
    
            queue.append(NodeAttributes('', 'root', parsed_file, 0, None, False, False))
    
            while queue:
                node_attr = queue.pop(0)
                handle = self.view.add_tree_item(node_attr.parent, node_attr.name, 
                                                parser.get_item_description(node_attr.value), 
                                                node_attr.start_offset, node_attr.end_offset, node_attr.is_metavar)
    
                invalidate_offsets = node_attr.invalidate_offsets
                
                if inspect.isgenerator(node_attr.value): # TODO: Find a better way
                    for i, (child, start_offset, end_offset) in enumerate(node_attr.value):
                        if invalidate_offsets:
                            start_offset = end_offset = None
                        queue.append( NodeAttributes(handle, f"[{i}]", child, start_offset, end_offset, False, invalidate_offsets) )
                else:
                    for name, value, start_offset, end_offset, is_metavar in parser.get_children(node_attr.value):
                        if (node_attr.start_offset != 0 and start_offset == 0):
                            invalidate_offsets = True
                        if invalidate_offsets:
                            start_offset = end_offset = None
                        queue.append( NodeAttributes(handle, name, value, start_offset, end_offset, is_metavar, invalidate_offsets) )

            self.view.set_status("Loaded")
        except PyTaiException as e:
            self.view.display_error(str(e))
        except Exception:
            raise


    def cb_refresh(self) -> None:
        """Callback for an event where the user refreshes the view."""
        self.view.reset()
        self.view.set_status("Refreshing...")
        self.populate_view(self.current_file_path, self.format)

    def cb_structure_selected(self, path: str, start_offset: int, end_offset: int) -> None:
        """Callback for an event where the user selects a structure from the tree."""
        self.view.mark_range(start_offset, end_offset)