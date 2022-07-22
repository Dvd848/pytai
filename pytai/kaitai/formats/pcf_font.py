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

import bytes_with_io
class PcfFont(KaitaiStruct):
    """Portable Compiled Format (PCF) font is a bitmap font format
    originating from X11 Window System. It matches BDF format (which is
    text-based) closely, but instead being binary and
    platform-independent (as opposed to previously used SNF binary
    format) due to introduced features to handle different endianness
    and bit order.
    
    The overall composition of the format is straightforward: it's more
    or less classic directory of type-offset-size pointers, pointing to
    what PCF format calls "tables". Each table carries a certain
    piece of information related to the font (metadata properties,
    metrics, bitmaps, mapping of glyphs to characters, etc).
    
    .. seealso::
       Source - https://fontforge.org/docs/techref/pcf-format.html
    """

    class Types(Enum):
        properties = 1
        accelerators = 2
        metrics = 4
        bitmaps = 8
        ink_metrics = 16
        bdf_encodings = 32
        swidths = 64
        glyph_names = 128
        bdf_accelerators = 256
    SEQ_FIELDS = ["magic", "num_tables", "tables"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x01\x66\x63\x70":
            raise kaitaistruct.ValidationNotEqualError(b"\x01\x66\x63\x70", self.magic, self._io, u"/seq/0")
        self._debug['num_tables']['start'] = self._io.pos()
        self.num_tables = self._io.read_u4le()
        self._debug['num_tables']['end'] = self._io.pos()
        self._debug['tables']['start'] = self._io.pos()
        self.tables = []
        for i in range(self.num_tables):
            if not 'arr' in self._debug['tables']:
                self._debug['tables']['arr'] = []
            self._debug['tables']['arr'].append({'start': self._io.pos()})
            _t_tables = PcfFont.Table(self._io, self, self._root)
            _t_tables._read()
            self.tables.append(_t_tables)
            self._debug['tables']['arr'][i]['end'] = self._io.pos()

        self._debug['tables']['end'] = self._io.pos()

    class Table(KaitaiStruct):
        """Table offers a offset + length pointer to a particular
        table. "Type" of table references certain enum. Applications can
        ignore enum values which they don't support.
        """
        SEQ_FIELDS = ["type", "format", "len_body", "ofs_body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(PcfFont.Types, self._io.read_u4le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['format']['start'] = self._io.pos()
            self.format = PcfFont.Format(self._io, self, self._root)
            self.format._read()
            self._debug['format']['end'] = self._io.pos()
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u4le()
            self._debug['len_body']['end'] = self._io.pos()
            self._debug['ofs_body']['start'] = self._io.pos()
            self.ofs_body = self._io.read_u4le()
            self._debug['ofs_body']['end'] = self._io.pos()

        class Swidths(KaitaiStruct):
            """Table containing scalable widths of characters.
            
            .. seealso::
               Source - https://fontforge.org/docs/techref/pcf-format.html#the-scalable-widths-table
            """
            SEQ_FIELDS = ["format", "num_glyphs", "swidths"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['format']['start'] = self._io.pos()
                self.format = PcfFont.Format(self._io, self, self._root)
                self.format._read()
                self._debug['format']['end'] = self._io.pos()
                self._debug['num_glyphs']['start'] = self._io.pos()
                self.num_glyphs = self._io.read_u4le()
                self._debug['num_glyphs']['end'] = self._io.pos()
                self._debug['swidths']['start'] = self._io.pos()
                self.swidths = []
                for i in range(self.num_glyphs):
                    if not 'arr' in self._debug['swidths']:
                        self._debug['swidths']['arr'] = []
                    self._debug['swidths']['arr'].append({'start': self._io.pos()})
                    self.swidths.append(self._io.read_u4le())
                    self._debug['swidths']['arr'][i]['end'] = self._io.pos()

                self._debug['swidths']['end'] = self._io.pos()


        class Properties(KaitaiStruct):
            """Array of properties (key-value pairs), used to convey different X11
            settings of a font. Key is always an X font atom.
            
            .. seealso::
               Source - https://fontforge.org/docs/techref/pcf-format.html#properties-table
            """
            SEQ_FIELDS = ["format", "num_props", "props", "padding", "len_strings", "strings"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['format']['start'] = self._io.pos()
                self.format = PcfFont.Format(self._io, self, self._root)
                self.format._read()
                self._debug['format']['end'] = self._io.pos()
                self._debug['num_props']['start'] = self._io.pos()
                self.num_props = self._io.read_u4le()
                self._debug['num_props']['end'] = self._io.pos()
                self._debug['props']['start'] = self._io.pos()
                self.props = []
                for i in range(self.num_props):
                    if not 'arr' in self._debug['props']:
                        self._debug['props']['arr'] = []
                    self._debug['props']['arr'].append({'start': self._io.pos()})
                    _t_props = PcfFont.Table.Properties.Prop(self._io, self, self._root)
                    _t_props._read()
                    self.props.append(_t_props)
                    self._debug['props']['arr'][i]['end'] = self._io.pos()

                self._debug['props']['end'] = self._io.pos()
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes((0 if (self.num_props & 3) == 0 else (4 - (self.num_props & 3))))
                self._debug['padding']['end'] = self._io.pos()
                self._debug['len_strings']['start'] = self._io.pos()
                self.len_strings = self._io.read_u4le()
                self._debug['len_strings']['end'] = self._io.pos()
                self._debug['strings']['start'] = self._io.pos()
                self._raw_strings = self._io.read_bytes(self.len_strings)
                _io__raw_strings = KaitaiStream(BytesIO(self._raw_strings))
                self.strings = bytes_with_io.BytesWithIo(_io__raw_strings)
                self.strings._read()
                self._debug['strings']['end'] = self._io.pos()

            class Prop(KaitaiStruct):
                """Property is a key-value pair, "key" being always a
                string and "value" being either a string or a 32-bit
                integer based on an additinal flag (`is_string`).
                
                Simple offset-based mechanism is employed to keep this
                type's sequence fixed-sized and thus have simple access
                to property key/value by index.
                """
                SEQ_FIELDS = ["ofs_name", "is_string", "value_or_ofs_value"]
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._debug = collections.defaultdict(dict)

                def _read(self):
                    self._debug['ofs_name']['start'] = self._io.pos()
                    self.ofs_name = self._io.read_u4le()
                    self._debug['ofs_name']['end'] = self._io.pos()
                    self._debug['is_string']['start'] = self._io.pos()
                    self.is_string = self._io.read_u1()
                    self._debug['is_string']['end'] = self._io.pos()
                    self._debug['value_or_ofs_value']['start'] = self._io.pos()
                    self.value_or_ofs_value = self._io.read_u4le()
                    self._debug['value_or_ofs_value']['end'] = self._io.pos()

                @property
                def name(self):
                    """Name of the property addressed in the strings buffer.
                    """
                    if hasattr(self, '_m_name'):
                        return self._m_name

                    io = self._parent.strings._io
                    _pos = io.pos()
                    io.seek(self.ofs_name)
                    self._debug['_m_name']['start'] = io.pos()
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                    self._debug['_m_name']['end'] = io.pos()
                    io.seek(_pos)
                    return getattr(self, '_m_name', None)

                @property
                def str_value(self):
                    """Value of the property addressed in the strings
                    buffer, if this is a string value.
                    """
                    if hasattr(self, '_m_str_value'):
                        return self._m_str_value

                    if self.is_string != 0:
                        io = self._parent.strings._io
                        _pos = io.pos()
                        io.seek(self.value_or_ofs_value)
                        self._debug['_m_str_value']['start'] = io.pos()
                        self._m_str_value = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                        self._debug['_m_str_value']['end'] = io.pos()
                        io.seek(_pos)

                    return getattr(self, '_m_str_value', None)

                @property
                def int_value(self):
                    """Value of the property, if this is an integer value.
                    """
                    if hasattr(self, '_m_int_value'):
                        return self._m_int_value

                    if self.is_string == 0:
                        self._m_int_value = self.value_or_ofs_value

                    return getattr(self, '_m_int_value', None)



        class BdfEncodings(KaitaiStruct):
            """Table that allows mapping of character codes to glyphs present in the
            font. Supports 1-byte and 2-byte character codes.
            
            Note that this mapping is agnostic to character encoding itself - it
            can represent ASCII, Unicode (ISO/IEC 10646), various single-byte
            national encodings, etc. If application cares about it, normally
            encoding will be specified in `properties` table, in the properties named
            `CHARSET_REGISTRY` / `CHARSET_ENCODING`.
            
            .. seealso::
               Source - https://fontforge.org/docs/techref/pcf-format.html#the-encoding-table
            """
            SEQ_FIELDS = ["format", "min_char_or_byte2", "max_char_or_byte2", "min_byte1", "max_byte1", "default_char", "glyph_indexes"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['format']['start'] = self._io.pos()
                self.format = PcfFont.Format(self._io, self, self._root)
                self.format._read()
                self._debug['format']['end'] = self._io.pos()
                self._debug['min_char_or_byte2']['start'] = self._io.pos()
                self.min_char_or_byte2 = self._io.read_u2le()
                self._debug['min_char_or_byte2']['end'] = self._io.pos()
                self._debug['max_char_or_byte2']['start'] = self._io.pos()
                self.max_char_or_byte2 = self._io.read_u2le()
                self._debug['max_char_or_byte2']['end'] = self._io.pos()
                self._debug['min_byte1']['start'] = self._io.pos()
                self.min_byte1 = self._io.read_u2le()
                self._debug['min_byte1']['end'] = self._io.pos()
                self._debug['max_byte1']['start'] = self._io.pos()
                self.max_byte1 = self._io.read_u2le()
                self._debug['max_byte1']['end'] = self._io.pos()
                self._debug['default_char']['start'] = self._io.pos()
                self.default_char = self._io.read_u2le()
                self._debug['default_char']['end'] = self._io.pos()
                self._debug['glyph_indexes']['start'] = self._io.pos()
                self.glyph_indexes = []
                for i in range((((self.max_char_or_byte2 - self.min_char_or_byte2) + 1) * ((self.max_byte1 - self.min_byte1) + 1))):
                    if not 'arr' in self._debug['glyph_indexes']:
                        self._debug['glyph_indexes']['arr'] = []
                    self._debug['glyph_indexes']['arr'].append({'start': self._io.pos()})
                    self.glyph_indexes.append(self._io.read_u2le())
                    self._debug['glyph_indexes']['arr'][i]['end'] = self._io.pos()

                self._debug['glyph_indexes']['end'] = self._io.pos()


        class GlyphNames(KaitaiStruct):
            """Table containing character names for every glyph.
            
            .. seealso::
               Source - https://fontforge.org/docs/techref/pcf-format.html#the-glyph-names-table
            """
            SEQ_FIELDS = ["format", "num_glyphs", "names", "len_strings", "strings"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['format']['start'] = self._io.pos()
                self.format = PcfFont.Format(self._io, self, self._root)
                self.format._read()
                self._debug['format']['end'] = self._io.pos()
                self._debug['num_glyphs']['start'] = self._io.pos()
                self.num_glyphs = self._io.read_u4le()
                self._debug['num_glyphs']['end'] = self._io.pos()
                self._debug['names']['start'] = self._io.pos()
                self.names = []
                for i in range(self.num_glyphs):
                    if not 'arr' in self._debug['names']:
                        self._debug['names']['arr'] = []
                    self._debug['names']['arr'].append({'start': self._io.pos()})
                    _t_names = PcfFont.Table.GlyphNames.StringRef(self._io, self, self._root)
                    _t_names._read()
                    self.names.append(_t_names)
                    self._debug['names']['arr'][i]['end'] = self._io.pos()

                self._debug['names']['end'] = self._io.pos()
                self._debug['len_strings']['start'] = self._io.pos()
                self.len_strings = self._io.read_u4le()
                self._debug['len_strings']['end'] = self._io.pos()
                self._debug['strings']['start'] = self._io.pos()
                self._raw_strings = self._io.read_bytes(self.len_strings)
                _io__raw_strings = KaitaiStream(BytesIO(self._raw_strings))
                self.strings = bytes_with_io.BytesWithIo(_io__raw_strings)
                self.strings._read()
                self._debug['strings']['end'] = self._io.pos()

            class StringRef(KaitaiStruct):
                SEQ_FIELDS = ["ofs_string"]
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._debug = collections.defaultdict(dict)

                def _read(self):
                    self._debug['ofs_string']['start'] = self._io.pos()
                    self.ofs_string = self._io.read_u4le()
                    self._debug['ofs_string']['end'] = self._io.pos()

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value

                    io = self._parent.strings._io
                    _pos = io.pos()
                    io.seek(self.ofs_string)
                    self._debug['_m_value']['start'] = io.pos()
                    self._m_value = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                    self._debug['_m_value']['end'] = io.pos()
                    io.seek(_pos)
                    return getattr(self, '_m_value', None)



        class Bitmaps(KaitaiStruct):
            """Table containing uncompressed glyph bitmaps.
            
            .. seealso::
               Source - https://fontforge.org/docs/techref/pcf-format.html#the-bitmap-table
            """
            SEQ_FIELDS = ["format", "num_glyphs", "offsets", "bitmap_sizes"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['format']['start'] = self._io.pos()
                self.format = PcfFont.Format(self._io, self, self._root)
                self.format._read()
                self._debug['format']['end'] = self._io.pos()
                self._debug['num_glyphs']['start'] = self._io.pos()
                self.num_glyphs = self._io.read_u4le()
                self._debug['num_glyphs']['end'] = self._io.pos()
                self._debug['offsets']['start'] = self._io.pos()
                self.offsets = []
                for i in range(self.num_glyphs):
                    if not 'arr' in self._debug['offsets']:
                        self._debug['offsets']['arr'] = []
                    self._debug['offsets']['arr'].append({'start': self._io.pos()})
                    self.offsets.append(self._io.read_u4le())
                    self._debug['offsets']['arr'][i]['end'] = self._io.pos()

                self._debug['offsets']['end'] = self._io.pos()
                self._debug['bitmap_sizes']['start'] = self._io.pos()
                self.bitmap_sizes = []
                for i in range(4):
                    if not 'arr' in self._debug['bitmap_sizes']:
                        self._debug['bitmap_sizes']['arr'] = []
                    self._debug['bitmap_sizes']['arr'].append({'start': self._io.pos()})
                    self.bitmap_sizes.append(self._io.read_u4le())
                    self._debug['bitmap_sizes']['arr'][i]['end'] = self._io.pos()

                self._debug['bitmap_sizes']['end'] = self._io.pos()


        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            _pos = self._io.pos()
            self._io.seek(self.ofs_body)
            self._debug['_m_body']['start'] = self._io.pos()
            _on = self.type
            if _on == PcfFont.Types.properties:
                self._raw__m_body = self._io.read_bytes(self.len_body)
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = PcfFont.Table.Properties(_io__raw__m_body, self, self._root)
                self._m_body._read()
            elif _on == PcfFont.Types.bdf_encodings:
                self._raw__m_body = self._io.read_bytes(self.len_body)
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = PcfFont.Table.BdfEncodings(_io__raw__m_body, self, self._root)
                self._m_body._read()
            elif _on == PcfFont.Types.swidths:
                self._raw__m_body = self._io.read_bytes(self.len_body)
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = PcfFont.Table.Swidths(_io__raw__m_body, self, self._root)
                self._m_body._read()
            elif _on == PcfFont.Types.glyph_names:
                self._raw__m_body = self._io.read_bytes(self.len_body)
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = PcfFont.Table.GlyphNames(_io__raw__m_body, self, self._root)
                self._m_body._read()
            elif _on == PcfFont.Types.bitmaps:
                self._raw__m_body = self._io.read_bytes(self.len_body)
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = PcfFont.Table.Bitmaps(_io__raw__m_body, self, self._root)
                self._m_body._read()
            else:
                self._m_body = self._io.read_bytes(self.len_body)
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_body', None)


    class Format(KaitaiStruct):
        """Table format specifier, always 4 bytes. Original implementation treats
        it as always little-endian and makes liberal use of bitmasking to parse
        various parts of it.
        
        TODO: this format specification recognizes endianness and bit
        order format bits, but it does not really takes any parsing
        decisions based on them.
        
        .. seealso::
           Source - https://fontforge.org/docs/techref/pcf-format.html#file-header
        """
        SEQ_FIELDS = ["padding1", "scan_unit_mask", "is_most_significant_bit_first", "is_big_endian", "glyph_pad_mask", "format", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bits_int_be(2)
            self._debug['padding1']['end'] = self._io.pos()
            self._debug['scan_unit_mask']['start'] = self._io.pos()
            self.scan_unit_mask = self._io.read_bits_int_be(2)
            self._debug['scan_unit_mask']['end'] = self._io.pos()
            self._debug['is_most_significant_bit_first']['start'] = self._io.pos()
            self.is_most_significant_bit_first = self._io.read_bits_int_be(1) != 0
            self._debug['is_most_significant_bit_first']['end'] = self._io.pos()
            self._debug['is_big_endian']['start'] = self._io.pos()
            self.is_big_endian = self._io.read_bits_int_be(1) != 0
            self._debug['is_big_endian']['end'] = self._io.pos()
            self._debug['glyph_pad_mask']['start'] = self._io.pos()
            self.glyph_pad_mask = self._io.read_bits_int_be(2)
            self._debug['glyph_pad_mask']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['format']['start'] = self._io.pos()
            self.format = self._io.read_u1()
            self._debug['format']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_u2le()
            self._debug['padding']['end'] = self._io.pos()



