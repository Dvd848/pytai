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


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Msgpack(KaitaiStruct):
    """MessagePack (msgpack) is a system to serialize arbitrary structured
    data into a compact binary stream.
    
    .. seealso::
       Source - https://github.com/msgpack/msgpack/blob/master/spec.md
    """
    SEQ_FIELDS = ["b1", "int_extra", "float_32_value", "float_64_value", "str_len_8", "str_len_16", "str_len_32", "str_value", "num_array_elements_16", "num_array_elements_32", "array_elements", "num_map_elements_16", "num_map_elements_32", "map_elements"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['b1']['start'] = self._io.pos()
        self.b1 = self._io.read_u1()
        self._debug['b1']['end'] = self._io.pos()
        self._debug['int_extra']['start'] = self._io.pos()
        _on = self.b1
        if _on == 211:
            self.int_extra = self._io.read_s8be()
        elif _on == 209:
            self.int_extra = self._io.read_s2be()
        elif _on == 210:
            self.int_extra = self._io.read_s4be()
        elif _on == 208:
            self.int_extra = self._io.read_s1()
        elif _on == 205:
            self.int_extra = self._io.read_u2be()
        elif _on == 207:
            self.int_extra = self._io.read_u8be()
        elif _on == 204:
            self.int_extra = self._io.read_u1()
        elif _on == 206:
            self.int_extra = self._io.read_u4be()
        self._debug['int_extra']['end'] = self._io.pos()
        if self.is_float_32:
            self._debug['float_32_value']['start'] = self._io.pos()
            self.float_32_value = self._io.read_f4be()
            self._debug['float_32_value']['end'] = self._io.pos()

        if self.is_float_64:
            self._debug['float_64_value']['start'] = self._io.pos()
            self.float_64_value = self._io.read_f8be()
            self._debug['float_64_value']['end'] = self._io.pos()

        if self.is_str_8:
            self._debug['str_len_8']['start'] = self._io.pos()
            self.str_len_8 = self._io.read_u1()
            self._debug['str_len_8']['end'] = self._io.pos()

        if self.is_str_16:
            self._debug['str_len_16']['start'] = self._io.pos()
            self.str_len_16 = self._io.read_u2be()
            self._debug['str_len_16']['end'] = self._io.pos()

        if self.is_str_32:
            self._debug['str_len_32']['start'] = self._io.pos()
            self.str_len_32 = self._io.read_u4be()
            self._debug['str_len_32']['end'] = self._io.pos()

        if self.is_str:
            self._debug['str_value']['start'] = self._io.pos()
            self.str_value = (self._io.read_bytes(self.str_len)).decode(u"UTF-8")
            self._debug['str_value']['end'] = self._io.pos()

        if self.is_array_16:
            self._debug['num_array_elements_16']['start'] = self._io.pos()
            self.num_array_elements_16 = self._io.read_u2be()
            self._debug['num_array_elements_16']['end'] = self._io.pos()

        if self.is_array_32:
            self._debug['num_array_elements_32']['start'] = self._io.pos()
            self.num_array_elements_32 = self._io.read_u4be()
            self._debug['num_array_elements_32']['end'] = self._io.pos()

        if self.is_array:
            self._debug['array_elements']['start'] = self._io.pos()
            self.array_elements = []
            for i in range(self.num_array_elements):
                if not 'arr' in self._debug['array_elements']:
                    self._debug['array_elements']['arr'] = []
                self._debug['array_elements']['arr'].append({'start': self._io.pos()})
                _t_array_elements = Msgpack(self._io)
                _t_array_elements._read()
                self.array_elements.append(_t_array_elements)
                self._debug['array_elements']['arr'][i]['end'] = self._io.pos()

            self._debug['array_elements']['end'] = self._io.pos()

        if self.is_map_16:
            self._debug['num_map_elements_16']['start'] = self._io.pos()
            self.num_map_elements_16 = self._io.read_u2be()
            self._debug['num_map_elements_16']['end'] = self._io.pos()

        if self.is_map_32:
            self._debug['num_map_elements_32']['start'] = self._io.pos()
            self.num_map_elements_32 = self._io.read_u4be()
            self._debug['num_map_elements_32']['end'] = self._io.pos()

        if self.is_map:
            self._debug['map_elements']['start'] = self._io.pos()
            self.map_elements = []
            for i in range(self.num_map_elements):
                if not 'arr' in self._debug['map_elements']:
                    self._debug['map_elements']['arr'] = []
                self._debug['map_elements']['arr'].append({'start': self._io.pos()})
                _t_map_elements = Msgpack.MapTuple(self._io, self, self._root)
                _t_map_elements._read()
                self.map_elements.append(_t_map_elements)
                self._debug['map_elements']['arr'][i]['end'] = self._io.pos()

            self._debug['map_elements']['end'] = self._io.pos()


    class MapTuple(KaitaiStruct):
        SEQ_FIELDS = ["key", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self.key = Msgpack(self._io)
            self.key._read()
            self._debug['key']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = Msgpack(self._io)
            self.value._read()
            self._debug['value']['end'] = self._io.pos()


    @property
    def is_array_32(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-array
        """
        if hasattr(self, '_m_is_array_32'):
            return self._m_is_array_32

        self._m_is_array_32 = self.b1 == 221
        return getattr(self, '_m_is_array_32', None)

    @property
    def int_value(self):
        if hasattr(self, '_m_int_value'):
            return self._m_int_value

        if self.is_int:
            self._m_int_value = (self.pos_int7_value if self.is_pos_int7 else (self.neg_int5_value if self.is_neg_int5 else 4919))

        return getattr(self, '_m_int_value', None)

    @property
    def str_len(self):
        if hasattr(self, '_m_str_len'):
            return self._m_str_len

        if self.is_str:
            self._m_str_len = ((self.b1 & 31) if self.is_fix_str else (self.str_len_8 if self.is_str_8 else (self.str_len_16 if self.is_str_16 else self.str_len_32)))

        return getattr(self, '_m_str_len', None)

    @property
    def is_fix_array(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-array
        """
        if hasattr(self, '_m_is_fix_array'):
            return self._m_is_fix_array

        self._m_is_fix_array = (self.b1 & 240) == 144
        return getattr(self, '_m_is_fix_array', None)

    @property
    def is_map(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-map
        """
        if hasattr(self, '_m_is_map'):
            return self._m_is_map

        self._m_is_map =  ((self.is_fix_map) or (self.is_map_16) or (self.is_map_32)) 
        return getattr(self, '_m_is_map', None)

    @property
    def is_array(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-array
        """
        if hasattr(self, '_m_is_array'):
            return self._m_is_array

        self._m_is_array =  ((self.is_fix_array) or (self.is_array_16) or (self.is_array_32)) 
        return getattr(self, '_m_is_array', None)

    @property
    def is_float(self):
        if hasattr(self, '_m_is_float'):
            return self._m_is_float

        self._m_is_float =  ((self.is_float_32) or (self.is_float_64)) 
        return getattr(self, '_m_is_float', None)

    @property
    def is_str_8(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-str
        """
        if hasattr(self, '_m_is_str_8'):
            return self._m_is_str_8

        self._m_is_str_8 = self.b1 == 217
        return getattr(self, '_m_is_str_8', None)

    @property
    def is_fix_map(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-map
        """
        if hasattr(self, '_m_is_fix_map'):
            return self._m_is_fix_map

        self._m_is_fix_map = (self.b1 & 240) == 128
        return getattr(self, '_m_is_fix_map', None)

    @property
    def is_int(self):
        if hasattr(self, '_m_is_int'):
            return self._m_is_int

        self._m_is_int =  ((self.is_pos_int7) or (self.is_neg_int5)) 
        return getattr(self, '_m_is_int', None)

    @property
    def is_bool(self):
        if hasattr(self, '_m_is_bool'):
            return self._m_is_bool

        self._m_is_bool =  ((self.b1 == 194) or (self.b1 == 195)) 
        return getattr(self, '_m_is_bool', None)

    @property
    def is_str_16(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-str
        """
        if hasattr(self, '_m_is_str_16'):
            return self._m_is_str_16

        self._m_is_str_16 = self.b1 == 218
        return getattr(self, '_m_is_str_16', None)

    @property
    def is_float_64(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-float
        """
        if hasattr(self, '_m_is_float_64'):
            return self._m_is_float_64

        self._m_is_float_64 = self.b1 == 203
        return getattr(self, '_m_is_float_64', None)

    @property
    def is_map_16(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-map
        """
        if hasattr(self, '_m_is_map_16'):
            return self._m_is_map_16

        self._m_is_map_16 = self.b1 == 222
        return getattr(self, '_m_is_map_16', None)

    @property
    def is_neg_int5(self):
        if hasattr(self, '_m_is_neg_int5'):
            return self._m_is_neg_int5

        self._m_is_neg_int5 = (self.b1 & 224) == 224
        return getattr(self, '_m_is_neg_int5', None)

    @property
    def pos_int7_value(self):
        if hasattr(self, '_m_pos_int7_value'):
            return self._m_pos_int7_value

        if self.is_pos_int7:
            self._m_pos_int7_value = self.b1

        return getattr(self, '_m_pos_int7_value', None)

    @property
    def is_nil(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-nil
        """
        if hasattr(self, '_m_is_nil'):
            return self._m_is_nil

        self._m_is_nil = self.b1 == 192
        return getattr(self, '_m_is_nil', None)

    @property
    def float_value(self):
        if hasattr(self, '_m_float_value'):
            return self._m_float_value

        if self.is_float:
            self._m_float_value = (self.float_32_value if self.is_float_32 else self.float_64_value)

        return getattr(self, '_m_float_value', None)

    @property
    def num_array_elements(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-array
        """
        if hasattr(self, '_m_num_array_elements'):
            return self._m_num_array_elements

        if self.is_array:
            self._m_num_array_elements = ((self.b1 & 15) if self.is_fix_array else (self.num_array_elements_16 if self.is_array_16 else self.num_array_elements_32))

        return getattr(self, '_m_num_array_elements', None)

    @property
    def neg_int5_value(self):
        if hasattr(self, '_m_neg_int5_value'):
            return self._m_neg_int5_value

        if self.is_neg_int5:
            self._m_neg_int5_value = -((self.b1 & 31))

        return getattr(self, '_m_neg_int5_value', None)

    @property
    def bool_value(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-bool
        """
        if hasattr(self, '_m_bool_value'):
            return self._m_bool_value

        if self.is_bool:
            self._m_bool_value = self.b1 == 195

        return getattr(self, '_m_bool_value', None)

    @property
    def is_pos_int7(self):
        if hasattr(self, '_m_is_pos_int7'):
            return self._m_is_pos_int7

        self._m_is_pos_int7 = (self.b1 & 128) == 0
        return getattr(self, '_m_is_pos_int7', None)

    @property
    def is_array_16(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-array
        """
        if hasattr(self, '_m_is_array_16'):
            return self._m_is_array_16

        self._m_is_array_16 = self.b1 == 220
        return getattr(self, '_m_is_array_16', None)

    @property
    def is_str(self):
        if hasattr(self, '_m_is_str'):
            return self._m_is_str

        self._m_is_str =  ((self.is_fix_str) or (self.is_str_8) or (self.is_str_16) or (self.is_str_32)) 
        return getattr(self, '_m_is_str', None)

    @property
    def is_fix_str(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-str
        """
        if hasattr(self, '_m_is_fix_str'):
            return self._m_is_fix_str

        self._m_is_fix_str = (self.b1 & 224) == 160
        return getattr(self, '_m_is_fix_str', None)

    @property
    def is_str_32(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-str
        """
        if hasattr(self, '_m_is_str_32'):
            return self._m_is_str_32

        self._m_is_str_32 = self.b1 == 219
        return getattr(self, '_m_is_str_32', None)

    @property
    def num_map_elements(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-map
        """
        if hasattr(self, '_m_num_map_elements'):
            return self._m_num_map_elements

        if self.is_map:
            self._m_num_map_elements = ((self.b1 & 15) if self.is_fix_map else (self.num_map_elements_16 if self.is_map_16 else self.num_map_elements_32))

        return getattr(self, '_m_num_map_elements', None)

    @property
    def is_float_32(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-float
        """
        if hasattr(self, '_m_is_float_32'):
            return self._m_is_float_32

        self._m_is_float_32 = self.b1 == 202
        return getattr(self, '_m_is_float_32', None)

    @property
    def is_map_32(self):
        """
        .. seealso::
           Source - https://github.com/msgpack/msgpack/blob/master/spec.md#formats-map
        """
        if hasattr(self, '_m_is_map_32'):
            return self._m_is_map_32

        self._m_is_map_32 = self.b1 == 223
        return getattr(self, '_m_is_map_32', None)


