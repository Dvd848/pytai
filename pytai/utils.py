"""Various utility functions.

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
import mmap
import os
from collections.abc import Iterable
from typing import Callable, Generator, List, Any
import inspect
import enum
import threading

def memory_map(filename: str, access=mmap.ACCESS_READ) -> mmap.mmap:
    """Map a file to the memory using mmap.

    Args:
        filename:
            Path to file to be mapped.
        access:
            Access type.
    
    Returns:
        Memory mapped object.
    """
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDONLY if access == mmap.ACCESS_READ else os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

def chunker(seq: Iterable, size: int) -> Generator[List, None, None]:
    """Divide iterable into chunks of given size.

    The returned generator will return chunks of requested size, except
    for the last chunk which might be smaller.

    Args:
        seq:
            Iterable to divide to chunks.
        size:
            Size of each chunk.
    
    Returns:
        Generator for chunks of the requested size.
    """
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def getproperties(obj):
    """Generator for properties of an object."""
    t = obj.__class__
    for tp in inspect.getmro(t):
        for name, value in vars(tp).items():
            if isinstance(value, property):
                yield name, getattr(obj, name)

def start_deamon(function: Callable, args: Iterable = ()) -> threading.Thread:
    """Start a deamon with the given function and arguments."""
    thread = threading.Thread(target = function, args = args)
    thread.daemon = True
    thread.start()
    return thread

class BackgroundTasks():
    """A class to track background operations."""

    class State(enum.Enum):
        STARTED     = enum.auto()
        FAILED      = enum.auto()
        SUCCEEDED   = enum.auto()

    def __init__(self) -> None:
        self.tasks = {}

    def start_task(self, task: Any) -> None:
        """Mark a task as started.
        
        Args:
            task:
                Identifier for the task.
        """
        if task in self.tasks:
            raise RuntimeError(f"Task {task} already started")
        self.tasks[task] = self.State.STARTED

    def task_done(self, task: Any, is_success: bool) -> None:
        """Mark a task as done.
        
        Args:
            is_success:
                True if task was successful, False otherwise
        """
        self.tasks[task] = self.State.SUCCEEDED if is_success else self.State.FAILED

    def all_done(self) -> bool:
        """Returns True if all tasks were completed."""
        return all([x != self.State.STARTED for x in self.tasks.values()])

    def all_succeeded(self) -> bool:
        """Returns True if all tasks were completed successfully."""
        return all([x == self.State.SUCCEEDED for x in self.tasks.values()])