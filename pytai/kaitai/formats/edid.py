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
import struct


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Edid(KaitaiStruct):
    SEQ_FIELDS = ["magic", "mfg_bytes", "product_code", "serial", "mfg_week", "mfg_year_mod", "edid_version_major", "edid_version_minor", "input_flags", "screen_size_h", "screen_size_v", "gamma_mod", "features_flags", "chromacity", "est_timings", "std_timings"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x00\xFF\xFF\xFF\xFF\xFF\xFF\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\xFF\xFF\xFF\xFF\xFF\xFF\x00", self.magic, self._io, u"/seq/0")
        self._debug['mfg_bytes']['start'] = self._io.pos()
        self.mfg_bytes = self._io.read_u2be()
        self._debug['mfg_bytes']['end'] = self._io.pos()
        self._debug['product_code']['start'] = self._io.pos()
        self.product_code = self._io.read_u2le()
        self._debug['product_code']['end'] = self._io.pos()
        self._debug['serial']['start'] = self._io.pos()
        self.serial = self._io.read_u4le()
        self._debug['serial']['end'] = self._io.pos()
        self._debug['mfg_week']['start'] = self._io.pos()
        self.mfg_week = self._io.read_u1()
        self._debug['mfg_week']['end'] = self._io.pos()
        self._debug['mfg_year_mod']['start'] = self._io.pos()
        self.mfg_year_mod = self._io.read_u1()
        self._debug['mfg_year_mod']['end'] = self._io.pos()
        self._debug['edid_version_major']['start'] = self._io.pos()
        self.edid_version_major = self._io.read_u1()
        self._debug['edid_version_major']['end'] = self._io.pos()
        self._debug['edid_version_minor']['start'] = self._io.pos()
        self.edid_version_minor = self._io.read_u1()
        self._debug['edid_version_minor']['end'] = self._io.pos()
        self._debug['input_flags']['start'] = self._io.pos()
        self.input_flags = self._io.read_u1()
        self._debug['input_flags']['end'] = self._io.pos()
        self._debug['screen_size_h']['start'] = self._io.pos()
        self.screen_size_h = self._io.read_u1()
        self._debug['screen_size_h']['end'] = self._io.pos()
        self._debug['screen_size_v']['start'] = self._io.pos()
        self.screen_size_v = self._io.read_u1()
        self._debug['screen_size_v']['end'] = self._io.pos()
        self._debug['gamma_mod']['start'] = self._io.pos()
        self.gamma_mod = self._io.read_u1()
        self._debug['gamma_mod']['end'] = self._io.pos()
        self._debug['features_flags']['start'] = self._io.pos()
        self.features_flags = self._io.read_u1()
        self._debug['features_flags']['end'] = self._io.pos()
        self._debug['chromacity']['start'] = self._io.pos()
        self.chromacity = Edid.ChromacityInfo(self._io, self, self._root)
        self.chromacity._read()
        self._debug['chromacity']['end'] = self._io.pos()
        self._debug['est_timings']['start'] = self._io.pos()
        self.est_timings = Edid.EstTimingsInfo(self._io, self, self._root)
        self.est_timings._read()
        self._debug['est_timings']['end'] = self._io.pos()
        self._debug['std_timings']['start'] = self._io.pos()
        self._raw_std_timings = []
        self.std_timings = []
        for i in range(8):
            if not 'arr' in self._debug['std_timings']:
                self._debug['std_timings']['arr'] = []
            self._debug['std_timings']['arr'].append({'start': self._io.pos()})
            self._raw_std_timings.append(self._io.read_bytes(2))
            _io__raw_std_timings = KaitaiStream(BytesIO(self._raw_std_timings[i]))
            _t_std_timings = Edid.StdTiming(_io__raw_std_timings, self, self._root)
            _t_std_timings._read()
            self.std_timings.append(_t_std_timings)
            self._debug['std_timings']['arr'][i]['end'] = self._io.pos()

        self._debug['std_timings']['end'] = self._io.pos()

    class ChromacityInfo(KaitaiStruct):
        """Chromaticity information: colorimetry and white point
        coordinates. All coordinates are stored as fixed precision
        10-bit numbers, bits are shuffled for compactness.
        """
        SEQ_FIELDS = ["red_x_1_0", "red_y_1_0", "green_x_1_0", "green_y_1_0", "blue_x_1_0", "blue_y_1_0", "white_x_1_0", "white_y_1_0", "red_x_9_2", "red_y_9_2", "green_x_9_2", "green_y_9_2", "blue_x_9_2", "blue_y_9_2", "white_x_9_2", "white_y_9_2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['red_x_1_0']['start'] = self._io.pos()
            self.red_x_1_0 = self._io.read_bits_int_be(2)
            self._debug['red_x_1_0']['end'] = self._io.pos()
            self._debug['red_y_1_0']['start'] = self._io.pos()
            self.red_y_1_0 = self._io.read_bits_int_be(2)
            self._debug['red_y_1_0']['end'] = self._io.pos()
            self._debug['green_x_1_0']['start'] = self._io.pos()
            self.green_x_1_0 = self._io.read_bits_int_be(2)
            self._debug['green_x_1_0']['end'] = self._io.pos()
            self._debug['green_y_1_0']['start'] = self._io.pos()
            self.green_y_1_0 = self._io.read_bits_int_be(2)
            self._debug['green_y_1_0']['end'] = self._io.pos()
            self._debug['blue_x_1_0']['start'] = self._io.pos()
            self.blue_x_1_0 = self._io.read_bits_int_be(2)
            self._debug['blue_x_1_0']['end'] = self._io.pos()
            self._debug['blue_y_1_0']['start'] = self._io.pos()
            self.blue_y_1_0 = self._io.read_bits_int_be(2)
            self._debug['blue_y_1_0']['end'] = self._io.pos()
            self._debug['white_x_1_0']['start'] = self._io.pos()
            self.white_x_1_0 = self._io.read_bits_int_be(2)
            self._debug['white_x_1_0']['end'] = self._io.pos()
            self._debug['white_y_1_0']['start'] = self._io.pos()
            self.white_y_1_0 = self._io.read_bits_int_be(2)
            self._debug['white_y_1_0']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['red_x_9_2']['start'] = self._io.pos()
            self.red_x_9_2 = self._io.read_u1()
            self._debug['red_x_9_2']['end'] = self._io.pos()
            self._debug['red_y_9_2']['start'] = self._io.pos()
            self.red_y_9_2 = self._io.read_u1()
            self._debug['red_y_9_2']['end'] = self._io.pos()
            self._debug['green_x_9_2']['start'] = self._io.pos()
            self.green_x_9_2 = self._io.read_u1()
            self._debug['green_x_9_2']['end'] = self._io.pos()
            self._debug['green_y_9_2']['start'] = self._io.pos()
            self.green_y_9_2 = self._io.read_u1()
            self._debug['green_y_9_2']['end'] = self._io.pos()
            self._debug['blue_x_9_2']['start'] = self._io.pos()
            self.blue_x_9_2 = self._io.read_u1()
            self._debug['blue_x_9_2']['end'] = self._io.pos()
            self._debug['blue_y_9_2']['start'] = self._io.pos()
            self.blue_y_9_2 = self._io.read_u1()
            self._debug['blue_y_9_2']['end'] = self._io.pos()
            self._debug['white_x_9_2']['start'] = self._io.pos()
            self.white_x_9_2 = self._io.read_u1()
            self._debug['white_x_9_2']['end'] = self._io.pos()
            self._debug['white_y_9_2']['start'] = self._io.pos()
            self.white_y_9_2 = self._io.read_u1()
            self._debug['white_y_9_2']['end'] = self._io.pos()

        @property
        def green_x_int(self):
            if hasattr(self, '_m_green_x_int'):
                return self._m_green_x_int

            self._m_green_x_int = ((self.green_x_9_2 << 2) | self.green_x_1_0)
            return getattr(self, '_m_green_x_int', None)

        @property
        def red_y(self):
            """Red Y coordinate."""
            if hasattr(self, '_m_red_y'):
                return self._m_red_y

            self._m_red_y = (self.red_y_int / 1024.0)
            return getattr(self, '_m_red_y', None)

        @property
        def green_y_int(self):
            if hasattr(self, '_m_green_y_int'):
                return self._m_green_y_int

            self._m_green_y_int = ((self.green_y_9_2 << 2) | self.green_y_1_0)
            return getattr(self, '_m_green_y_int', None)

        @property
        def white_y(self):
            """White Y coordinate."""
            if hasattr(self, '_m_white_y'):
                return self._m_white_y

            self._m_white_y = (self.white_y_int / 1024.0)
            return getattr(self, '_m_white_y', None)

        @property
        def red_x(self):
            """Red X coordinate."""
            if hasattr(self, '_m_red_x'):
                return self._m_red_x

            self._m_red_x = (self.red_x_int / 1024.0)
            return getattr(self, '_m_red_x', None)

        @property
        def white_x(self):
            """White X coordinate."""
            if hasattr(self, '_m_white_x'):
                return self._m_white_x

            self._m_white_x = (self.white_x_int / 1024.0)
            return getattr(self, '_m_white_x', None)

        @property
        def blue_x(self):
            """Blue X coordinate."""
            if hasattr(self, '_m_blue_x'):
                return self._m_blue_x

            self._m_blue_x = (self.blue_x_int / 1024.0)
            return getattr(self, '_m_blue_x', None)

        @property
        def white_x_int(self):
            if hasattr(self, '_m_white_x_int'):
                return self._m_white_x_int

            self._m_white_x_int = ((self.white_x_9_2 << 2) | self.white_x_1_0)
            return getattr(self, '_m_white_x_int', None)

        @property
        def white_y_int(self):
            if hasattr(self, '_m_white_y_int'):
                return self._m_white_y_int

            self._m_white_y_int = ((self.white_y_9_2 << 2) | self.white_y_1_0)
            return getattr(self, '_m_white_y_int', None)

        @property
        def green_x(self):
            """Green X coordinate."""
            if hasattr(self, '_m_green_x'):
                return self._m_green_x

            self._m_green_x = (self.green_x_int / 1024.0)
            return getattr(self, '_m_green_x', None)

        @property
        def red_x_int(self):
            if hasattr(self, '_m_red_x_int'):
                return self._m_red_x_int

            self._m_red_x_int = ((self.red_x_9_2 << 2) | self.red_x_1_0)
            return getattr(self, '_m_red_x_int', None)

        @property
        def red_y_int(self):
            if hasattr(self, '_m_red_y_int'):
                return self._m_red_y_int

            self._m_red_y_int = ((self.red_y_9_2 << 2) | self.red_y_1_0)
            return getattr(self, '_m_red_y_int', None)

        @property
        def blue_x_int(self):
            if hasattr(self, '_m_blue_x_int'):
                return self._m_blue_x_int

            self._m_blue_x_int = ((self.blue_x_9_2 << 2) | self.blue_x_1_0)
            return getattr(self, '_m_blue_x_int', None)

        @property
        def blue_y(self):
            """Blue Y coordinate."""
            if hasattr(self, '_m_blue_y'):
                return self._m_blue_y

            self._m_blue_y = (self.blue_y_int / 1024.0)
            return getattr(self, '_m_blue_y', None)

        @property
        def green_y(self):
            """Green Y coordinate."""
            if hasattr(self, '_m_green_y'):
                return self._m_green_y

            self._m_green_y = (self.green_y_int / 1024.0)
            return getattr(self, '_m_green_y', None)

        @property
        def blue_y_int(self):
            if hasattr(self, '_m_blue_y_int'):
                return self._m_blue_y_int

            self._m_blue_y_int = ((self.blue_y_9_2 << 2) | self.blue_y_1_0)
            return getattr(self, '_m_blue_y_int', None)


    class EstTimingsInfo(KaitaiStruct):
        SEQ_FIELDS = ["can_720x400px_70hz", "can_720x400px_88hz", "can_640x480px_60hz", "can_640x480px_67hz", "can_640x480px_72hz", "can_640x480px_75hz", "can_800x600px_56hz", "can_800x600px_60hz", "can_800x600px_72hz", "can_800x600px_75hz", "can_832x624px_75hz", "can_1024x768px_87hz_i", "can_1024x768px_60hz", "can_1024x768px_70hz", "can_1024x768px_75hz", "can_1280x1024px_75hz", "can_1152x870px_75hz", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['can_720x400px_70hz']['start'] = self._io.pos()
            self.can_720x400px_70hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_720x400px_70hz']['end'] = self._io.pos()
            self._debug['can_720x400px_88hz']['start'] = self._io.pos()
            self.can_720x400px_88hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_720x400px_88hz']['end'] = self._io.pos()
            self._debug['can_640x480px_60hz']['start'] = self._io.pos()
            self.can_640x480px_60hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_640x480px_60hz']['end'] = self._io.pos()
            self._debug['can_640x480px_67hz']['start'] = self._io.pos()
            self.can_640x480px_67hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_640x480px_67hz']['end'] = self._io.pos()
            self._debug['can_640x480px_72hz']['start'] = self._io.pos()
            self.can_640x480px_72hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_640x480px_72hz']['end'] = self._io.pos()
            self._debug['can_640x480px_75hz']['start'] = self._io.pos()
            self.can_640x480px_75hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_640x480px_75hz']['end'] = self._io.pos()
            self._debug['can_800x600px_56hz']['start'] = self._io.pos()
            self.can_800x600px_56hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_800x600px_56hz']['end'] = self._io.pos()
            self._debug['can_800x600px_60hz']['start'] = self._io.pos()
            self.can_800x600px_60hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_800x600px_60hz']['end'] = self._io.pos()
            self._debug['can_800x600px_72hz']['start'] = self._io.pos()
            self.can_800x600px_72hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_800x600px_72hz']['end'] = self._io.pos()
            self._debug['can_800x600px_75hz']['start'] = self._io.pos()
            self.can_800x600px_75hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_800x600px_75hz']['end'] = self._io.pos()
            self._debug['can_832x624px_75hz']['start'] = self._io.pos()
            self.can_832x624px_75hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_832x624px_75hz']['end'] = self._io.pos()
            self._debug['can_1024x768px_87hz_i']['start'] = self._io.pos()
            self.can_1024x768px_87hz_i = self._io.read_bits_int_be(1) != 0
            self._debug['can_1024x768px_87hz_i']['end'] = self._io.pos()
            self._debug['can_1024x768px_60hz']['start'] = self._io.pos()
            self.can_1024x768px_60hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_1024x768px_60hz']['end'] = self._io.pos()
            self._debug['can_1024x768px_70hz']['start'] = self._io.pos()
            self.can_1024x768px_70hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_1024x768px_70hz']['end'] = self._io.pos()
            self._debug['can_1024x768px_75hz']['start'] = self._io.pos()
            self.can_1024x768px_75hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_1024x768px_75hz']['end'] = self._io.pos()
            self._debug['can_1280x1024px_75hz']['start'] = self._io.pos()
            self.can_1280x1024px_75hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_1280x1024px_75hz']['end'] = self._io.pos()
            self._debug['can_1152x870px_75hz']['start'] = self._io.pos()
            self.can_1152x870px_75hz = self._io.read_bits_int_be(1) != 0
            self._debug['can_1152x870px_75hz']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bits_int_be(7)
            self._debug['reserved']['end'] = self._io.pos()


    class StdTiming(KaitaiStruct):

        class AspectRatios(Enum):
            ratio_16_10 = 0
            ratio_4_3 = 1
            ratio_5_4 = 2
            ratio_16_9 = 3
        SEQ_FIELDS = ["horiz_active_pixels_mod", "aspect_ratio", "refresh_rate_mod"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['horiz_active_pixels_mod']['start'] = self._io.pos()
            self.horiz_active_pixels_mod = self._io.read_u1()
            self._debug['horiz_active_pixels_mod']['end'] = self._io.pos()
            self._debug['aspect_ratio']['start'] = self._io.pos()
            self.aspect_ratio = KaitaiStream.resolve_enum(Edid.StdTiming.AspectRatios, self._io.read_bits_int_be(2))
            self._debug['aspect_ratio']['end'] = self._io.pos()
            self._debug['refresh_rate_mod']['start'] = self._io.pos()
            self.refresh_rate_mod = self._io.read_bits_int_be(6)
            self._debug['refresh_rate_mod']['end'] = self._io.pos()

        @property
        def bytes_lookahead(self):
            if hasattr(self, '_m_bytes_lookahead'):
                return self._m_bytes_lookahead

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_bytes_lookahead']['start'] = self._io.pos()
            self._m_bytes_lookahead = self._io.read_bytes(2)
            self._debug['_m_bytes_lookahead']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_bytes_lookahead', None)

        @property
        def is_used(self):
            if hasattr(self, '_m_is_used'):
                return self._m_is_used

            self._m_is_used = self.bytes_lookahead != b"\x01\x01"
            return getattr(self, '_m_is_used', None)

        @property
        def horiz_active_pixels(self):
            """Range of horizontal active pixels."""
            if hasattr(self, '_m_horiz_active_pixels'):
                return self._m_horiz_active_pixels

            if self.is_used:
                self._m_horiz_active_pixels = ((self.horiz_active_pixels_mod + 31) * 8)

            return getattr(self, '_m_horiz_active_pixels', None)

        @property
        def refresh_rate(self):
            """Vertical refresh rate, Hz."""
            if hasattr(self, '_m_refresh_rate'):
                return self._m_refresh_rate

            if self.is_used:
                self._m_refresh_rate = (self.refresh_rate_mod + 60)

            return getattr(self, '_m_refresh_rate', None)


    @property
    def mfg_year(self):
        if hasattr(self, '_m_mfg_year'):
            return self._m_mfg_year

        self._m_mfg_year = (self.mfg_year_mod + 1990)
        return getattr(self, '_m_mfg_year', None)

    @property
    def mfg_id_ch1(self):
        if hasattr(self, '_m_mfg_id_ch1'):
            return self._m_mfg_id_ch1

        self._m_mfg_id_ch1 = ((self.mfg_bytes & 31744) >> 10)
        return getattr(self, '_m_mfg_id_ch1', None)

    @property
    def mfg_id_ch3(self):
        if hasattr(self, '_m_mfg_id_ch3'):
            return self._m_mfg_id_ch3

        self._m_mfg_id_ch3 = (self.mfg_bytes & 31)
        return getattr(self, '_m_mfg_id_ch3', None)

    @property
    def gamma(self):
        if hasattr(self, '_m_gamma'):
            return self._m_gamma

        if self.gamma_mod != 255:
            self._m_gamma = ((self.gamma_mod + 100) / 100.0)

        return getattr(self, '_m_gamma', None)

    @property
    def mfg_str(self):
        if hasattr(self, '_m_mfg_str'):
            return self._m_mfg_str

        self._m_mfg_str = (struct.pack('3b', (self.mfg_id_ch1 + 64), (self.mfg_id_ch2 + 64), (self.mfg_id_ch3 + 64))).decode(u"ASCII")
        return getattr(self, '_m_mfg_str', None)

    @property
    def mfg_id_ch2(self):
        if hasattr(self, '_m_mfg_id_ch2'):
            return self._m_mfg_id_ch2

        self._m_mfg_id_ch2 = ((self.mfg_bytes & 992) >> 5)
        return getattr(self, '_m_mfg_id_ch2', None)


