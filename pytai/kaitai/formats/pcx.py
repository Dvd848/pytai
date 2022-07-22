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

class Pcx(KaitaiStruct):
    """PCX is a bitmap image format originally used by PC Paintbrush from
    ZSoft Corporation. Originally, it was a relatively simple 128-byte
    header + uncompressed bitmap format, but latest versions introduced
    more complicated palette support and RLE compression.
    
    There's an option to encode 32-bit or 16-bit RGBA pixels, and thus
    it can potentially include transparency. Theoretically, it's
    possible to encode resolution or pixel density in the some of the
    header fields too, but in reality there's no uniform standard for
    these, so different implementations treat these differently.
    
    PCX format was never made a formal standard. "ZSoft Corporation
    Technical Reference Manual" for "Image File (.PCX) Format", last
    updated in 1991, is likely the closest authoritative source.
    
    .. seealso::
       Source - https://web.archive.org/web/20100206055706/http://www.qzx.com/pc-gpe/pcx.txt
    """

    class Versions(Enum):
        v2_5 = 0
        v2_8_with_palette = 2
        v2_8_without_palette = 3
        paintbrush_for_windows = 4
        v3_0 = 5

    class Encodings(Enum):
        rle = 1
    SEQ_FIELDS = ["hdr"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['hdr']['start'] = self._io.pos()
        self._raw_hdr = self._io.read_bytes(128)
        _io__raw_hdr = KaitaiStream(BytesIO(self._raw_hdr))
        self.hdr = Pcx.Header(_io__raw_hdr, self, self._root)
        self.hdr._read()
        self._debug['hdr']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        """
        .. seealso::
           - "ZSoft .PCX FILE HEADER FORMAT" - https://web.archive.org/web/20100206055706/http://www.qzx.com/pc-gpe/pcx.txt
        """
        SEQ_FIELDS = ["magic", "version", "encoding", "bits_per_pixel", "img_x_min", "img_y_min", "img_x_max", "img_y_max", "hdpi", "vdpi", "palette_16", "reserved", "num_planes", "bytes_per_line", "palette_info", "h_screen_size", "v_screen_size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(1)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x0A", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = KaitaiStream.resolve_enum(Pcx.Versions, self._io.read_u1())
            self._debug['version']['end'] = self._io.pos()
            self._debug['encoding']['start'] = self._io.pos()
            self.encoding = KaitaiStream.resolve_enum(Pcx.Encodings, self._io.read_u1())
            self._debug['encoding']['end'] = self._io.pos()
            self._debug['bits_per_pixel']['start'] = self._io.pos()
            self.bits_per_pixel = self._io.read_u1()
            self._debug['bits_per_pixel']['end'] = self._io.pos()
            self._debug['img_x_min']['start'] = self._io.pos()
            self.img_x_min = self._io.read_u2le()
            self._debug['img_x_min']['end'] = self._io.pos()
            self._debug['img_y_min']['start'] = self._io.pos()
            self.img_y_min = self._io.read_u2le()
            self._debug['img_y_min']['end'] = self._io.pos()
            self._debug['img_x_max']['start'] = self._io.pos()
            self.img_x_max = self._io.read_u2le()
            self._debug['img_x_max']['end'] = self._io.pos()
            self._debug['img_y_max']['start'] = self._io.pos()
            self.img_y_max = self._io.read_u2le()
            self._debug['img_y_max']['end'] = self._io.pos()
            self._debug['hdpi']['start'] = self._io.pos()
            self.hdpi = self._io.read_u2le()
            self._debug['hdpi']['end'] = self._io.pos()
            self._debug['vdpi']['start'] = self._io.pos()
            self.vdpi = self._io.read_u2le()
            self._debug['vdpi']['end'] = self._io.pos()
            self._debug['palette_16']['start'] = self._io.pos()
            self.palette_16 = self._io.read_bytes(48)
            self._debug['palette_16']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(1)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.reserved, self._io, u"/types/header/seq/11")
            self._debug['num_planes']['start'] = self._io.pos()
            self.num_planes = self._io.read_u1()
            self._debug['num_planes']['end'] = self._io.pos()
            self._debug['bytes_per_line']['start'] = self._io.pos()
            self.bytes_per_line = self._io.read_u2le()
            self._debug['bytes_per_line']['end'] = self._io.pos()
            self._debug['palette_info']['start'] = self._io.pos()
            self.palette_info = self._io.read_u2le()
            self._debug['palette_info']['end'] = self._io.pos()
            self._debug['h_screen_size']['start'] = self._io.pos()
            self.h_screen_size = self._io.read_u2le()
            self._debug['h_screen_size']['end'] = self._io.pos()
            self._debug['v_screen_size']['start'] = self._io.pos()
            self.v_screen_size = self._io.read_u2le()
            self._debug['v_screen_size']['end'] = self._io.pos()


    class TPalette256(KaitaiStruct):
        SEQ_FIELDS = ["magic", "colors"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(1)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x0C":
                raise kaitaistruct.ValidationNotEqualError(b"\x0C", self.magic, self._io, u"/types/t_palette_256/seq/0")
            self._debug['colors']['start'] = self._io.pos()
            self.colors = []
            for i in range(256):
                if not 'arr' in self._debug['colors']:
                    self._debug['colors']['arr'] = []
                self._debug['colors']['arr'].append({'start': self._io.pos()})
                _t_colors = Pcx.Rgb(self._io, self, self._root)
                _t_colors._read()
                self.colors.append(_t_colors)
                self._debug['colors']['arr'][i]['end'] = self._io.pos()

            self._debug['colors']['end'] = self._io.pos()


    class Rgb(KaitaiStruct):
        SEQ_FIELDS = ["r", "g", "b"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['r']['start'] = self._io.pos()
            self.r = self._io.read_u1()
            self._debug['r']['end'] = self._io.pos()
            self._debug['g']['start'] = self._io.pos()
            self.g = self._io.read_u1()
            self._debug['g']['end'] = self._io.pos()
            self._debug['b']['start'] = self._io.pos()
            self.b = self._io.read_u1()
            self._debug['b']['end'] = self._io.pos()


    @property
    def palette_256(self):
        """
        .. seealso::
           - "VGA 256 Color Palette Information" - https://web.archive.org/web/20100206055706/http://www.qzx.com/pc-gpe/pcx.txt
        """
        if hasattr(self, '_m_palette_256'):
            return self._m_palette_256

        if  ((self.hdr.version == Pcx.Versions.v3_0) and (self.hdr.bits_per_pixel == 8) and (self.hdr.num_planes == 1)) :
            _pos = self._io.pos()
            self._io.seek((self._io.size() - 769))
            self._debug['_m_palette_256']['start'] = self._io.pos()
            self._m_palette_256 = Pcx.TPalette256(self._io, self, self._root)
            self._m_palette_256._read()
            self._debug['_m_palette_256']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_palette_256', None)


