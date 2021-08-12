"""The 'View' Module of the application.

This file contains the main "View" logic.

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
#import importlib.resources

from tkinter import messagebox, simpledialog
from typing import Dict, Callable

from .menus import *
from .tree_area import *
from .hex_area import *
from .events import *

#from ..common import *

class View(tk.Tk):
    """ The application 'View' Model."""
    
    def __init__(self, title, callbacks: Dict[Events, Callable[..., None]], *args, **kwargs):
        """Instantiate the class.
        
        Args:
            title: 
                Title of the application.
            
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        super().__init__(*args, **kwargs)

        self.root = self
        self.callbacks = callbacks

        self.title(title)
        self.resizable(width = True, height = True)
        self.geometry('1280x720')

        
        #with importlib.resources.path(f"{__package__}.assets", "icon.ico") as icon_path:
        #    self.iconbitmap(default = icon_path)
        

        self.menubar = MenuBar(self.root, {
            MenuBar.Events.REFRESH:                 self.refresh,
            MenuBar.Events.GOTO:                    self.show_goto,
        })
        self.root.config(menu = self.menubar)
        

        self.top_frame = tk.Frame()
        self.address_bar = AddressBar(self.top_frame)
        self.top_frame.pack(side=tk.TOP, fill = tk.BOTH)

        self.bottom_frame = tk.Frame()
        self.status_bar = StatusBar(self.bottom_frame)
        self.bottom_frame.pack(side=tk.BOTTOM, fill = tk.BOTH)

        self.pw = tk.PanedWindow(orient = 'horizontal') 
        self.tree_view = TreeAreaView(self.pw, self.address_bar, self.callbacks)
        self.hex_view = HexAreaView(self.pw, self.callbacks)

        self.pw.add(self.tree_view.widget, minsize = 450)
        self.pw.add(self.hex_view.widget, minsize = 740)
        self.pw.pack(fill = tk.BOTH, expand = True) 
        self.pw.configure(sashrelief = tk.RAISED)

        self.root.bind('<F5>', self.refresh)
        self.root.bind('<Control-g>', self.show_goto)

        # Delegate a few interface functions directly to internal implementation
        self.add_tree_item = self.tree_view.add_item
        self.populate_hex_view = self.hex_view.populate_hex_view
        self.make_visible = self.hex_view.make_visible

        self.reset()

    def reset(self) -> None:
        """Reset the view to its initial state."""
        self.hex_view.reset()
        self.tree_view.reset()

    def refresh(self, event) -> None:
        """Handle a user refresh request."""
        self.callbacks[Events.REFRESH]()

    def show_goto(self, event) -> None:
        """Show the 'goto' diaglog to jump to an arbitrary offset."""
        answer = simpledialog.askstring("Go to...", "Enter offset (prefix with '0x' for hex)",
                                         parent = self.root)
        if answer is None:
            return

        try:
            offset = int(answer, 0)
            self.callbacks[Events.GOTO](offset)
        except ValueError as e:
            self.display_error(f"Unable to jump to offset {answer}:\n({str(e)})")

    def set_status(self, status: str) -> None:
        """Set the given status in the status bar.
        
        Args:
            status:
                Status to set.
        """
        self.status_bar.set_status(status)

    @staticmethod
    def display_error(msg: str) -> None:
        """Display the given error.
        
        Args:
            msg:
                Error message to display.
        """
        messagebox.showerror("Error", msg)

    def mark_range(self, start_offset: int, end_offset: int) -> None:
        """Highlight a range between the given offsets.
        
        Args:
            start_offset:
                Offset to highlight from (absolute index of byte in file)
            end_offset:
                Offset to highlight to (absolute index of byte in file)
        """
        if start_offset is not None and end_offset is not None:
            length = end_offset - start_offset
            
            status = []
            if length > 0:
                # end offset is exclusive, but we want to show inclusive range
                status.append(f"Range: {hex(start_offset)}-{hex(end_offset - 1)}")

            status.append(f"Length: {length} ({hex(length)}) bytes")

            self.set_status(" | ".join(status))
        else:
            self.set_status("")
        self.hex_view.mark_range(start_offset, end_offset)