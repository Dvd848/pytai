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
from io import StringIO

import queue

from .events import *
from .menus import *

from ..common import *
from ..utils import *

TAG_JUSTIFY_RIGHT = 'justify_right'
TAG_HIGHLIGHT = 'highlight'
TAG_SELECTION = 'selection'
TAG_GOTO = 'goto'
TAG_HIGHLIGHT_CUSTOM1 = 'highlight_c1'
TAG_HIGHLIGHT_CUSTOM2 = 'highlight_c2'
TAG_HIGHLIGHT_CUSTOM3 = 'highlight_c3'

TAGS = [
    TAG_JUSTIFY_RIGHT, TAG_HIGHLIGHT, TAG_SELECTION, TAG_GOTO, 
    TAG_HIGHLIGHT_CUSTOM1, TAG_HIGHLIGHT_CUSTOM2, TAG_HIGHLIGHT_CUSTOM3
]

class HexAreaView():
    """Implements the view for the hex area."""

    # Bytes to show per row in hex view
    BYTES_PER_ROW = 16
    REPR_CHARS_PER_BYTE_HEX = 3 # Two chars for hex representation + one space
    REPR_CHARS_PER_BYTE_ASCII = 1

    def __init__(self, root, parent, callbacks: Dict[Events, Callable[..., None]]):
        """Instantiate the class.
        
        Args:
            root:
                Root tk class.
                
            parent: 
                Parent tk class.
                            
            callbacks:
                Dictionary of callbacks to call when an event from Events occurs
                
        """
        self.root = root
        self.parent = parent
        self.callbacks = callbacks

        self.main_frame = tk.Frame(parent, bg = 'white')

        # Create the widgets
        self.textbox_address = tk.Text(self.main_frame, width = 17, padx = 10, wrap = tk.NONE, bd = 0)
        self.textbox_address.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.textbox_address.tag_configure(TAG_JUSTIFY_RIGHT, justify = tk.RIGHT)

        self.textbox_hex = tk.Text(self.main_frame, width = 47, padx = 10, wrap = tk.NONE, bd = 0)
        self.textbox_hex.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.textbox_hex.tag_config(TAG_HIGHLIGHT_CUSTOM1, background='khaki1')
        self.textbox_hex.tag_config(TAG_HIGHLIGHT_CUSTOM2, background='DarkSeaGreen1')
        self.textbox_hex.tag_config(TAG_HIGHLIGHT_CUSTOM3, background='thistle1')
        self.textbox_hex.tag_config(TAG_HIGHLIGHT, background='gold3') # Must be last of highlight tags
        self.textbox_hex.tag_config(TAG_GOTO, background='lightcyan')

        self.textbox_ascii = tk.Text(self.main_frame, width = 17, padx = 10, wrap = tk.NONE, bd = 0)
        self.textbox_ascii.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.textbox_ascii.tag_config(TAG_HIGHLIGHT_CUSTOM1, background='khaki1')
        self.textbox_ascii.tag_config(TAG_HIGHLIGHT_CUSTOM2, background='DarkSeaGreen1')
        self.textbox_ascii.tag_config(TAG_HIGHLIGHT_CUSTOM3, background='thistle1')
        self.textbox_ascii.tag_config(TAG_HIGHLIGHT, background='gold3') # Must be last of highlight tags
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

        self.hex_rightclick_menu = HexAreaMenu(self.parent, {
            HexAreaMenu.Events.GET_XREF: self._get_hex_xref
        })

        self.textbox_hex.bind("<Button-3>", self._show_rightclick_hex_menu)

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

    def _get_hex_xref(self, event) -> None:
        """Show X-Ref for current offset in Hex Area.

        Args:
            event:
                A tkinter event containing the (x,y) coordinates
                of where the user originally right-clicked to get the X-Ref.
        """
        #hex_line, hex_char = map(int, self.textbox_hex.index(tk.CURRENT).split("."))
        hex_line, hex_char = map(int, self.textbox_hex.index(f"@{event.x},{event.y}").split("."))
        offset = ((hex_line - 1) * self.BYTES_PER_ROW) + (hex_char // self.REPR_CHARS_PER_BYTE_HEX)
        self.callbacks[Events.GET_XREF](offset)

    def _show_rightclick_hex_menu(self, event) -> None:
        """Show the Right-Click menu for the hex area.

        Args:
            event:
                A tkinter event containing the (x,y) coordinates
                of where the user right-clicked to get the X-Ref.
        """
        assert(self.textbox_hex.index(tk.CURRENT) == self.textbox_hex.index(f"@{event.x},{event.y}"))
        self.hex_rightclick_menu.show(event)
        

    def reset(self):
        """Reset the text widgets to the original state."""
        self.abort_load = True
        for textbox in self.textboxes:
            textbox.config(state = tk.NORMAL)
            textbox.delete('1.0', tk.END)
            for tag in TAGS:
                textbox.tag_remove(tag, "1.0", tk.END)

    @property
    def widget(self) -> tk.Frame:
        """Return the actual widget."""
        return self.main_frame

    def populate_hex_view(self, byte_arr: bytes, done_cb: Callable[[], None]) -> None:
        """Populate the hex view with the content of the file.

        Args:
            byte_arr:
                The contents of the file, as a binary array.

            done_cb:
                A callback to call when the hex view is fully populated.

        """
        self.abort_load = False

        self.hex_content_done_cb = done_cb
        self.hex_thread_queue = queue.Queue()
        start_deamon(function = self._create_hex_view_content, args = (byte_arr, self.hex_thread_queue))
        self.root.after(50, self._add_content_to_hex_view)

    def _create_hex_view_content(self, byte_arr: bytes, queue: queue.Queue) -> None:
        """Create the content to be insterted into the hex view and pass it to the given queue.

        This function runs is a separate thread, and feeds the queue with chunks of content to be 
        appended to the hex view.

        Args:
            byte_arr:
                The byte array to be formatted into the hex view.

            queue:
                The output queue to which the chunks of formatted text need to be sent to.
        
        """
        try:
            chars_per_byte = 2
            format_pad_len = 8 * chars_per_byte

            chunk_size = 0x1000

            for i, chunk_external in enumerate(chunker(byte_arr, chunk_size)):
                if self.abort_load:
                    break

                # String concatenation is faster with StringIO
                textbox_hex_content = StringIO()
                textbox_ascii_content = StringIO()
                textbox_address_content = StringIO()
                base_addr = chunk_size * i

                for j, chunk_16b in enumerate(chunker(chunk_external, self.BYTES_PER_ROW)):
                    
                    if self.abort_load:
                        break

                    hex_format = chunk_16b.hex(" ")
                    textbox_hex_content.write(hex_format + "\n")

                    ascii_format = "".join([chr(c) if 32 <= c <= 127 else "." for c in chunk_16b])
                    textbox_ascii_content.write(ascii_format + "\n")

                    textbox_address_content.write(format(base_addr + (j * self.BYTES_PER_ROW), 'X').rjust(format_pad_len, '0') + "\n")

                queue.put((textbox_address_content, textbox_hex_content, textbox_ascii_content))

            queue.put(None)
        except Exception as e:
            queue.put(e)

    def _add_content_to_hex_view(self) -> None:
        """Listens to the hex content thread queue and appends content to the hex view.
        
        This function runs in the context of the View, reads formatted text from the content
        creation thread and appends it to the hex view.

        If needed, this function reschedules itself to run again.
        """
        
        try:
            queue_item = self.hex_thread_queue.get(block = False)

            if queue_item is None or self.abort_load: 
                self._cleanup_hex_content(is_success = not self.abort_load)
                return
            elif isinstance(queue_item, Exception):
                raise queue_item

            textbox_address_content, textbox_hex_content, textbox_ascii_content = queue_item

            self.textbox_hex.insert(tk.END, textbox_hex_content.getvalue())
            self.textbox_ascii.insert(tk.END, textbox_ascii_content.getvalue())
            self.textbox_address.insert(tk.END, textbox_address_content.getvalue())
            self.textbox_address.tag_add(TAG_JUSTIFY_RIGHT, 1.0, tk.END)
            self.root.after_idle(self._add_content_to_hex_view)
        except tk.TclError as e:
            self._cleanup_hex_content(is_success = False)
            if not self.abort_load:
                raise e
        except queue.Empty:
            self.root.after_idle(self._add_content_to_hex_view)
        except Exception as e:
            self._cleanup_hex_content(is_success = False)
            self.callbacks[Events.SHOW_ERROR](f"Error: {str(e)}")

    def _cleanup_hex_content(self, is_success: bool) -> None:
        self.textbox_address.config(state = tk.DISABLED)
        self.textbox_hex.config(state = tk.DISABLED)
        self.textbox_ascii.config(state = tk.DISABLED)
        self.hex_content_done_cb(is_success)
        self.hex_content_done_cb = None
        self.hex_thread_queue = None

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
    
    @staticmethod
    def _highlight_to_tag(highlight_type: HighlightType):
        """Mapping of highlighter to tag."""
        tag = {
            HighlightType.DEFAULT: TAG_HIGHLIGHT,
            HighlightType.CUSTOM1: TAG_HIGHLIGHT_CUSTOM1,    
            HighlightType.CUSTOM2: TAG_HIGHLIGHT_CUSTOM2,
            HighlightType.CUSTOM3: TAG_HIGHLIGHT_CUSTOM3    
        }.get(highlight_type)

        return tag

    def unmark_range(self, start_offset: int, end_offset: int, highlight_type: HighlightType = HighlightType.DEFAULT) -> None:
        """Unmarks the given range for the given highlighter."""
        tag = self._highlight_to_tag(highlight_type)

        self.textbox_hex.tag_remove(tag, 
            self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, start_offset) if start_offset is not None else "1.0", 
            self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, end_offset, -1) if end_offset is not None else tk.END)
        self.textbox_ascii.tag_remove(tag, 
            self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_ASCII, start_offset) if start_offset is not None else "1.0", 
            self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_ASCII, end_offset) if end_offset is not None else tk.END)


    def mark_range(self, start_offset: int, end_offset: int, mark: bool, highlight_type: HighlightType = HighlightType.DEFAULT) -> None:
        """Highlight a range between the given offsets, and optionally jump to it.
        
        Args:
            start_offset:
                Offset to highlight from (absolute index of byte in file)
            end_offset:
                Offset to highlight to (absolute index of byte in file)
            highlight_type:
                Type of highlight to use. Use HighlightType.DEFAULT for selection, 
                or HighlightType.CUSTOMx for user triggered custom highlights
        """

        tag = self._highlight_to_tag(highlight_type)

        if start_offset is not None and end_offset is not None:
            # Mark in hex view:
            self.textbox_hex.tag_add(tag, 
                                     self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, start_offset), 
                                     self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, end_offset, -1)) # Remove trailing space

            # Mark in ASCII view:
            self.textbox_ascii.tag_add(tag, 
                                       self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_ASCII, start_offset), 
                                       self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_ASCII, end_offset))

    def make_visible(self, offset: Optional[int], length: int = 1, highlight: bool = False) -> None:
        """Jump to a given offset in the HEX viewer, and optionally highlight it.
        
        Args:
            offset:
                The offset to jump to. If is None, will clear the highlight.
            length:
                Length of sequence to highlight, if selected.
            highlight:
                In addition, highlight the location.
        """
        self.textbox_hex.tag_remove(TAG_GOTO, "1.0", tk.END)

        if offset is None:
            return

        location = self._offset_to_line_column(self.REPR_CHARS_PER_BYTE_HEX, offset)
        self.textbox_hex.see(location)

        if highlight:
            self.textbox_hex.tag_add(TAG_GOTO, location, f"{location}+{(length * self.REPR_CHARS_PER_BYTE_HEX) - 1}c")

        