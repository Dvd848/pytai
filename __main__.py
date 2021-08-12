"""A basic Visualizer and HEX Viewer GUI in Python, based on Kaitai Struct parsing.

This program offers a basic user interface to analyze the internal structure of 
binary files for a number of predefined formats. 
It utilizes the Kaitai Struct project to allow the user to navigate through 
a given binary file and match its logical contents to the matching binary
representation as displayed in the HEX view.

Source:
    https://github.com/Dvd848/pytai

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
import argparse
import importlib.resources
from pathlib import Path

from pytai.application import Application
from pytai.common import *

def kaitai_formats():
    res = []
    for filename in importlib.resources.contents(f"pytai.{SUBFOLDER_KAITAI}.{SUBFOLDER_FORMATS}"):
        file = Path(filename)
        if file.suffix == ".py" and not file.stem.startswith("__"):
            res.append(file.stem)
    return res

def main() -> None:
    allowed_formats = kaitai_formats()
    parser = argparse.ArgumentParser(description='pytai: A Python-based Kaitai Struct Visualizer and HEX Viewer')
    parser.add_argument('-f', '--file', action="store", required = True, help='Path to binary file')
    parser.add_argument('-kf', '--kaitai-format', action="store", required = True, 
                        choices = allowed_formats, metavar="FORMAT", 
                        help='Kaitai Format to use when parsing the file. '
                             f'Current formats found under "{SUBFOLDER_KAITAI}/{SUBFOLDER_FORMATS}" are: {", ".join(allowed_formats)}')
    args = parser.parse_args()


    format = {"kaitai_format": args.kaitai_format}

    app = Application(args.file, format)
    
    app.run()


if __name__ == "__main__":
    main()