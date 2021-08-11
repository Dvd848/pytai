import argparse


from pytai.application import Application
from pytai.common import *

def kaitai_formats():
    res = []
    for file in KAITAI_FORMAT_DIR.glob('*.py'):
        if not file.stem.startswith("__"):
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