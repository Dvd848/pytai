"""Unit tests for the pytai application.

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
import sys
import unittest
import xml.etree.ElementTree as ET

from typing import Union, Callable

from unittest.mock import patch, MagicMock
from pathlib import Path

thisDir = Path(__file__).parent
sys.path.insert(0, str(thisDir.parent))

from pytai import application
from pytai.tests.xml_utils import *


class MockView(MagicMock):
    """Mock class to mock the application's View"""
    def __init__(self, *args, **kwargs):
        super().__init__()

    def add_tree_item(self, parent_handle: Union[ET.Element, str], **kwargs) -> ET.ElementTree:
        """Build an XML tree using the provided input."""
        if parent_handle == "":
            self.root = ET.Element("root")
            return self.root
        d = {k: str(v) for k, v in kwargs.items()}

        return ET.SubElement(parent_handle, "node", **d)

    def schedule_function(self, time_ms: int, callback: Callable[[], None]) -> None:
        callback()

    def start_worker(self, callback: Callable[[], bool]) -> None:
        reschedule = True
        while reschedule:
            reschedule = callback()

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

            with open(self.tmp_path / "actual_output.xml", "w", encoding="utf-8") as o:
                o.write(xml_to_str(app.view.root))

            expected_xml = xml_from_file(self.get_resource_path(f"{file_type}.xml"))

            try:
                xml_compare(app.view.root, expected_xml)
            except RuntimeError as e:
                self.fail(str(e))
    
    def test_png(self):
        self.generic_test("png")

    def test_bmp(self):
        self.generic_test("bmp")

    def test_zip(self):
        self.generic_test("zip")

    def test_elf(self):
        self.generic_test("elf")

    def test_wav(self):
        self.generic_test("wav")

    def test_ttf(self):
        self.generic_test("ttf")

if __name__ == "__main__":
    unittest.main()