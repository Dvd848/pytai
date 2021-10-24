"""A utility to output an XML representation of a binary file using Kaitai.

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
from typing import Union, List
from pathlib import Path

import xml.etree.ElementTree as ET
import argparse
import sys

try:
    from .. import model
    from .xml_utils import *
except ImportError:
    if __name__ == "__main__":
        sys.exit(f'This utility needs to be run from the root folder:\npython -m pytai.tests.{Path(sys.argv[0]).stem}')
    else:
        raise


def kaitai_to_xml(parser: "KaitaiParser", path: str) -> ET.ElementTree:
    """Transform a KaitaiStruct object to an XML tree.
    
    Args:
        parser: 
            A KaitaiParser instance matching the parsed file.
        
        path:
            Path to file to be converted to XML via the parser.

    Returns:
        XML representation of the file structure.

    """
    reparse_needed = False

    def recurse(parent_object: Union[List["KaitaiStruct"], "KaitaiStruct"], parent_node: ET.Element, is_array: bool) -> None:
        """Recursive function to built the XML tree.

        Args:
            parent_object:
                A KaitaiStruct from which the child nodes will be extracted (if is_array is False),
                or a list of KaitaiStructs (if is_array is True).

            parent_node:
                An XML node representing the parent of child nodes.

            is_array:
                True if parent_object is a list, false otherwise.

        """
        nonlocal reparse_needed

        if is_array:
            values = parent_object
        else:
            values = parser.get_children(parent_object)

        for child_attr in values:
            if child_attr is not None:
                current_node = ET.SubElement(parent_node, "node", name = child_attr.name, 
                                                extra_info = parser.get_item_description(child_attr.value), 
                                                start_offset = str(child_attr.start_offset), 
                                                end_offset = str(child_attr.end_offset),
                                                is_metavar = str(child_attr.is_metavar))
                recurse(child_attr.value, current_node, child_attr.is_array)
            else:
                reparse_needed = True

    max_retries = 5
    with parser.parse(path) as parsed_file:
        for _ in range(max_retries):
            root = ET.Element("root")
            recurse(parent_object = parsed_file, parent_node = root, is_array = False)
            if reparse_needed:
                reparse_needed = False
                # Try again
            else:
                return root

    raise RuntimeError(f"Could not parse {path}")

def save_kaitai_to_xml(kaitai_format: str, input_path: Union[str, Path], output_path: Union[str, Path]) -> None:
    """Save an XML representation of the given file to the given output path.
    
    Args:
        kaitai_format:
            The Kaitai format used to parse the given file.

        input_path:
            Path to input file to be parsed.

        output_path:
            Path to output file where XML will be saved to.
    """
    m = model.Model()
    format = {"kaitai_format": kaitai_format}
    parser = m.get_parser(**format)
    
    xml_representation = kaitai_to_xml(parser, input_path)
    
    with open(output_path, "w") as o:
        o.write(xml_to_str(xml_representation))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A utility to output an XML representation of a binary file using Kaitai')

    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-f', '--file', action="store", help='Path to binary file')
    group.add_argument('-d', '--dir', action="store", 
                        help='Path to a directory containing multiple binary files (all files will be translated according to name)')

    parser.add_argument('-kf', '--kaitai-format', action="store", help = "Kaitai format (see list in pytai's usage) - required for 'file'")

    parser.add_argument('-o', '--output', action="store", 
                        help='Path to output file (default: Input file\'s path with XML extention) - optional for "file", forbidden for "dir"')
                        
    args = parser.parse_args()

    if args.file is not None:
        if args.kaitai_format is None:
            parser.error("Must provide 'kaitai-format' if 'file' was provided")
        files = [args.file]
    else:
        if args.output is not None:
            parser.error("'output' cannot be provided for 'dir'")
        directory = Path(args.dir).resolve()
        if not directory.is_dir():
            parser.error("'dir' must contain a legal directory path")
        files = [x for x in directory.glob("*") if not x.suffix.lower() == ".xml"]

    for file in files:
        input_path = Path(file)
        output_path = args.output

        if output_path is None:
            output_path = input_path.parent / (input_path.stem + ".xml")

        format = args.kaitai_format
        if args.kaitai_format is None:
            format = input_path.stem

        print(f"Processing {input_path} as {format}")
        save_kaitai_to_xml(format, input_path, output_path)
        print(f"Saved to '{output_path}'")
    print(f"If used for validation purposed, please review the output manually since the output relies on the model.")