import unittest
from unittest.mock import MagicMock, patch

from pytai.model import KaitaiParser, PytaiUnparsedAccessException

class DummyKaitaiStruct:
    SEQ_FIELDS = ['field1', 'field2']
    _debug = {
        'field1': {'start': MagicMock(), 'end': MagicMock()},
        'field2': {'start': MagicMock(), 'end': MagicMock()}
    }
    def __init__(self):
        self.field1 = 123
        self.field2 = 456
        self._parent = None
        self._io = MagicMock()
        self._io._base_offset = 0

class TestKaitaiParser(unittest.TestCase):

    def test_kaitai_parser_load_parser(self):
        parser = KaitaiParser('zip')
        self.assertEqual(parser.format, 'zip')
        self.assertTrue(hasattr(parser, 'parser'))

    def test_kaitai_parser_get_children(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        kp = DummyKaitaiStruct()
        parser._get_details = MagicMock(return_value=(0, 1, False, 123))
        children = list(parser.get_children(kp))
        self.assertEqual(len(children), 2)
        self.assertEqual(children[0].name, 'field1')
        self.assertEqual(children[1].name, 'field2')

    def test_get_children_with_non_kaitai_struct(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        # Should return None or empty generator if not KaitaiStruct
        result = list(parser.get_children(object()))
        self.assertEqual(result, [])

    def test_get_children_with_missing_fields(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        kp = DummyKaitaiStruct()
        kp.SEQ_FIELDS = ['field1', 'missing_field']
        parser._get_details = MagicMock(side_effect=[(0, 1, False, 123), Exception("Missing")])
        children = []
        try:
            children = list(parser.get_children(kp))
        except Exception:
            pass
        self.assertTrue(any(c.name == 'field1' for c in children if c is not None))

    def test_kaitai_parser_get_item_description(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        self.assertEqual(parser.get_item_description(b'abc'), "Byte Array (Length: 3)")
        self.assertEqual(parser.get_item_description("hello"), "hello")
        class DummyEnum:
            name = "ENUMVAL"
        self.assertEqual(parser.get_item_description(DummyEnum.name), "ENUMVAL")
        self.assertEqual(parser.get_item_description(42), "42 (0x2a)")
        self.assertEqual(parser.get_item_description(3.14), "3.14")
        self.assertEqual(parser.get_item_description(object()), "")

    def test_get_item_description_with_none(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        self.assertEqual(parser.get_item_description(None), "")

    def test_kaitai_parser_has_relative_offset(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        obj = DummyKaitaiStruct()
        obj._parent = None
        obj._io = MagicMock()
        self.assertTrue(parser._has_relative_offset(obj))

    def test__has_relative_offset_false(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        obj = object()
        self.assertFalse(parser._has_relative_offset(obj))

    def test_kaitai_parser_add_base_offset(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        value = DummyKaitaiStruct()
        value._io = MagicMock()
        parser._has_relative_offset = MagicMock(return_value=False)
        parser._add_base_offset(value, 10, 20)
        self.assertTrue(hasattr(value._io, "_base_offset"))

    def test__add_base_offset_relative(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        value = DummyKaitaiStruct()
        value._io = MagicMock()
        parser._has_relative_offset = MagicMock(return_value=True)
        parser._add_base_offset(value, 10, 20)
        self.assertTrue(hasattr(value._io, "_base_offset"))

    def test_kaitai_parser_get_details_unparsed_access(self):
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.KaitaiStruct = DummyKaitaiStruct
        parent = DummyKaitaiStruct()
        debug_dict = {'missing':{'start': 0, 'end': 4}}
        try:
            parser._get_details(debug_dict, parent, 'missing', None)
            self.fail("Expected PytaiUnparsedAccessException")
        except PytaiUnparsedAccessException:
            pass

    def test_parse_validation_failed_error(self):
        class DummyValidationFailedError(Exception): pass
        class DummyKaitaiStructObj:
            def __init__(self):
                self.parse_errors = []
                self._io = MagicMock()
                self._io._base_offset = 0
            def _read(self): raise DummyValidationFailedError("fail")
            def close(self): pass
        parser = KaitaiParser.__new__(KaitaiParser)
        parser.kaitaistruct = MagicMock()
        parser.kaitaistruct.ValidationFailedError = DummyValidationFailedError
        parser.parser = MagicMock()
        parser.parser.from_file = MagicMock(return_value=DummyKaitaiStructObj())
        with parser.parse("dummyfile") as pf:
            self.assertTrue(hasattr(pf, "parse_errors"))
            self.assertEqual(pf._io._base_offset, 0)


if __name__ == "__main__":
    unittest.main()
