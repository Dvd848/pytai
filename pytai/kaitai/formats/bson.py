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
import collections
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bson(KaitaiStruct):
    """BSON, short for Binary JSON, is a binary-encoded serialization of JSON-like documents. Like JSON, BSON supports the embedding of documents and arrays within other documents and arrays. BSON also contains extensions that allow representation of data types that are not part of the JSON spec. For example, BSON has a Date type and a BinData type. BSON can be compared to binary interchange formats, like Protocol Buffers. BSON is more "schemaless" than Protocol Buffers, which can give it an advantage in flexibility but also a slight disadvantage in space efficiency (BSON has overhead for field names within the serialized data). BSON was designed to have the following three characteristics:
      * Lightweight. Keeping spatial overhead to a minimum is important for any data representation format, especially when used over the network.
      * Traversable. BSON is designed to be traversed easily. This is a vital property in its role as the primary data representation for MongoDB.
      * Efficient. Encoding data to BSON and decoding from BSON can be performed very quickly in most languages due to the use of C data types.
    """
    SEQ_FIELDS = ["len", "fields", "terminator"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['len']['start'] = self._io.pos()
        self.len = self._io.read_s4le()
        self._debug['len']['end'] = self._io.pos()
        self._debug['fields']['start'] = self._io.pos()
        self._raw_fields = self._io.read_bytes((self.len - 5))
        _io__raw_fields = KaitaiStream(BytesIO(self._raw_fields))
        self.fields = Bson.ElementsList(_io__raw_fields, self, self._root)
        self.fields._read()
        self._debug['fields']['end'] = self._io.pos()
        self._debug['terminator']['start'] = self._io.pos()
        self.terminator = self._io.read_bytes(1)
        self._debug['terminator']['end'] = self._io.pos()
        if not self.terminator == b"\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00", self.terminator, self._io, u"/seq/2")

    class Timestamp(KaitaiStruct):
        """Special internal type used by MongoDB replication and sharding. First 4 bytes are an increment, second 4 are a timestamp."""
        SEQ_FIELDS = ["increment", "timestamp"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['increment']['start'] = self._io.pos()
            self.increment = self._io.read_u4le()
            self._debug['increment']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_u4le()
            self._debug['timestamp']['end'] = self._io.pos()


    class BinData(KaitaiStruct):
        """The BSON "binary" or "BinData" datatype is used to represent arrays of bytes. It is somewhat analogous to the Java notion of a ByteArray. BSON binary values have a subtype. This is used to indicate what kind of data is in the byte array. Subtypes from zero to 127 are predefined or reserved. Subtypes from 128-255 are user-defined."""

        class Subtype(Enum):
            generic = 0
            function = 1
            byte_array_deprecated = 2
            uuid_deprecated = 3
            uuid = 4
            md5 = 5
            custom = 128
        SEQ_FIELDS = ["len", "subtype", "content"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_s4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['subtype']['start'] = self._io.pos()
            self.subtype = KaitaiStream.resolve_enum(Bson.BinData.Subtype, self._io.read_u1())
            self._debug['subtype']['end'] = self._io.pos()
            self._debug['content']['start'] = self._io.pos()
            _on = self.subtype
            if _on == Bson.BinData.Subtype.byte_array_deprecated:
                self._raw_content = self._io.read_bytes(self.len)
                _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
                self.content = Bson.BinData.ByteArrayDeprecated(_io__raw_content, self, self._root)
                self.content._read()
            else:
                self.content = self._io.read_bytes(self.len)
            self._debug['content']['end'] = self._io.pos()

        class ByteArrayDeprecated(KaitaiStruct):
            """The BSON "binary" or "BinData" datatype is used to represent arrays of bytes. It is somewhat analogous to the Java notion of a ByteArray. BSON binary values have a subtype. This is used to indicate what kind of data is in the byte array. Subtypes from zero to 127 are predefined or reserved. Subtypes from 128-255 are user-defined."""
            SEQ_FIELDS = ["len", "content"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['len']['start'] = self._io.pos()
                self.len = self._io.read_s4le()
                self._debug['len']['end'] = self._io.pos()
                self._debug['content']['start'] = self._io.pos()
                self.content = self._io.read_bytes(self.len)
                self._debug['content']['end'] = self._io.pos()



    class ElementsList(KaitaiStruct):
        SEQ_FIELDS = ["elements"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['elements']['start'] = self._io.pos()
            self.elements = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['elements']:
                    self._debug['elements']['arr'] = []
                self._debug['elements']['arr'].append({'start': self._io.pos()})
                _t_elements = Bson.Element(self._io, self, self._root)
                _t_elements._read()
                self.elements.append(_t_elements)
                self._debug['elements']['arr'][len(self.elements) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['elements']['end'] = self._io.pos()


    class Cstring(KaitaiStruct):
        SEQ_FIELDS = ["str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['str']['end'] = self._io.pos()


    class String(KaitaiStruct):
        SEQ_FIELDS = ["len", "str", "terminator"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_s4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes((self.len - 1))).decode(u"UTF-8")
            self._debug['str']['end'] = self._io.pos()
            self._debug['terminator']['start'] = self._io.pos()
            self.terminator = self._io.read_bytes(1)
            self._debug['terminator']['end'] = self._io.pos()
            if not self.terminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.terminator, self._io, u"/types/string/seq/2")


    class Element(KaitaiStruct):

        class BsonType(Enum):
            min_key = -1
            end_of_object = 0
            number_double = 1
            string = 2
            document = 3
            array = 4
            bin_data = 5
            undefined = 6
            object_id = 7
            boolean = 8
            utc_datetime = 9
            jst_null = 10
            reg_ex = 11
            db_pointer = 12
            javascript = 13
            symbol = 14
            code_with_scope = 15
            number_int = 16
            timestamp = 17
            number_long = 18
            number_decimal = 19
            max_key = 127
        SEQ_FIELDS = ["type_byte", "name", "content"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type_byte']['start'] = self._io.pos()
            self.type_byte = KaitaiStream.resolve_enum(Bson.Element.BsonType, self._io.read_u1())
            self._debug['type_byte']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = Bson.Cstring(self._io, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()
            self._debug['content']['start'] = self._io.pos()
            _on = self.type_byte
            if _on == Bson.Element.BsonType.code_with_scope:
                self.content = Bson.CodeWithScope(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.reg_ex:
                self.content = Bson.RegEx(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.number_double:
                self.content = self._io.read_f8le()
            elif _on == Bson.Element.BsonType.symbol:
                self.content = Bson.String(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.timestamp:
                self.content = Bson.Timestamp(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.number_int:
                self.content = self._io.read_s4le()
            elif _on == Bson.Element.BsonType.document:
                self.content = Bson(self._io)
                self.content._read()
            elif _on == Bson.Element.BsonType.object_id:
                self.content = Bson.ObjectId(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.javascript:
                self.content = Bson.String(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.utc_datetime:
                self.content = self._io.read_s8le()
            elif _on == Bson.Element.BsonType.boolean:
                self.content = self._io.read_u1()
            elif _on == Bson.Element.BsonType.number_long:
                self.content = self._io.read_s8le()
            elif _on == Bson.Element.BsonType.bin_data:
                self.content = Bson.BinData(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.string:
                self.content = Bson.String(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.db_pointer:
                self.content = Bson.DbPointer(self._io, self, self._root)
                self.content._read()
            elif _on == Bson.Element.BsonType.array:
                self.content = Bson(self._io)
                self.content._read()
            elif _on == Bson.Element.BsonType.number_decimal:
                self.content = Bson.F16(self._io, self, self._root)
                self.content._read()
            self._debug['content']['end'] = self._io.pos()


    class DbPointer(KaitaiStruct):
        SEQ_FIELDS = ["namespace", "id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['namespace']['start'] = self._io.pos()
            self.namespace = Bson.String(self._io, self, self._root)
            self.namespace._read()
            self._debug['namespace']['end'] = self._io.pos()
            self._debug['id']['start'] = self._io.pos()
            self.id = Bson.ObjectId(self._io, self, self._root)
            self.id._read()
            self._debug['id']['end'] = self._io.pos()


    class U3(KaitaiStruct):
        """Implements unsigned 24-bit (3 byte) integer.
        """
        SEQ_FIELDS = ["b1", "b2", "b3"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['b1']['start'] = self._io.pos()
            self.b1 = self._io.read_u1()
            self._debug['b1']['end'] = self._io.pos()
            self._debug['b2']['start'] = self._io.pos()
            self.b2 = self._io.read_u1()
            self._debug['b2']['end'] = self._io.pos()
            self._debug['b3']['start'] = self._io.pos()
            self.b3 = self._io.read_u1()
            self._debug['b3']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.b1 | (self.b2 << 8)) | (self.b3 << 16))
            return getattr(self, '_m_value', None)


    class CodeWithScope(KaitaiStruct):
        SEQ_FIELDS = ["id", "source", "scope"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_s4le()
            self._debug['id']['end'] = self._io.pos()
            self._debug['source']['start'] = self._io.pos()
            self.source = Bson.String(self._io, self, self._root)
            self.source._read()
            self._debug['source']['end'] = self._io.pos()
            self._debug['scope']['start'] = self._io.pos()
            self.scope = Bson(self._io)
            self.scope._read()
            self._debug['scope']['end'] = self._io.pos()


    class F16(KaitaiStruct):
        """128-bit IEEE 754-2008 decimal floating point."""
        SEQ_FIELDS = ["str", "exponent", "significand_hi", "significand_lo"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['str']['start'] = self._io.pos()
            self.str = self._io.read_bits_int_be(1) != 0
            self._debug['str']['end'] = self._io.pos()
            self._debug['exponent']['start'] = self._io.pos()
            self.exponent = self._io.read_bits_int_be(15)
            self._debug['exponent']['end'] = self._io.pos()
            self._debug['significand_hi']['start'] = self._io.pos()
            self.significand_hi = self._io.read_bits_int_be(49)
            self._debug['significand_hi']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['significand_lo']['start'] = self._io.pos()
            self.significand_lo = self._io.read_u8le()
            self._debug['significand_lo']['end'] = self._io.pos()


    class ObjectId(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.mongodb.com/docs/manual/reference/method/ObjectId/
        """
        SEQ_FIELDS = ["epoch_time", "machine_id", "process_id", "counter"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['epoch_time']['start'] = self._io.pos()
            self.epoch_time = self._io.read_u4le()
            self._debug['epoch_time']['end'] = self._io.pos()
            self._debug['machine_id']['start'] = self._io.pos()
            self.machine_id = Bson.U3(self._io, self, self._root)
            self.machine_id._read()
            self._debug['machine_id']['end'] = self._io.pos()
            self._debug['process_id']['start'] = self._io.pos()
            self.process_id = self._io.read_u2le()
            self._debug['process_id']['end'] = self._io.pos()
            self._debug['counter']['start'] = self._io.pos()
            self.counter = Bson.U3(self._io, self, self._root)
            self.counter._read()
            self._debug['counter']['end'] = self._io.pos()


    class RegEx(KaitaiStruct):
        SEQ_FIELDS = ["pattern", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['pattern']['start'] = self._io.pos()
            self.pattern = Bson.Cstring(self._io, self, self._root)
            self.pattern._read()
            self._debug['pattern']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self.options = Bson.Cstring(self._io, self, self._root)
            self.options._read()
            self._debug['options']['end'] = self._io.pos()



