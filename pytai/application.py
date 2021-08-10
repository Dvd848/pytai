from pathlib import Path
from collections import namedtuple
from typing import Union

from . import view as v
from . import model as m

class Application():
    def __init__(self, *args, **kwargs):

        # These callbacks are used to notify the application
        #  of events from the view
        callbacks = {
            v.Events.REFRESH:             self.cb_refresh,
        }

        self.view = v.View(title = "PyTai", callbacks = callbacks)
        self.model = m.Model()

        # TODO: Currently hardcoded
        self.populate_structure_tree(Path(__file__).resolve().parent / "tmp" / "test.png")

    def run(self) -> None:
        """Run the application."""
        self.view.mainloop()

    def populate_structure_tree(self, path_file: Union[str, Path]) -> None:
        """Populates the View's structure tree for the given file.
        
        Args:
            path_file:
                Path to the file to be parsed.
        """

        self.current_file_path = path_file

        # TODO: Currently hardcoded
        parser = self.model.get_parser(path_ksy = "/path/to/png.ksy")
        parsed_file = parser.parse(self.current_file_path)

        NodeAttributes = namedtuple("NodeAttributes", "parent name value")

        # Build the structure tree by iterating the parsed file (BFS)

        queue = []
 
        queue.append(NodeAttributes('', 'root', parsed_file))
 
        while queue:
            node_attr = queue.pop(0)
            handle = self.view.add_tree_item(node_attr.parent, node_attr.name)
 
            if isinstance(node_attr.value, list):
                for i, child in enumerate(node_attr.value):
                    queue.append( NodeAttributes(handle, f"[{i}]", child) )
            else:
                for name, value in parser.get_children(node_attr.value):
                    queue.append( NodeAttributes(handle, name, value) )


    def cb_refresh(self) -> None:
        """Callback for an event where the user refreshes the view."""
        self.view.set_status("Refreshing...")
        self.populate_structure_tree(self.current_file_path)