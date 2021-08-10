from pathlib import Path
from collections import namedtuple
from pytai.view.events import Events
from typing import Union
import inspect

from . import view as v
from . import model as m

from . import utils

class Application():
    def __init__(self, *args, **kwargs):

        # These callbacks are used to notify the application
        #  of events from the view
        callbacks = {
            v.Events.REFRESH:             self.cb_refresh,
            v.Events.STRUCTURE_SELECTED:  self.cb_structure_selected,
        }

        self.view = v.View(title = "PyTai", callbacks = callbacks)
        self.model = m.Model()

        # TODO: Currently hardcoded
        self.populate_view(Path(__file__).resolve().parent / "tmp" / "test.png")

    def run(self) -> None:
        """Run the application."""
        self.view.mainloop()

    def populate_view(self, path_file: Union[str, Path]) -> None:
        """Populates the View for the given file.
        
        Args:
            path_file:
                Path to the file to be parsed.
        """
        self._populate_structure_tree(path_file)
        with utils.memory_map(path_file) as f:
            self.view.populate_hex_view(f)

    def _populate_structure_tree(self, path_file: Union[str, Path]) -> None:
        """Populates the View's structure tree for the given file.
        
        Args:
            path_file:
                Path to the file to be parsed.
        """

        self.current_file_path = path_file

        # TODO: Currently hardcoded
        parser = self.model.get_parser(path_ksy = "/path/to/png.ksy")
        parsed_file = parser.parse(self.current_file_path)

        NodeAttributes = namedtuple("NodeAttributes", "parent name value start_offset end_offset")

        # Build the structure tree by iterating the parsed file (BFS)

        queue = []
 
        queue.append(NodeAttributes('', 'root', parsed_file, None, None))
 
        while queue:
            node_attr = queue.pop(0)
            handle = self.view.add_tree_item(node_attr.parent, node_attr.name, 
                                             parser.get_item_description(node_attr.value), 
                                             node_attr.start_offset, node_attr.end_offset)
 
            # TODO: Find a better way
            if inspect.isgenerator(node_attr.value):
                for i, (child, start_offset, end_offset) in enumerate(node_attr.value):
                    queue.append( NodeAttributes(handle, f"[{i}]", child, start_offset, end_offset) )
            else:
                for name, value, start_offset, end_offset in parser.get_children(node_attr.value):
                    queue.append( NodeAttributes(handle, name, value, start_offset, end_offset) )

        self.view.set_status("Loaded")


    def cb_refresh(self) -> None:
        """Callback for an event where the user refreshes the view."""
        self.view.reset()
        self.view.set_status("Refreshing...")
        self.populate_view(self.current_file_path)

    def cb_structure_selected(self, path: str, start_offset: int, end_offset: int) -> None:
        """Callback for an event where the user selects a structure from the tree."""
        self.view.mark_range(start_offset, end_offset)