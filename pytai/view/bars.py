"""The 'View' Module of the application: Bar representation.

This file contains the implementation for various bars in the view.

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

class ReadOnlyBar():
    """A read-only bar."""
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.bar = tk.Entry(parent, borderwidth = kwargs.get("borderwidth", 4), relief = kwargs.get("relief", tk.FLAT))
        self.bar.pack(fill = tk.BOTH)

        self.bar.config(state="readonly")

    def set_text(self, text: str) -> None:
        """Set the text to display in the bar."""
        self.bar.config(state="normal")
        self.bar.delete(0, tk.END)
        self.bar.insert(0, text)
        self.bar.config(state="readonly")

    def reset(self) -> None:
        """Erase the bar's text."""
        self.set_text("")

class AddressBar(ReadOnlyBar):
    """The address bar containing the path to the current key."""
    def __init__(self, parent):
        super().__init__(parent)

    def set_address(self, address: str) -> None:
        """Set the address to the given string."""
        self.set_text(address)

class StatusBar(ReadOnlyBar):
    """The status bar, displaying information to the user."""
    def __init__(self, parent):
        super().__init__(parent, borderwidth = 2, relief = tk.RIDGE )

    def set_status(self, status: str) -> None:
        """Set the status to the given string."""
        self.set_text(" " + status)
