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
