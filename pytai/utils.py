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
from typing import Generator, List
import inspect

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