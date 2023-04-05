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

class AndroidSparse(KaitaiStruct):
    """The Android sparse format is a format to more efficiently store files
    for for example firmware updates to save on bandwidth. Files in sparse
    format first have to be converted back to their original format.
    
    A tool to create images for testing can be found in the Android source code tree:
    
    <https://android.googlesource.com/platform/system/core/+/e8d02c50d7/libsparse> - `img2simg.c`
    
    Note: this is not the same as the Android sparse data image format.
    
    .. seealso::
       Source - https://android.googlesource.com/platform/system/core/+/e8d02c50d7/libsparse/sparse_format.h
    
    
    .. seealso::
       Source - https://web.archive.org/web/20220322054458/https://source.android.com/devices/bootloader/images#sparse-image-format
    """

    class ChunkTypes(Enum):
        raw = 51905
        fill = 51906
        dont_care = 51907
        crc32 = 51908
    SEQ_FIELDS = ["header_prefix", "header", "chunks"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header_prefix']['start'] = self._io.pos()
        self.header_prefix = AndroidSparse.FileHeaderPrefix(self._io, self, self._root)
        self.header_prefix._read()
        self._debug['header_prefix']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes((self.header_prefix.len_header - 10))
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = AndroidSparse.FileHeader(_io__raw_header, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['chunks']['start'] = self._io.pos()
        self.chunks = []
        for i in range(self.header.num_chunks):
            if not 'arr' in self._debug['chunks']:
                self._debug['chunks']['arr'] = []
            self._debug['chunks']['arr'].append({'start': self._io.pos()})
            _t_chunks = AndroidSparse.Chunk(self._io, self, self._root)
            _t_chunks._read()
            self.chunks.append(_t_chunks)
            self._debug['chunks']['arr'][i]['end'] = self._io.pos()

        self._debug['chunks']['end'] = self._io.pos()

    class FileHeaderPrefix(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_header"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x3A\xFF\x26\xED":
                raise kaitaistruct.ValidationNotEqualError(b"\x3A\xFF\x26\xED", self.magic, self._io, u"/types/file_header_prefix/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = AndroidSparse.Version(self._io, self, self._root)
            self.version._read()
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u2le()
            self._debug['len_header']['end'] = self._io.pos()


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["len_chunk_header", "block_size", "num_blocks", "num_chunks", "checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_chunk_header']['start'] = self._io.pos()
            self.len_chunk_header = self._io.read_u2le()
            self._debug['len_chunk_header']['end'] = self._io.pos()
            self._debug['block_size']['start'] = self._io.pos()
            self.block_size = self._io.read_u4le()
            self._debug['block_size']['end'] = self._io.pos()
            _ = self.block_size
            if not (_ % 4) == 0:
                raise kaitaistruct.ValidationExprError(self.block_size, self._io, u"/types/file_header/seq/1")
            self._debug['num_blocks']['start'] = self._io.pos()
            self.num_blocks = self._io.read_u4le()
            self._debug['num_blocks']['end'] = self._io.pos()
            self._debug['num_chunks']['start'] = self._io.pos()
            self.num_chunks = self._io.read_u4le()
            self._debug['num_chunks']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4le()
            self._debug['checksum']['end'] = self._io.pos()

        @property
        def version(self):
            if hasattr(self, '_m_version'):
                return self._m_version

            self._m_version = self._root.header_prefix.version
            return getattr(self, '_m_version', None)

        @property
        def len_header(self):
            """size of file header, should be 28."""
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = self._root.header_prefix.len_header
            return getattr(self, '_m_len_header', None)


    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self._raw_header = self._io.read_bytes(self._root.header.len_chunk_header)
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = AndroidSparse.Chunk.ChunkHeader(_io__raw_header, self, self._root)
            self.header._read()
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.header.chunk_type
            if _on == AndroidSparse.ChunkTypes.crc32:
                self.body = self._io.read_u4le()
            else:
                self.body = self._io.read_bytes(self.header.len_body)
            self._debug['body']['end'] = self._io.pos()

        class ChunkHeader(KaitaiStruct):
            SEQ_FIELDS = ["chunk_type", "reserved1", "num_body_blocks", "len_chunk"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['chunk_type']['start'] = self._io.pos()
                self.chunk_type = KaitaiStream.resolve_enum(AndroidSparse.ChunkTypes, self._io.read_u2le())
                self._debug['chunk_type']['end'] = self._io.pos()
                self._debug['reserved1']['start'] = self._io.pos()
                self.reserved1 = self._io.read_u2le()
                self._debug['reserved1']['end'] = self._io.pos()
                self._debug['num_body_blocks']['start'] = self._io.pos()
                self.num_body_blocks = self._io.read_u4le()
                self._debug['num_body_blocks']['end'] = self._io.pos()
                self._debug['len_chunk']['start'] = self._io.pos()
                self.len_chunk = self._io.read_u4le()
                self._debug['len_chunk']['end'] = self._io.pos()
                if not self.len_chunk == ((self._root.header.len_chunk_header + self.len_body_expected) if self.len_body_expected != -1 else self.len_chunk):
                    raise kaitaistruct.ValidationNotEqualError(((self._root.header.len_chunk_header + self.len_body_expected) if self.len_body_expected != -1 else self.len_chunk), self.len_chunk, self._io, u"/types/chunk/types/chunk_header/seq/3")

            @property
            def len_body(self):
                if hasattr(self, '_m_len_body'):
                    return self._m_len_body

                self._m_len_body = (self.len_chunk - self._root.header.len_chunk_header)
                return getattr(self, '_m_len_body', None)

            @property
            def len_body_expected(self):
                """
                .. seealso::
                   Source - https://android.googlesource.com/platform/system/core/+/e8d02c50d7/libsparse/sparse_read.cpp#184
                
                
                .. seealso::
                   Source - https://android.googlesource.com/platform/system/core/+/e8d02c50d7/libsparse/sparse_read.cpp#215
                
                
                .. seealso::
                   Source - https://android.googlesource.com/platform/system/core/+/e8d02c50d7/libsparse/sparse_read.cpp#249
                
                
                .. seealso::
                   Source - https://android.googlesource.com/platform/system/core/+/e8d02c50d7/libsparse/sparse_read.cpp#270
                """
                if hasattr(self, '_m_len_body_expected'):
                    return self._m_len_body_expected

                self._m_len_body_expected = ((self._root.header.block_size * self.num_body_blocks) if self.chunk_type == AndroidSparse.ChunkTypes.raw else (4 if self.chunk_type == AndroidSparse.ChunkTypes.fill else (0 if self.chunk_type == AndroidSparse.ChunkTypes.dont_care else (4 if self.chunk_type == AndroidSparse.ChunkTypes.crc32 else -1))))
                return getattr(self, '_m_len_body_expected', None)



    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            if not self.major == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.major, self._io, u"/types/version/seq/0")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()



