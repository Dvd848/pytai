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

class GimpBrush(KaitaiStruct):
    """GIMP brush format is native to the GIMP image editor for storing a brush or a texture.
    It can be used in all [Paint Tools](https://docs.gimp.org/2.10/en/gimp-tools-paint.html),
    for example Pencil and Paintbrush. It works by repeating the brush bitmap as you move
    the tool. The Spacing parameter sets the distance between the brush marks as a percentage
    of brush width. Its default value can be set in the brush file.
    
    You can also use GIMP to create new brushes in this format. Custom brushes can be loaded
    into GIMP for use in the paint tools by copying them into one of the Brush Folders -
    select **Edit** > **Preferences** in the menu bar, expand the **Folders** section
    and choose **Brushes** to see the recognized Brush Folders or to add new ones.
    
    .. seealso::
       Source - https://github.com/GNOME/gimp/blob/441631322b/devel-docs/gbr.txt
    """

    class ColorDepth(Enum):
        grayscale = 1
        rgba = 4
    SEQ_FIELDS = ["len_header", "header"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['len_header']['start'] = self._io.pos()
        self.len_header = self._io.read_u4be()
        self._debug['len_header']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes((self.len_header - 4))
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = GimpBrush.Header(_io__raw_header, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["version", "width", "height", "bytes_per_pixel", "magic", "spacing", "brush_name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 2:
                raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/types/header/seq/0")
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            if not self.width >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.width, self._io, u"/types/header/seq/1")
            if not self.width <= 10000:
                raise kaitaistruct.ValidationGreaterThanError(10000, self.width, self._io, u"/types/header/seq/1")
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()
            if not self.height >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.height, self._io, u"/types/header/seq/2")
            if not self.height <= 10000:
                raise kaitaistruct.ValidationGreaterThanError(10000, self.height, self._io, u"/types/header/seq/2")
            self._debug['bytes_per_pixel']['start'] = self._io.pos()
            self.bytes_per_pixel = KaitaiStream.resolve_enum(GimpBrush.ColorDepth, self._io.read_u4be())
            self._debug['bytes_per_pixel']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x47\x49\x4D\x50":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x49\x4D\x50", self.magic, self._io, u"/types/header/seq/4")
            self._debug['spacing']['start'] = self._io.pos()
            self.spacing = self._io.read_u4be()
            self._debug['spacing']['end'] = self._io.pos()
            self._debug['brush_name']['start'] = self._io.pos()
            self.brush_name = (KaitaiStream.bytes_terminate(self._io.read_bytes_full(), 0, False)).decode(u"UTF-8")
            self._debug['brush_name']['end'] = self._io.pos()


    class Bitmap(KaitaiStruct):
        SEQ_FIELDS = ["rows"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['rows']['start'] = self._io.pos()
            self.rows = []
            for i in range(self._root.header.height):
                if not 'arr' in self._debug['rows']:
                    self._debug['rows']['arr'] = []
                self._debug['rows']['arr'].append({'start': self._io.pos()})
                _t_rows = GimpBrush.Row(self._io, self, self._root)
                _t_rows._read()
                self.rows.append(_t_rows)
                self._debug['rows']['arr'][i]['end'] = self._io.pos()

            self._debug['rows']['end'] = self._io.pos()


    class Row(KaitaiStruct):
        SEQ_FIELDS = ["pixels"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['pixels']['start'] = self._io.pos()
            self.pixels = []
            for i in range(self._root.header.width):
                if not 'arr' in self._debug['pixels']:
                    self._debug['pixels']['arr'] = []
                self._debug['pixels']['arr'].append({'start': self._io.pos()})
                _on = self._root.header.bytes_per_pixel
                if _on == GimpBrush.ColorDepth.grayscale:
                    if not 'arr' in self._debug['pixels']:
                        self._debug['pixels']['arr'] = []
                    self._debug['pixels']['arr'].append({'start': self._io.pos()})
                    _t_pixels = GimpBrush.Row.PixelGray(self._io, self, self._root)
                    _t_pixels._read()
                    self.pixels.append(_t_pixels)
                    self._debug['pixels']['arr'][i]['end'] = self._io.pos()
                elif _on == GimpBrush.ColorDepth.rgba:
                    if not 'arr' in self._debug['pixels']:
                        self._debug['pixels']['arr'] = []
                    self._debug['pixels']['arr'].append({'start': self._io.pos()})
                    _t_pixels = GimpBrush.Row.PixelRgba(self._io, self, self._root)
                    _t_pixels._read()
                    self.pixels.append(_t_pixels)
                    self._debug['pixels']['arr'][i]['end'] = self._io.pos()
                self._debug['pixels']['arr'][i]['end'] = self._io.pos()

            self._debug['pixels']['end'] = self._io.pos()

        class PixelGray(KaitaiStruct):
            SEQ_FIELDS = ["gray"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['gray']['start'] = self._io.pos()
                self.gray = self._io.read_u1()
                self._debug['gray']['end'] = self._io.pos()

            @property
            def red(self):
                if hasattr(self, '_m_red'):
                    return self._m_red

                self._m_red = 0
                return getattr(self, '_m_red', None)

            @property
            def green(self):
                if hasattr(self, '_m_green'):
                    return self._m_green

                self._m_green = 0
                return getattr(self, '_m_green', None)

            @property
            def blue(self):
                if hasattr(self, '_m_blue'):
                    return self._m_blue

                self._m_blue = 0
                return getattr(self, '_m_blue', None)

            @property
            def alpha(self):
                if hasattr(self, '_m_alpha'):
                    return self._m_alpha

                self._m_alpha = self.gray
                return getattr(self, '_m_alpha', None)


        class PixelRgba(KaitaiStruct):
            SEQ_FIELDS = ["red", "green", "blue", "alpha"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['red']['start'] = self._io.pos()
                self.red = self._io.read_u1()
                self._debug['red']['end'] = self._io.pos()
                self._debug['green']['start'] = self._io.pos()
                self.green = self._io.read_u1()
                self._debug['green']['end'] = self._io.pos()
                self._debug['blue']['start'] = self._io.pos()
                self.blue = self._io.read_u1()
                self._debug['blue']['end'] = self._io.pos()
                self._debug['alpha']['start'] = self._io.pos()
                self.alpha = self._io.read_u1()
                self._debug['alpha']['end'] = self._io.pos()



    @property
    def len_body(self):
        if hasattr(self, '_m_len_body'):
            return self._m_len_body

        self._m_len_body = ((self.header.width * self.header.height) * self.header.bytes_per_pixel.value)
        return getattr(self, '_m_len_body', None)

    @property
    def body(self):
        if hasattr(self, '_m_body'):
            return self._m_body

        _pos = self._io.pos()
        self._io.seek(self.len_header)
        self._debug['_m_body']['start'] = self._io.pos()
        self._m_body = self._io.read_bytes(self.len_body)
        self._debug['_m_body']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_body', None)


