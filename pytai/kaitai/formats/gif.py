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

class Gif(KaitaiStruct):
    """GIF (Graphics Interchange Format) is an image file format, developed
    in 1987. It became popular in 1990s as one of the main image formats
    used in World Wide Web.
    
    GIF format allows encoding of palette-based images up to 256 colors
    (each of the colors can be chosen from a 24-bit RGB
    colorspace). Image data stream uses LZW (Lempel-Ziv-Welch) lossless
    compression.
    
    Over the years, several version of the format were published and
    several extensions to it were made, namely, a popular Netscape
    extension that allows to store several images in one file, switching
    between them, which produces crude form of animation.
    
    Structurally, format consists of several mandatory headers and then
    a stream of blocks follows. Blocks can carry additional
    metainformation or image data.
    """

    class BlockType(Enum):
        extension = 33
        local_image_descriptor = 44
        end_of_file = 59

    class ExtensionLabel(Enum):
        graphic_control = 249
        comment = 254
        application = 255
    SEQ_FIELDS = ["hdr", "logical_screen_descriptor", "global_color_table", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['hdr']['start'] = self._io.pos()
        self.hdr = Gif.Header(self._io, self, self._root)
        self.hdr._read()
        self._debug['hdr']['end'] = self._io.pos()
        self._debug['logical_screen_descriptor']['start'] = self._io.pos()
        self.logical_screen_descriptor = Gif.LogicalScreenDescriptorStruct(self._io, self, self._root)
        self.logical_screen_descriptor._read()
        self._debug['logical_screen_descriptor']['end'] = self._io.pos()
        if self.logical_screen_descriptor.has_color_table:
            self._debug['global_color_table']['start'] = self._io.pos()
            self._raw_global_color_table = self._io.read_bytes((self.logical_screen_descriptor.color_table_size * 3))
            _io__raw_global_color_table = KaitaiStream(BytesIO(self._raw_global_color_table))
            self.global_color_table = Gif.ColorTable(_io__raw_global_color_table, self, self._root)
            self.global_color_table._read()
            self._debug['global_color_table']['end'] = self._io.pos()

        self._debug['blocks']['start'] = self._io.pos()
        self.blocks = []
        i = 0
        while True:
            if not 'arr' in self._debug['blocks']:
                self._debug['blocks']['arr'] = []
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _t_blocks = Gif.Block(self._io, self, self._root)
            _t_blocks._read()
            _ = _t_blocks
            self.blocks.append(_)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            if  ((self._io.is_eof()) or (_.block_type == Gif.BlockType.end_of_file)) :
                break
            i += 1
        self._debug['blocks']['end'] = self._io.pos()

    class ImageData(KaitaiStruct):
        """
        .. seealso::
           - section 22 - https://www.w3.org/Graphics/GIF/spec-gif89a.txt
        """
        SEQ_FIELDS = ["lzw_min_code_size", "subblocks"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['lzw_min_code_size']['start'] = self._io.pos()
            self.lzw_min_code_size = self._io.read_u1()
            self._debug['lzw_min_code_size']['end'] = self._io.pos()
            self._debug['subblocks']['start'] = self._io.pos()
            self.subblocks = Gif.Subblocks(self._io, self, self._root)
            self.subblocks._read()
            self._debug['subblocks']['end'] = self._io.pos()


    class ColorTableEntry(KaitaiStruct):
        SEQ_FIELDS = ["red", "green", "blue"]
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


    class LogicalScreenDescriptorStruct(KaitaiStruct):
        """
        .. seealso::
           - section 18 - https://www.w3.org/Graphics/GIF/spec-gif89a.txt
        """
        SEQ_FIELDS = ["screen_width", "screen_height", "flags", "bg_color_index", "pixel_aspect_ratio"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['screen_width']['start'] = self._io.pos()
            self.screen_width = self._io.read_u2le()
            self._debug['screen_width']['end'] = self._io.pos()
            self._debug['screen_height']['start'] = self._io.pos()
            self.screen_height = self._io.read_u2le()
            self._debug['screen_height']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['bg_color_index']['start'] = self._io.pos()
            self.bg_color_index = self._io.read_u1()
            self._debug['bg_color_index']['end'] = self._io.pos()
            self._debug['pixel_aspect_ratio']['start'] = self._io.pos()
            self.pixel_aspect_ratio = self._io.read_u1()
            self._debug['pixel_aspect_ratio']['end'] = self._io.pos()

        @property
        def has_color_table(self):
            if hasattr(self, '_m_has_color_table'):
                return self._m_has_color_table

            self._m_has_color_table = (self.flags & 128) != 0
            return getattr(self, '_m_has_color_table', None)

        @property
        def color_table_size(self):
            if hasattr(self, '_m_color_table_size'):
                return self._m_color_table_size

            self._m_color_table_size = (2 << (self.flags & 7))
            return getattr(self, '_m_color_table_size', None)


    class LocalImageDescriptor(KaitaiStruct):
        SEQ_FIELDS = ["left", "top", "width", "height", "flags", "local_color_table", "image_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['left']['start'] = self._io.pos()
            self.left = self._io.read_u2le()
            self._debug['left']['end'] = self._io.pos()
            self._debug['top']['start'] = self._io.pos()
            self.top = self._io.read_u2le()
            self._debug['top']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            if self.has_color_table:
                self._debug['local_color_table']['start'] = self._io.pos()
                self._raw_local_color_table = self._io.read_bytes((self.color_table_size * 3))
                _io__raw_local_color_table = KaitaiStream(BytesIO(self._raw_local_color_table))
                self.local_color_table = Gif.ColorTable(_io__raw_local_color_table, self, self._root)
                self.local_color_table._read()
                self._debug['local_color_table']['end'] = self._io.pos()

            self._debug['image_data']['start'] = self._io.pos()
            self.image_data = Gif.ImageData(self._io, self, self._root)
            self.image_data._read()
            self._debug['image_data']['end'] = self._io.pos()

        @property
        def has_color_table(self):
            if hasattr(self, '_m_has_color_table'):
                return self._m_has_color_table

            self._m_has_color_table = (self.flags & 128) != 0
            return getattr(self, '_m_has_color_table', None)

        @property
        def has_interlace(self):
            if hasattr(self, '_m_has_interlace'):
                return self._m_has_interlace

            self._m_has_interlace = (self.flags & 64) != 0
            return getattr(self, '_m_has_interlace', None)

        @property
        def has_sorted_color_table(self):
            if hasattr(self, '_m_has_sorted_color_table'):
                return self._m_has_sorted_color_table

            self._m_has_sorted_color_table = (self.flags & 32) != 0
            return getattr(self, '_m_has_sorted_color_table', None)

        @property
        def color_table_size(self):
            if hasattr(self, '_m_color_table_size'):
                return self._m_color_table_size

            self._m_color_table_size = (2 << (self.flags & 7))
            return getattr(self, '_m_color_table_size', None)


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["block_type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['block_type']['start'] = self._io.pos()
            self.block_type = KaitaiStream.resolve_enum(Gif.BlockType, self._io.read_u1())
            self._debug['block_type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.block_type
            if _on == Gif.BlockType.extension:
                self.body = Gif.Extension(self._io, self, self._root)
                self.body._read()
            elif _on == Gif.BlockType.local_image_descriptor:
                self.body = Gif.LocalImageDescriptor(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()


    class ColorTable(KaitaiStruct):
        """
        .. seealso::
           - section 19 - https://www.w3.org/Graphics/GIF/spec-gif89a.txt
        """
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self.entries = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['entries']:
                    self._debug['entries']['arr'] = []
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _t_entries = Gif.ColorTableEntry(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class Header(KaitaiStruct):
        """
        .. seealso::
           - section 17 - https://www.w3.org/Graphics/GIF/spec-gif89a.txt
        """
        SEQ_FIELDS = ["magic", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(3)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x47\x49\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x49\x46", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = (self._io.read_bytes(3)).decode(u"ASCII")
            self._debug['version']['end'] = self._io.pos()


    class ExtGraphicControl(KaitaiStruct):
        """
        .. seealso::
           - section 23 - https://www.w3.org/Graphics/GIF/spec-gif89a.txt
        """
        SEQ_FIELDS = ["block_size", "flags", "delay_time", "transparent_idx", "terminator"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['block_size']['start'] = self._io.pos()
            self.block_size = self._io.read_bytes(1)
            self._debug['block_size']['end'] = self._io.pos()
            if not self.block_size == b"\x04":
                raise kaitaistruct.ValidationNotEqualError(b"\x04", self.block_size, self._io, u"/types/ext_graphic_control/seq/0")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['delay_time']['start'] = self._io.pos()
            self.delay_time = self._io.read_u2le()
            self._debug['delay_time']['end'] = self._io.pos()
            self._debug['transparent_idx']['start'] = self._io.pos()
            self.transparent_idx = self._io.read_u1()
            self._debug['transparent_idx']['end'] = self._io.pos()
            self._debug['terminator']['start'] = self._io.pos()
            self.terminator = self._io.read_bytes(1)
            self._debug['terminator']['end'] = self._io.pos()
            if not self.terminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.terminator, self._io, u"/types/ext_graphic_control/seq/4")

        @property
        def transparent_color_flag(self):
            if hasattr(self, '_m_transparent_color_flag'):
                return self._m_transparent_color_flag

            self._m_transparent_color_flag = (self.flags & 1) != 0
            return getattr(self, '_m_transparent_color_flag', None)

        @property
        def user_input_flag(self):
            if hasattr(self, '_m_user_input_flag'):
                return self._m_user_input_flag

            self._m_user_input_flag = (self.flags & 2) != 0
            return getattr(self, '_m_user_input_flag', None)


    class Subblock(KaitaiStruct):
        SEQ_FIELDS = ["len_bytes", "bytes"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_bytes']['start'] = self._io.pos()
            self.len_bytes = self._io.read_u1()
            self._debug['len_bytes']['end'] = self._io.pos()
            self._debug['bytes']['start'] = self._io.pos()
            self.bytes = self._io.read_bytes(self.len_bytes)
            self._debug['bytes']['end'] = self._io.pos()


    class ApplicationId(KaitaiStruct):
        SEQ_FIELDS = ["len_bytes", "application_identifier", "application_auth_code"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_bytes']['start'] = self._io.pos()
            self.len_bytes = self._io.read_u1()
            self._debug['len_bytes']['end'] = self._io.pos()
            if not self.len_bytes == 11:
                raise kaitaistruct.ValidationNotEqualError(11, self.len_bytes, self._io, u"/types/application_id/seq/0")
            self._debug['application_identifier']['start'] = self._io.pos()
            self.application_identifier = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['application_identifier']['end'] = self._io.pos()
            self._debug['application_auth_code']['start'] = self._io.pos()
            self.application_auth_code = self._io.read_bytes(3)
            self._debug['application_auth_code']['end'] = self._io.pos()


    class ExtApplication(KaitaiStruct):
        SEQ_FIELDS = ["application_id", "subblocks"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['application_id']['start'] = self._io.pos()
            self.application_id = Gif.ApplicationId(self._io, self, self._root)
            self.application_id._read()
            self._debug['application_id']['end'] = self._io.pos()
            self._debug['subblocks']['start'] = self._io.pos()
            self.subblocks = []
            i = 0
            while True:
                if not 'arr' in self._debug['subblocks']:
                    self._debug['subblocks']['arr'] = []
                self._debug['subblocks']['arr'].append({'start': self._io.pos()})
                _t_subblocks = Gif.Subblock(self._io, self, self._root)
                _t_subblocks._read()
                _ = _t_subblocks
                self.subblocks.append(_)
                self._debug['subblocks']['arr'][len(self.subblocks) - 1]['end'] = self._io.pos()
                if _.len_bytes == 0:
                    break
                i += 1
            self._debug['subblocks']['end'] = self._io.pos()


    class Subblocks(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self.entries = []
            i = 0
            while True:
                if not 'arr' in self._debug['entries']:
                    self._debug['entries']['arr'] = []
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _t_entries = Gif.Subblock(self._io, self, self._root)
                _t_entries._read()
                _ = _t_entries
                self.entries.append(_)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                if _.len_bytes == 0:
                    break
                i += 1
            self._debug['entries']['end'] = self._io.pos()


    class Extension(KaitaiStruct):
        SEQ_FIELDS = ["label", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['label']['start'] = self._io.pos()
            self.label = KaitaiStream.resolve_enum(Gif.ExtensionLabel, self._io.read_u1())
            self._debug['label']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.label
            if _on == Gif.ExtensionLabel.application:
                self.body = Gif.ExtApplication(self._io, self, self._root)
                self.body._read()
            elif _on == Gif.ExtensionLabel.comment:
                self.body = Gif.Subblocks(self._io, self, self._root)
                self.body._read()
            elif _on == Gif.ExtensionLabel.graphic_control:
                self.body = Gif.ExtGraphicControl(self._io, self, self._root)
                self.body._read()
            else:
                self.body = Gif.Subblocks(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()



