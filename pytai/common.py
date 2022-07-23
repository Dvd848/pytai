"""Common definitions for the package.

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
import importlib.resources
from typing import List

APP_NAME = "pytai"
PACKAGE_NAME = "pytai-hex"

SUBFOLDER_KAITAI = "kaitai"
SUBFOLDER_FORMATS = "formats"

KAITAI_DIR = Path(__file__).resolve().parent / SUBFOLDER_KAITAI
KAITAI_FORMAT_DIR = KAITAI_DIR / SUBFOLDER_FORMATS

class PyTaiException(Exception):
    pass

class PyTaiViewException(Exception):
    pass

class PyTaiReparseException(Exception):
    pass

def kaitai_formats() -> List[str]:
    """Returns a list of supporeted Kaitai formats."""
    res = []
    for filename in importlib.resources.contents(f"pytai.{SUBFOLDER_KAITAI}.{SUBFOLDER_FORMATS}"):
        file = Path(filename)
        if file.suffix == ".py" and not file.stem.startswith("__"):
            res.append(file.stem)
    return res

def get_version() -> str:
    try:
        from importlib import metadata
        version = metadata.version(PACKAGE_NAME)
        if not version:
            raise ValueError("Can't find version from importlib metadata")
        return version
    except (ImportError, ValueError):
        pass

    try:
        from .version import __version__ # type: ignore
        return __version__
    except ImportError:
        pass

    try:
        import setuptools_scm
        version = setuptools_scm.get_version(root="..", relative_to=__file__)
        return version
    except (ImportError, LookupError):
        pass

    return ""