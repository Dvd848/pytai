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

class Riff(KaitaiStruct):
    """The Resource Interchange File Format (RIFF) is a generic file container format
    for storing data in tagged chunks. It is primarily used to store multimedia
    such as sound and video, though it may also be used to store any arbitrary data.
    
    The Microsoft implementation is mostly known through container formats
    like AVI, ANI and WAV, which use RIFF as their basis.
    
    .. seealso::
       Source - https://www.johnloomis.org/cpe102/asgn/asgn1/riff.html
    """

    class Fourcc(Enum):
        riff = 1179011410
        info = 1330007625
        list = 1414744396
    SEQ_FIELDS = ["chunk"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['chunk']['start'] = self._io.pos()
        self.chunk = Riff.Chunk(self._io, self, self._root)
        self.chunk._read()
        self._debug['chunk']['end'] = self._io.pos()

    class ListChunkData(KaitaiStruct):
        SEQ_FIELDS = ["save_parent_chunk_data_ofs", "parent_chunk_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if self.parent_chunk_data_ofs < 0:
                self._debug['save_parent_chunk_data_ofs']['start'] = self._io.pos()
                self.save_parent_chunk_data_ofs = self._io.read_bytes(0)
                self._debug['save_parent_chunk_data_ofs']['end'] = self._io.pos()

            self._debug['parent_chunk_data']['start'] = self._io.pos()
            self.parent_chunk_data = Riff.ParentChunkData(self._io, self, self._root)
            self.parent_chunk_data._read()
            self._debug['parent_chunk_data']['end'] = self._io.pos()

        @property
        def parent_chunk_data_ofs(self):
            if hasattr(self, '_m_parent_chunk_data_ofs'):
                return self._m_parent_chunk_data_ofs

            self._m_parent_chunk_data_ofs = self._io.pos()
            return getattr(self, '_m_parent_chunk_data_ofs', None)

        @property
        def form_type(self):
            if hasattr(self, '_m_form_type'):
                return self._m_form_type

            self._m_form_type = KaitaiStream.resolve_enum(Riff.Fourcc, self.parent_chunk_data.form_type)
            return getattr(self, '_m_form_type', None)

        @property
        def form_type_readable(self):
            if hasattr(self, '_m_form_type_readable'):
                return self._m_form_type_readable

            _pos = self._io.pos()
            self._io.seek(self.parent_chunk_data_ofs)
            self._debug['_m_form_type_readable']['start'] = self._io.pos()
            self._m_form_type_readable = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['_m_form_type_readable']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_form_type_readable', None)

        @property
        def subchunks(self):
            if hasattr(self, '_m_subchunks'):
                return self._m_subchunks

            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_subchunks']['start'] = io.pos()
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                if not 'arr' in self._debug['_m_subchunks']:
                    self._debug['_m_subchunks']['arr'] = []
                self._debug['_m_subchunks']['arr'].append({'start': io.pos()})
                _on = self.form_type
                if _on == Riff.Fourcc.info:
                    if not 'arr' in self._debug['_m_subchunks']:
                        self._debug['_m_subchunks']['arr'] = []
                    self._debug['_m_subchunks']['arr'].append({'start': io.pos()})
                    _t__m_subchunks = Riff.InfoSubchunk(io, self, self._root)
                    _t__m_subchunks._read()
                    self._m_subchunks.append(_t__m_subchunks)
                    self._debug['_m_subchunks']['arr'][len(self._m_subchunks) - 1]['end'] = io.pos()
                else:
                    if not 'arr' in self._debug['_m_subchunks']:
                        self._debug['_m_subchunks']['arr'] = []
                    self._debug['_m_subchunks']['arr'].append({'start': io.pos()})
                    _t__m_subchunks = Riff.ChunkType(io, self, self._root)
                    _t__m_subchunks._read()
                    self._m_subchunks.append(_t__m_subchunks)
                    self._debug['_m_subchunks']['arr'][len(self._m_subchunks) - 1]['end'] = io.pos()
                self._debug['_m_subchunks']['arr'][len(self._m_subchunks) - 1]['end'] = io.pos()
                i += 1

            self._debug['_m_subchunks']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_subchunks', None)


    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["id", "len", "data_slot", "pad_byte"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_u4le()
            self._debug['id']['end'] = self._io.pos()
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['data_slot']['start'] = self._io.pos()
            self._raw_data_slot = self._io.read_bytes(self.len)
            _io__raw_data_slot = KaitaiStream(BytesIO(self._raw_data_slot))
            self.data_slot = Riff.Chunk.Slot(_io__raw_data_slot, self, self._root)
            self.data_slot._read()
            self._debug['data_slot']['end'] = self._io.pos()
            self._debug['pad_byte']['start'] = self._io.pos()
            self.pad_byte = self._io.read_bytes((self.len % 2))
            self._debug['pad_byte']['end'] = self._io.pos()

        class Slot(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                pass



    class ParentChunkData(KaitaiStruct):
        SEQ_FIELDS = ["form_type", "subchunks_slot"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['form_type']['start'] = self._io.pos()
            self.form_type = self._io.read_u4le()
            self._debug['form_type']['end'] = self._io.pos()
            self._debug['subchunks_slot']['start'] = self._io.pos()
            self._raw_subchunks_slot = self._io.read_bytes_full()
            _io__raw_subchunks_slot = KaitaiStream(BytesIO(self._raw_subchunks_slot))
            self.subchunks_slot = Riff.ParentChunkData.Slot(_io__raw_subchunks_slot, self, self._root)
            self.subchunks_slot._read()
            self._debug['subchunks_slot']['end'] = self._io.pos()

        class Slot(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                pass



    class InfoSubchunk(KaitaiStruct):
        """All registered subchunks in the INFO chunk are NULL-terminated strings,
        but the unregistered might not be. By convention, the registered
        chunk IDs are in uppercase and the unregistered IDs are in lowercase.
        
        If the chunk ID of an INFO subchunk contains a lowercase
        letter, this chunk is considered as unregistered and thus we can make
        no assumptions about the type of data.
        """
        SEQ_FIELDS = ["save_chunk_ofs", "chunk"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if self.chunk_ofs < 0:
                self._debug['save_chunk_ofs']['start'] = self._io.pos()
                self.save_chunk_ofs = self._io.read_bytes(0)
                self._debug['save_chunk_ofs']['end'] = self._io.pos()

            self._debug['chunk']['start'] = self._io.pos()
            self.chunk = Riff.Chunk(self._io, self, self._root)
            self.chunk._read()
            self._debug['chunk']['end'] = self._io.pos()

        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_chunk_data']['start'] = io.pos()
            _on = self.is_unregistered_tag
            if _on == False:
                self._m_chunk_data = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_chunk_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_chunk_data', None)

        @property
        def is_unregistered_tag(self):
            """Check if chunk_id contains lowercase characters ([a-z], ASCII 97 = a, ASCII 122 = z).
            """
            if hasattr(self, '_m_is_unregistered_tag'):
                return self._m_is_unregistered_tag

            self._m_is_unregistered_tag =  (( ((KaitaiStream.byte_array_index(self.id_chars, 0) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 0) <= 122)) ) or ( ((KaitaiStream.byte_array_index(self.id_chars, 1) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 1) <= 122)) ) or ( ((KaitaiStream.byte_array_index(self.id_chars, 2) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 2) <= 122)) ) or ( ((KaitaiStream.byte_array_index(self.id_chars, 3) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 3) <= 122)) )) 
            return getattr(self, '_m_is_unregistered_tag', None)

        @property
        def id_chars(self):
            if hasattr(self, '_m_id_chars'):
                return self._m_id_chars

            _pos = self._io.pos()
            self._io.seek(self.chunk_ofs)
            self._debug['_m_id_chars']['start'] = self._io.pos()
            self._m_id_chars = self._io.read_bytes(4)
            self._debug['_m_id_chars']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_id_chars', None)

        @property
        def chunk_id_readable(self):
            if hasattr(self, '_m_chunk_id_readable'):
                return self._m_chunk_id_readable

            self._m_chunk_id_readable = (self.id_chars).decode(u"ASCII")
            return getattr(self, '_m_chunk_id_readable', None)

        @property
        def chunk_ofs(self):
            if hasattr(self, '_m_chunk_ofs'):
                return self._m_chunk_ofs

            self._m_chunk_ofs = self._io.pos()
            return getattr(self, '_m_chunk_ofs', None)


    class ChunkType(KaitaiStruct):
        SEQ_FIELDS = ["save_chunk_ofs", "chunk"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if self.chunk_ofs < 0:
                self._debug['save_chunk_ofs']['start'] = self._io.pos()
                self.save_chunk_ofs = self._io.read_bytes(0)
                self._debug['save_chunk_ofs']['end'] = self._io.pos()

            self._debug['chunk']['start'] = self._io.pos()
            self.chunk = Riff.Chunk(self._io, self, self._root)
            self.chunk._read()
            self._debug['chunk']['end'] = self._io.pos()

        @property
        def chunk_ofs(self):
            if hasattr(self, '_m_chunk_ofs'):
                return self._m_chunk_ofs

            self._m_chunk_ofs = self._io.pos()
            return getattr(self, '_m_chunk_ofs', None)

        @property
        def chunk_id(self):
            if hasattr(self, '_m_chunk_id'):
                return self._m_chunk_id

            self._m_chunk_id = KaitaiStream.resolve_enum(Riff.Fourcc, self.chunk.id)
            return getattr(self, '_m_chunk_id', None)

        @property
        def chunk_id_readable(self):
            if hasattr(self, '_m_chunk_id_readable'):
                return self._m_chunk_id_readable

            _pos = self._io.pos()
            self._io.seek(self.chunk_ofs)
            self._debug['_m_chunk_id_readable']['start'] = self._io.pos()
            self._m_chunk_id_readable = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['_m_chunk_id_readable']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_chunk_id_readable', None)

        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_chunk_data']['start'] = io.pos()
            _on = self.chunk_id
            if _on == Riff.Fourcc.list:
                self._m_chunk_data = Riff.ListChunkData(io, self, self._root)
                self._m_chunk_data._read()
            self._debug['_m_chunk_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_chunk_data', None)


    @property
    def chunk_id(self):
        if hasattr(self, '_m_chunk_id'):
            return self._m_chunk_id

        self._m_chunk_id = KaitaiStream.resolve_enum(Riff.Fourcc, self.chunk.id)
        return getattr(self, '_m_chunk_id', None)

    @property
    def is_riff_chunk(self):
        if hasattr(self, '_m_is_riff_chunk'):
            return self._m_is_riff_chunk

        self._m_is_riff_chunk = self.chunk_id == Riff.Fourcc.riff
        return getattr(self, '_m_is_riff_chunk', None)

    @property
    def parent_chunk_data(self):
        if hasattr(self, '_m_parent_chunk_data'):
            return self._m_parent_chunk_data

        if self.is_riff_chunk:
            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_parent_chunk_data']['start'] = io.pos()
            self._m_parent_chunk_data = Riff.ParentChunkData(io, self, self._root)
            self._m_parent_chunk_data._read()
            self._debug['_m_parent_chunk_data']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_parent_chunk_data', None)

    @property
    def subchunks(self):
        if hasattr(self, '_m_subchunks'):
            return self._m_subchunks

        if self.is_riff_chunk:
            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_subchunks']['start'] = io.pos()
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                if not 'arr' in self._debug['_m_subchunks']:
                    self._debug['_m_subchunks']['arr'] = []
                self._debug['_m_subchunks']['arr'].append({'start': io.pos()})
                _t__m_subchunks = Riff.ChunkType(io, self, self._root)
                _t__m_subchunks._read()
                self._m_subchunks.append(_t__m_subchunks)
                self._debug['_m_subchunks']['arr'][len(self._m_subchunks) - 1]['end'] = io.pos()
                i += 1

            self._debug['_m_subchunks']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_subchunks', None)


