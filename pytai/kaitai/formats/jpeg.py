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

import exif
class Jpeg(KaitaiStruct):
    """JPEG File Interchange Format, or JFIF, or, more colloquially known
    as just "JPEG" or "JPG", is a popular 2D bitmap image file format,
    offering lossy compression which works reasonably well with
    photographic images.
    
    Format is organized as a container format, serving multiple
    "segments", each starting with a magic and a marker. JFIF standard
    dictates order and mandatory apperance of segments:
    
    * SOI
    * APP0 (with JFIF magic)
    * APP0 (with JFXX magic, optional)
    * everything else
    * SOS
    * JPEG-compressed stream
    * EOI
    """

    class ComponentId(Enum):
        y = 1
        cb = 2
        cr = 3
        i = 4
        q = 5
    SEQ_FIELDS = ["segments"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['segments']['start'] = self._io.pos()
        self.segments = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['segments']:
                self._debug['segments']['arr'] = []
            self._debug['segments']['arr'].append({'start': self._io.pos()})
            _t_segments = Jpeg.Segment(self._io, self, self._root)
            _t_segments._read()
            self.segments.append(_t_segments)
            self._debug['segments']['arr'][len(self.segments) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['segments']['end'] = self._io.pos()

    class Segment(KaitaiStruct):

        class MarkerEnum(Enum):
            tem = 1
            sof0 = 192
            sof1 = 193
            sof2 = 194
            sof3 = 195
            dht = 196
            sof5 = 197
            sof6 = 198
            sof7 = 199
            soi = 216
            eoi = 217
            sos = 218
            dqt = 219
            dnl = 220
            dri = 221
            dhp = 222
            app0 = 224
            app1 = 225
            app2 = 226
            app3 = 227
            app4 = 228
            app5 = 229
            app6 = 230
            app7 = 231
            app8 = 232
            app9 = 233
            app10 = 234
            app11 = 235
            app12 = 236
            app13 = 237
            app14 = 238
            app15 = 239
            com = 254
        SEQ_FIELDS = ["magic", "marker", "length", "data", "image_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(1)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF", self.magic, self._io, u"/types/segment/seq/0")
            self._debug['marker']['start'] = self._io.pos()
            self.marker = KaitaiStream.resolve_enum(Jpeg.Segment.MarkerEnum, self._io.read_u1())
            self._debug['marker']['end'] = self._io.pos()
            if  ((self.marker != Jpeg.Segment.MarkerEnum.soi) and (self.marker != Jpeg.Segment.MarkerEnum.eoi)) :
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u2be()
                self._debug['length']['end'] = self._io.pos()

            if  ((self.marker != Jpeg.Segment.MarkerEnum.soi) and (self.marker != Jpeg.Segment.MarkerEnum.eoi)) :
                self._debug['data']['start'] = self._io.pos()
                _on = self.marker
                if _on == Jpeg.Segment.MarkerEnum.app1:
                    self._raw_data = self._io.read_bytes((self.length - 2))
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Jpeg.SegmentApp1(_io__raw_data, self, self._root)
                    self.data._read()
                elif _on == Jpeg.Segment.MarkerEnum.app0:
                    self._raw_data = self._io.read_bytes((self.length - 2))
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Jpeg.SegmentApp0(_io__raw_data, self, self._root)
                    self.data._read()
                elif _on == Jpeg.Segment.MarkerEnum.sof0:
                    self._raw_data = self._io.read_bytes((self.length - 2))
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Jpeg.SegmentSof0(_io__raw_data, self, self._root)
                    self.data._read()
                elif _on == Jpeg.Segment.MarkerEnum.sos:
                    self._raw_data = self._io.read_bytes((self.length - 2))
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Jpeg.SegmentSos(_io__raw_data, self, self._root)
                    self.data._read()
                else:
                    self.data = self._io.read_bytes((self.length - 2))
                self._debug['data']['end'] = self._io.pos()

            if self.marker == Jpeg.Segment.MarkerEnum.sos:
                self._debug['image_data']['start'] = self._io.pos()
                self.image_data = self._io.read_bytes_full()
                self._debug['image_data']['end'] = self._io.pos()



    class SegmentSos(KaitaiStruct):
        SEQ_FIELDS = ["num_components", "components", "start_spectral_selection", "end_spectral", "appr_bit_pos"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_components']['start'] = self._io.pos()
            self.num_components = self._io.read_u1()
            self._debug['num_components']['end'] = self._io.pos()
            self._debug['components']['start'] = self._io.pos()
            self.components = []
            for i in range(self.num_components):
                if not 'arr' in self._debug['components']:
                    self._debug['components']['arr'] = []
                self._debug['components']['arr'].append({'start': self._io.pos()})
                _t_components = Jpeg.SegmentSos.Component(self._io, self, self._root)
                _t_components._read()
                self.components.append(_t_components)
                self._debug['components']['arr'][i]['end'] = self._io.pos()

            self._debug['components']['end'] = self._io.pos()
            self._debug['start_spectral_selection']['start'] = self._io.pos()
            self.start_spectral_selection = self._io.read_u1()
            self._debug['start_spectral_selection']['end'] = self._io.pos()
            self._debug['end_spectral']['start'] = self._io.pos()
            self.end_spectral = self._io.read_u1()
            self._debug['end_spectral']['end'] = self._io.pos()
            self._debug['appr_bit_pos']['start'] = self._io.pos()
            self.appr_bit_pos = self._io.read_u1()
            self._debug['appr_bit_pos']['end'] = self._io.pos()

        class Component(KaitaiStruct):
            SEQ_FIELDS = ["id", "huffman_table"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['id']['start'] = self._io.pos()
                self.id = KaitaiStream.resolve_enum(Jpeg.ComponentId, self._io.read_u1())
                self._debug['id']['end'] = self._io.pos()
                self._debug['huffman_table']['start'] = self._io.pos()
                self.huffman_table = self._io.read_u1()
                self._debug['huffman_table']['end'] = self._io.pos()



    class SegmentApp1(KaitaiStruct):
        SEQ_FIELDS = ["magic", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['magic']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.magic
            if _on == u"Exif":
                self.body = Jpeg.ExifInJpeg(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()


    class SegmentSof0(KaitaiStruct):
        SEQ_FIELDS = ["bits_per_sample", "image_height", "image_width", "num_components", "components"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bits_per_sample']['start'] = self._io.pos()
            self.bits_per_sample = self._io.read_u1()
            self._debug['bits_per_sample']['end'] = self._io.pos()
            self._debug['image_height']['start'] = self._io.pos()
            self.image_height = self._io.read_u2be()
            self._debug['image_height']['end'] = self._io.pos()
            self._debug['image_width']['start'] = self._io.pos()
            self.image_width = self._io.read_u2be()
            self._debug['image_width']['end'] = self._io.pos()
            self._debug['num_components']['start'] = self._io.pos()
            self.num_components = self._io.read_u1()
            self._debug['num_components']['end'] = self._io.pos()
            self._debug['components']['start'] = self._io.pos()
            self.components = []
            for i in range(self.num_components):
                if not 'arr' in self._debug['components']:
                    self._debug['components']['arr'] = []
                self._debug['components']['arr'].append({'start': self._io.pos()})
                _t_components = Jpeg.SegmentSof0.Component(self._io, self, self._root)
                _t_components._read()
                self.components.append(_t_components)
                self._debug['components']['arr'][i]['end'] = self._io.pos()

            self._debug['components']['end'] = self._io.pos()

        class Component(KaitaiStruct):
            SEQ_FIELDS = ["id", "sampling_factors", "quantization_table_id"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['id']['start'] = self._io.pos()
                self.id = KaitaiStream.resolve_enum(Jpeg.ComponentId, self._io.read_u1())
                self._debug['id']['end'] = self._io.pos()
                self._debug['sampling_factors']['start'] = self._io.pos()
                self.sampling_factors = self._io.read_u1()
                self._debug['sampling_factors']['end'] = self._io.pos()
                self._debug['quantization_table_id']['start'] = self._io.pos()
                self.quantization_table_id = self._io.read_u1()
                self._debug['quantization_table_id']['end'] = self._io.pos()

            @property
            def sampling_x(self):
                if hasattr(self, '_m_sampling_x'):
                    return self._m_sampling_x

                self._m_sampling_x = ((self.sampling_factors & 240) >> 4)
                return getattr(self, '_m_sampling_x', None)

            @property
            def sampling_y(self):
                if hasattr(self, '_m_sampling_y'):
                    return self._m_sampling_y

                self._m_sampling_y = (self.sampling_factors & 15)
                return getattr(self, '_m_sampling_y', None)



    class ExifInJpeg(KaitaiStruct):
        SEQ_FIELDS = ["extra_zero", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['extra_zero']['start'] = self._io.pos()
            self.extra_zero = self._io.read_bytes(1)
            self._debug['extra_zero']['end'] = self._io.pos()
            if not self.extra_zero == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.extra_zero, self._io, u"/types/exif_in_jpeg/seq/0")
            self._debug['data']['start'] = self._io.pos()
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = exif.Exif(_io__raw_data)
            self.data._read()
            self._debug['data']['end'] = self._io.pos()


    class SegmentApp0(KaitaiStruct):

        class DensityUnit(Enum):
            no_units = 0
            pixels_per_inch = 1
            pixels_per_cm = 2
        SEQ_FIELDS = ["magic", "version_major", "version_minor", "density_units", "density_x", "density_y", "thumbnail_x", "thumbnail_y", "thumbnail"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = (self._io.read_bytes(5)).decode(u"ASCII")
            self._debug['magic']['end'] = self._io.pos()
            self._debug['version_major']['start'] = self._io.pos()
            self.version_major = self._io.read_u1()
            self._debug['version_major']['end'] = self._io.pos()
            self._debug['version_minor']['start'] = self._io.pos()
            self.version_minor = self._io.read_u1()
            self._debug['version_minor']['end'] = self._io.pos()
            self._debug['density_units']['start'] = self._io.pos()
            self.density_units = KaitaiStream.resolve_enum(Jpeg.SegmentApp0.DensityUnit, self._io.read_u1())
            self._debug['density_units']['end'] = self._io.pos()
            self._debug['density_x']['start'] = self._io.pos()
            self.density_x = self._io.read_u2be()
            self._debug['density_x']['end'] = self._io.pos()
            self._debug['density_y']['start'] = self._io.pos()
            self.density_y = self._io.read_u2be()
            self._debug['density_y']['end'] = self._io.pos()
            self._debug['thumbnail_x']['start'] = self._io.pos()
            self.thumbnail_x = self._io.read_u1()
            self._debug['thumbnail_x']['end'] = self._io.pos()
            self._debug['thumbnail_y']['start'] = self._io.pos()
            self.thumbnail_y = self._io.read_u1()
            self._debug['thumbnail_y']['end'] = self._io.pos()
            self._debug['thumbnail']['start'] = self._io.pos()
            self.thumbnail = self._io.read_bytes(((self.thumbnail_x * self.thumbnail_y) * 3))
            self._debug['thumbnail']['end'] = self._io.pos()



