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

class Xwd(KaitaiStruct):
    """xwd is a file format written by eponymous X11 screen capture
    application (xwd stands for "X Window Dump"). Typically, an average
    user transforms xwd format into something more widespread by any of
    `xwdtopnm` and `pnmto...` utilities right away.
    
    xwd format itself provides a raw uncompressed bitmap with some
    metainformation, like pixel format, width, height, bit depth,
    etc. Note that technically format includes machine-dependent fields
    and thus is probably a poor choice for true cross-platform usage.
    """

    class PixmapFormat(Enum):
        x_y_bitmap = 0
        x_y_pixmap = 1
        z_pixmap = 2

    class ByteOrder(Enum):
        le = 0
        be = 1

    class VisualClass(Enum):
        static_gray = 0
        gray_scale = 1
        static_color = 2
        pseudo_color = 3
        true_color = 4
        direct_color = 5
    SEQ_FIELDS = ["len_header", "hdr", "color_map"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['len_header']['start'] = self._io.pos()
        self.len_header = self._io.read_u4be()
        self._debug['len_header']['end'] = self._io.pos()
        self._debug['hdr']['start'] = self._io.pos()
        self._raw_hdr = self._io.read_bytes((self.len_header - 4))
        _io__raw_hdr = KaitaiStream(BytesIO(self._raw_hdr))
        self.hdr = Xwd.Header(_io__raw_hdr, self, self._root)
        self.hdr._read()
        self._debug['hdr']['end'] = self._io.pos()
        self._debug['color_map']['start'] = self._io.pos()
        self._raw_color_map = []
        self.color_map = []
        for i in range(self.hdr.color_map_entries):
            if not 'arr' in self._debug['color_map']:
                self._debug['color_map']['arr'] = []
            self._debug['color_map']['arr'].append({'start': self._io.pos()})
            self._raw_color_map.append(self._io.read_bytes(12))
            _io__raw_color_map = KaitaiStream(BytesIO(self._raw_color_map[i]))
            _t_color_map = Xwd.ColorMapEntry(_io__raw_color_map, self, self._root)
            _t_color_map._read()
            self.color_map.append(_t_color_map)
            self._debug['color_map']['arr'][i]['end'] = self._io.pos()

        self._debug['color_map']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["file_version", "pixmap_format", "pixmap_depth", "pixmap_width", "pixmap_height", "x_offset", "byte_order", "bitmap_unit", "bitmap_bit_order", "bitmap_pad", "bits_per_pixel", "bytes_per_line", "visual_class", "red_mask", "green_mask", "blue_mask", "bits_per_rgb", "number_of_colors", "color_map_entries", "window_width", "window_height", "window_x", "window_y", "window_border_width", "creator"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['file_version']['start'] = self._io.pos()
            self.file_version = self._io.read_u4be()
            self._debug['file_version']['end'] = self._io.pos()
            self._debug['pixmap_format']['start'] = self._io.pos()
            self.pixmap_format = KaitaiStream.resolve_enum(Xwd.PixmapFormat, self._io.read_u4be())
            self._debug['pixmap_format']['end'] = self._io.pos()
            self._debug['pixmap_depth']['start'] = self._io.pos()
            self.pixmap_depth = self._io.read_u4be()
            self._debug['pixmap_depth']['end'] = self._io.pos()
            self._debug['pixmap_width']['start'] = self._io.pos()
            self.pixmap_width = self._io.read_u4be()
            self._debug['pixmap_width']['end'] = self._io.pos()
            self._debug['pixmap_height']['start'] = self._io.pos()
            self.pixmap_height = self._io.read_u4be()
            self._debug['pixmap_height']['end'] = self._io.pos()
            self._debug['x_offset']['start'] = self._io.pos()
            self.x_offset = self._io.read_u4be()
            self._debug['x_offset']['end'] = self._io.pos()
            self._debug['byte_order']['start'] = self._io.pos()
            self.byte_order = KaitaiStream.resolve_enum(Xwd.ByteOrder, self._io.read_u4be())
            self._debug['byte_order']['end'] = self._io.pos()
            self._debug['bitmap_unit']['start'] = self._io.pos()
            self.bitmap_unit = self._io.read_u4be()
            self._debug['bitmap_unit']['end'] = self._io.pos()
            self._debug['bitmap_bit_order']['start'] = self._io.pos()
            self.bitmap_bit_order = self._io.read_u4be()
            self._debug['bitmap_bit_order']['end'] = self._io.pos()
            self._debug['bitmap_pad']['start'] = self._io.pos()
            self.bitmap_pad = self._io.read_u4be()
            self._debug['bitmap_pad']['end'] = self._io.pos()
            self._debug['bits_per_pixel']['start'] = self._io.pos()
            self.bits_per_pixel = self._io.read_u4be()
            self._debug['bits_per_pixel']['end'] = self._io.pos()
            self._debug['bytes_per_line']['start'] = self._io.pos()
            self.bytes_per_line = self._io.read_u4be()
            self._debug['bytes_per_line']['end'] = self._io.pos()
            self._debug['visual_class']['start'] = self._io.pos()
            self.visual_class = KaitaiStream.resolve_enum(Xwd.VisualClass, self._io.read_u4be())
            self._debug['visual_class']['end'] = self._io.pos()
            self._debug['red_mask']['start'] = self._io.pos()
            self.red_mask = self._io.read_u4be()
            self._debug['red_mask']['end'] = self._io.pos()
            self._debug['green_mask']['start'] = self._io.pos()
            self.green_mask = self._io.read_u4be()
            self._debug['green_mask']['end'] = self._io.pos()
            self._debug['blue_mask']['start'] = self._io.pos()
            self.blue_mask = self._io.read_u4be()
            self._debug['blue_mask']['end'] = self._io.pos()
            self._debug['bits_per_rgb']['start'] = self._io.pos()
            self.bits_per_rgb = self._io.read_u4be()
            self._debug['bits_per_rgb']['end'] = self._io.pos()
            self._debug['number_of_colors']['start'] = self._io.pos()
            self.number_of_colors = self._io.read_u4be()
            self._debug['number_of_colors']['end'] = self._io.pos()
            self._debug['color_map_entries']['start'] = self._io.pos()
            self.color_map_entries = self._io.read_u4be()
            self._debug['color_map_entries']['end'] = self._io.pos()
            self._debug['window_width']['start'] = self._io.pos()
            self.window_width = self._io.read_u4be()
            self._debug['window_width']['end'] = self._io.pos()
            self._debug['window_height']['start'] = self._io.pos()
            self.window_height = self._io.read_u4be()
            self._debug['window_height']['end'] = self._io.pos()
            self._debug['window_x']['start'] = self._io.pos()
            self.window_x = self._io.read_s4be()
            self._debug['window_x']['end'] = self._io.pos()
            self._debug['window_y']['start'] = self._io.pos()
            self.window_y = self._io.read_s4be()
            self._debug['window_y']['end'] = self._io.pos()
            self._debug['window_border_width']['start'] = self._io.pos()
            self.window_border_width = self._io.read_u4be()
            self._debug['window_border_width']['end'] = self._io.pos()
            self._debug['creator']['start'] = self._io.pos()
            self.creator = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['creator']['end'] = self._io.pos()


    class ColorMapEntry(KaitaiStruct):
        SEQ_FIELDS = ["entry_number", "red", "green", "blue", "flags", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['entry_number']['start'] = self._io.pos()
            self.entry_number = self._io.read_u4be()
            self._debug['entry_number']['end'] = self._io.pos()
            self._debug['red']['start'] = self._io.pos()
            self.red = self._io.read_u2be()
            self._debug['red']['end'] = self._io.pos()
            self._debug['green']['start'] = self._io.pos()
            self.green = self._io.read_u2be()
            self._debug['green']['end'] = self._io.pos()
            self._debug['blue']['start'] = self._io.pos()
            self.blue = self._io.read_u2be()
            self._debug['blue']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_u1()
            self._debug['padding']['end'] = self._io.pos()



