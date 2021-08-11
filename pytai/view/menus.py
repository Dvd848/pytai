from typing import Dict, Callable
from tkinter import messagebox

import tkinter as tk
import enum


class RegistryDetailsMenu():
    """Base class for a menu in the details area."""
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

    def __init__(self, parent, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
                
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        super().__init__(parent)

        self.callbacks = callbacks

        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="Exit", command=parent.quit)
        self.add_cascade(label="File", menu=filemenu)

        searchmenu = tk.Menu(self, tearoff=0)
        searchmenu.add_command(label="Go to...", command=lambda: self.callbacks[self.Events.GOTO](None), accelerator="Ctrl+G")
        self.add_cascade(label="Search", menu=searchmenu)

        viewmenu = tk.Menu(self, tearoff=0)
        viewmenu.add_command(label="Refresh", command=lambda: self.callbacks[self.Events.REFRESH](None), accelerator="F5")
        self.add_cascade(label="View", menu=viewmenu)

        helpmenu = tk.Menu(self, tearoff=0)
        helpmenu.add_command(label="About...", command=self.show_about)
        self.add_cascade(label="Help", menu=helpmenu)

    def show_about(self):
        """Show the "About" window."""
        messagebox.showinfo("About", "PyTai: A Kaitai Struct Visualizer and HEX Viewer GUI in Python\nhttps://github.com/Dvd848/pytai\n\n"
                                     "Based on structure parsers provided by the Kaitai project\nhttps://kaitai.io/")