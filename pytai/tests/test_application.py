import unittest
import xml.etree.ElementTree as ET

from typing import Union, Any
from xml.dom import minidom
from unittest.mock import patch, MagicMock
from pathlib import Path

from .. import application

class XmlUtils():
    """Various XML Utilities."""

    @classmethod
    def xml_compare(cls, x1: ET.Element, x2: ET.Element, excludes = None):
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

        if not cls.text_compare(x1.text, x2.text):
            raise RuntimeError(f'text: {x1.text} != {x2.text}')

        if not cls.text_compare(x1.tail, x2.tail):
            raise RuntimeError(f'tail: {x1.tail} != {x2.tail}')

        cl1 = list(x1)
        cl2 = list(x2)
        if len(cl1) != len(cl2):
            raise RuntimeError(f'children length differs, {len(cl1)} != {len(cl2)}')

        i = 0
        for c1, c2 in zip(cl1, cl2):
            i += 1
            if not c1.tag in excludes:
                if not cls.xml_compare(c1, c2, excludes):
                    raise RuntimeError(f'children {i} do not match: {c1.tag}')

        return True

    @staticmethod
    def text_compare(t1, t2):
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

    @staticmethod
    def xml_to_str(root: ET.ElementTree) -> str:
        """Pretty print an XML tree."""
        return minidom.parseString(ET.tostring(root).decode()).toprettyxml(indent="   ")

class MockView(MagicMock):
    """Mock class to mock the application's View"""
    def __init__(self, *args, **kwargs):
        super().__init__()

    def add_tree_item(self, parent_handle: Union[ET.Element, str], name: str, extra_info: str, start_offset: int, end_offset: int, is_metavar: bool) -> ET.ElementTree:
        """Build an XML tree using the provided input."""
        if parent_handle == "":
            self.root = ET.Element("root")
            return self.root
        return ET.SubElement(parent_handle, "node", name = str(name), extra_info = str(extra_info), 
                      start_offset = str(start_offset), end_offset = str(end_offset), is_metavar = str(is_metavar))


def KaitaiToXml(parser: "KaitaiParser", path: str) -> ET.ElementTree:
    """Transform a KaitaiStruct object to an XML tree.
    
    Args:
        parser: 
            A KaitaiParser instance matching the parsed file.
        
        path:
            Path to file to be converted to XML via the parser.

    Returns:
        XML representation of the file structure.

    """
    root = ET.Element("root")

    def recurse(parent_object, parent_node, parent_offset, is_array, invalidate_offsets):
        if is_array:
            for i, (arr_attr) in enumerate(parent_object):
                current_node = ET.SubElement(parent_node, "node", name = f"[{i}]", 
                                             extra_info = parser.get_item_description(arr_attr.value), 
                                             start_offset = str(arr_attr.start_offset if not invalidate_offsets else None), 
                                             end_offset = str(arr_attr.end_offset if not invalidate_offsets else None),
                                             is_metavar = str(False))
                recurse(arr_attr.value, current_node, parent_offset, False, invalidate_offsets)
        else:
            for child_attr in parser.get_children(parent_object):
                if (parent_offset != 0 and child_attr.start_offset == 0):
                    invalidate_offsets = True
                current_node = ET.SubElement(parent_node, "node", name = child_attr.name, 
                                             extra_info = parser.get_item_description(child_attr.value),
                                             start_offset = str(child_attr.start_offset if not invalidate_offsets else None), 
                                             end_offset = str(child_attr.end_offset if not invalidate_offsets else None),
                                             is_metavar = str(child_attr.is_metavar))
                recurse(child_attr.value, current_node, child_attr.start_offset, child_attr.is_array, invalidate_offsets)

    parsed_file = parser.parse(path)
    recurse(parsed_file, root, 0, False, False)
    parsed_file.close()
    return root

class TestOffsets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp_path = Path(__file__).resolve().parent / "tmp"
        cls.tmp_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_resource_path(file_name: str):
        return Path(__file__).resolve().parent / "resources" / file_name

    def generic_test(self, file_type):
        path = self.get_resource_path(f"{file_type}.{file_type}")
        format = {"kaitai_format": file_type}

        with patch(__name__ + '.application.v.View', MockView()):
            app = application.Application(file = path, format = format)

            with open(self.tmp_path / "actual_output.xml", "w") as o:
                o.write(XmlUtils.xml_to_str(app.view.root))

            parser = app.model.get_parser(**format)
            
            expected_xml = KaitaiToXml(parser, path)
            
            with open(self.tmp_path / "expected_output.xml", "w") as o:
                o.write(XmlUtils.xml_to_str(expected_xml))

            try:
                XmlUtils.xml_compare(app.view.root, expected_xml)
            except RuntimeError as e:
                self.fail(str(e))
    
    def test_png(self):
        self.generic_test("png")

    def test_bmp(self):
        self.generic_test("bmp")

    def test_zip(self):
        self.generic_test("zip")


# From root folder:
#   python -m unittest pytai.tests.test_application
#   python -m pytai.tests.test_application
if __name__ == "__main__":
    unittest.main()