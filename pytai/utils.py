import mmap
import os
from collections.abc import Iterable
from typing import Generator, List

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