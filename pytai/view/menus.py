"""The 'View' Module of the application: Various menus.

This file contains the implementation for the different menus
of the View.

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
from typing import Dict, Callable
from functools import partial

import tkinter as tk
import enum
from ..common import *


class BaseHexAreaMenu():
    """Base class for a menu in the Hex area."""
    def __init__(self, parent):
        self.parent = parent

    def show(self, event) -> None:
        """Show the menu."""
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()


class MenuBar(tk.Menu):
    """The main application menu."""
    
    class Events(enum.Enum):
        """Events that can be triggered by the menu."""
        
        # User wants to refresh the view
        REFRESH                 = enum.auto()

        # User wants to jump to offset
        GOTO                    = enum.auto()

        # User wants to open file
        OPEN                    = enum.auto()

        # User wants to search file
        SEARCH                  = enum.auto()

        # User wants to find the next occurrance of the search term
        FIND_NEXT               = enum.auto()

        # User wants to find the previous occurrance of the search term
        FIND_PREV               = enum.auto()

        # User wants to view "about" window
        ABOUT                   = enum.auto()

        # User wants to expand all tree items
        EXPAND_TREE            = enum.auto()

        # User wants to collapse all tree items
        COLLAPSE_TREE           = enum.auto()

    def __init__(self, parent, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
                
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        super().__init__(parent)

        if callbacks.keys() != set(self.Events):
            raise KeyError(f"Callbacks must contain all events in {set(self.Events)} ")

        self.callbacks = callbacks

        self.commands_require_file = {}

        def add_command(menu, requires_file: bool, **kwargs) -> None:
            self.commands_require_file[(menu, kwargs['label'])] = requires_file
            menu.add_command(**kwargs)

        filemenu = tk.Menu(self, tearoff=0)
        add_command(filemenu, False, label = "Open...", 
                    command = lambda: self.callbacks[self.Events.OPEN](None), accelerator = "Ctrl+O")
        add_command(filemenu, False, label = "Exit", 
                    command = parent.quit)
        self.add_cascade(label = "File", menu = filemenu)

        searchmenu = tk.Menu(self, tearoff = 0)
        add_command(searchmenu, True, label = "Find...", 
                    command = lambda: self.callbacks[self.Events.SEARCH](None), accelerator = "Ctrl+F")
        add_command(searchmenu, True, label = "Find Next", 
                    command = lambda: self.callbacks[self.Events.FIND_NEXT](None), accelerator = "F3")
        add_command(searchmenu, True, label = "Find Previous", 
                    command = lambda: self.callbacks[self.Events.FIND_PREV](None), accelerator = "Shift+F3")
        searchmenu.add_separator()
        add_command(searchmenu, True, label = "Go to...", 
                    command = lambda: self.callbacks[self.Events.GOTO](None), accelerator = "Ctrl+G")
        self.add_cascade(label = "Search", menu = searchmenu)
        
        viewmenu = tk.Menu(self, tearoff = 0)
        add_command(viewmenu, True, label = "Refresh", 
                    command = lambda: self.callbacks[self.Events.REFRESH](None), accelerator = "F5")
        viewmenu.add_separator()
        add_command(viewmenu, True, label = "Expand Tree", 
                    command = lambda: self.callbacks[self.Events.EXPAND_TREE]())
        add_command(viewmenu, True, label = "Collapse Tree", 
                    command = lambda: self.callbacks[self.Events.COLLAPSE_TREE]())
        self.add_cascade(label = "View", menu = viewmenu)

        helpmenu = tk.Menu(self, tearoff = 0)
        add_command(helpmenu, False, label = "About...", command = self.show_about)
        self.add_cascade(label = "Help", menu = helpmenu)

        self.toggle_loaded_file_commands(enable = False)

    def show_about(self) -> None:
        """Show the "About" window."""
        self.callbacks[self.Events.ABOUT]()

    def toggle_loaded_file_commands(self, enable: bool) -> None:
        """Enables/disables menu options which require an open file."""
        target = tk.NORMAL if enable else tk.DISABLED 
        for (menu, label), requires_file in self.commands_require_file.items():
            if requires_file:
                menu.entryconfigure(label, state = target)

class HexAreaMenu(BaseHexAreaMenu):
    class Events(enum.Enum):
        """Events that can be triggered by the menu."""
        
        # Show cross-reference for current byte
        GET_XREF = enum.auto()

    def __init__(self, parent, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
                
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        super().__init__(parent)

        self.parent = parent

        self.menu = tk.Menu(self.parent, tearoff = 0)

        if callbacks.keys() != set(self.Events):
            raise KeyError(f"Callbacks must contain all events in {set(self.Events)} ")
        self.callbacks = callbacks

        self.menu.add_command(label = "Show X-Ref", 
                              command = lambda: self.callbacks[self.Events.GET_XREF](self._current_event))

    def show(self, event) -> None:
        """Show the menu."""
        self._current_event = event
        super().show(event)

class TreeItemMenu():
    """Menu displayed after right-clicking an item in the tree area."""

    class Events(enum.Enum):
        """Events that can be triggered by the menu."""
        
        # User wants to copy the selection to the clipboard
        COPY = enum.auto()
        
        # User wants to export the selection to a binary
        SAVE_AS = enum.auto()

        # User wants to highlight a selection with a custom color
        HIGHLIGHT = enum.auto()

    def __init__(self, parent, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
                
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        self.parent = parent
        self.menu = tk.Menu(self.parent, tearoff = 0)

        if callbacks.keys() != set(self.Events):
            raise KeyError(f"Callbacks must contain all events in {set(self.Events)} ")
        self.callbacks = callbacks

        copy_menu = tk.Menu(self.parent, tearoff=0)
        copy_menu.add_command(label = "Copy as Hex Array",  command = self._copy_hex)
        copy_menu.add_command(label = "Copy as Hex Stream", command = self._copy_hex_stream)
        copy_menu.add_command(label = "Copy as Raw Bytes",  command = self._copy_raw_bytes)

        self.highlight_menu = tk.Menu(self.parent, tearoff=0)
        self.highlight_colors = {}
        for ht in HighlightType:
            if (not HighlightType.is_custom(ht)):
                continue

            self.highlight_colors[ht] = {
                "label": f"Color {len(self.highlight_colors) + 1}", 
                "variable": tk.BooleanVar(), 
                "command": partial(self._highlight, highlight_type = ht)
            }
            self.highlight_menu.add_checkbutton(self.highlight_colors[ht])

 
        self.menu.add_cascade(label='Highlight', menu = self.highlight_menu)
        self.menu.add_cascade(label = "Copy", menu = copy_menu)
        self.menu.add_separator()
        self.menu.add_command(label ="Save as...", command = self._save_as)
        

    def show(self, event, highlighted_colors: Dict[HighlightType, HighlightDetails]) -> None:
        """Show the menu.
        
        Args:
            highlighted_colors:
                A mapping between the different highlighters available and their details:
                    - Whether the given highlighter is active for this item
                    - If it's active, whether it was added explicitly for this item
        """
        self._current_event = event
        for ht, details in highlighted_colors.items():
            self.highlight_colors[ht]["variable"].set(details.is_active)

            # If the highlighter was added for the parent, don't allow removing
            # if from this item, only from the parent.
            is_disabled = details.is_active and not details.is_exact_match

            self.highlight_menu.entryconfig(self.highlight_colors[ht]["label"], 
                                            state = tk.DISABLED if is_disabled else tk.NORMAL)

        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def hide(self):
        """Hide the menu"""
        self.menu.unpost()

    def _copy_hex(self):
        """Copy the selection as a Hex Array"""
        self.callbacks[self.Events.COPY](self._current_event, ByteRepresentation.HEX)

    def _copy_hex_stream(self):
        """Copy the selection as a Hex Stream"""
        self.callbacks[self.Events.COPY](self._current_event, ByteRepresentation.HEX_STREAM)

    def _copy_raw_bytes(self):
        """Copy the selection as raw bytes"""
        self.callbacks[self.Events.COPY](self._current_event, ByteRepresentation.RAW_BYTES)

    def _save_as(self):
        """Export the selection to a binary"""
        self.callbacks[self.Events.SAVE_AS](self._current_event)

    def _highlight(self, highlight_type: HighlightType):
        """Highlight a selection with a custom color"""
        self.callbacks[self.Events.HIGHLIGHT](self._current_event, highlight_type, 
                                              bool(self.highlight_colors[highlight_type]["variable"].get()))