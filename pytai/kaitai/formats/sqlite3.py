# Creative Commons Legal Code
#
# CC0 1.0 Universal
#
#     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
#     LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
#     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
#     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
#     REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
#     PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
#     THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
#     HEREUNDER.
#
# Statement of Purpose
#
# The laws of most jurisdictions throughout the world automatically confer
# exclusive Copyright and Related Rights (defined below) upon the creator
# and subsequent owner(s) (each and all, an "owner") of an original work of
# authorship and/or a database (each, a "Work").
#
# Certain owners wish to permanently relinquish those rights to a Work for
# the purpose of contributing to a commons of creative, cultural and
# scientific works ("Commons") that the public can reliably and without fear
# of later claims of infringement build upon, modify, incorporate in other
# works, reuse and redistribute as freely as possible in any form whatsoever
# and for any purposes, including without limitation commercial purposes.
# These owners may contribute to the Commons to promote the ideal of a free
# culture and the further production of creative, cultural and scientific
# works, or to gain reputation or greater distribution for their Work in
# part through the use and efforts of others.
#
# For these and/or other purposes and motivations, and without any
# expectation of additional consideration or compensation, the person
# associating CC0 with a Work (the "Affirmer"), to the extent that he or she
# is an owner of Copyright and Related Rights in the Work, voluntarily
# elects to apply CC0 to the Work and publicly distribute the Work under its
# terms, with knowledge of his or her Copyright and Related Rights in the
# Work and the meaning and intended legal effect of CC0 on those rights.
#
# 1. Copyright and Related Rights. A Work made available under CC0 may be
# protected by copyright and related or neighboring rights ("Copyright and
# Related Rights"). Copyright and Related Rights include, but are not
# limited to, the following:
#
#   i. the right to reproduce, adapt, distribute, perform, display,
#      communicate, and translate a Work;
#  ii. moral rights retained by the original author(s) and/or performer(s);
# iii. publicity and privacy rights pertaining to a person's image or
#      likeness depicted in a Work;
#  iv. rights protecting against unfair competition in regards to a Work,
#      subject to the limitations in paragraph 4(a), below;
#   v. rights protecting the extraction, dissemination, use and reuse of data
#      in a Work;
#  vi. database rights (such as those arising under Directive 96/9/EC of the
#      European Parliament and of the Council of 11 March 1996 on the legal
#      protection of databases, and under any national implementation
#      thereof, including any amended or successor version of such
#      directive); and
# vii. other similar, equivalent or corresponding rights throughout the
#      world based on applicable law or treaty, and any national
#      implementations thereof.
#
# 2. Waiver. To the greatest extent permitted by, but not in contravention
# of, applicable law, Affirmer hereby overtly, fully, permanently,
# irrevocably and unconditionally waives, abandons, and surrenders all of
# Affirmer's Copyright and Related Rights and associated claims and causes
# of action, whether now known or unknown (including existing as well as
# future claims and causes of action), in the Work (i) in all territories
# worldwide, (ii) for the maximum duration provided by applicable law or
# treaty (including future time extensions), (iii) in any current or future
# medium and for any number of copies, and (iv) for any purpose whatsoever,
# including without limitation commercial, advertising or promotional
# purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
# member of the public at large and to the detriment of Affirmer's heirs and
# successors, fully intending that such Waiver shall not be subject to
# revocation, rescission, cancellation, termination, or any other legal or
# equitable action to disrupt the quiet enjoyment of the Work by the public
# as contemplated by Affirmer's express Statement of Purpose.
#
# 3. Public License Fallback. Should any part of the Waiver for any reason
# be judged legally invalid or ineffective under applicable law, then the
# Waiver shall be preserved to the maximum extent permitted taking into
# account Affirmer's express Statement of Purpose. In addition, to the
# extent the Waiver is so judged Affirmer hereby grants to each affected
# person a royalty-free, non transferable, non sublicensable, non exclusive,
# irrevocable and unconditional license to exercise Affirmer's Copyright and
# Related Rights in the Work (i) in all territories worldwide, (ii) for the
# maximum duration provided by applicable law or treaty (including future
# time extensions), (iii) in any current or future medium and for any number
# of copies, and (iv) for any purpose whatsoever, including without
# limitation commercial, advertising or promotional purposes (the
# "License"). The License shall be deemed effective as of the date CC0 was
# applied by Affirmer to the Work. Should any part of the License for any
# reason be judged legally invalid or ineffective under applicable law, such
# partial invalidity or ineffectiveness shall not invalidate the remainder
# of the License, and in such case Affirmer hereby affirms that he or she
# will not (i) exercise any of his or her remaining Copyright and Related
# Rights in the Work or (ii) assert any associated claims and causes of
# action with respect to the Work, in either case contrary to Affirmer's
# express Statement of Purpose.
#
# 4. Limitations and Disclaimers.
#
#  a. No trademark or patent rights held by Affirmer are waived, abandoned,
#     surrendered, licensed or otherwise affected by this document.
#  b. Affirmer offers the Work as-is and makes no representations or
#     warranties of any kind concerning the Work, express, implied,
#     statutory or otherwise, including without limitation warranties of
#     title, merchantability, fitness for a particular purpose, non
#     infringement, or the absence of latent or other defects, accuracy, or
#     the present or absence of errors, whether or not discoverable, all to
#     the greatest extent permissible under applicable law.
#  c. Affirmer disclaims responsibility for clearing rights of other persons
#     that may apply to the Work or any use thereof, including without
#     limitation any person's Copyright and Related Rights in the Work.
#     Further, Affirmer disclaims responsibility for obtaining any necessary
#     consents, permissions or other rights required for any use of the
#     Work.
#  d. Affirmer understands and acknowledges that Creative Commons is not a
#     party to this document and has no duty or obligation with respect to
#     this CC0 or use of the Work.

# This file was compiled from a KSY format file downloaded from:
# https://github.com/kaitai-io/kaitai_struct_formats


# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

import vlq_base128_be
class Sqlite3(KaitaiStruct):
    """SQLite3 is a popular serverless SQL engine, implemented as a library
    to be used within other applications. It keeps its databases as
    regular disk files.
    
    Every database file is segmented into pages. First page (starting at
    the very beginning) is special: it contains a file-global header
    which specifies some data relevant to proper parsing (i.e. format
    versions, size of page, etc). After the header, normal contents of
    the first page follow.
    
    Each page would be of some type, and generally, they would be
    reached via the links starting from the first page. First page type
    (`root_page`) is always "btree_page".
    
    .. seealso::
       Source - https://www.sqlite.org/fileformat.html
    """

    class Versions(Enum):
        legacy = 1
        wal = 2

    class Encodings(Enum):
        utf_8 = 1
        utf_16le = 2
        utf_16be = 3
    SEQ_FIELDS = ["magic", "len_page_mod", "write_version", "read_version", "reserved_space", "max_payload_frac", "min_payload_frac", "leaf_payload_frac", "file_change_counter", "num_pages", "first_freelist_trunk_page", "num_freelist_pages", "schema_cookie", "schema_format", "def_page_cache_size", "largest_root_page", "text_encoding", "user_version", "is_incremental_vacuum", "application_id", "reserved", "version_valid_for", "sqlite_version_number", "root_page"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(16)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x53\x51\x4C\x69\x74\x65\x20\x66\x6F\x72\x6D\x61\x74\x20\x33\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x53\x51\x4C\x69\x74\x65\x20\x66\x6F\x72\x6D\x61\x74\x20\x33\x00", self.magic, self._io, u"/seq/0")
        self._debug['len_page_mod']['start'] = self._io.pos()
        self.len_page_mod = self._io.read_u2be()
        self._debug['len_page_mod']['end'] = self._io.pos()
        self._debug['write_version']['start'] = self._io.pos()
        self.write_version = KaitaiStream.resolve_enum(Sqlite3.Versions, self._io.read_u1())
        self._debug['write_version']['end'] = self._io.pos()
        self._debug['read_version']['start'] = self._io.pos()
        self.read_version = KaitaiStream.resolve_enum(Sqlite3.Versions, self._io.read_u1())
        self._debug['read_version']['end'] = self._io.pos()
        self._debug['reserved_space']['start'] = self._io.pos()
        self.reserved_space = self._io.read_u1()
        self._debug['reserved_space']['end'] = self._io.pos()
        self._debug['max_payload_frac']['start'] = self._io.pos()
        self.max_payload_frac = self._io.read_u1()
        self._debug['max_payload_frac']['end'] = self._io.pos()
        self._debug['min_payload_frac']['start'] = self._io.pos()
        self.min_payload_frac = self._io.read_u1()
        self._debug['min_payload_frac']['end'] = self._io.pos()
        self._debug['leaf_payload_frac']['start'] = self._io.pos()
        self.leaf_payload_frac = self._io.read_u1()
        self._debug['leaf_payload_frac']['end'] = self._io.pos()
        self._debug['file_change_counter']['start'] = self._io.pos()
        self.file_change_counter = self._io.read_u4be()
        self._debug['file_change_counter']['end'] = self._io.pos()
        self._debug['num_pages']['start'] = self._io.pos()
        self.num_pages = self._io.read_u4be()
        self._debug['num_pages']['end'] = self._io.pos()
        self._debug['first_freelist_trunk_page']['start'] = self._io.pos()
        self.first_freelist_trunk_page = self._io.read_u4be()
        self._debug['first_freelist_trunk_page']['end'] = self._io.pos()
        self._debug['num_freelist_pages']['start'] = self._io.pos()
        self.num_freelist_pages = self._io.read_u4be()
        self._debug['num_freelist_pages']['end'] = self._io.pos()
        self._debug['schema_cookie']['start'] = self._io.pos()
        self.schema_cookie = self._io.read_u4be()
        self._debug['schema_cookie']['end'] = self._io.pos()
        self._debug['schema_format']['start'] = self._io.pos()
        self.schema_format = self._io.read_u4be()
        self._debug['schema_format']['end'] = self._io.pos()
        self._debug['def_page_cache_size']['start'] = self._io.pos()
        self.def_page_cache_size = self._io.read_u4be()
        self._debug['def_page_cache_size']['end'] = self._io.pos()
        self._debug['largest_root_page']['start'] = self._io.pos()
        self.largest_root_page = self._io.read_u4be()
        self._debug['largest_root_page']['end'] = self._io.pos()
        self._debug['text_encoding']['start'] = self._io.pos()
        self.text_encoding = KaitaiStream.resolve_enum(Sqlite3.Encodings, self._io.read_u4be())
        self._debug['text_encoding']['end'] = self._io.pos()
        self._debug['user_version']['start'] = self._io.pos()
        self.user_version = self._io.read_u4be()
        self._debug['user_version']['end'] = self._io.pos()
        self._debug['is_incremental_vacuum']['start'] = self._io.pos()
        self.is_incremental_vacuum = self._io.read_u4be()
        self._debug['is_incremental_vacuum']['end'] = self._io.pos()
        self._debug['application_id']['start'] = self._io.pos()
        self.application_id = self._io.read_u4be()
        self._debug['application_id']['end'] = self._io.pos()
        self._debug['reserved']['start'] = self._io.pos()
        self.reserved = self._io.read_bytes(20)
        self._debug['reserved']['end'] = self._io.pos()
        self._debug['version_valid_for']['start'] = self._io.pos()
        self.version_valid_for = self._io.read_u4be()
        self._debug['version_valid_for']['end'] = self._io.pos()
        self._debug['sqlite_version_number']['start'] = self._io.pos()
        self.sqlite_version_number = self._io.read_u4be()
        self._debug['sqlite_version_number']['end'] = self._io.pos()
        self._debug['root_page']['start'] = self._io.pos()
        self.root_page = Sqlite3.BtreePage(self._io, self, self._root)
        self.root_page._read()
        self._debug['root_page']['end'] = self._io.pos()

    class Serial(KaitaiStruct):
        SEQ_FIELDS = ["code"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = vlq_base128_be.VlqBase128Be(self._io)
            self.code._read()
            self._debug['code']['end'] = self._io.pos()

        @property
        def is_blob(self):
            if hasattr(self, '_m_is_blob'):
                return self._m_is_blob

            self._m_is_blob =  ((self.code.value >= 12) and ((self.code.value % 2) == 0)) 
            return getattr(self, '_m_is_blob', None)

        @property
        def is_string(self):
            if hasattr(self, '_m_is_string'):
                return self._m_is_string

            self._m_is_string =  ((self.code.value >= 13) and ((self.code.value % 2) == 1)) 
            return getattr(self, '_m_is_string', None)

        @property
        def len_content(self):
            if hasattr(self, '_m_len_content'):
                return self._m_len_content

            if self.code.value >= 12:
                self._m_len_content = (self.code.value - 12) // 2

            return getattr(self, '_m_len_content', None)


    class BtreePage(KaitaiStruct):
        SEQ_FIELDS = ["page_type", "first_freeblock", "num_cells", "ofs_cells", "num_frag_free_bytes", "right_ptr", "cells"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['page_type']['start'] = self._io.pos()
            self.page_type = self._io.read_u1()
            self._debug['page_type']['end'] = self._io.pos()
            self._debug['first_freeblock']['start'] = self._io.pos()
            self.first_freeblock = self._io.read_u2be()
            self._debug['first_freeblock']['end'] = self._io.pos()
            self._debug['num_cells']['start'] = self._io.pos()
            self.num_cells = self._io.read_u2be()
            self._debug['num_cells']['end'] = self._io.pos()
            self._debug['ofs_cells']['start'] = self._io.pos()
            self.ofs_cells = self._io.read_u2be()
            self._debug['ofs_cells']['end'] = self._io.pos()
            self._debug['num_frag_free_bytes']['start'] = self._io.pos()
            self.num_frag_free_bytes = self._io.read_u1()
            self._debug['num_frag_free_bytes']['end'] = self._io.pos()
            if  ((self.page_type == 2) or (self.page_type == 5)) :
                self._debug['right_ptr']['start'] = self._io.pos()
                self.right_ptr = self._io.read_u4be()
                self._debug['right_ptr']['end'] = self._io.pos()

            self._debug['cells']['start'] = self._io.pos()
            self.cells = []
            for i in range(self.num_cells):
                if not 'arr' in self._debug['cells']:
                    self._debug['cells']['arr'] = []
                self._debug['cells']['arr'].append({'start': self._io.pos()})
                _t_cells = Sqlite3.RefCell(self._io, self, self._root)
                _t_cells._read()
                self.cells.append(_t_cells)
                self._debug['cells']['arr'][i]['end'] = self._io.pos()

            self._debug['cells']['end'] = self._io.pos()


    class CellIndexLeaf(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.sqlite.org/fileformat.html#b_tree_pages
        """
        SEQ_FIELDS = ["len_payload", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_payload']['start'] = self._io.pos()
            self.len_payload = vlq_base128_be.VlqBase128Be(self._io)
            self.len_payload._read()
            self._debug['len_payload']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            self._raw_payload = self._io.read_bytes(self.len_payload.value)
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = Sqlite3.CellPayload(_io__raw_payload, self, self._root)
            self.payload._read()
            self._debug['payload']['end'] = self._io.pos()


    class Serials(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self.entries = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['entries']:
                    self._debug['entries']['arr'] = []
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _t_entries = vlq_base128_be.VlqBase128Be(self._io)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class CellTableLeaf(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.sqlite.org/fileformat.html#b_tree_pages
        """
        SEQ_FIELDS = ["len_payload", "row_id", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_payload']['start'] = self._io.pos()
            self.len_payload = vlq_base128_be.VlqBase128Be(self._io)
            self.len_payload._read()
            self._debug['len_payload']['end'] = self._io.pos()
            self._debug['row_id']['start'] = self._io.pos()
            self.row_id = vlq_base128_be.VlqBase128Be(self._io)
            self.row_id._read()
            self._debug['row_id']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            self._raw_payload = self._io.read_bytes(self.len_payload.value)
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = Sqlite3.CellPayload(_io__raw_payload, self, self._root)
            self.payload._read()
            self._debug['payload']['end'] = self._io.pos()


    class CellPayload(KaitaiStruct):
        """
        .. seealso::
           Source - https://sqlite.org/fileformat2.html#record_format
        """
        SEQ_FIELDS = ["len_header_and_len", "column_serials", "column_contents"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_header_and_len']['start'] = self._io.pos()
            self.len_header_and_len = vlq_base128_be.VlqBase128Be(self._io)
            self.len_header_and_len._read()
            self._debug['len_header_and_len']['end'] = self._io.pos()
            self._debug['column_serials']['start'] = self._io.pos()
            self._raw_column_serials = self._io.read_bytes((self.len_header_and_len.value - 1))
            _io__raw_column_serials = KaitaiStream(BytesIO(self._raw_column_serials))
            self.column_serials = Sqlite3.Serials(_io__raw_column_serials, self, self._root)
            self.column_serials._read()
            self._debug['column_serials']['end'] = self._io.pos()
            self._debug['column_contents']['start'] = self._io.pos()
            self.column_contents = []
            for i in range(len(self.column_serials.entries)):
                if not 'arr' in self._debug['column_contents']:
                    self._debug['column_contents']['arr'] = []
                self._debug['column_contents']['arr'].append({'start': self._io.pos()})
                _t_column_contents = Sqlite3.ColumnContent(self.column_serials.entries[i], self._io, self, self._root)
                _t_column_contents._read()
                self.column_contents.append(_t_column_contents)
                self._debug['column_contents']['arr'][i]['end'] = self._io.pos()

            self._debug['column_contents']['end'] = self._io.pos()


    class CellTableInterior(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.sqlite.org/fileformat.html#b_tree_pages
        """
        SEQ_FIELDS = ["left_child_page", "row_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['left_child_page']['start'] = self._io.pos()
            self.left_child_page = self._io.read_u4be()
            self._debug['left_child_page']['end'] = self._io.pos()
            self._debug['row_id']['start'] = self._io.pos()
            self.row_id = vlq_base128_be.VlqBase128Be(self._io)
            self.row_id._read()
            self._debug['row_id']['end'] = self._io.pos()


    class CellIndexInterior(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.sqlite.org/fileformat.html#b_tree_pages
        """
        SEQ_FIELDS = ["left_child_page", "len_payload", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['left_child_page']['start'] = self._io.pos()
            self.left_child_page = self._io.read_u4be()
            self._debug['left_child_page']['end'] = self._io.pos()
            self._debug['len_payload']['start'] = self._io.pos()
            self.len_payload = vlq_base128_be.VlqBase128Be(self._io)
            self.len_payload._read()
            self._debug['len_payload']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            self._raw_payload = self._io.read_bytes(self.len_payload.value)
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = Sqlite3.CellPayload(_io__raw_payload, self, self._root)
            self.payload._read()
            self._debug['payload']['end'] = self._io.pos()


    class ColumnContent(KaitaiStruct):
        SEQ_FIELDS = ["as_int", "as_float", "as_blob", "as_str"]
        def __init__(self, ser, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.ser = ser
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if  ((self.serial_type.code.value >= 1) and (self.serial_type.code.value <= 6)) :
                self._debug['as_int']['start'] = self._io.pos()
                _on = self.serial_type.code.value
                if _on == 4:
                    self.as_int = self._io.read_u4be()
                elif _on == 6:
                    self.as_int = self._io.read_u8be()
                elif _on == 1:
                    self.as_int = self._io.read_u1()
                elif _on == 3:
                    self.as_int = self._io.read_bits_int_be(24)
                elif _on == 5:
                    self.as_int = self._io.read_bits_int_be(48)
                elif _on == 2:
                    self.as_int = self._io.read_u2be()
                self._debug['as_int']['end'] = self._io.pos()

            if self.serial_type.code.value == 7:
                self._debug['as_float']['start'] = self._io.pos()
                self.as_float = self._io.read_f8be()
                self._debug['as_float']['end'] = self._io.pos()

            if self.serial_type.is_blob:
                self._debug['as_blob']['start'] = self._io.pos()
                self.as_blob = self._io.read_bytes(self.serial_type.len_content)
                self._debug['as_blob']['end'] = self._io.pos()

            self._debug['as_str']['start'] = self._io.pos()
            self.as_str = (self._io.read_bytes(self.serial_type.len_content)).decode(u"UTF-8")
            self._debug['as_str']['end'] = self._io.pos()

        @property
        def serial_type(self):
            if hasattr(self, '_m_serial_type'):
                return self._m_serial_type

            self._m_serial_type = self.ser
            return getattr(self, '_m_serial_type', None)


    class RefCell(KaitaiStruct):
        SEQ_FIELDS = ["ofs_body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['ofs_body']['start'] = self._io.pos()
            self.ofs_body = self._io.read_u2be()
            self._debug['ofs_body']['end'] = self._io.pos()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            _pos = self._io.pos()
            self._io.seek(self.ofs_body)
            self._debug['_m_body']['start'] = self._io.pos()
            _on = self._parent.page_type
            if _on == 13:
                self._m_body = Sqlite3.CellTableLeaf(self._io, self, self._root)
                self._m_body._read()
            elif _on == 5:
                self._m_body = Sqlite3.CellTableInterior(self._io, self, self._root)
                self._m_body._read()
            elif _on == 10:
                self._m_body = Sqlite3.CellIndexLeaf(self._io, self, self._root)
                self._m_body._read()
            elif _on == 2:
                self._m_body = Sqlite3.CellIndexInterior(self._io, self, self._root)
                self._m_body._read()
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_body', None)


    @property
    def len_page(self):
        if hasattr(self, '_m_len_page'):
            return self._m_len_page

        self._m_len_page = (65536 if self.len_page_mod == 1 else self.len_page_mod)
        return getattr(self, '_m_len_page', None)


