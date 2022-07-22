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
import zlib


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Xar(KaitaiStruct):
    """From [Wikipedia](https://en.wikipedia.org/wiki/Xar_(archiver)):
    
    "XAR (short for eXtensible ARchive format) is an open source file archiver
    and the archiver's file format. It was created within the OpenDarwin project
    and is used in macOS X 10.5 and up for software installation routines, as
    well as browser extensions in Safari 5.0 and up."
    
    .. seealso::
       Source - https://github.com/mackyle/xar/wiki/xarformat
    """

    class ChecksumAlgorithmsApple(Enum):
        none = 0
        sha1 = 1
        md5 = 2
        sha256 = 3
        sha512 = 4
    SEQ_FIELDS = ["header_prefix", "header", "toc"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header_prefix']['start'] = self._io.pos()
        self.header_prefix = Xar.FileHeaderPrefix(self._io, self, self._root)
        self.header_prefix._read()
        self._debug['header_prefix']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes((self.header_prefix.len_header - 6))
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Xar.FileHeader(_io__raw_header, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['toc']['start'] = self._io.pos()
        self._raw__raw_toc = self._io.read_bytes(self.header.len_toc_compressed)
        self._raw_toc = zlib.decompress(self._raw__raw_toc)
        _io__raw_toc = KaitaiStream(BytesIO(self._raw_toc))
        self.toc = Xar.TocType(_io__raw_toc, self, self._root)
        self.toc._read()
        self._debug['toc']['end'] = self._io.pos()

    class FileHeaderPrefix(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_header"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x78\x61\x72\x21":
                raise kaitaistruct.ValidationNotEqualError(b"\x78\x61\x72\x21", self.magic, self._io, u"/types/file_header_prefix/seq/0")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u2be()
            self._debug['len_header']['end'] = self._io.pos()


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["version", "len_toc_compressed", "toc_length_uncompressed", "checksum_algorithm_int", "checksum_alg_name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2be()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/types/file_header/seq/0")
            self._debug['len_toc_compressed']['start'] = self._io.pos()
            self.len_toc_compressed = self._io.read_u8be()
            self._debug['len_toc_compressed']['end'] = self._io.pos()
            self._debug['toc_length_uncompressed']['start'] = self._io.pos()
            self.toc_length_uncompressed = self._io.read_u8be()
            self._debug['toc_length_uncompressed']['end'] = self._io.pos()
            self._debug['checksum_algorithm_int']['start'] = self._io.pos()
            self.checksum_algorithm_int = self._io.read_u4be()
            self._debug['checksum_algorithm_int']['end'] = self._io.pos()
            if self.has_checksum_alg_name:
                self._debug['checksum_alg_name']['start'] = self._io.pos()
                self.checksum_alg_name = (KaitaiStream.bytes_terminate(self._io.read_bytes_full(), 0, False)).decode(u"UTF-8")
                self._debug['checksum_alg_name']['end'] = self._io.pos()
                _ = self.checksum_alg_name
                if not  ((_ != u"") and (_ != u"none")) :
                    raise kaitaistruct.ValidationExprError(self.checksum_alg_name, self._io, u"/types/file_header/seq/4")


        @property
        def checksum_algorithm_name(self):
            """If it is not
            
            * `""` (empty string), indicating an unknown integer value (access
              `checksum_algorithm_int` for debugging purposes to find out
              what that value is), or
            * `"none"`, indicating that the TOC checksum is not provided (in that
              case, the `<checksum>` property or its `style` attribute should be
              missing, or the `style` attribute must be set to `"none"`),
            
            it must exactly match the `style` attribute value of the
            `<checksum>` property in the root node `<toc>`. See
            <https://github.com/mackyle/xar/blob/66d451d/xar/lib/archive.c#L345-L371>
            for reference.
            
            The `xar` (eXtensible ARchiver) program [uses OpenSSL's function
            `EVP_get_digestbyname`](
              https://github.com/mackyle/xar/blob/66d451d/xar/lib/archive.c#L328
            ) to verify this value (if it's not `""` or `"none"`, of course).
            So it's reasonable to assume that this can only have one of the values
            that OpenSSL recognizes.
            """
            if hasattr(self, '_m_checksum_algorithm_name'):
                return self._m_checksum_algorithm_name

            self._m_checksum_algorithm_name = (self.checksum_alg_name if self.has_checksum_alg_name else (u"none" if self.checksum_algorithm_int == Xar.ChecksumAlgorithmsApple.none.value else (u"sha1" if self.checksum_algorithm_int == Xar.ChecksumAlgorithmsApple.sha1.value else (u"md5" if self.checksum_algorithm_int == Xar.ChecksumAlgorithmsApple.md5.value else (u"sha256" if self.checksum_algorithm_int == Xar.ChecksumAlgorithmsApple.sha256.value else (u"sha512" if self.checksum_algorithm_int == Xar.ChecksumAlgorithmsApple.sha512.value else u""))))))
            return getattr(self, '_m_checksum_algorithm_name', None)

        @property
        def has_checksum_alg_name(self):
            if hasattr(self, '_m_has_checksum_alg_name'):
                return self._m_has_checksum_alg_name

            self._m_has_checksum_alg_name =  ((self.checksum_algorithm_int == self._root.checksum_algorithm_other) and (self.len_header >= 32) and ((self.len_header % 4) == 0)) 
            return getattr(self, '_m_has_checksum_alg_name', None)

        @property
        def len_header(self):
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = self._root.header_prefix.len_header
            return getattr(self, '_m_len_header', None)


    class TocType(KaitaiStruct):
        SEQ_FIELDS = ["xml_string"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['xml_string']['start'] = self._io.pos()
            self.xml_string = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._debug['xml_string']['end'] = self._io.pos()


    @property
    def checksum_algorithm_other(self):
        """
        .. seealso::
           Source - https://github.com/mackyle/xar/blob/66d451d/xar/include/xar.h.in#L85
        """
        if hasattr(self, '_m_checksum_algorithm_other'):
            return self._m_checksum_algorithm_other

        self._m_checksum_algorithm_other = 3
        return getattr(self, '_m_checksum_algorithm_other', None)


