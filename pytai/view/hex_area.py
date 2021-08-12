"""The 'View' Module of the application: The HEX area.

This file contains the implementation for the HEX area:

+------+--------------+
| Tree | Hex          |
| Area | Area         |
|      |              |
+------+--------------+

The hex area displays the hex representation of the file.

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

from typing import Dict, Callable, Optional

from .events import *

from ..utils import *

TAG_JUSTIFY_RIGHT = 'justify_right'
TAG_HIGHLIGHT = 'highlight'
TAG_SELECTION = 'selection'
TAG_GOTO = 'goto'

class HexViewWidget(tk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg = 'white')



class HexAreaView():
    """Implements the view for the hex area."""

    # Bytes to show per row in hex view
    BYTES_PER_ROW = 16
    REPR_CHARS_PER_BYTE_HEX = 3 # Two chars for hex representation + one space
    REPR_CHARS_PER_BYTE_ASCII = 1

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

        self.main_frame = tk.Frame(parent, bg = 'white')

        # Create the widgets
        self.textbox_address = tk.Text(self.main_frame, width = 17, padx = 10, wrap = tk.NONE)
        self.textbox_address.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.textbox_address.tag_configure(TAG_JUSTIFY_RIGHT, justify = tk.RIGHT)

        self.textbox_hex = tk.Text(self.main_frame, width = 47, padx = 10, wrap = tk.NONE)
        self.textbox_hex.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.textbox_hex.tag_config(TAG_HIGHLIGHT, background='gold3')
        self.textbox_hex.tag_config(TAG_GOTO, background='lightcyan')

        self.textbox_ascii = tk.Text(self.main_frame, width = 17, padx = 10, wrap = tk.NONE)
        self.textbox_ascii.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.textbox_ascii.tag_config(TAG_HIGHLIGHT, background='gold3')
        self.textbox_ascii.tag_config(TAG_SELECTION, background='lightgray')

        self.textboxes = [self.textbox_address, self.textbox_hex, self.textbox_ascii]

        self.scrollbar = tk.Scrollbar(self.main_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand = False)

        # Change the settings to make the scrolling work
        self.scrollbar['command'] = self._on_scrollbar
        for textbox in self.textboxes:
            textbox['yscrollcommand'] = self._on_textscroll

        self.main_frame.pack(fill=tk.BOTH, expand=True, side = tk.RIGHT)

        self.textbox_hex.bind("<<Selection>>", self._on_hex_selection)

    def _on_scrollbar(self, *args) -> None:
        """Scroll all text widgets when the scrollbar is moved."""
        for textbox in self.textboxes:
            textbox.yview(*args)

    def _on_textscroll(self, *args) -> None:
        """Move the scrollbar and scroll text widgets when the mousewheel is moved on a text widget."""
        self.scrollbar.set(*args)
        self._on_scrollbar('moveto', args[0])

    def _on_hex_selection(self, event) -> None:
        """Highlight ASCII view upon selection of HEX view."""
        self.textbox_ascii.tag_remove(TAG_SELECTION, "1.0", tk.END)
        try:
            hex_start_line, hex_start_char = map(int, self.textbox_hex.index(tk.SEL_FIRST).split("."))
            hex_end_line,   hex_end_char   = map(int, self.textbox_hex.index(tk.SEL_LAST).split("."))
            ascii_start = f"{hex_start_line}.{hex_start_char // self.REPR_CHARS_PER_BYTE_HEX}"
            ascii_end   = f"{hex_end_line}.{( (hex_end_char - 1) // self.REPR_CHARS_PER_BYTE_HEX) + 1}"
            self.textbox_ascii.tag_add(TAG_SELECTION, ascii_start, ascii_end)
        except Exception:
            pass
        

    def reset(self):
        """Reset the text widgets to the original state."""
        for textbox in self.textboxes:
            textbox.delete('1.0', tk.END)

    @property
    def widget(self) -> tk.Frame:
        """Return the actual widget."""
        return self.main_frame

    def _populate_address_area(self, num_bytes: int) -> None:
        """Populate the address area with addresses given the file length.

        Args:
            num_bytes:
                Length of the file.
        """
        num_lines = num_bytes // self.BYTES_PER_ROW
        chars_per_byte = 2
        format_pad_len = 8 * chars_per_byte

        for i in range(num_lines + 1):
            base_address = format(i * self.BYTES_PER_ROW, 'X').rjust(format_pad_len, '0')
            self.textbox_address.insert(tk.END, f"{base_address}\n")

        self.textbox_address.tag_add(TAG_JUSTIFY_RIGHT, 1.0, tk.END)
        self.textbox_address.config(state = tk.DISABLED)

    def populate_hex_view(self, byte_arr: bytes) -> None:
        """Populate the hex view with the content of the file.

        Args:
            byte_arr:
                The contents of the file, as a binary array.
        """
        self._populate_address_area(len(byte_arr))
        
        for chunk in chunker(byte_arr, self.BYTES_PER_ROW):
            hex_format = chunk.hex(" ")
            self.textbox_hex.insert(tk.END, f"{hex_format}\n")

            ascii_format = "".join([chr(i) if 32 <= i <= 127 else "." for i in chunk])
            self.textbox_ascii.insert(tk.END, f"{ascii_format}\n")

        self.textbox_address.tag_add(TAG_JUSTIFY_RIGHT, 1.0, tk.END)

        self.textbox_address.config(state = tk.DISABLED)
        self.textbox_hex.config(state = tk.DISABLED)
        self.textbox_ascii.config(state = tk.DISABLED)

    @classmethod
    def _offset_to_line_column(cls, chars_per_byte: int, offset: int, adjust_column: int = 0) -> str:
        """Translate an offset in a text box to tkinter line.column notation.
        
        Args:
            chars_per_byte:
                Number of characters in the text box needed to represent a single byte.
            offset:
                Offset to translate from.
            adjust_column:
                Can be used to adjust the column value after the initial calculation.
        
        Returns:
            Offset in tkinter line.column notation.
        """
        line = (offset // cls.BYTES_PER_ROW) + 1 # Line is 1-based
        column = ((offset % cls.BYTES_PER_ROW) * chars_per_byte)
        return f"{line}.{column + adjust_column}"

    def mark_range(self, start_offset: int, end_offset: int) -> None:
        """Highlight a range between the given offsets, and optionally jump to it.
        
        Args:
            start_offset:
                Offset to highlight from (absolute index of byte in file)
            end_offset:
                Offset to highlight to (absolute index of byte in file)
        """
        self.textbox_hex.tag_remove(TAG_HIGHLIGHT, "1.0", tk.END)
        self.textbox_ascii.tag_remove(TAG_HIGHLIGHT, "1.0", tk.END)

        if start_offset is not None and end_offset is not None:
            # Mark in hex view:
            self.textbox_hex.tag_add(TAG_HIGHLIGHT, 
                                     self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, start_offset), 
                                     self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, end_offset, -1)) # Remove trailing space

            # Mark in ASCII view:
            self.textbox_ascii.tag_add(TAG_HIGHLIGHT, 
                                       self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_ASCII, start_offset), 
                                       self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_ASCII, end_offset))

    def make_visible(self, offset: Optional[int], highlight: bool = False) -> None:
        """Jump to a given offset in the HEX viewer.
        
        Args:
            offset:
                The offset to jump to.
            highlight:
                In addition, highlight the location.
        """
        self.textbox_hex.tag_remove(TAG_GOTO, "1.0", tk.END)

        if offset is None:
            return

        location = self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, offset)
        self.textbox_hex.see(location)

        if highlight:
            self.textbox_hex.tag_add(TAG_GOTO, location, f"{location}+2c")
        