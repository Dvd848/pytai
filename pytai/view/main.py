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
import importlib.resources

from tkinter import messagebox, simpledialog, filedialog
from typing import Dict, Callable

from .menus import *
from .tree_area import *
from .hex_area import *
from .events import *
from .widgets import *

from ..common import *

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

        try:
            with importlib.resources.path(f"{__package__}.assets", "pytai.ico") as icon_path:
                self.iconbitmap(default = icon_path)
        except tk.TclError:
            try:
                with importlib.resources.path(f"{__package__}.assets", "pytai.gif") as icon_path:
                    icon = tk.PhotoImage(file = icon_path)
                    self.root.call('wm', 'iconphoto', self.root._w, icon)
            except Exception:
                pass


        self.menubar = MenuBar(self.root, {
            MenuBar.Events.REFRESH:                 self.refresh,
            MenuBar.Events.GOTO:                    self.show_goto,
            MenuBar.Events.OPEN:                    self.show_open,
        })
        self.root.config(menu = self.menubar)
        

        self.top_frame = tk.Frame()
        self.address_bar = AddressBar(self.top_frame)
        self.top_frame.pack(side=tk.TOP, fill = tk.BOTH)

        self.bottom_frame = tk.Frame()
        self.status_bar = StatusBar(self.bottom_frame)
        self.bottom_frame.pack(side=tk.BOTTOM, fill = tk.BOTH)

        self.pw = tk.PanedWindow(orient = 'horizontal') 
        self.tree_view = TreeAreaView(self, self.pw, self.address_bar, self.callbacks)
        self.hex_view = HexAreaView(self, self.pw, self.callbacks)

        self.pw.add(self.tree_view.widget, minsize = 450)
        self.pw.add(self.hex_view.widget, minsize = 740)
        self.pw.pack(fill = tk.BOTH, expand = True) 
        self.pw.configure(sashrelief = tk.RAISED)

        self.root.bind('<F5>', self.refresh)
        self.root.bind('<Control-g>', self.show_goto)
        self.root.bind('<Control-o>', self.show_open)

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

    def show_open(self, event) -> None:
        cwd = self.callbacks[Events.GET_CWD]()
        OpenFileWindow(self.root, cwd, self.callbacks[Events.OPEN])


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

    def show_loading(self) -> None:
        """Show the loading window."""
        
        # tkinter has better performance when the widgets aren't visible
        self.pw.pack_forget() 

        self.loading = LoadingWindow(self.root, self.callbacks[Events.CANCEL_LOAD])
        

    def hide_loading(self) -> None:
        """Hide the loading window."""

        try:
            self.pw.pack(fill = tk.BOTH, expand = True) # Show the widgets again
            self.loading.stop()
            self.loading = None
        except AttributeError:
            assert(self.loading is None)
            pass

    def start_worker(self, callback: Callable[[], bool]) -> None:
        """Start a worker provided by the caller.
        
        The worker will be called again as long as the previous call returned True.

        Args:
            callback:
                The callback to the worker. Expected to return a boolean indicating
                whether it should be called again.
        
        """
        reschedule = callback()
        if reschedule:
            self.root.after_idle(lambda: self.start_worker(callback))

    def schedule_function(self, time_ms: int, callback: Callable[[], None]) -> None:
        """Schedule a function to run after time_ms milliseconds.

        Function will run in the View context.
        
        Args:
            time_ms:
                Time in milliseconds after which the callback will be called.

            callback:
                Callback to call.
                
        """
        self.root.after(time_ms, callback)

class LoadingWindow():
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

        cancel_button = tk.Button(self.window, text="Cancel", padx = 3, pady = 3, command = self.cancel)
        cancel_button.pack(side = tk.BOTTOM, pady = 15)

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
        if messagebox.askokcancel("Cancel Loading...", "Are you sure you want to cancel loading?"):
            self.cancel_callback()
            self.stop()

    def on_close(self) -> None:
        """Handle an event where the user closes the loading window."""
        self.cancel()

    def center_window(self, parent):
        """Centers the window within the given parent window."""
        self.window.update()
        height = self.window.winfo_height()
        width = self.window.winfo_width()
        x = (parent.winfo_width() - width) // 2
        y = (parent.winfo_height() - height) // 2
        self.window.geometry('+{}+{}'.format(self.parent.winfo_rootx() + x, self.parent.winfo_rooty() + y))


class OpenFileWindow():
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
        lbox_scrollbar = tk.Scrollbar(lbox_frame)
        self.lbox = tk.Listbox(lbox_frame, height = 10)
        self.lbox.config(yscrollcommand= lbox_scrollbar.set)
        self.search_var.trace("w", lambda name, index, mode: self.update_list())

        lbox_scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.lbox.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
         
        label_format.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = tk.W)
        self.entry_format.grid(row = 1, column = 1, padx = 10, pady = 0)
        lbox_frame.grid(row = 2, column = 1, padx = 10, pady = 0, sticky='ew')
        
        self.update_list()

        button_ok = tk.Button(self.window,
                        text = "OK",
                        command = self.submit, width = 7)
        button_cancel = tk.Button(self.window,
                        text = "Cancel",
                        command = self.cancel, width = 7)

        button_ok.grid(row = 3, column = 1, padx = 5, pady = 12, sticky = tk.E)
        button_cancel.grid(row = 3, column = 2, padx = 5, pady = 12, sticky = tk.W)

        self.window.bind('<Return>', self.submit)
        self.window.bind('<Escape>', self.cancel)
        self.window.focus_force()

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = str(self.cwd),
                                              title = "Select a File",
                                              filetypes = [("all files", "*.*")])
        self.entry_file_name.delete(0, tk.END)
        self.entry_file_name.insert(0, filename)
      
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
            messagebox.showerror("Error", str(e))
        

    def cancel(self, event = None) -> None:
        """Cancel the operation."""
        self.window.destroy()