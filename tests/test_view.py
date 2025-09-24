import unittest
from unittest.mock import MagicMock, patch
import sys

# Patch tkinter so tests can run headless
with patch.dict('sys.modules', {
    'tkinter': MagicMock(),
    'tkinter.messagebox': MagicMock(),
    'tkinter.simpledialog': MagicMock(),
}):
    from pytai.view.main import View
    from pytai.view.events import Events
    from pytai.common import HighlightType

class TestView(unittest.TestCase):
    def setUp(self):
        self.callbacks = {
            Events.REFRESH: MagicMock(),
            Events.GOTO: MagicMock(),
            Events.GET_CWD: MagicMock(return_value="."),
            Events.OPEN: MagicMock(),
            Events.SEARCH: MagicMock(),
            Events.FIND_NEXT: MagicMock(),
            Events.FIND_PREV: MagicMock(),
            Events.CANCEL_LOAD: MagicMock(),
        }
        self.view = View("TestApp", self.callbacks)

    def test_initialization(self):
        self.assertEqual(self.view.app_title, "TestApp")
        self.assertFalse(self.view.is_file_open)

    def test_set_status(self):
        self.view.status_bar.set_status = MagicMock()
        self.view.set_status("Ready")
        self.view.status_bar.set_status.assert_called_with("Ready")

    @patch("tkinter.messagebox.showerror")
    def test_display_error(self, mock_showerror):
        View.display_error("Error!")
        mock_showerror.assert_called_with("Error", "Error!")

    @patch("tkinter.messagebox.showwarning")
    def test_display_warning(self, mock_showwarning):
        View.display_warning("Warn!")
        mock_showwarning.assert_called_with("Warning", "Warn!")

    def test_set_current_file_path(self):
        self.view.menubar.toggle_loaded_file_commands = MagicMock()
        self.view.winfo_toplevel = MagicMock(return_value=MagicMock())
        self.view.set_current_file_path("file.bin")
        self.assertTrue(self.view.is_file_open)
        self.view.menubar.toggle_loaded_file_commands.assert_called_with(enable=True)
        self.view.set_current_file_path("")
        self.assertFalse(self.view.is_file_open)
        self.view.menubar.toggle_loaded_file_commands.assert_called_with(enable=False)

    def test_mark_range(self):
        self.view.hex_view.mark_range = MagicMock()
        self.view.hex_view.unmark_range = MagicMock()
        self.view.set_status = MagicMock()
        self.view.mark_range(0, 10, True)
        self.view.hex_view.mark_range.assert_called()
        self.view.mark_range(0, 10, False)
        self.view.hex_view.unmark_range.assert_called()

    def test_reset_calls_internal_resets(self):
        self.view.hex_view.reset = MagicMock()
        self.view.tree_view.reset = MagicMock()
        self.view.reset()
        self.view.hex_view.reset.assert_called_once()
        self.view.tree_view.reset.assert_called_once()

    def test_refresh_calls_callback_when_file_open(self):
        self.view.is_file_open = True
        self.view.callbacks[Events.REFRESH] = MagicMock()
        self.view.refresh(None)
        self.view.callbacks[Events.REFRESH].assert_called_once()

    def test_refresh_does_nothing_when_file_closed(self):
        self.view.is_file_open = False
        self.view.callbacks[Events.REFRESH] = MagicMock()
        self.view.refresh(None)
        self.view.callbacks[Events.REFRESH].assert_not_called()

    def test_show_goto_valid_and_invalid(self):
        self.view.is_file_open = True
        with patch("tkinter.simpledialog.askstring", return_value="123"):
            self.view.callbacks[Events.GOTO] = MagicMock()
            self.view.show_goto(None)
            self.view.callbacks[Events.GOTO].assert_called_with(123)
        with patch("tkinter.simpledialog.askstring", return_value="0x10"):
            self.view.callbacks[Events.GOTO] = MagicMock()
            self.view.show_goto(None)
            self.view.callbacks[Events.GOTO].assert_called_with(16)
        with patch("tkinter.simpledialog.askstring", return_value="bad"):
            with patch.object(self.view, "display_error") as mock_error:
                self.view.show_goto(None)
                mock_error.assert_called()

    def test_show_goto_does_nothing_when_file_closed(self):
        self.view.is_file_open = False
        with patch("tkinter.simpledialog.askstring") as mock_ask:
            self.view.show_goto(None)
            mock_ask.assert_not_called()

    def test_show_open_calls_openfilewindow(self):
        with patch("pytai.view.main.OpenFileWindow") as mock_open:
            self.view.show_open()
            mock_open.assert_called()

    def test_show_search_calls_searchwindow_when_file_open(self):
        self.view.is_file_open = True
        with patch("pytai.view.main.SearchWindow") as mock_search:
            self.view.show_search()
            mock_search.assert_called()

    def test_show_search_does_nothing_when_file_closed(self):
        self.view.is_file_open = False
        with patch("pytai.view.main.SearchWindow") as mock_search:
            self.view.show_search()
            mock_search.assert_not_called()

    def test_find_next_and_prev(self):
        self.view.is_file_open = True
        self.view.callbacks[Events.FIND_NEXT] = MagicMock()
        self.view.callbacks[Events.FIND_PREV] = MagicMock()
        self.view.find_next()
        self.view.callbacks[Events.FIND_NEXT].assert_called_once()
        self.view.find_prev()
        self.view.callbacks[Events.FIND_PREV].assert_called_once()

    def test_find_next_and_prev_do_nothing_when_file_closed(self):
        self.view.is_file_open = False
        self.view.callbacks[Events.FIND_NEXT] = MagicMock()
        self.view.callbacks[Events.FIND_PREV] = MagicMock()
        self.view.find_next()
        self.view.find_prev()
        self.view.callbacks[Events.FIND_NEXT].assert_not_called()
        self.view.callbacks[Events.FIND_PREV].assert_not_called()

    def test_show_about_calls_aboutwindow(self):
        with patch("pytai.view.main.AboutWindow") as mock_about:
            self.view.show_about()
            mock_about.assert_called()

    def test_show_loading_and_hide_loading(self):
        self.view.pw.pack_forget = MagicMock()
        with patch("pytai.view.main.LoadingWindow") as mock_loading:
            mock_instance = MagicMock()
            mock_loading.return_value = mock_instance
            self.view.show_loading()
            self.assertEqual(self.view.loading, mock_instance)
            self.view.pw.pack = MagicMock()
            self.view.hide_loading()
            mock_instance.stop.assert_called()
            self.assertIsNone(self.view.loading)

    def test_hide_loading_handles_missing_loading(self):
        self.view.loading = None
        self.view.pw.pack = MagicMock()
        # Should not raise
        self.view.hide_loading()

    def test_start_worker_reschedules(self):
        called = []
        def worker():
            called.append(1)
            return len(called) < 2
        self.view.root.after_idle = MagicMock(side_effect=lambda cb: cb())
        self.view.start_worker(worker)
        self.assertEqual(len(called), 2)

    def test_schedule_function(self):
        self.view.root.after = MagicMock()
        cb = MagicMock()
        self.view.schedule_function(100, cb)
        self.view.root.after.assert_called_with(100, cb)

if __name__ == "__main__":
    unittest.main()
