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

from .application import Application
from .common import *
from .utils import get_kaitai_format

def main() -> None:
    allowed_formats = kaitai_formats()
    parser = argparse.ArgumentParser(description='pytai: A Python-based Kaitai Struct Visualizer and HEX Viewer')
    parser.add_argument('file', action="store", nargs='?', default = None, help='Path to binary file')
    parser.add_argument('-kf', '--kaitai-format', action="store", 
                        choices = allowed_formats, metavar="FORMAT", 
                        help='Kaitai Format to use when parsing the file. '
                             f'Current formats found under "{SUBFOLDER_KAITAI}/{SUBFOLDER_FORMATS}" are: {", ".join(allowed_formats)}')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=get_version()))
    args = parser.parse_args()

    

    if args.file is not None:
        if args.kaitai_format is None:
            args.kaitai_format = get_kaitai_format(args.file)
            if args.kaitai_format is not None:
                print(f"Format detection: {args.kaitai_format}")

        if args.kaitai_format is None:
            parser.error("Format unknown. Requires --kaitai-format")
    else:
        if args.kaitai_format is not None:
            parser.error("--kaitai-format requires a file")
        #else: Just open the GUI

    format = {"kaitai_format": args.kaitai_format}

    app = Application(args.file, format)
    
    app.run()


if __name__ == "__main__":
    main()
