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

class RubyMarshal(KaitaiStruct):
    """Ruby's Marshal module allows serialization and deserialization of
    many standard and arbitrary Ruby objects in a compact binary
    format. It is relatively fast, available in stdlibs standard and
    allows conservation of language-specific properties (such as symbols
    or encoding-aware strings).
    
    Feature-wise, it is comparable to other language-specific
    implementations, such as:
    
    * Java's
      [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)
    * .NET
      [BinaryFormatter](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.binary.binaryformatter?view=net-7.0)
    * Python's
      [marshal](https://docs.python.org/3/library/marshal.html),
      [pickle](https://docs.python.org/3/library/pickle.html) and
      [shelve](https://docs.python.org/3/library/shelve.html)
    
    From internal perspective, serialized stream consists of a simple
    magic header and a record.
    
    .. seealso::
       Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Stream+Format
    """

    class Codes(Enum):
        ruby_string = 34
        const_nil = 48
        ruby_symbol = 58
        ruby_symbol_link = 59
        ruby_object_link = 64
        const_false = 70
        instance_var = 73
        ruby_struct = 83
        const_true = 84
        ruby_array = 91
        packed_int = 105
        bignum = 108
        ruby_hash = 123
    SEQ_FIELDS = ["version", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_bytes(2)
        self._debug['version']['end'] = self._io.pos()
        if not self.version == b"\x04\x08":
            raise kaitaistruct.ValidationNotEqualError(b"\x04\x08", self.version, self._io, u"/seq/0")
        self._debug['records']['start'] = self._io.pos()
        self.records = RubyMarshal.Record(self._io, self, self._root)
        self.records._read()
        self._debug['records']['end'] = self._io.pos()

    class RubyArray(KaitaiStruct):
        SEQ_FIELDS = ["num_elements", "elements"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_elements']['start'] = self._io.pos()
            self.num_elements = RubyMarshal.PackedInt(self._io, self, self._root)
            self.num_elements._read()
            self._debug['num_elements']['end'] = self._io.pos()
            self._debug['elements']['start'] = self._io.pos()
            self.elements = []
            for i in range(self.num_elements.value):
                if not 'arr' in self._debug['elements']:
                    self._debug['elements']['arr'] = []
                self._debug['elements']['arr'].append({'start': self._io.pos()})
                _t_elements = RubyMarshal.Record(self._io, self, self._root)
                _t_elements._read()
                self.elements.append(_t_elements)
                self._debug['elements']['arr'][i]['end'] = self._io.pos()

            self._debug['elements']['end'] = self._io.pos()


    class Bignum(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Bignum
        """
        SEQ_FIELDS = ["sign", "len_div_2", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['sign']['start'] = self._io.pos()
            self.sign = self._io.read_u1()
            self._debug['sign']['end'] = self._io.pos()
            self._debug['len_div_2']['start'] = self._io.pos()
            self.len_div_2 = RubyMarshal.PackedInt(self._io, self, self._root)
            self.len_div_2._read()
            self._debug['len_div_2']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes((self.len_div_2.value * 2))
            self._debug['body']['end'] = self._io.pos()


    class RubyStruct(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Struct
        """
        SEQ_FIELDS = ["name", "num_members", "members"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = RubyMarshal.Record(self._io, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()
            self._debug['num_members']['start'] = self._io.pos()
            self.num_members = RubyMarshal.PackedInt(self._io, self, self._root)
            self.num_members._read()
            self._debug['num_members']['end'] = self._io.pos()
            self._debug['members']['start'] = self._io.pos()
            self.members = []
            for i in range(self.num_members.value):
                if not 'arr' in self._debug['members']:
                    self._debug['members']['arr'] = []
                self._debug['members']['arr'].append({'start': self._io.pos()})
                _t_members = RubyMarshal.Pair(self._io, self, self._root)
                _t_members._read()
                self.members.append(_t_members)
                self._debug['members']['arr'][i]['end'] = self._io.pos()

            self._debug['members']['end'] = self._io.pos()


    class RubySymbol(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Symbols+and+Byte+Sequence
        """
        SEQ_FIELDS = ["len", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = RubyMarshal.PackedInt(self._io, self, self._root)
            self.len._read()
            self._debug['len']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.len.value)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


    class PackedInt(KaitaiStruct):
        """Ruby uses sophisticated system to pack integers: first `code`
        byte either determines packing scheme or carries encoded
        immediate value (thus allowing smaller values from -123 to 122
        (inclusive) to take only one byte. There are 11 encoding schemes
        in total:
        
        * 0 is encoded specially (as 0)
        * 1..122 are encoded as immediate value with a shift
        * 123..255 are encoded with code of 0x01 and 1 extra byte
        * 0x100..0xffff are encoded with code of 0x02 and 2 extra bytes
        * 0x10000..0xffffff are encoded with code of 0x03 and 3 extra
          bytes
        * 0x1000000..0xffffffff are encoded with code of 0x04 and 4
          extra bytes
        * -123..-1 are encoded as immediate value with another shift
        * -256..-124 are encoded with code of 0xff and 1 extra byte
        * -0x10000..-257 are encoded with code of 0xfe and 2 extra bytes
        * -0x1000000..0x10001 are encoded with code of 0xfd and 3 extra
           bytes
        * -0x40000000..-0x1000001 are encoded with code of 0xfc and 4
           extra bytes
        
        Values beyond that are serialized as bignum (even if they
        technically might be not Bignum class in Ruby implementation,
        i.e. if they fit into 64 bits on a 64-bit platform).
        
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Fixnum+and+long
        """
        SEQ_FIELDS = ["code", "encoded", "encoded2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = self._io.read_u1()
            self._debug['code']['end'] = self._io.pos()
            self._debug['encoded']['start'] = self._io.pos()
            _on = self.code
            if _on == 4:
                self.encoded = self._io.read_u4le()
            elif _on == 1:
                self.encoded = self._io.read_u1()
            elif _on == 252:
                self.encoded = self._io.read_u4le()
            elif _on == 253:
                self.encoded = self._io.read_u2le()
            elif _on == 3:
                self.encoded = self._io.read_u2le()
            elif _on == 2:
                self.encoded = self._io.read_u2le()
            elif _on == 255:
                self.encoded = self._io.read_u1()
            elif _on == 254:
                self.encoded = self._io.read_u2le()
            self._debug['encoded']['end'] = self._io.pos()
            self._debug['encoded2']['start'] = self._io.pos()
            _on = self.code
            if _on == 3:
                self.encoded2 = self._io.read_u1()
            elif _on == 253:
                self.encoded2 = self._io.read_u1()
            self._debug['encoded2']['end'] = self._io.pos()

        @property
        def is_immediate(self):
            if hasattr(self, '_m_is_immediate'):
                return self._m_is_immediate

            self._m_is_immediate =  ((self.code > 4) and (self.code < 252)) 
            return getattr(self, '_m_is_immediate', None)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (((self.code - 5) if self.code < 128 else (4 - (~(self.code) & 127))) if self.is_immediate else (0 if self.code == 0 else ((self.encoded - 256) if self.code == 255 else ((self.encoded - 65536) if self.code == 254 else ((((self.encoded2 << 16) | self.encoded) - 16777216) if self.code == 253 else (((self.encoded2 << 16) | self.encoded) if self.code == 3 else self.encoded))))))
            return getattr(self, '_m_value', None)


    class Pair(KaitaiStruct):
        SEQ_FIELDS = ["key", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self.key = RubyMarshal.Record(self._io, self, self._root)
            self.key._read()
            self._debug['key']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = RubyMarshal.Record(self._io, self, self._root)
            self.value._read()
            self._debug['value']['end'] = self._io.pos()


    class InstanceVar(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Instance+Variables
        """
        SEQ_FIELDS = ["obj", "num_vars", "vars"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['obj']['start'] = self._io.pos()
            self.obj = RubyMarshal.Record(self._io, self, self._root)
            self.obj._read()
            self._debug['obj']['end'] = self._io.pos()
            self._debug['num_vars']['start'] = self._io.pos()
            self.num_vars = RubyMarshal.PackedInt(self._io, self, self._root)
            self.num_vars._read()
            self._debug['num_vars']['end'] = self._io.pos()
            self._debug['vars']['start'] = self._io.pos()
            self.vars = []
            for i in range(self.num_vars.value):
                if not 'arr' in self._debug['vars']:
                    self._debug['vars']['arr'] = []
                self._debug['vars']['arr'].append({'start': self._io.pos()})
                _t_vars = RubyMarshal.Pair(self._io, self, self._root)
                _t_vars._read()
                self.vars.append(_t_vars)
                self._debug['vars']['arr'][i]['end'] = self._io.pos()

            self._debug['vars']['end'] = self._io.pos()


    class Record(KaitaiStruct):
        """Each record starts with a single byte that determines its type
        (`code`) and contents. If necessary, additional info as parsed
        as `body`, to be determined by `code`.
        """
        SEQ_FIELDS = ["code", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = KaitaiStream.resolve_enum(RubyMarshal.Codes, self._io.read_u1())
            self._debug['code']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.code
            if _on == RubyMarshal.Codes.packed_int:
                self.body = RubyMarshal.PackedInt(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.bignum:
                self.body = RubyMarshal.Bignum(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_array:
                self.body = RubyMarshal.RubyArray(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_symbol_link:
                self.body = RubyMarshal.PackedInt(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_struct:
                self.body = RubyMarshal.RubyStruct(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_string:
                self.body = RubyMarshal.RubyString(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.instance_var:
                self.body = RubyMarshal.InstanceVar(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_hash:
                self.body = RubyMarshal.RubyHash(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_symbol:
                self.body = RubyMarshal.RubySymbol(self._io, self, self._root)
                self.body._read()
            elif _on == RubyMarshal.Codes.ruby_object_link:
                self.body = RubyMarshal.PackedInt(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()


    class RubyHash(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Hash+and+Hash+with+Default+Value
        """
        SEQ_FIELDS = ["num_pairs", "pairs"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_pairs']['start'] = self._io.pos()
            self.num_pairs = RubyMarshal.PackedInt(self._io, self, self._root)
            self.num_pairs._read()
            self._debug['num_pairs']['end'] = self._io.pos()
            self._debug['pairs']['start'] = self._io.pos()
            self.pairs = []
            for i in range(self.num_pairs.value):
                if not 'arr' in self._debug['pairs']:
                    self._debug['pairs']['arr'] = []
                self._debug['pairs']['arr'].append({'start': self._io.pos()})
                _t_pairs = RubyMarshal.Pair(self._io, self, self._root)
                _t_pairs._read()
                self.pairs.append(_t_pairs)
                self._debug['pairs']['arr'][i]['end'] = self._io.pos()

            self._debug['pairs']['end'] = self._io.pos()


    class RubyString(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-String
        """
        SEQ_FIELDS = ["len", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = RubyMarshal.PackedInt(self._io, self, self._root)
            self.len._read()
            self._debug['len']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(self.len.value)
            self._debug['body']['end'] = self._io.pos()



