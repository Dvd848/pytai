"""The 'Controller' module, connecting between the 'View' and 'Model'.

The application module acts as the 'Controller' and is responsible for
connecting between the 'View' and the 'Model' in the MVC pattern.

It receives user-triggered events from the View via callbacks, translates
them to operations which need to be performed by the Model, and updates
the View when the operations are completed.

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
from pathlib import Path
from typing import Union, Dict, Optional
from collections import namedtuple

import enum
import queue
import bisect

from . import view as v
from . import model as m

from . import utils

from .common import *
from .utils import *

class Application():
    class Task(enum.Enum):
        BUILD_TREE         = enum.auto()
        POPULATE_HEX_AREA  = enum.auto()

    XRefAttr = namedtuple("XRefAttr", "start_offset end_offset tree_handle")

    def __init__(self, file: Optional[str], format: Dict[str, Optional[str]], *args, **kwargs):

        # These callbacks are used to notify the application
        #  of events from the view
        callbacks = {
            v.Events.REFRESH:             self.cb_refresh,
            v.Events.STRUCTURE_SELECTED:  self.cb_structure_selected,
            v.Events.GOTO:                self.cb_goto,
            v.Events.OPEN:                self.cb_open,
            v.Events.GET_CWD:             self.cb_get_cwd,
            v.Events.CANCEL_LOAD:         self.cb_cancel_load,
            v.Events.SEARCH:              self.cb_search,
            v.Events.FIND_NEXT:           self.cb_find_next,
            v.Events.FIND_PREV:           lambda: self.cb_find_next(reverse = True),
            v.Events.GET_XREF:            self.cb_get_xref,
        }

        self.current_file_path = None
        self.format = None

        self.view = v.View(title = APP_NAME, callbacks = callbacks)
        self.model = m.Model()

        if (file is not None):
            # Need to run populate_view in the View context, *after* the View mainloop is in action 
            self.view.schedule_function(time_ms = 100, callback = lambda: self.populate_view(file, format))

    def run(self) -> None:
        """Runs the application."""
        self.view.mainloop()

    def populate_view(self, path_file: Union[str, Path], format: Dict[str, str]) -> None:
        """Populates the View for the given file.
        
        Args:
            path_file:
                Path to the file to be parsed.
            format:
                Dictionary containing the type of format to use for parsing the file.
                The file will be parsed based on the format type.
                Dictionary should contain one of the following pairs:
                    (-) kaitai_format -> Name of Kaitai format module from format folder
        """
        self.abort_load = False


        self.background_tasks = BackgroundTasks()
        self.background_tasks.start_task(self.Task.BUILD_TREE)
        self.background_tasks.start_task(self.Task.POPULATE_HEX_AREA)
        
        self.tree_parents = dict()
        self.xref_offset_map = []

        self.view.set_current_file_path("")
        self.search_context = None

        self.view.show_loading()

        self.current_file_path = Path(path_file).resolve()
        self.format = format
        parser = self.model.get_parser(**format)

        def abort_cb():
            return self.abort_load

        self.tree_thread_queue = queue.Queue()
        start_deamon(function = self.model.build_structure_tree, args = (self.current_file_path, parser, self.tree_thread_queue, abort_cb))
        self.view.start_worker(self._add_nodes_to_tree)

        def done_loading_hex(is_success: bool) -> None:
            self.background_tasks.task_done(self.Task.POPULATE_HEX_AREA, is_success)
            self._finalize_load()

        self.file_mmap = utils.memory_map(path_file)
        self.view.populate_hex_view(self.file_mmap, done_loading_hex)

    
    def _add_nodes_to_tree(self) -> bool:
        """Adds a subset of nodes to the tree view.

        This function will read up to MAX_NODES_PER_CALL nodes from the 
        node queue and add them to the tree. If needed, it will
        request to reschedule itself to add more nodes.
        The function stops requesting to reschedule itself when it reads
        None from the queue (or when any exception other than an empty queue
        exception is raised).
        
        Called in the context of the View.
        
        Returns:
            True if it needs to be called again, False otherwise.
        """
        MAX_NODES_PER_CALL = 100
        try:
            for _ in range(MAX_NODES_PER_CALL):
                queue_item = self.tree_thread_queue.get(block = False)

                if queue_item is None: 
                    # All done
                    self.background_tasks.task_done(self.Task.BUILD_TREE, is_success = True)
                    self._finalize_load()
                    return False
                elif isinstance(queue_item, PyTaiReparseException):
                    self.view.tree_view.reset() # TODO: Access via View API
                    self.tree_parents = dict()
                    self.xref_offset_map = []
                    return True
                elif isinstance(queue_item, Exception):
                    raise queue_item

                parent = self.tree_parents.get(queue_item["parent"], '')

                handle = self.view.add_tree_item(parent, name = queue_item["name"], 
                                                extra_info = queue_item["extra_info"], 
                                                start_offset = queue_item["start_offset"], 
                                                end_offset = queue_item["end_offset"], 
                                                is_metavar = queue_item["is_metavar"])
                self.tree_parents[queue_item["current"]] = handle
                if queue_item["start_offset"] is not None and queue_item["end_offset"] is not None and parent != "":
                    self.xref_offset_map.append(self.XRefAttr(queue_item["start_offset"], queue_item["end_offset"], handle))
            return True
        except queue.Empty:
            return True
        except PyTaiViewException as e:
            if not self.abort_load:
                self.view.display_error(str(e))
        except Exception as e:
            self.view.display_error(str(e))
            
        self.background_tasks.task_done(self.Task.BUILD_TREE, is_success = False)
        self.cb_cancel_load()
        self._finalize_load()
        return False

    def _finalize_load(self) -> None:
        """Finalize loading by performing cleanups and any other action needed at end of load."""
        if self.background_tasks.all_done():
            self.tree_parents = None
            self.tree_thread_queue = None
            self.view.hide_loading()
            #self.file_mmap.close()

        if self.background_tasks.all_succeeded():
            self.view.set_status("Loaded")
            self.view.set_current_file_path(self.current_file_path)
            self.xref_offset_map.sort()
            self.xref_offset_map_start = [x.start_offset for x in self.xref_offset_map]


    def cb_refresh(self) -> None:
        """Callback for an event where the user refreshes the view."""
        self.view.reset()
        self.view.set_status("Refreshing...")
        if self.current_file_path is not None:
            self.populate_view(self.current_file_path, self.format)

    def cb_structure_selected(self, path: str, start_offset: int, end_offset: int) -> None:
        """Callback for an event where the user selects a structure from the tree."""
        self.view.mark_range(start_offset, end_offset)
        self.view.make_visible(start_offset)

    def cb_goto(self, offset: int) -> None:
        """Callback for an event where the user wants to jump to a given offset."""
        if offset < 0 or offset >= len(self.file_mmap):
            raise ValueError("Offset out of range")
        self.view.make_visible(offset, highlight = True)
        self.view.set_status(f"Jumping to offset {hex(offset)} ({offset})")

    def cb_open(self, path: str, format: Dict[str, str]) -> None:
        """Callback for an event where the user wants to open a new file."""
        self.view.reset()
        self.populate_view(path, format)
        self.view.set_status(f"Opening {Path(path).resolve()}")

    def cb_get_cwd(self) -> str:
        """Callback for getting the current working directory.
        The CWD is defined as the parent directory of the last file opened,
        or the current directory if no file was previously opened.
        """
        if self.current_file_path is not None:
            return Path(self.current_file_path).parent

        return "."

    def cb_cancel_load(self) -> None:
        """Callback for an event where the user aborts loading."""
        self.abort_load = True
        self.view.hide_loading()
        self.view.reset()
        self.view.set_status(f"Aborted")
        self.view.set_current_file_path("")

    def cb_search(self, term: bytes) -> None:
        """Callback for an event where the user wants to search the binary."""
        # TODO: Should communicate with GUI thread via queue
        self.search_context = m.SearchContext(self.file_mmap, term)
        self.cb_find_next()

    def cb_find_next(self, reverse: bool = False) -> None:
        """Callback for an event where the user wants to find the next occurrence of the term.
        
        Args:
            reverse:
                Search in reverse direction.
        """

        if self.search_context is None:
            # If there is no term, open the original "Search" dialog
            self.view.show_search()
            return

        offset = self.search_context.find_next(reverse)
        if offset >= 0:
            self.view.make_visible(offset, length = len(self.search_context.term), highlight = True)
            self.view.set_status(f"Found at offset {hex(offset)} ({offset})")
        else:
            self.view.make_visible(None)
            self.view.set_status(f"Search term not found")
            self.view.display_error("Search term not found")

    def cb_get_xref(self, offset: int) -> None:
        """Given an offset in the file, mark the matching tree element.

        Marks the inner-most tree element which matches the offset.

        Args:
            offset:
                Offset within the file.
        
        """
        if offset > len(self.file_mmap):
            return

        index = bisect.bisect_right(self.xref_offset_map_start, offset)

        match = None
        
        try:
            index -= 1
            start_offset = self.xref_offset_map[index].start_offset
        except IndexError:
            return

        while index >= 0:
            t = self.xref_offset_map[index]
            if t.start_offset == start_offset and offset <= t.end_offset and t.start_offset != t.end_offset:
                match = t
                index -= 1
            else:
                break
            
        if match is not None:
            assert(match.start_offset <= offset <= match.end_offset)
            self.view.mark_tree_element(match.tree_handle)
            

