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

class AllegroDat(KaitaiStruct):
    """Allegro library for C (mostly used for game and multimedia apps
    programming) used its own container file format.
    
    In general, it allows storage of arbitrary binary data blocks
    bundled together with some simple key-value style metadata
    ("properties") for every block. Allegro also pre-defines some simple
    formats for bitmaps, fonts, MIDI music, sound samples and
    palettes. Allegro library v4.0+ also support LZSS compression.
    
    This spec applies to Allegro data files for library versions 2.2 up
    to 4.4.
    
    .. seealso::
       Source - https://liballeg.org/stabledocs/en/datafile.html
    """

    class PackEnum(Enum):
        unpacked = 1936484398
    SEQ_FIELDS = ["pack_magic", "dat_magic", "num_objects", "objects"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['pack_magic']['start'] = self._io.pos()
        self.pack_magic = KaitaiStream.resolve_enum(AllegroDat.PackEnum, self._io.read_u4be())
        self._debug['pack_magic']['end'] = self._io.pos()
        self._debug['dat_magic']['start'] = self._io.pos()
        self.dat_magic = self._io.read_bytes(4)
        self._debug['dat_magic']['end'] = self._io.pos()
        if not self.dat_magic == b"\x41\x4C\x4C\x2E":
            raise kaitaistruct.ValidationNotEqualError(b"\x41\x4C\x4C\x2E", self.dat_magic, self._io, u"/seq/1")
        self._debug['num_objects']['start'] = self._io.pos()
        self.num_objects = self._io.read_u4be()
        self._debug['num_objects']['end'] = self._io.pos()
        self._debug['objects']['start'] = self._io.pos()
        self.objects = []
        for i in range(self.num_objects):
            if not 'arr' in self._debug['objects']:
                self._debug['objects']['arr'] = []
            self._debug['objects']['arr'].append({'start': self._io.pos()})
            _t_objects = AllegroDat.DatObject(self._io, self, self._root)
            _t_objects._read()
            self.objects.append(_t_objects)
            self._debug['objects']['arr'][i]['end'] = self._io.pos()

        self._debug['objects']['end'] = self._io.pos()

    class DatFont16(KaitaiStruct):
        """Simple monochrome monospaced font, 95 characters, 8x16 px
        characters.
        """
        SEQ_FIELDS = ["chars"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['chars']['start'] = self._io.pos()
            self.chars = []
            for i in range(95):
                if not 'arr' in self._debug['chars']:
                    self._debug['chars']['arr'] = []
                self._debug['chars']['arr'].append({'start': self._io.pos()})
                self.chars.append(self._io.read_bytes(16))
                self._debug['chars']['arr'][i]['end'] = self._io.pos()

            self._debug['chars']['end'] = self._io.pos()


    class DatBitmap(KaitaiStruct):
        SEQ_FIELDS = ["bits_per_pixel", "width", "height", "image"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bits_per_pixel']['start'] = self._io.pos()
            self.bits_per_pixel = self._io.read_s2be()
            self._debug['bits_per_pixel']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['image']['start'] = self._io.pos()
            self.image = self._io.read_bytes_full()
            self._debug['image']['end'] = self._io.pos()


    class DatFont(KaitaiStruct):
        SEQ_FIELDS = ["font_size", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['font_size']['start'] = self._io.pos()
            self.font_size = self._io.read_s2be()
            self._debug['font_size']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.font_size
            if _on == 8:
                self.body = AllegroDat.DatFont8(self._io, self, self._root)
                self.body._read()
            elif _on == 16:
                self.body = AllegroDat.DatFont16(self._io, self, self._root)
                self.body._read()
            elif _on == 0:
                self.body = AllegroDat.DatFont39(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()


    class DatFont8(KaitaiStruct):
        """Simple monochrome monospaced font, 95 characters, 8x8 px
        characters.
        """
        SEQ_FIELDS = ["chars"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['chars']['start'] = self._io.pos()
            self.chars = []
            for i in range(95):
                if not 'arr' in self._debug['chars']:
                    self._debug['chars']['arr'] = []
                self._debug['chars']['arr'].append({'start': self._io.pos()})
                self.chars.append(self._io.read_bytes(8))
                self._debug['chars']['arr'][i]['end'] = self._io.pos()

            self._debug['chars']['end'] = self._io.pos()


    class DatObject(KaitaiStruct):
        SEQ_FIELDS = ["properties", "len_compressed", "len_uncompressed", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['properties']['start'] = self._io.pos()
            self.properties = []
            i = 0
            while True:
                if not 'arr' in self._debug['properties']:
                    self._debug['properties']['arr'] = []
                self._debug['properties']['arr'].append({'start': self._io.pos()})
                _t_properties = AllegroDat.Property(self._io, self, self._root)
                _t_properties._read()
                _ = _t_properties
                self.properties.append(_)
                self._debug['properties']['arr'][len(self.properties) - 1]['end'] = self._io.pos()
                if not (_.is_valid):
                    break
                i += 1
            self._debug['properties']['end'] = self._io.pos()
            self._debug['len_compressed']['start'] = self._io.pos()
            self.len_compressed = self._io.read_s4be()
            self._debug['len_compressed']['end'] = self._io.pos()
            self._debug['len_uncompressed']['start'] = self._io.pos()
            self.len_uncompressed = self._io.read_s4be()
            self._debug['len_uncompressed']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.type
            if _on == u"BMP ":
                self._raw_body = self._io.read_bytes(self.len_compressed)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AllegroDat.DatBitmap(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"RLE ":
                self._raw_body = self._io.read_bytes(self.len_compressed)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AllegroDat.DatRleSprite(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"FONT":
                self._raw_body = self._io.read_bytes(self.len_compressed)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AllegroDat.DatFont(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes(self.len_compressed)
            self._debug['body']['end'] = self._io.pos()

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = self.properties[-1].magic
            return getattr(self, '_m_type', None)


    class DatFont39(KaitaiStruct):
        """New bitmap font format introduced since Allegro 3.9: allows
        flexible designation of character ranges, 8-bit colored
        characters, etc.
        """
        SEQ_FIELDS = ["num_ranges", "ranges"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_ranges']['start'] = self._io.pos()
            self.num_ranges = self._io.read_s2be()
            self._debug['num_ranges']['end'] = self._io.pos()
            self._debug['ranges']['start'] = self._io.pos()
            self.ranges = []
            for i in range(self.num_ranges):
                if not 'arr' in self._debug['ranges']:
                    self._debug['ranges']['arr'] = []
                self._debug['ranges']['arr'].append({'start': self._io.pos()})
                _t_ranges = AllegroDat.DatFont39.Range(self._io, self, self._root)
                _t_ranges._read()
                self.ranges.append(_t_ranges)
                self._debug['ranges']['arr'][i]['end'] = self._io.pos()

            self._debug['ranges']['end'] = self._io.pos()

        class Range(KaitaiStruct):
            SEQ_FIELDS = ["mono", "start_char", "end_char", "chars"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['mono']['start'] = self._io.pos()
                self.mono = self._io.read_u1()
                self._debug['mono']['end'] = self._io.pos()
                self._debug['start_char']['start'] = self._io.pos()
                self.start_char = self._io.read_u4be()
                self._debug['start_char']['end'] = self._io.pos()
                self._debug['end_char']['start'] = self._io.pos()
                self.end_char = self._io.read_u4be()
                self._debug['end_char']['end'] = self._io.pos()
                self._debug['chars']['start'] = self._io.pos()
                self.chars = []
                for i in range(((self.end_char - self.start_char) + 1)):
                    if not 'arr' in self._debug['chars']:
                        self._debug['chars']['arr'] = []
                    self._debug['chars']['arr'].append({'start': self._io.pos()})
                    _t_chars = AllegroDat.DatFont39.FontChar(self._io, self, self._root)
                    _t_chars._read()
                    self.chars.append(_t_chars)
                    self._debug['chars']['arr'][i]['end'] = self._io.pos()

                self._debug['chars']['end'] = self._io.pos()


        class FontChar(KaitaiStruct):
            SEQ_FIELDS = ["width", "height", "body"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['width']['start'] = self._io.pos()
                self.width = self._io.read_u2be()
                self._debug['width']['end'] = self._io.pos()
                self._debug['height']['start'] = self._io.pos()
                self.height = self._io.read_u2be()
                self._debug['height']['end'] = self._io.pos()
                self._debug['body']['start'] = self._io.pos()
                self.body = self._io.read_bytes((self.width * self.height))
                self._debug['body']['end'] = self._io.pos()



    class Property(KaitaiStruct):
        SEQ_FIELDS = ["magic", "type", "len_body", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = (self._io.read_bytes(4)).decode(u"UTF-8")
            self._debug['magic']['end'] = self._io.pos()
            if self.is_valid:
                self._debug['type']['start'] = self._io.pos()
                self.type = (self._io.read_bytes(4)).decode(u"UTF-8")
                self._debug['type']['end'] = self._io.pos()

            if self.is_valid:
                self._debug['len_body']['start'] = self._io.pos()
                self.len_body = self._io.read_u4be()
                self._debug['len_body']['end'] = self._io.pos()

            if self.is_valid:
                self._debug['body']['start'] = self._io.pos()
                self.body = (self._io.read_bytes(self.len_body)).decode(u"UTF-8")
                self._debug['body']['end'] = self._io.pos()


        @property
        def is_valid(self):
            if hasattr(self, '_m_is_valid'):
                return self._m_is_valid

            self._m_is_valid = self.magic == u"prop"
            return getattr(self, '_m_is_valid', None)


    class DatRleSprite(KaitaiStruct):
        SEQ_FIELDS = ["bits_per_pixel", "width", "height", "len_image", "image"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bits_per_pixel']['start'] = self._io.pos()
            self.bits_per_pixel = self._io.read_s2be()
            self._debug['bits_per_pixel']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4be()
            self._debug['len_image']['end'] = self._io.pos()
            self._debug['image']['start'] = self._io.pos()
            self.image = self._io.read_bytes_full()
            self._debug['image']['end'] = self._io.pos()



