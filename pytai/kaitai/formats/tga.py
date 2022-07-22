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

class Tga(KaitaiStruct):
    """TGA (AKA Truevision TGA, AKA TARGA), is a raster image file format created by Truevision. It supports up to 32 bits per pixel (three 8-bit RGB channels + 8-bit alpha channel), color mapping and optional lossless RLE compression.
    
    .. seealso::
       Source - https://www.dca.fee.unicamp.br/~martino/disciplinas/ea978/tgaffs.pdf
    """

    class ColorMapEnum(Enum):
        no_color_map = 0
        has_color_map = 1

    class ImageTypeEnum(Enum):
        no_image_data = 0
        uncomp_color_mapped = 1
        uncomp_true_color = 2
        uncomp_bw = 3
        rle_color_mapped = 9
        rle_true_color = 10
        rle_bw = 11
    SEQ_FIELDS = ["image_id_len", "color_map_type", "image_type", "color_map_ofs", "num_color_map", "color_map_depth", "x_offset", "y_offset", "width", "height", "image_depth", "img_descriptor", "image_id", "color_map"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['image_id_len']['start'] = self._io.pos()
        self.image_id_len = self._io.read_u1()
        self._debug['image_id_len']['end'] = self._io.pos()
        self._debug['color_map_type']['start'] = self._io.pos()
        self.color_map_type = KaitaiStream.resolve_enum(Tga.ColorMapEnum, self._io.read_u1())
        self._debug['color_map_type']['end'] = self._io.pos()
        self._debug['image_type']['start'] = self._io.pos()
        self.image_type = KaitaiStream.resolve_enum(Tga.ImageTypeEnum, self._io.read_u1())
        self._debug['image_type']['end'] = self._io.pos()
        self._debug['color_map_ofs']['start'] = self._io.pos()
        self.color_map_ofs = self._io.read_u2le()
        self._debug['color_map_ofs']['end'] = self._io.pos()
        self._debug['num_color_map']['start'] = self._io.pos()
        self.num_color_map = self._io.read_u2le()
        self._debug['num_color_map']['end'] = self._io.pos()
        self._debug['color_map_depth']['start'] = self._io.pos()
        self.color_map_depth = self._io.read_u1()
        self._debug['color_map_depth']['end'] = self._io.pos()
        self._debug['x_offset']['start'] = self._io.pos()
        self.x_offset = self._io.read_u2le()
        self._debug['x_offset']['end'] = self._io.pos()
        self._debug['y_offset']['start'] = self._io.pos()
        self.y_offset = self._io.read_u2le()
        self._debug['y_offset']['end'] = self._io.pos()
        self._debug['width']['start'] = self._io.pos()
        self.width = self._io.read_u2le()
        self._debug['width']['end'] = self._io.pos()
        self._debug['height']['start'] = self._io.pos()
        self.height = self._io.read_u2le()
        self._debug['height']['end'] = self._io.pos()
        self._debug['image_depth']['start'] = self._io.pos()
        self.image_depth = self._io.read_u1()
        self._debug['image_depth']['end'] = self._io.pos()
        self._debug['img_descriptor']['start'] = self._io.pos()
        self.img_descriptor = self._io.read_u1()
        self._debug['img_descriptor']['end'] = self._io.pos()
        self._debug['image_id']['start'] = self._io.pos()
        self.image_id = self._io.read_bytes(self.image_id_len)
        self._debug['image_id']['end'] = self._io.pos()
        if self.color_map_type == Tga.ColorMapEnum.has_color_map:
            self._debug['color_map']['start'] = self._io.pos()
            self.color_map = []
            for i in range(self.num_color_map):
                if not 'arr' in self._debug['color_map']:
                    self._debug['color_map']['arr'] = []
                self._debug['color_map']['arr'].append({'start': self._io.pos()})
                self.color_map.append(self._io.read_bytes((self.color_map_depth + 7) // 8))
                self._debug['color_map']['arr'][i]['end'] = self._io.pos()

            self._debug['color_map']['end'] = self._io.pos()


    class TgaFooter(KaitaiStruct):
        SEQ_FIELDS = ["ext_area_ofs", "dev_dir_ofs", "version_magic"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['ext_area_ofs']['start'] = self._io.pos()
            self.ext_area_ofs = self._io.read_u4le()
            self._debug['ext_area_ofs']['end'] = self._io.pos()
            self._debug['dev_dir_ofs']['start'] = self._io.pos()
            self.dev_dir_ofs = self._io.read_u4le()
            self._debug['dev_dir_ofs']['end'] = self._io.pos()
            self._debug['version_magic']['start'] = self._io.pos()
            self.version_magic = self._io.read_bytes(18)
            self._debug['version_magic']['end'] = self._io.pos()

        @property
        def is_valid(self):
            if hasattr(self, '_m_is_valid'):
                return self._m_is_valid

            self._m_is_valid = self.version_magic == b"\x54\x52\x55\x45\x56\x49\x53\x49\x4F\x4E\x2D\x58\x46\x49\x4C\x45\x2E\x00"
            return getattr(self, '_m_is_valid', None)

        @property
        def ext_area(self):
            if hasattr(self, '_m_ext_area'):
                return self._m_ext_area

            if self.is_valid:
                _pos = self._io.pos()
                self._io.seek(self.ext_area_ofs)
                self._debug['_m_ext_area']['start'] = self._io.pos()
                self._m_ext_area = Tga.TgaExtArea(self._io, self, self._root)
                self._m_ext_area._read()
                self._debug['_m_ext_area']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_ext_area', None)


    class TgaExtArea(KaitaiStruct):
        SEQ_FIELDS = ["ext_area_size", "author_name", "comments", "timestamp", "job_id", "job_time", "software_id", "software_version", "key_color", "pixel_aspect_ratio", "gamma_value", "color_corr_ofs", "postage_stamp_ofs", "scan_line_ofs", "attributes"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['ext_area_size']['start'] = self._io.pos()
            self.ext_area_size = self._io.read_u2le()
            self._debug['ext_area_size']['end'] = self._io.pos()
            self._debug['author_name']['start'] = self._io.pos()
            self.author_name = (self._io.read_bytes(41)).decode(u"ASCII")
            self._debug['author_name']['end'] = self._io.pos()
            self._debug['comments']['start'] = self._io.pos()
            self.comments = []
            for i in range(4):
                if not 'arr' in self._debug['comments']:
                    self._debug['comments']['arr'] = []
                self._debug['comments']['arr'].append({'start': self._io.pos()})
                self.comments.append((self._io.read_bytes(81)).decode(u"ASCII"))
                self._debug['comments']['arr'][i]['end'] = self._io.pos()

            self._debug['comments']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_bytes(12)
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['job_id']['start'] = self._io.pos()
            self.job_id = (self._io.read_bytes(41)).decode(u"ASCII")
            self._debug['job_id']['end'] = self._io.pos()
            self._debug['job_time']['start'] = self._io.pos()
            self.job_time = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['job_time']['end'] = self._io.pos()
            self._debug['software_id']['start'] = self._io.pos()
            self.software_id = (self._io.read_bytes(41)).decode(u"ASCII")
            self._debug['software_id']['end'] = self._io.pos()
            self._debug['software_version']['start'] = self._io.pos()
            self.software_version = self._io.read_bytes(3)
            self._debug['software_version']['end'] = self._io.pos()
            self._debug['key_color']['start'] = self._io.pos()
            self.key_color = self._io.read_u4le()
            self._debug['key_color']['end'] = self._io.pos()
            self._debug['pixel_aspect_ratio']['start'] = self._io.pos()
            self.pixel_aspect_ratio = self._io.read_u4le()
            self._debug['pixel_aspect_ratio']['end'] = self._io.pos()
            self._debug['gamma_value']['start'] = self._io.pos()
            self.gamma_value = self._io.read_u4le()
            self._debug['gamma_value']['end'] = self._io.pos()
            self._debug['color_corr_ofs']['start'] = self._io.pos()
            self.color_corr_ofs = self._io.read_u4le()
            self._debug['color_corr_ofs']['end'] = self._io.pos()
            self._debug['postage_stamp_ofs']['start'] = self._io.pos()
            self.postage_stamp_ofs = self._io.read_u4le()
            self._debug['postage_stamp_ofs']['end'] = self._io.pos()
            self._debug['scan_line_ofs']['start'] = self._io.pos()
            self.scan_line_ofs = self._io.read_u4le()
            self._debug['scan_line_ofs']['end'] = self._io.pos()
            self._debug['attributes']['start'] = self._io.pos()
            self.attributes = self._io.read_u1()
            self._debug['attributes']['end'] = self._io.pos()


    @property
    def footer(self):
        if hasattr(self, '_m_footer'):
            return self._m_footer

        _pos = self._io.pos()
        self._io.seek((self._io.size() - 26))
        self._debug['_m_footer']['start'] = self._io.pos()
        self._m_footer = Tga.TgaFooter(self._io, self, self._root)
        self._m_footer._read()
        self._debug['_m_footer']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_footer', None)


