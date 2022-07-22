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
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Zisofs(KaitaiStruct):
    """zisofs is a compression format for files on ISO9660 file system. It has
    limited support across operating systems, mainly Linux kernel. Typically a
    directory tree is first preprocessed by mkzftree (from the zisofs-tools
    package before being turned into an ISO9660 image by mkisofs, genisoimage
    or similar tool. The data is zlib compressed.
    
    The specification here describes the structure of a file that has been
    preprocessed by mkzftree, not of a full ISO9660 ziso. Data is not
    decompressed, as blocks with length 0 have a special meaning. Decompression
    and deconstruction of this data should be done outside of Kaitai Struct.
    
    .. seealso::
       Source - https://web.archive.org/web/20200612093441/https://dev.lovelyhq.com/libburnia/web/-/wikis/zisofs
    """
    SEQ_FIELDS = ["header", "block_pointers"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(16)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Zisofs.Header(_io__raw_header, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['block_pointers']['start'] = self._io.pos()
        self.block_pointers = []
        for i in range((self.header.num_blocks + 1)):
            if not 'arr' in self._debug['block_pointers']:
                self._debug['block_pointers']['arr'] = []
            self._debug['block_pointers']['arr'].append({'start': self._io.pos()})
            self.block_pointers.append(self._io.read_u4le())
            self._debug['block_pointers']['arr'][i]['end'] = self._io.pos()

        self._debug['block_pointers']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "uncompressed_size", "len_header", "block_size_log2", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x37\xE4\x53\x96\xC9\xDB\xD6\x07":
                raise kaitaistruct.ValidationNotEqualError(b"\x37\xE4\x53\x96\xC9\xDB\xD6\x07", self.magic, self._io, u"/types/header/seq/0")
            self._debug['uncompressed_size']['start'] = self._io.pos()
            self.uncompressed_size = self._io.read_u4le()
            self._debug['uncompressed_size']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u1()
            self._debug['len_header']['end'] = self._io.pos()
            if not self.len_header == 4:
                raise kaitaistruct.ValidationNotEqualError(4, self.len_header, self._io, u"/types/header/seq/2")
            self._debug['block_size_log2']['start'] = self._io.pos()
            self.block_size_log2 = self._io.read_u1()
            self._debug['block_size_log2']['end'] = self._io.pos()
            if not  ((self.block_size_log2 == 15) or (self.block_size_log2 == 16) or (self.block_size_log2 == 17)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.block_size_log2, self._io, u"/types/header/seq/3")
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(2)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.reserved, self._io, u"/types/header/seq/4")

        @property
        def block_size(self):
            if hasattr(self, '_m_block_size'):
                return self._m_block_size

            self._m_block_size = (1 << self.block_size_log2)
            return getattr(self, '_m_block_size', None)

        @property
        def num_blocks(self):
            """ceil(uncompressed_size / block_size)."""
            if hasattr(self, '_m_num_blocks'):
                return self._m_num_blocks

            self._m_num_blocks = (self.uncompressed_size // self.block_size + (1 if (self.uncompressed_size % self.block_size) != 0 else 0))
            return getattr(self, '_m_num_blocks', None)


    class Block(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, ofs_start, ofs_end, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.ofs_start = ofs_start
            self.ofs_end = ofs_end
            self._debug = collections.defaultdict(dict)

        def _read(self):
            pass

        @property
        def len_data(self):
            if hasattr(self, '_m_len_data'):
                return self._m_len_data

            self._m_len_data = (self.ofs_end - self.ofs_start)
            return getattr(self, '_m_len_data', None)

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_start)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    @property
    def blocks(self):
        if hasattr(self, '_m_blocks'):
            return self._m_blocks

        self._debug['_m_blocks']['start'] = self._io.pos()
        self._m_blocks = []
        for i in range(self.header.num_blocks):
            if not 'arr' in self._debug['_m_blocks']:
                self._debug['_m_blocks']['arr'] = []
            self._debug['_m_blocks']['arr'].append({'start': self._io.pos()})
            _t__m_blocks = Zisofs.Block(self.block_pointers[i], self.block_pointers[(i + 1)], self._io, self, self._root)
            _t__m_blocks._read()
            self._m_blocks.append(_t__m_blocks)
            self._debug['_m_blocks']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_blocks']['end'] = self._io.pos()
        return getattr(self, '_m_blocks', None)


