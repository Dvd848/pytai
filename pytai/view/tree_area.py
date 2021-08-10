
import tkinter as tk
from tkinter import ttk

from typing import Dict, Callable

from .bars import *
from .events import *

class TreeItem():
    """Wrapper for tree GUI item."""
    def __init__(self, tree: ttk.Treeview, id: str):
        """Instantiate a tree item.
        
        Args:
            tree:
                Parent Treeview for this item.
            id: 
                Treeview ID for this item.
        """
        self._id = id
        self._tree = tree
        self._item = self._tree.item(self._id)

    @property
    def id(self) -> str:
        """Treeview ID for this item."""
        return self._id

    @property
    def path(self) -> str:
        """Full path up to this item."""
        path = []
        path.append(self._item["text"])
        current_item: str = self._id

        while (parent := self._tree.parent(current_item)) != "":
            tree_item = self._tree.item(parent)
            path.append(tree_item["text"])
            current_item = parent

        return ".".join(reversed(path))


class TreeAreaView():
    """Implements the view for the key area."""
    
    def __init__(self, parent, address_bar: AddressBar, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
            
            address_bar:
                Instance of AddressBar
                
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        self.parent = parent
        self.callbacks = callbacks
        self.address_bar = address_bar

        self.wrapper = ttk.Frame(parent)

        self.tree = ttk.Treeview(self.wrapper, show = 'tree', selectmode = 'browse')
        self.tree.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)
        self.tree.bind('<<TreeviewSelect>>', self._item_selected)
        #self.tree.tag_configure(TAG, foreground = 'gray')

        self.vsb = ttk.Scrollbar(self.wrapper, orient = tk.VERTICAL, command = self.tree.yview)
        self.vsb.pack(side = tk.RIGHT, fill = tk.Y)

        self.tree.configure(yscrollcommand = self.vsb.set)


    def reset(self) -> None:
        """Reset the key area to its initial state."""
        self.tree.delete(*self.tree.get_children())

    @property
    def widget(self) -> ttk.Treeview:
        """Return the actual widget."""
        return self.wrapper

    @property
    def selected_item(self) -> TreeItem:
        """Return the currently selected item."""
        return TreeItem(self.tree, self.tree.selection()[0])

    def _item_selected(self, event) -> None:
        """Handle an event where the user selects a key."""
        selected_item = self.selected_item
        
    def add_item(self, parent_handle: str, name: str) -> str:
        """Add an item to the structure tree.
        
        Args:
            parent_handle:
                Handle to the parent of the current item, based on a previous
                return value of add_item() (or '' for the root)
            name:
                Name of the current item.
        
        Returns:
            Handle to this item, to be used for child items.
        """
        handle = self.tree.insert(parent_handle, 'end', text = name, open = True)
        return handle