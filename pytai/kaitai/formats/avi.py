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

class Avi(KaitaiStruct):
    """
    .. seealso::
       Source - https://learn.microsoft.com/en-us/previous-versions/ms779636(v=vs.85)
    """

    class ChunkType(Enum):
        idx1 = 829973609
        junk = 1263424842
        info = 1330007625
        isft = 1413894985
        list = 1414744396
        strf = 1718776947
        avih = 1751742049
        strh = 1752331379
        movi = 1769369453
        hdrl = 1819436136
        strl = 1819440243

    class StreamType(Enum):
        mids = 1935960429
        vids = 1935960438
        auds = 1935963489
        txts = 1937012852

    class HandlerType(Enum):
        mp3 = 85
        ac3 = 8192
        dts = 8193
        cvid = 1684633187
        xvid = 1684633208
    SEQ_FIELDS = ["magic1", "file_size", "magic2", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic1']['start'] = self._io.pos()
        self.magic1 = self._io.read_bytes(4)
        self._debug['magic1']['end'] = self._io.pos()
        if not self.magic1 == b"\x52\x49\x46\x46":
            raise kaitaistruct.ValidationNotEqualError(b"\x52\x49\x46\x46", self.magic1, self._io, u"/seq/0")
        self._debug['file_size']['start'] = self._io.pos()
        self.file_size = self._io.read_u4le()
        self._debug['file_size']['end'] = self._io.pos()
        self._debug['magic2']['start'] = self._io.pos()
        self.magic2 = self._io.read_bytes(4)
        self._debug['magic2']['end'] = self._io.pos()
        if not self.magic2 == b"\x41\x56\x49\x20":
            raise kaitaistruct.ValidationNotEqualError(b"\x41\x56\x49\x20", self.magic2, self._io, u"/seq/2")
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes((self.file_size - 4))
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = Avi.Blocks(_io__raw_data, self, self._root)
        self.data._read()
        self._debug['data']['end'] = self._io.pos()

    class ListBody(KaitaiStruct):
        SEQ_FIELDS = ["list_type", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['list_type']['start'] = self._io.pos()
            self.list_type = KaitaiStream.resolve_enum(Avi.ChunkType, self._io.read_u4le())
            self._debug['list_type']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = Avi.Blocks(self._io, self, self._root)
            self.data._read()
            self._debug['data']['end'] = self._io.pos()


    class Rect(KaitaiStruct):
        SEQ_FIELDS = ["left", "top", "right", "bottom"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['left']['start'] = self._io.pos()
            self.left = self._io.read_s2le()
            self._debug['left']['end'] = self._io.pos()
            self._debug['top']['start'] = self._io.pos()
            self.top = self._io.read_s2le()
            self._debug['top']['end'] = self._io.pos()
            self._debug['right']['start'] = self._io.pos()
            self.right = self._io.read_s2le()
            self._debug['right']['end'] = self._io.pos()
            self._debug['bottom']['start'] = self._io.pos()
            self.bottom = self._io.read_s2le()
            self._debug['bottom']['end'] = self._io.pos()


    class Blocks(KaitaiStruct):
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
                _t_entries = Avi.Block(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class AvihBody(KaitaiStruct):
        """Main header of an AVI file, defined as AVIMAINHEADER structure.
        
        .. seealso::
           Source - https://learn.microsoft.com/en-us/previous-versions/ms779632(v=vs.85)
        """
        SEQ_FIELDS = ["micro_sec_per_frame", "max_bytes_per_sec", "padding_granularity", "flags", "total_frames", "initial_frames", "streams", "suggested_buffer_size", "width", "height", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['micro_sec_per_frame']['start'] = self._io.pos()
            self.micro_sec_per_frame = self._io.read_u4le()
            self._debug['micro_sec_per_frame']['end'] = self._io.pos()
            self._debug['max_bytes_per_sec']['start'] = self._io.pos()
            self.max_bytes_per_sec = self._io.read_u4le()
            self._debug['max_bytes_per_sec']['end'] = self._io.pos()
            self._debug['padding_granularity']['start'] = self._io.pos()
            self.padding_granularity = self._io.read_u4le()
            self._debug['padding_granularity']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['total_frames']['start'] = self._io.pos()
            self.total_frames = self._io.read_u4le()
            self._debug['total_frames']['end'] = self._io.pos()
            self._debug['initial_frames']['start'] = self._io.pos()
            self.initial_frames = self._io.read_u4le()
            self._debug['initial_frames']['end'] = self._io.pos()
            self._debug['streams']['start'] = self._io.pos()
            self.streams = self._io.read_u4le()
            self._debug['streams']['end'] = self._io.pos()
            self._debug['suggested_buffer_size']['start'] = self._io.pos()
            self.suggested_buffer_size = self._io.read_u4le()
            self._debug['suggested_buffer_size']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(16)
            self._debug['reserved']['end'] = self._io.pos()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["four_cc", "block_size", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['four_cc']['start'] = self._io.pos()
            self.four_cc = KaitaiStream.resolve_enum(Avi.ChunkType, self._io.read_u4le())
            self._debug['four_cc']['end'] = self._io.pos()
            self._debug['block_size']['start'] = self._io.pos()
            self.block_size = self._io.read_u4le()
            self._debug['block_size']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.four_cc
            if _on == Avi.ChunkType.list:
                self._raw_data = self._io.read_bytes(self.block_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Avi.ListBody(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == Avi.ChunkType.avih:
                self._raw_data = self._io.read_bytes(self.block_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Avi.AvihBody(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == Avi.ChunkType.strh:
                self._raw_data = self._io.read_bytes(self.block_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Avi.StrhBody(_io__raw_data, self, self._root)
                self.data._read()
            else:
                self.data = self._io.read_bytes(self.block_size)
            self._debug['data']['end'] = self._io.pos()


    class StrhBody(KaitaiStruct):
        """Stream header (one header per stream), defined as AVISTREAMHEADER structure.
        
        .. seealso::
           Source - https://learn.microsoft.com/en-us/previous-versions/ms779638(v=vs.85)
        """
        SEQ_FIELDS = ["fcc_type", "fcc_handler", "flags", "priority", "language", "initial_frames", "scale", "rate", "start", "length", "suggested_buffer_size", "quality", "sample_size", "frame"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['fcc_type']['start'] = self._io.pos()
            self.fcc_type = KaitaiStream.resolve_enum(Avi.StreamType, self._io.read_u4le())
            self._debug['fcc_type']['end'] = self._io.pos()
            self._debug['fcc_handler']['start'] = self._io.pos()
            self.fcc_handler = KaitaiStream.resolve_enum(Avi.HandlerType, self._io.read_u4le())
            self._debug['fcc_handler']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['priority']['start'] = self._io.pos()
            self.priority = self._io.read_u2le()
            self._debug['priority']['end'] = self._io.pos()
            self._debug['language']['start'] = self._io.pos()
            self.language = self._io.read_u2le()
            self._debug['language']['end'] = self._io.pos()
            self._debug['initial_frames']['start'] = self._io.pos()
            self.initial_frames = self._io.read_u4le()
            self._debug['initial_frames']['end'] = self._io.pos()
            self._debug['scale']['start'] = self._io.pos()
            self.scale = self._io.read_u4le()
            self._debug['scale']['end'] = self._io.pos()
            self._debug['rate']['start'] = self._io.pos()
            self.rate = self._io.read_u4le()
            self._debug['rate']['end'] = self._io.pos()
            self._debug['start']['start'] = self._io.pos()
            self.start = self._io.read_u4le()
            self._debug['start']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u4le()
            self._debug['length']['end'] = self._io.pos()
            self._debug['suggested_buffer_size']['start'] = self._io.pos()
            self.suggested_buffer_size = self._io.read_u4le()
            self._debug['suggested_buffer_size']['end'] = self._io.pos()
            self._debug['quality']['start'] = self._io.pos()
            self.quality = self._io.read_u4le()
            self._debug['quality']['end'] = self._io.pos()
            self._debug['sample_size']['start'] = self._io.pos()
            self.sample_size = self._io.read_u4le()
            self._debug['sample_size']['end'] = self._io.pos()
            self._debug['frame']['start'] = self._io.pos()
            self.frame = Avi.Rect(self._io, self, self._root)
            self.frame._read()
            self._debug['frame']['end'] = self._io.pos()


    class StrfBody(KaitaiStruct):
        """Stream format description."""
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            pass



