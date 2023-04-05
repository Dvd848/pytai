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

class Au(KaitaiStruct):
    """The NeXT/Sun audio file format.
    
    Sample files:
    
    * <https://github.com/python/cpython/tree/b8a7daf077da/Lib/test/sndhdrdata>
    * <ftp://ftp-ccrma.stanford.edu/pub/Lisp/sf.tar.gz>
    * <https://www.mmsp.ece.mcgill.ca/Documents/AudioFormats/AU/Samples.html>
    
    .. seealso::
       Source - https://www.mmsp.ece.mcgill.ca/Documents/AudioFormats/AU/AU.html
    
    
    .. seealso::
       Source - http://soundfile.sapp.org/doc/NextFormat/
    
    
    .. seealso::
       Source - http://soundfile.sapp.org/doc/NextFormat/soundstruct.h
    
    
    .. seealso::
       Source - https://github.com/andreiw/polaris/blob/deb47cb/usr/src/head/audio/au.h#L87-L112
    
    
    .. seealso::
       Source - https://github.com/libsndfile/libsndfile/blob/86c9f9eb/src/au.c#L39-L74
    
    
    .. seealso::
       Source - https://github.com/chirlu/sox/blob/dd8b63bd/src/au.c#L34-L49
    
    
    .. seealso::
       Source - https://github.com/mpruett/audiofile/blob/b62c902/libaudiofile/NeXT.cpp#L65-L96
    """

    class Encodings(Enum):
        mulaw_8 = 1
        linear_8 = 2
        linear_16 = 3
        linear_24 = 4
        linear_32 = 5
        float = 6
        double = 7
        fragmented = 8
        nested = 9
        dsp_core = 10
        fixed_point_8 = 11
        fixed_point_16 = 12
        fixed_point_24 = 13
        fixed_point_32 = 14
        display = 16
        mulaw_squelch = 17
        emphasized = 18
        compressed = 19
        compressed_emphasized = 20
        dsp_commands = 21
        dsp_commands_samples = 22
        adpcm_g721 = 23
        adpcm_g722 = 24
        adpcm_g723_3 = 25
        adpcm_g723_5 = 26
        alaw_8 = 27
        aes = 28
        delta_mulaw_8 = 29
    SEQ_FIELDS = ["magic", "ofs_data", "header"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x2E\x73\x6E\x64":
            raise kaitaistruct.ValidationNotEqualError(b"\x2E\x73\x6E\x64", self.magic, self._io, u"/seq/0")
        self._debug['ofs_data']['start'] = self._io.pos()
        self.ofs_data = self._io.read_u4be()
        self._debug['ofs_data']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(((self.ofs_data - 4) - 4))
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Au.Header(_io__raw_header, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["data_size", "encoding", "sample_rate", "num_channels", "comment"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['data_size']['start'] = self._io.pos()
            self.data_size = self._io.read_u4be()
            self._debug['data_size']['end'] = self._io.pos()
            self._debug['encoding']['start'] = self._io.pos()
            self.encoding = KaitaiStream.resolve_enum(Au.Encodings, self._io.read_u4be())
            self._debug['encoding']['end'] = self._io.pos()
            self._debug['sample_rate']['start'] = self._io.pos()
            self.sample_rate = self._io.read_u4be()
            self._debug['sample_rate']['end'] = self._io.pos()
            self._debug['num_channels']['start'] = self._io.pos()
            self.num_channels = self._io.read_u4be()
            self._debug['num_channels']['end'] = self._io.pos()
            if not self.num_channels >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_channels, self._io, u"/types/header/seq/3")
            self._debug['comment']['start'] = self._io.pos()
            self.comment = (KaitaiStream.bytes_terminate(self._io.read_bytes_full(), 0, False)).decode(u"ASCII")
            self._debug['comment']['end'] = self._io.pos()


    @property
    def len_data(self):
        if hasattr(self, '_m_len_data'):
            return self._m_len_data

        self._m_len_data = ((self._io.size() - self.ofs_data) if self.header.data_size == 4294967295 else self.header.data_size)
        return getattr(self, '_m_len_data', None)


