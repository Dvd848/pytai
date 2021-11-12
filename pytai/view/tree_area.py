"""The 'View' Module of the application: The Tree area.

This file contains the implementation for the tree area:

+------+--------------+
| Tree | HEX          |
| Area | Area         |
|      |              |
+------+--------------+

The tree area displays a tree representing the internal structure
of the file.

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
import tkinter as tk
from tkinter import ttk

from typing import Dict, Callable, Tuple

from .bars import *
from .events import *

from ..common import *

TAG_OFFSET_PREFIX = "_offset_"
TAG_OFFSET_SEPARATOR = "-"
TAG_METAVAR = "metavar"

class TreeItem():
    """Wrapper for tree GUI item."""
    def __init__(self, tree: ttk.Treeview, id: str):
        """Instantiate a tree item.
        
        Args:
            root:
                Root tk class.

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

        return ".".join(reversed(path)).replace(".[", "[")

    @property
    def range(self) -> Tuple[int, int]:
        """Return the range of the structure as offsets in the file.
        
        Offsets are returned as tuple(start_offset, end_offset).

        If no range was entered for this structure, returns (None, None).
        """
        range_tag = None
        for tag in self._item["tags"]:
            if tag.startswith(TAG_OFFSET_PREFIX):
                range_tag = tag.replace(TAG_OFFSET_PREFIX, "")
                break
        
        if range_tag == None:
            return (None, None)

        return tuple(map(int, range_tag.split(TAG_OFFSET_SEPARATOR)))


class TreeAreaView():
    """Implements the view for the key area."""

    def __init__(self, root, parent, address_bar: AddressBar, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
            
            address_bar:
                Instance of AddressBar
                
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        self.root = root
        self.parent = parent
        self.callbacks = callbacks
        self.address_bar = address_bar

        self.wrapper = ttk.Frame(parent)

        columns = ['Name', 'Extra Info']

        self.tree = ttk.Treeview(self.wrapper, selectmode = 'browse', columns = len(columns))

        for i, column in enumerate(columns):
            self.tree.heading(f"#{i}", text = column, anchor = tk.W)
            self.tree.column(f"#{i}", minwidth = 100, stretch = tk.NO, anchor = tk.W)

        self.tree.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)
        self.tree.bind('<<TreeviewSelect>>', self._item_selected)
        self.tree.tag_configure(TAG_METAVAR, foreground = 'gray')

        self.vsb = ttk.Scrollbar(self.wrapper, orient = tk.VERTICAL, command = self.tree.yview)
        self.vsb.pack(side = tk.RIGHT, fill = tk.Y)

        self.tree.configure(yscrollcommand = self.vsb.set)

        self.fix_tkinter_color_tags()


    def reset(self) -> None:
        """Reset the key area to its initial state."""
        self.tree.delete(*self.tree.get_children())
        self.address_bar.set_address('')
        
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

        self.callbacks[Events.STRUCTURE_SELECTED](selected_item.path, *selected_item.range)
        self.address_bar.set_address(selected_item.path)
        
    def add_item(self, parent_handle: str, name: str, extra_info: str, start_offset: int, end_offset: int, is_metavar: bool) -> str:
        """Add an item to the structure tree.
        
        Args:
            parent_handle:
                Handle to the parent of the current item, based on a previous
                return value of add_item() (or '' for the root)
            name:
                Name of the current item.
            extra_info:
                Extra information for the entry.
            start_offset:
                Start offset of structure in file.
            end_offset:
                End offset of structure in file.
            is_metavar:
                True if this is a metavar (user friendly representation of a value located elsewhere).
        
        Returns:
            Handle to this item, to be used for child items.
        """

        try:
            tags = []
            if start_offset is not None and end_offset is not None:
                tags.append(f"{TAG_OFFSET_PREFIX}{start_offset}{TAG_OFFSET_SEPARATOR}{end_offset}")
            
            if is_metavar:
                tags.append(TAG_METAVAR)

            handle = self.tree.insert(parent_handle, 'end', text = name, open = True, values = (extra_info,), tags = tuple(tags))

            return handle
        except tk.TclError as e:
            raise PyTaiViewException from e

    def mark_tree_element(self, handle: str) -> None:
        """Mark an element in the tree and make it visible.

        Args:
            handle:
                A handle to the tree element as returned by add_item()
        
        """
        self.tree.selection_set(handle)
        self.tree.focus(handle)
        self.tree.see(handle)

    def expand_children(self, expand: bool, parent: str = '') -> None:
        """Expand or collapse a sub-tree.
        
        Args:
            expand:
                True to expand the tree, False to collapse

            parent:
                ID of the root tree to start from.
        
        """
        work_queue = [parent]
        while len(work_queue) > 0:
            current = work_queue.pop(0)
            self.tree.item(current, open = expand)
            for child in self.tree.get_children(current):
                work_queue.append(child)

    def fix_tkinter_color_tags(self) -> None:
        """A W/A to allow tkinter to display a TreeView's foreground/background."""
        def fixed_map(option):
            # Fix for setting text colour for Tkinter 8.6.9
            # From: https://core.tcl.tk/tk/info/509cafafae
            #
            # Returns the style map for 'option' with any styles starting with
            # ('!disabled', '!selected', ...) filtered out.

            # style.map() returns an empty list for missing options, so this
            # should be future-safe.
            return [elm for elm in style.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]

        style = ttk.Style()
        style.map('Treeview', foreground = fixed_map('foreground'), background = fixed_map('background'))