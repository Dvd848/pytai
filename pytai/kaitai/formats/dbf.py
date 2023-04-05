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

class Dbf(KaitaiStruct):
    """.dbf is a relational database format introduced in DOS database
    management system dBASE in 1982.
    
    One .dbf file corresponds to one table and contains a series of headers,
    specification of fields, and a number of fixed-size records.
    
    .. seealso::
       Source - http://www.dbase.com/Knowledgebase/INT/db7_file_fmt.htm
    """

    class DeleteState(Enum):
        false = 32
        true = 42
    SEQ_FIELDS = ["header1", "header2", "header_terminator", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header1']['start'] = self._io.pos()
        self.header1 = Dbf.Header1(self._io, self, self._root)
        self.header1._read()
        self._debug['header1']['end'] = self._io.pos()
        self._debug['header2']['start'] = self._io.pos()
        self._raw_header2 = self._io.read_bytes(((self.header1.len_header - 12) - 1))
        _io__raw_header2 = KaitaiStream(BytesIO(self._raw_header2))
        self.header2 = Dbf.Header2(_io__raw_header2, self, self._root)
        self.header2._read()
        self._debug['header2']['end'] = self._io.pos()
        self._debug['header_terminator']['start'] = self._io.pos()
        self.header_terminator = self._io.read_bytes(1)
        self._debug['header_terminator']['end'] = self._io.pos()
        if not self.header_terminator == b"\x0D":
            raise kaitaistruct.ValidationNotEqualError(b"\x0D", self.header_terminator, self._io, u"/seq/2")
        self._debug['records']['start'] = self._io.pos()
        self._raw_records = []
        self.records = []
        for i in range(self.header1.num_records):
            if not 'arr' in self._debug['records']:
                self._debug['records']['arr'] = []
            self._debug['records']['arr'].append({'start': self._io.pos()})
            self._raw_records.append(self._io.read_bytes(self.header1.len_record))
            _io__raw_records = KaitaiStream(BytesIO(self._raw_records[i]))
            _t_records = Dbf.Record(_io__raw_records, self, self._root)
            _t_records._read()
            self.records.append(_t_records)
            self._debug['records']['arr'][i]['end'] = self._io.pos()

        self._debug['records']['end'] = self._io.pos()

    class Header2(KaitaiStruct):
        SEQ_FIELDS = ["header_dbase_3", "header_dbase_7", "fields"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if self._root.header1.dbase_level == 3:
                self._debug['header_dbase_3']['start'] = self._io.pos()
                self.header_dbase_3 = Dbf.HeaderDbase3(self._io, self, self._root)
                self.header_dbase_3._read()
                self._debug['header_dbase_3']['end'] = self._io.pos()

            if self._root.header1.dbase_level == 7:
                self._debug['header_dbase_7']['start'] = self._io.pos()
                self.header_dbase_7 = Dbf.HeaderDbase7(self._io, self, self._root)
                self.header_dbase_7._read()
                self._debug['header_dbase_7']['end'] = self._io.pos()

            self._debug['fields']['start'] = self._io.pos()
            self.fields = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['fields']:
                    self._debug['fields']['arr'] = []
                self._debug['fields']['arr'].append({'start': self._io.pos()})
                _t_fields = Dbf.Field(self._io, self, self._root)
                _t_fields._read()
                self.fields.append(_t_fields)
                self._debug['fields']['arr'][len(self.fields) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['fields']['end'] = self._io.pos()


    class Field(KaitaiStruct):
        SEQ_FIELDS = ["name", "datatype", "data_address", "length", "decimal_count", "reserved1", "work_area_id", "reserved2", "set_fields_flag", "reserved3"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(11), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['datatype']['start'] = self._io.pos()
            self.datatype = self._io.read_u1()
            self._debug['datatype']['end'] = self._io.pos()
            self._debug['data_address']['start'] = self._io.pos()
            self.data_address = self._io.read_u4le()
            self._debug['data_address']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u1()
            self._debug['length']['end'] = self._io.pos()
            self._debug['decimal_count']['start'] = self._io.pos()
            self.decimal_count = self._io.read_u1()
            self._debug['decimal_count']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(2)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['work_area_id']['start'] = self._io.pos()
            self.work_area_id = self._io.read_u1()
            self._debug['work_area_id']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(2)
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['set_fields_flag']['start'] = self._io.pos()
            self.set_fields_flag = self._io.read_u1()
            self._debug['set_fields_flag']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bytes(8)
            self._debug['reserved3']['end'] = self._io.pos()


    class Header1(KaitaiStruct):
        """
        .. seealso::
           - section 1.1 - http://www.dbase.com/Knowledgebase/INT/db7_file_fmt.htm
        """
        SEQ_FIELDS = ["version", "last_update_y", "last_update_m", "last_update_d", "num_records", "len_header", "len_record"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['last_update_y']['start'] = self._io.pos()
            self.last_update_y = self._io.read_u1()
            self._debug['last_update_y']['end'] = self._io.pos()
            self._debug['last_update_m']['start'] = self._io.pos()
            self.last_update_m = self._io.read_u1()
            self._debug['last_update_m']['end'] = self._io.pos()
            self._debug['last_update_d']['start'] = self._io.pos()
            self.last_update_d = self._io.read_u1()
            self._debug['last_update_d']['end'] = self._io.pos()
            self._debug['num_records']['start'] = self._io.pos()
            self.num_records = self._io.read_u4le()
            self._debug['num_records']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u2le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_record']['start'] = self._io.pos()
            self.len_record = self._io.read_u2le()
            self._debug['len_record']['end'] = self._io.pos()

        @property
        def dbase_level(self):
            if hasattr(self, '_m_dbase_level'):
                return self._m_dbase_level

            self._m_dbase_level = (self.version & 7)
            return getattr(self, '_m_dbase_level', None)


    class HeaderDbase3(KaitaiStruct):
        SEQ_FIELDS = ["reserved1", "reserved2", "reserved3"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(3)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(13)
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bytes(4)
            self._debug['reserved3']['end'] = self._io.pos()


    class HeaderDbase7(KaitaiStruct):
        SEQ_FIELDS = ["reserved1", "has_incomplete_transaction", "dbase_iv_encryption", "reserved2", "production_mdx", "language_driver_id", "reserved3", "language_driver_name", "reserved4"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(2)
            self._debug['reserved1']['end'] = self._io.pos()
            if not self.reserved1 == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.reserved1, self._io, u"/types/header_dbase_7/seq/0")
            self._debug['has_incomplete_transaction']['start'] = self._io.pos()
            self.has_incomplete_transaction = self._io.read_u1()
            self._debug['has_incomplete_transaction']['end'] = self._io.pos()
            self._debug['dbase_iv_encryption']['start'] = self._io.pos()
            self.dbase_iv_encryption = self._io.read_u1()
            self._debug['dbase_iv_encryption']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(12)
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['production_mdx']['start'] = self._io.pos()
            self.production_mdx = self._io.read_u1()
            self._debug['production_mdx']['end'] = self._io.pos()
            self._debug['language_driver_id']['start'] = self._io.pos()
            self.language_driver_id = self._io.read_u1()
            self._debug['language_driver_id']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bytes(2)
            self._debug['reserved3']['end'] = self._io.pos()
            if not self.reserved3 == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.reserved3, self._io, u"/types/header_dbase_7/seq/6")
            self._debug['language_driver_name']['start'] = self._io.pos()
            self.language_driver_name = self._io.read_bytes(32)
            self._debug['language_driver_name']['end'] = self._io.pos()
            self._debug['reserved4']['start'] = self._io.pos()
            self.reserved4 = self._io.read_bytes(4)
            self._debug['reserved4']['end'] = self._io.pos()


    class Record(KaitaiStruct):
        SEQ_FIELDS = ["deleted", "record_fields"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['deleted']['start'] = self._io.pos()
            self.deleted = KaitaiStream.resolve_enum(Dbf.DeleteState, self._io.read_u1())
            self._debug['deleted']['end'] = self._io.pos()
            self._debug['record_fields']['start'] = self._io.pos()
            self.record_fields = []
            for i in range(len(self._root.header2.fields)):
                if not 'arr' in self._debug['record_fields']:
                    self._debug['record_fields']['arr'] = []
                self._debug['record_fields']['arr'].append({'start': self._io.pos()})
                self.record_fields.append(self._io.read_bytes(self._root.header2.fields[i].length))
                self._debug['record_fields']['arr'][i]['end'] = self._io.pos()

            self._debug['record_fields']['end'] = self._io.pos()



