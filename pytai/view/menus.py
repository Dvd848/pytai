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
from tkinter import messagebox

import tkinter as tk
import enum


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
        add_command(filemenu, False, label = "Open...", command = lambda: self.callbacks[self.Events.OPEN](None), accelerator = "Ctrl+O")
        add_command(filemenu, False, label = "Exit", command = parent.quit)
        self.add_cascade(label = "File", menu = filemenu)

        searchmenu = tk.Menu(self, tearoff = 0)
        add_command(searchmenu, True, label = "Find...", command = lambda: self.callbacks[self.Events.SEARCH](None), accelerator = "Ctrl+F")
        add_command(searchmenu, True, label = "Find Next", command = lambda: self.callbacks[self.Events.FIND_NEXT](None), accelerator = "F3")
        add_command(searchmenu, True, label = "Find Previous", command = lambda: self.callbacks[self.Events.FIND_PREV](None), accelerator = "Shift+F3")
        searchmenu.add_separator()
        add_command(searchmenu, True, label = "Go to...", command = lambda: self.callbacks[self.Events.GOTO](None), accelerator = "Ctrl+G")
        self.add_cascade(label = "Search", menu = searchmenu)
        
        viewmenu = tk.Menu(self, tearoff = 0)
        add_command(viewmenu, True, label = "Refresh", command = lambda: self.callbacks[self.Events.REFRESH](None), accelerator = "F5")
        viewmenu.add_separator()
        add_command(viewmenu, True, label = "Expand Tree", command = lambda: self.callbacks[self.Events.EXPAND_TREE]())
        add_command(viewmenu, True, label = "Collapse Tree", command = lambda: self.callbacks[self.Events.COLLAPSE_TREE]())
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

        self.menu.add_command(label = "Show X-Ref", command = lambda: self.callbacks[self.Events.GET_XREF](self._current_event))

    def show(self, event) -> None:
        """Show the menu."""
        self._current_event = event
        super().show(event)