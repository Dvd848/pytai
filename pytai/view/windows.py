"""Various windows.

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

import enum
import re
import webbrowser

from tkinter import messagebox, filedialog
from typing import Callable


from .widgets import *
from ..common import *
from ..utils import get_kaitai_format

class BaseWindow():
    """Base class for windows."""

    def center_window(self, parent):
        """Centers the window within the given parent window."""
        self.window.update()
        height = self.window.winfo_height()
        width = self.window.winfo_width()
        x = (parent.winfo_width() - width) // 2
        y = (parent.winfo_height() - height) // 2
        self.window.geometry('+{}+{}'.format(self.parent.winfo_rootx() + x, self.parent.winfo_rooty() + y))

class LoadingWindow(BaseWindow):
    def __init__(self, parent, cancel_callback: Callable[[], None]):
        """Instantiate the class.
        
        Args:
            parent:
                Parent tk class.

            cancel_callback: 
                Callback to call if the user cancels loading.
                
        """
        self.parent = parent
        self.cancel_callback = cancel_callback

        self.window = tk.Toplevel(self.parent)
        self.window.title(f"Loading...") 
        self.window.resizable(0, 0)
        self.window.transient(self.parent)
        self.window.grab_set()
        #self.window.overrideredirect(True)

        self.progress = ttk.Progressbar(self.window, orient = tk.HORIZONTAL, length = 150, mode = 'indeterminate')
        self.progress.start()
        self.progress.pack(padx = 30, pady = (20, 0))

        self.cancel_button = tk.Button(self.window, text="Cancel", padx = 3, pady = 3, command = self.cancel)
        self.cancel_button.pack(side = tk.BOTTOM, pady = 15)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.center_window(self.parent)

    def stop(self) -> None:
        """Stop loading and kill the loading window."""
        try:
            self.window.destroy()
        except tk.TclError:
            pass

    def cancel(self) -> None:
        """Handle an event where the user clicks the 'cancel' button."""
        self.cancel_button.config(state = tk.DISABLED)
        if messagebox.askokcancel("Cancel Loading...", "Are you sure you want to cancel loading?"):
            self.cancel_callback()
            self.stop()
        else:
            self.cancel_button.config(state = tk.NORMAL)

    def on_close(self) -> None:
        """Handle an event where the user closes the loading window."""
        self.cancel()




class OpenFileWindow(BaseWindow):
    """Window for selecting the file to view."""
    
    def __init__(self, parent, cwd: str, open_file_callback: Callable[[str, str], None]):
        """Instantiate the class.
        
        Args:
            parent:
                Parent tk class.
                
            open_file_callback:
                Callback to be called once the user selects the file to open
        """
        self.parent = parent

        self.cwd = cwd
        self.open_file_callback = open_file_callback

        self.window = tk.Toplevel(self.parent)
        self.window.title(f"Open file...") 
        #self.window.geometry(f"400x300") 
        #self.window.attributes('-toolwindow', True)
        self.window.resizable(0, 0)
        self.window.transient(self.parent)
        self.window.grab_set()

        label_file_explorer = tk.Label(self.window,
                                       text = "File: ",
                                       anchor=tk.W)

        self.entry_file_name = tk.Entry(self.window, width = 40)

        button_explore = tk.Button(self.window,
                        text = "Browse...",
                        command = self.browseFiles)

        label_file_explorer.grid(row = 0, column = 0, padx = 5, pady = 20, sticky = tk.W)
        self.entry_file_name.grid(row = 0, column = 1, padx = 5, pady = 20)
        button_explore.grid(row = 0, column = 2, padx = 5, pady = 20)

        label_format = tk.Label(self.window,
                                text = "Format: ",
                                anchor=tk.W)

        self.search_var = tk.StringVar()
        self.filter_str = "Filter..."
        self.entry_format = EntryWithPlaceholder(self.window, placeholder = self.filter_str, textvariable = self.search_var, width = 40)

        lbox_frame = tk.Frame(self.window)
        self.lbox = tk.Listbox(lbox_frame, height = 10)
        lbox_scrollbar = tk.Scrollbar(lbox_frame, command = self.lbox.yview)
        self.lbox.config(yscrollcommand= lbox_scrollbar.set)
        self.search_var.trace("w", lambda name, index, mode: self.update_list())

        lbox_scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.lbox.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
         
        label_format.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = tk.W)
        self.entry_format.grid(row = 1, column = 1, padx = 10, pady = 0)
        lbox_frame.grid(row = 2, column = 1, padx = 10, pady = 0, sticky='ew')
        
        self.update_list()

        self.button_ok = tk.Button(self.window,
                        text = "OK",
                        command = self.submit, width = 7)
        self.button_cancel = tk.Button(self.window,
                        text = "Cancel",
                        command = self.cancel, width = 7)

        self.button_ok.grid(row = 3, column = 1, padx = 5, pady = 12, sticky = tk.E)
        self.button_cancel.grid(row = 3, column = 2, padx = 5, pady = 12, sticky = tk.W)

        self.window.bind('<Return>', self.submit)
        self.window.bind('<Escape>', self.cancel)
        self.window.focus_force()

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = str(self.cwd),
                                              title = "Select a File",
                                              filetypes = [("all files", "*.*")])
        self.entry_file_name.delete(0, tk.END)
        self.entry_file_name.insert(0, filename)

        try:
            format = get_kaitai_format(filename)
            if format is not None:
                self.select_from_list(format)
        except Exception:
            pass

    def select_from_list(self, name: str) -> None:
        self.search_var.set(name)
        for i, listbox_entry in enumerate(self.lbox.get(0, tk.END)):
            if listbox_entry == name:
                self.lbox.select_set(i)
                break
      
    def update_list(self):
        search_term = self.search_var.get()

        lbox_list = kaitai_formats()
         
        self.lbox.delete(0, tk.END)
     
        if search_term == self.filter_str:
            for item in lbox_list:
                self.lbox.insert(tk.END, item)
        else:
            for item in lbox_list:
                if search_term.lower() in item.lower():
                    self.lbox.insert(tk.END, item)

        if self.lbox.size() == 1:
            self.lbox.select_set(0)

    def submit(self, event = None) -> None:
        try:
            file_path = self.entry_file_name.get()
            if file_path.strip() == "":
                raise RuntimeError("Please select file to open")

            lbox_selection = self.lbox.curselection()
            if len(lbox_selection) == 0:
                raise RuntimeError("Please select format")

            format = self.lbox.get(lbox_selection)

            self.open_file_callback(file_path, {"kaitai_format": format})
            self.window.destroy()
        except Exception as e:
            self.button_ok.config(state = tk.DISABLED)
            self.button_cancel.config(state = tk.DISABLED)
            messagebox.showerror("Error", str(e))
            self.button_ok.config(state = tk.NORMAL)
            self.button_cancel.config(state = tk.NORMAL)
        

    def cancel(self, event = None) -> None:
        """Cancel the operation."""
        self.window.destroy()

class SearchWindow(BaseWindow):
    """Window for searching within the open file."""

    class SearchType(enum.Enum):
        # Must be sequential, zero-based
        HEX_VALUES  = 0
        TEXT_STRING = 1
    
    def __init__(self, parent, search_callback: Callable[[bytes], None]):
        """Instantiate the class.
        
        Args:
            parent:
                Parent tk class.

            search_callback:
                Callback to perform the search.
                
        """
        self.parent = parent
        self.search_callback = search_callback

        self.window = tk.Toplevel(self.parent)
        self.window.title(f"Find") 
        self.window.resizable(0, 0)
        self.window.transient(self.parent)
        self.window.grab_set()

        label_search_for = tk.Label(self.window,
                                       text = "Search for: ",
                                       anchor = tk.W)

        self.entry_search_term = tk.Entry(self.window, width = 40)

        label_search_for.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_search_term.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        label_as = tk.Label(self.window,
                                text = "As: ",
                                anchor=tk.W)

        self.search_type = ttk.Combobox(self.window, values = [v.name.replace("_", " ").title() for v in self.SearchType])
        self.search_type.current(self.SearchType.HEX_VALUES.value)
        label_as.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = tk.W)
        self.search_type.grid(row = 1, column = 1, padx = 5, pady = 5, sticky="ew")
                
        button_frame = tk.Frame(self.window)

        self.button_ok = tk.Button(button_frame,
                        text = "OK",
                        command = self.submit, width = 7)
        self.button_cancel = tk.Button(button_frame,
                        text = "Cancel",
                        command = self.cancel, width = 7)

        self.button_cancel.pack(side = tk.RIGHT)
        self.button_ok.pack(side = tk.RIGHT, padx = 10)
        button_frame.grid(row = 3, column = 1, padx = 5, pady = 12, sticky = tk.E)

        self.window.bind('<Return>', self.submit)
        self.window.bind('<Escape>', self.cancel)
        self.window.focus_force()
        self.entry_search_term.focus()

        self.center_window(self.parent)

    def _validate_search_term(cls, term: str, type: "SearchType"):
        """Validate the given search term according to the given type.

        A valid HEX search term must only contain pairs of legal HEX characters
        (and spaces which are discarded).

        An empty string is illegal.

        An exception is raised if the search term is invalid.
        
        Args:
            term:
                The search term.

            type:
                The type of the search term.
        """

        if type == cls.SearchType.HEX_VALUES:
            term = re.sub(r'\s+', '', term)
            if re.fullmatch(r"^[0-9a-fA-F]*$", term) is None or ( (len(term) % 2) != 0):
                raise ValueError("Invalid hex string")

        if term == "":
            raise ValueError("Please enter a search term")
            
    def _term_to_byte_arr(cls, term: str, type: "SearchType") -> bytes:
        """Converts a search term to a byte array.
        
        Args:
            term:
                Search term in string representation.

            type:
                Type of search term.

        Returns:
            Search term as byte array representation.
        """
        if type == cls.SearchType.HEX_VALUES:
            return bytes.fromhex(term)
        elif type == cls.SearchType.TEXT_STRING:
            return term.encode("utf-8")
        else:
            raise ValueError(f"Invalid search type: {type}")

    def submit(self, event = None) -> None:
        try:
            term = self.entry_search_term.get()
            type = self.SearchType(self.search_type.current())
            self._validate_search_term(term, type)
            byte_arr = self._term_to_byte_arr(term, type)
            self.search_callback(byte_arr)
            
            self.window.destroy()
        except Exception as e:
            self.button_ok.config(state = tk.DISABLED)
            self.button_cancel.config(state = tk.DISABLED)
            messagebox.showerror("Error", str(e))
            self.button_ok.config(state = tk.NORMAL)
            self.button_cancel.config(state = tk.NORMAL)
        

    def cancel(self, event = None) -> None:
        """Cancel the operation."""
        self.window.destroy()

class AboutWindow(BaseWindow):
    """The "about" window."""
    
    def __init__(self, parent):
        """Instantiate the class.
        
        Args:
            parent:
                Parent tk class.
        """
        self.parent = parent

        def open_link(event):
            webbrowser.open_new(event.widget.cget("text"))

        background = '#F8F8F8'

        self.window = tk.Toplevel(self.parent, bg = background)
        self.window.title(f"About {APP_NAME}") 
        self.window.resizable(0, 0)
        self.window.transient(self.parent)
        self.window.grab_set()

        row = 0

        frame = tk.Frame(self.window, background = background)

        title = tk.Label(frame, text = APP_NAME, font=("Arial", 18, 'bold'), background = background)
        title.grid(row = row, column = 0, pady = (0, 7))

        version_str = get_version()
        if version_str:
            row += 1
            version = tk.Label(frame, text = f"Version: {version_str}", font=("Arial", 8), background = background) 
            version.grid(row = row, column = 0, pady = (0, 7))

        row += 1
        line1 = tk.Label(frame, text = "A Kaitai Struct Visualizer and Hex Viewer GUI in Python", background = background)
        line1.grid(row = row, column = 0, sticky = tk.W)

        row += 1
        link1 = tk.Label(frame, text="https://github.com/Dvd848/pytai", fg="blue", cursor="hand2", background = background)
        link1.bind("<Button-1>", open_link)
        link1.grid(row = row, column = 0, sticky = tk.W, pady = (0, 15))

        row += 1
        line2 = tk.Label(frame, text = "Based on structure parsers provided by the Kaitai project", background = background)
        line2.grid(row = row, column = 0, sticky = tk.W)

        row += 1
        link2 = tk.Label(frame, text="https://kaitai.io/", fg="blue", cursor="hand2", background = background)
        link2.bind("<Button-1>", open_link)
        link2.grid(row = row, column = 0, sticky = tk.W)

        row += 1
        button_close = tk.Button(frame, text = "Close", command = self.close, width = 7)
        button_close.grid(row = row, column = 0, columnspan = 2)

        frame.pack(padx = 15, pady = 15)
        
        self.window.bind('<Escape>', self.close)
        self.center_window(self.parent)
        self.window.focus_force()


    def close(self, event = None) -> None:
        """Close the window."""
        self.window.destroy()
