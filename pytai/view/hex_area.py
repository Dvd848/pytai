import tkinter as tk
from tkinter import ttk
from typing import Dict, Callable

from .events import *


class HexViewWidget(tk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        # Creating the widgets
        self.textbox_address = tk.Text(self, width = '10')
        self.textbox_address.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.textbox_hex = tk.Text(self, width = '40')
        self.textbox_hex.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.textbox_ascii = tk.Text(self, width = '20')
        self.textbox_ascii.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.textboxes = [self.textbox_address, self.textbox_hex, self.textbox_ascii]

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Changing the settings to make the scrolling work
        self.scrollbar['command'] = self.on_scrollbar
        for textbox in self.textboxes:
            textbox['yscrollcommand'] = self.on_textscroll

    def on_scrollbar(self, *args):
        """Scrolls all text widgets when the scrollbar is moved."""
        for textbox in self.textboxes:
            textbox.yview(*args)

    def on_textscroll(self, *args):
        """Moves the scrollbar and scrolls text widgets when the mousewheel is moved on a text widget."""
        self.scrollbar.set(*args)
        self.on_scrollbar('moveto', args[0])

class HexAreaView():
    """Implements the view for the hex area."""

    def __init__(self, parent, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            parent: 
                Parent tk class.
                            
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        self.parent = parent
        self.callbacks = callbacks

        self.main_frame = ttk.Frame(parent)

        self.hex_widget = HexViewWidget(self.main_frame, bg='white', fg='black')
        self.hex_widget.pack(fill=tk.BOTH, expand=True)
        
        self.main_frame.pack(side = tk.RIGHT)



    def reset(self) -> None:
        """Reset the area to its initial state."""
        # TODO
        pass

    @property
    def widget(self) -> ttk.Frame:
        """Return the actual widget."""
        return self.main_frame

