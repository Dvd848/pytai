import unittest
from unittest.mock import MagicMock, patch
import mmap
import queue

from pytai.model import Model, HighlightType, HighlightDetails, PyTaiException, PyTaiWarning, PyTaiReparseException
from pytai.common import ByteRepresentation
from pytai.model import SearchContext, XRefManager

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    @patch('pytai.model.KaitaiParser')
    def test_parse_success(self, MockKaitaiParser):
        # Arrange
        mock_parser = MockKaitaiParser.return_value
        mock_context = MagicMock()
        mock_context.__enter__.return_value = "parsed_file"
        mock_context.__exit__.return_value = None
        mock_parser.parse.return_value = mock_context

        parser = self.model.get_parser(kaitai_format="dummy_format")
        with parser.parse("dummy_path") as result:
            self.assertEqual(result, "parsed_file")
        mock_parser.parse.assert_called_once_with("dummy_path")

    @patch('pytai.model.KaitaiParser')
    def test_parse_raises_exception(self, MockKaitaiParser):
        # Arrange
        mock_parser = MockKaitaiParser.return_value
        mock_parser.parse.side_effect = Exception("Parse error")

        parser = self.model.get_parser(kaitai_format="dummy_format")
        with self.assertRaises(Exception) as cm:
            with parser.parse("dummy_path"):
                pass
        self.assertEqual(str(cm.exception), "Parse error")

    @patch('pytai.model.KaitaiParser')
    def test_parse_context_manager_cleanup(self, MockKaitaiParser):
        # Arrange
        mock_parser = MockKaitaiParser.return_value
        mock_context = MagicMock()
        mock_context.__enter__.return_value = "parsed_file"
        mock_context.__exit__.return_value = None
        mock_parser.parse.return_value = mock_context

        parser = self.model.get_parser(kaitai_format="dummy_format")
        with parser.parse("dummy_path") as result:
            pass
        mock_context.__exit__.assert_called()

    @patch('pytai.model.KaitaiParser')
    def test_get_parser_caching(self, MockKaitaiParser):
        # Should cache parser instance
        parser1 = self.model.get_parser(kaitai_format="fmt1")
        parser2 = self.model.get_parser(kaitai_format="fmt1")
        self.assertIs(parser1, parser2)

    def test_get_parser_invalid(self):
        with self.assertRaises(RuntimeError):
            self.model.get_parser(other_arg="value")

    def test_process_highlight_add_remove(self):
        ht = next(ht for ht in HighlightType if HighlightType.is_custom(ht))
        # Add a highlight
        added = self.model.process_highlight(0, 10, True, ht)
        self.assertTrue(added)
        # Add overlapping highlight (should replace)
        added2 = self.model.process_highlight(0, 20, True, ht)
        self.assertTrue(added2)
        # Remove highlight
        removed = self.model.process_highlight(0, 20, False, ht)
        self.assertTrue(removed)
        # Remove non-existent
        removed2 = self.model.process_highlight(0, 20, False, ht)
        self.assertFalse(removed2)

    def test_process_highlight_no_action(self):
        ht = next(ht for ht in HighlightType if HighlightType.is_custom(ht))
        self.model.process_highlight(0, 10, True, ht)
        # Adding same segment again should do nothing
        self.assertFalse(self.model.process_highlight(0, 10, True, ht))

    def test_get_highlighted_colors(self):
        ht = next(ht for ht in HighlightType if HighlightType.is_custom(ht))
        self.model.process_highlight(5, 15, True, ht)
        res = self.model.get_highlighted_colors(5, 15)
        self.assertIn(ht, res)
        self.assertTrue(res[ht].is_active)
        self.assertTrue(res[ht].is_exact_match)
        # Test contained range
        res2 = self.model.get_highlighted_colors(7, 10)
        self.assertTrue(res2[ht].is_active)
        self.assertFalse(res2[ht].is_exact_match)

    def test_process_highlight_multiple_types(self):
        # Ensure highlights are independent per type
        types = [ht for ht in HighlightType if HighlightType.is_custom(ht)]
        self.model.process_highlight(1, 2, True, types[0])
        self.model.process_highlight(3, 4, True, types[1])
        self.assertIn((1, 2), self.model.highlight_context[types[0]])
        self.assertIn((3, 4), self.model.highlight_context[types[1]])
        self.assertNotIn((1, 2), self.model.highlight_context[types[1]])

    def test_process_highlight_remove_nonexistent(self):
        ht = next(ht for ht in HighlightType if HighlightType.is_custom(ht))
        # Remove a segment that was never added
        self.assertFalse(self.model.process_highlight(100, 200, False, ht))

    def test_get_highlighted_colors_no_highlight(self):
        ht = next(ht for ht in HighlightType if HighlightType.is_custom(ht))
        res = self.model.get_highlighted_colors(100, 200)
        self.assertIn(ht, res)
        self.assertFalse(res[ht].is_active)
        self.assertFalse(res[ht].is_exact_match)

    def test__s1_contains_s2(self):
        self.assertTrue(self.model._s1_contains_s2((0, 10), (2, 8)))
        self.assertFalse(self.model._s1_contains_s2((0, 10), (2, 12)))
        self.assertTrue(self.model._s1_contains_s2((0, 10), (0, 10)))

    def test_s1_contains_s2_edge_cases(self):
        # s1 and s2 are the same
        self.assertTrue(self.model._s1_contains_s2((5, 10), (5, 10)))
        # s2 outside s1
        self.assertFalse(self.model._s1_contains_s2((5, 10), (4, 11)))
        # s2 starts before s1
        self.assertFalse(self.model._s1_contains_s2((5, 10), (4, 8)))
        # s2 ends after s1
        self.assertFalse(self.model._s1_contains_s2((5, 10), (6, 11)))

    def test_get_byte_range(self):
        # Create a fake mmap object
        class FakeMmap:
            def __getitem__(self, key):
                return b'\x01\x02\x03\x04'[key]
            def hex(self, sep=None):
                return '01 02 03 04' if sep else '01020304'
        fake_mmap = FakeMmap()
        # HEX_STREAM
        self.assertEqual(self.model.get_byte_range(fake_mmap, 0, 4, ByteRepresentation.HEX_STREAM), '01020304')
        # HEX
        self.assertEqual(self.model.get_byte_range(fake_mmap, 0, 4, ByteRepresentation.HEX), '01 02 03 04')
        # RAW_BYTES
        self.assertEqual(self.model.get_byte_range(fake_mmap, 0, 4, ByteRepresentation.RAW_BYTES), b'\x01\x02\x03\x04')

    def test_get_byte_range_invalid_representation(self):
        class FakeMmap:
            def __getitem__(self, key):
                return b'\x01\x02\x03\x04'[key]
            def hex(self, sep=None):
                return '01 02 03 04' if sep else '01020304'
        fake_mmap = FakeMmap()
        # Should not raise, but return None for unknown representation
        result = self.model.get_byte_range(fake_mmap, 0, 4, None)
        self.assertIsNone(result)

    @patch('pytai.model.queue.Queue')
    def test_build_structure_tree_success(self, MockQueue):
        parser = MagicMock()
        parser.get_item_description.return_value = "desc"
        parser.get_children.return_value = []
        parsed_file = MagicMock()
        parsed_file.parse_errors = []
        parser.parse.return_value.__enter__.return_value = parsed_file
        comm_queue = MockQueue()
        comm_queue.put = MagicMock()
        abort_cb = MagicMock(return_value=False)
        self.model.build_structure_tree("dummy_path", parser, comm_queue, abort_cb)
        comm_queue.put.assert_any_call(None)

    @patch('pytai.model.queue.Queue')
    def test_build_structure_tree_parse_error(self, MockQueue):
        parser = MagicMock()
        parser.get_item_description.return_value = "desc"
        parser.get_children.return_value = []
        parsed_file = MagicMock()
        parsed_file.parse_errors = ["error"]
        parser.parse.return_value.__enter__.return_value = parsed_file
        comm_queue = MockQueue()
        comm_queue.put = MagicMock()
        abort_cb = MagicMock(return_value=False)
        self.model.build_structure_tree("dummy_path", parser, comm_queue, abort_cb)
        self.assertTrue(any(isinstance(call[0][0], PyTaiWarning) for call in comm_queue.put.call_args_list))

    @patch('pytai.model.queue.Queue')
    def test_build_structure_tree_abort(self, MockQueue):
        parser = MagicMock()
        parser.get_item_description.return_value = "desc"
        parser.get_children.return_value = []
        parsed_file = MagicMock()
        parsed_file.parse_errors = []
        parser.parse.return_value.__enter__.return_value = parsed_file
        comm_queue = MockQueue()
        comm_queue.put = MagicMock()
        abort_cb = MagicMock(return_value=True)
        self.model.build_structure_tree("dummy_path", parser, comm_queue, abort_cb)
        comm_queue.put.assert_any_call(None)

    @patch('pytai.model.queue.Queue')
    def test_build_structure_tree_exception(self, MockQueue):
        parser = MagicMock()
        parser.parse.side_effect = Exception("fail")
        comm_queue = MockQueue()
        comm_queue.put = MagicMock()
        abort_cb = MagicMock(return_value=False)
        self.model.build_structure_tree("dummy_path", parser, comm_queue, abort_cb)
        self.assertTrue(any(isinstance(call[0][0], PyTaiException) for call in comm_queue.put.call_args_list))

    def test_search_context_find_next_and_reverse(self):
        data = b"abc123abc456abc"
        mmap_mock = bytearray(data)
        ctx = SearchContext(mmap_mock, b"abc")
        # Forward search
        self.assertEqual(ctx.find_next(), 0)
        self.assertEqual(ctx.find_next(), 6)
        self.assertEqual(ctx.find_next(), 12)
        self.assertEqual(ctx.find_next(), -1)
        # Reverse search
        ctx = SearchContext(mmap_mock, b"abc")
        ctx.find_next()  # 0
        ctx.find_next()  # 6
        ctx.find_next()  # 12
        self.assertEqual(ctx.find_next(reverse=True), 6)
        self.assertEqual(ctx.find_next(reverse=True), 0)
        self.assertEqual(ctx.find_next(reverse=True), -1)

    def test_search_context_empty_term(self):
        mmap_mock = bytearray(b"abcdef")
        ctx = SearchContext(mmap_mock, b"")
        # Should always match at offset 0, then next offset
        self.assertEqual(ctx.find_next(), 0)
        self.assertEqual(ctx.find_next(), 1)

    def test_search_context_not_found(self):
        mmap_mock = bytearray(b"abcdef")
        ctx = SearchContext(mmap_mock, b"xyz")
        self.assertEqual(ctx.find_next(), -1)
        self.assertEqual(ctx.find_next(reverse=True), -1)

    def test_xref_manager_add_and_get(self):
        xref = XRefManager()
        # Add ranges
        xref.add_range(0, 100, "h1")
        xref.add_range(0, 10, "h2")
        xref.add_range(10, 20, "h3")
        xref.add_range(15, 20, "h5")
        xref.add_range(20, 100, "h6")
        xref.finalize()
        # Test handle retrieval
        self.assertEqual(xref.get_xref_handle(5), "h2")
        self.assertEqual(xref.get_xref_handle(12), "h3")
        self.assertEqual(xref.get_xref_handle(17), "h5")
        self.assertEqual(xref.get_xref_handle(50), "h6")
        self.assertEqual(xref.get_xref_handle(105), None)

    def test_xref_manager_no_match(self):
        xref = XRefManager()
        xref.add_range(10, 20, "h3")
        xref.finalize()
        self.assertIsNone(xref.get_xref_handle(5))
        self.assertEqual(xref.get_xref_handle(15), "h3")
        self.assertIsNone(xref.get_xref_handle(25))

    def test_xref_manager_inner_most(self):
        xref = XRefManager()
        xref.add_range(0, 100, "h1")
        xref.add_range(0, 10, "h2")
        xref.add_range(0, 10, "h3")
        xref.finalize()
        self.assertIn(xref.get_xref_handle(5), ["h2", "h3"])

    def test_xref_manager_finalize_empty(self):
        xref = XRefManager()
        xref.finalize()
        self.assertIsNone(xref.get_xref_handle(0))

    def test_xref_manager_handle_exact_end(self):
        xref = XRefManager()
        xref.add_range(0, 10, "h1")
        xref.finalize()
        # Should match at end offset
        self.assertEqual(xref.get_xref_handle(10), "h1")

    def test_xref_manager_handle_start_equals_end(self):
        xref = XRefManager()
        xref.add_range(5, 5, "h1")
        xref.finalize()
        # Should not match since start == end
        self.assertIsNone(xref.get_xref_handle(5))

    def test_xref_manager_multiple_ranges(self):
        xref = XRefManager()
        xref.add_range(0, 10, "h1")
        xref.add_range(0, 20, "h2")
        xref.add_range(0, 30, "h3")
        xref.finalize()
        self.assertEqual(xref.get_xref_handle(5), "h1")

    def test_xref_manager_out_of_bounds(self):
        xref = XRefManager()
        xref.add_range(10, 20, "h1")
        xref.finalize()
        # Offset before any range
        self.assertIsNone(xref.get_xref_handle(0))
        # Offset after any range
        self.assertIsNone(xref.get_xref_handle(21))

    def test_model_highlight_context_initialization(self):
        # All custom highlight types should have empty sets
        for ht in HighlightType:
            if HighlightType.is_custom(ht):
                self.assertEqual(self.model.highlight_context[ht], set())

    def test_model_get_parser_invalid_args(self):
        with self.assertRaises(RuntimeError):
            self.model.get_parser(foo="bar")

    def test_model_build_structure_tree_reparse(self):
        # Simulate reparse needed
        parser = MagicMock()
        parser.get_item_description.return_value = "desc"
        parser.get_children.return_value = [None]
        parsed_file = MagicMock()
        parsed_file.parse_errors = []
        parser.parse.return_value.__enter__.return_value = parsed_file
        comm_queue = MagicMock()
        comm_queue.put = MagicMock()
        comm_queue.get_nowait = MagicMock(side_effect=queue.Empty)
        abort_cb = MagicMock(return_value=False)
        self.model.build_structure_tree("dummy_path", parser, comm_queue, abort_cb)
        # Should call PyTaiReparseException at least once
        self.assertTrue(any(isinstance(call[0][0], PyTaiReparseException) for call in comm_queue.put.call_args_list))

    def test_model_build_structure_tree_abort_on_reparse(self):
        # Simulate abort during reparse
        parser = MagicMock()
        parser.get_item_description.return_value = "desc"
        parser.get_children.return_value = [None]
        parsed_file = MagicMock()
        parsed_file.parse_errors = []
        parser.parse.return_value.__enter__.return_value = parsed_file
        comm_queue = MagicMock()
        comm_queue.put = MagicMock()
        comm_queue.get_nowait = MagicMock(side_effect=queue.Empty)
        abort_cb = MagicMock(side_effect=[False, True])
        self.model.build_structure_tree("dummy_path", parser, comm_queue, abort_cb)
        comm_queue.put.assert_any_call(None)

if __name__ == "__main__":
    unittest.main()