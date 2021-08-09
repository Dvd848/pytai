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

        self.pw.add(self.tree_view.widget, width = 400)
        self.pw.add(self.hex_view.widget)
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

