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
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class VlqBase128Le(KaitaiStruct):
    """A variable-length unsigned/signed integer using base128 encoding. 1-byte groups
    consist of 1-bit flag of continuation and 7-bit value chunk, and are ordered
    "least significant group first", i.e. in "little-endian" manner.
    
    This particular encoding is specified and used in:
    
    * DWARF debug file format, where it's dubbed "unsigned LEB128" or "ULEB128".
      <https://dwarfstd.org/doc/dwarf-2.0.0.pdf> - page 139
    * Google Protocol Buffers, where it's called "Base 128 Varints".
      <https://protobuf.dev/programming-guides/encoding/#varints>
    * Apache Lucene, where it's called "VInt"
      <https://lucene.apache.org/core/3_5_0/fileformats.html#VInt>
    * Apache Avro uses this as a basis for integer encoding, adding ZigZag on
      top of it for signed ints
      <https://avro.apache.org/docs/1.12.0/specification/#primitive-types-1>
    
    More information on this encoding is available at <https://en.wikipedia.org/wiki/LEB128>
    
    This particular implementation supports integer values up to 64 bits (i.e. the
    maximum unsigned value supported is `2**64 - 1`), which implies that serialized
    values can be up to 10 bytes in length.
    
    If the most significant 10th byte (`groups[9]`) is present, its `has_next`
    must be `false` (otherwise we would have 11 or more bytes, which is not
    supported) and its `value` can be only `0` or `1` (because a 9-byte VLQ can
    represent `9 * 7 = 63` bits already, so the 10th byte can only add 1 bit,
    since only integers up to 64 bits are supported). These restrictions are
    enforced by this implementation. They were inspired by the Protoscope tool,
    see <https://github.com/protocolbuffers/protoscope/blob/8e7a6aafa2c9958527b1e0747e66e1bfff045819/writer.go#L644-L648>.
    """
    SEQ_FIELDS = ["groups"]
    def __init__(self, _io, _parent=None, _root=None):
        super(VlqBase128Le, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['groups']['start'] = self._io.pos()
        self._debug['groups']['arr'] = []
        self.groups = []
        i = 0
        while True:
            self._debug['groups']['arr'].append({'start': self._io.pos()})
            _t_groups = VlqBase128Le.Group(i, (self.groups[i - 1].interm_value if i != 0 else 0), ((9223372036854775808 if i == 9 else self.groups[i - 1].multiplier * 128) if i != 0 else 1), self._io, self, self._root)
            try:
                _t_groups._read()
            finally:
                _ = _t_groups
                self.groups.append(_)
            self._debug['groups']['arr'][len(self.groups) - 1]['end'] = self._io.pos()
            if (not (_.has_next)):
                break
            i += 1
        self._debug['groups']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.groups)):
            pass
            self.groups[i]._fetch_instances()


    class Group(KaitaiStruct):
        """One byte group, clearly divided into 7-bit "value" chunk and 1-bit "continuation" flag.
        """
        SEQ_FIELDS = ["has_next", "value"]
        def __init__(self, idx, prev_interm_value, multiplier, _io, _parent=None, _root=None):
            super(VlqBase128Le.Group, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.idx = idx
            self.prev_interm_value = prev_interm_value
            self.multiplier = multiplier
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['has_next']['start'] = self._io.pos()
            self.has_next = self._io.read_bits_int_be(1) != 0
            self._debug['has_next']['end'] = self._io.pos()
            if not self.has_next == (False if self.idx == 9 else self.has_next):
                raise kaitaistruct.ValidationNotEqualError((False if self.idx == 9 else self.has_next), self.has_next, self._io, u"/types/group/seq/0")
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bits_int_be(7)
            self._debug['value']['end'] = self._io.pos()
            if not self.value <= (1 if self.idx == 9 else 127):
                raise kaitaistruct.ValidationGreaterThanError((1 if self.idx == 9 else 127), self.value, self._io, u"/types/group/seq/1")


        def _fetch_instances(self):
            pass

        @property
        def interm_value(self):
            if hasattr(self, '_m_interm_value'):
                return self._m_interm_value

            self._m_interm_value = (self.prev_interm_value + self.value * self.multiplier)
            return getattr(self, '_m_interm_value', None)


    @property
    def len(self):
        if hasattr(self, '_m_len'):
            return self._m_len

        self._m_len = len(self.groups)
        return getattr(self, '_m_len', None)

    @property
    def sign_bit(self):
        if hasattr(self, '_m_sign_bit'):
            return self._m_sign_bit

        self._m_sign_bit = (9223372036854775808 if self.len == 10 else self.groups[-1].multiplier * 64)
        return getattr(self, '_m_sign_bit', None)

    @property
    def value(self):
        """Resulting unsigned value as normal integer."""
        if hasattr(self, '_m_value'):
            return self._m_value

        self._m_value = self.groups[-1].interm_value
        return getattr(self, '_m_value', None)

    @property
    def value_signed(self):
        if hasattr(self, '_m_value_signed'):
            return self._m_value_signed

        self._m_value_signed = (-((self.sign_bit - (self.value - self.sign_bit))) if  ((self.sign_bit > 0) and (self.value >= self.sign_bit))  else self.value)
        return getattr(self, '_m_value_signed', None)


