import tkinter as tk
from tkinter import ttk
from typing import Dict, Callable

from .events import *

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
        self.main_frame.pack(side = tk.RIGHT)

    def reset(self) -> None:
        """Reset the area to its initial state."""
        # TODO
        pass

    @property
    def widget(self) -> ttk.Frame:
        """Return the actual widget."""
        return self.main_frame

