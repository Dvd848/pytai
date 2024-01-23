"""Various XML utilities.

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
import xml.etree.ElementTree as ET

from xml.dom import minidom
from typing import Optional, List

def xml_compare(x1: ET.Element, x2: ET.Element, excludes: Optional[List[str]] = None) -> bool:
    """Compares two xml eTrees.

    Based on https://stackoverflow.com/questions/24492895/

    Args:
        x1: 
            The first (sub)tree.
        x2: 
            The second (sub)tree.
        excludes: 
            List of string of attributes to exclude from comparison, or None.
    
    Returns:
        True if both XML trees match, raises exception otherwise.
    """

    if excludes is None:
        excludes = []

    if x1.tag != x2.tag:
        raise RuntimeError(f'Tags do not match: "{x1.tag}" and "{x2.tag}"')

    for name, value in x1.attrib.items():
        if not name in excludes:
            if x2.attrib.get(name) != value:
                raise RuntimeError(f'Attributes do not match: {name}={value}, {name}={x2.attrib.get(name)}')

    for name in x2.attrib.keys():
        if not name in excludes:
            if name not in x1.attrib:
                raise RuntimeError(f'x2 has an attribute x1 is missing: {name}')

    if not _text_compare(x1.text, x2.text):
        raise RuntimeError(f'text: {x1.text} != {x2.text}')

    if not _text_compare(x1.tail, x2.tail):
        raise RuntimeError(f'tail: {x1.tail} != {x2.tail}')

    cl1 = list(x1)
    cl2 = list(x2)
    if len(cl1) != len(cl2):
        raise RuntimeError(f'children length differs, {len(cl1)} != {len(cl2)}')

    i = 0
    for c1, c2 in zip(cl1, cl2):
        i += 1
        if not c1.tag in excludes:
            if not xml_compare(c1, c2, excludes):
                raise RuntimeError(f'children {i} do not match: {c1.tag}')

    return True


def _text_compare(t1: Optional[str], t2: Optional[str]) -> bool:
    """Compare two text strings, ignoring wrapping whitespaces.

    Args:
        t1:
            First text.
        t2:
            Second text.
    
    Returns:
        True if they are equal, False otherwise.
    """
    if not t1 and not t2:
        return True
    
    #if t1 == '*' or t2 == '*':
    #    return True

    return (t1 or '').strip() == (t2 or '').strip()

def xml_to_str(root: ET.ElementTree) -> str:
    """Pretty print an XML tree."""
    return minidom.parseString(ET.tostring(root).decode()).toprettyxml(indent="   ")

def xml_from_file(path: str) -> ET.ElementTree:
    """Return XML ElementTree from given file path"""
    with open(path, encoding="utf-8") as f:
        return ET.fromstring(f.read())
