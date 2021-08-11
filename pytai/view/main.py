import tkinter as tk
#import importlib.resources

from tkinter import messagebox
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
            MenuBar.Events.REFRESH:                 self.refresh
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

        self.pw.add(self.tree_view.widget, minsize = 200)
        self.pw.add(self.hex_view.widget, minsize = 740)
        self.pw.pack(fill = tk.BOTH, expand = True) 
        self.pw.configure(sashrelief = tk.RAISED)

        self.root.bind('<F5>', self.refresh)

        self.reset()

    def reset(self) -> None:
        """Reset the view to its initial state."""
        self.reset_details()
        self.tree_view.reset()

    def reset_details(self) -> None:
        """Reset the details area to its initial state."""
        self.hex_view.reset()

    def refresh(self, event) -> None:
        """Handle a user refresh request."""
        self.callbacks[Events.REFRESH]()

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

    # TODO: These are just wrapper functions, redundant?

    def add_tree_item(self, parent_handle: str, name: str, extra_info: str, start_offset: int, end_offset: int, is_metavar: bool) -> str:
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
        return self.tree_view.add_item(parent_handle, name, extra_info, start_offset, end_offset, is_metavar)

    def populate_hex_view(self, byte_arr: bytes) -> None:
        """Populate the hex view with the content of the file.

        Args:
            byte_arr:
                The contents of the file, as a binary array.
        """
        self.hex_view.populate_hex_view(byte_arr)

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