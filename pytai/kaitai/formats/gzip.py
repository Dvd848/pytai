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

class Gzip(KaitaiStruct):
    """Gzip is a popular and standard single-file archiving format. It
    essentially provides a container that stores original file name,
    timestamp and a few other things (like optional comment), basic
    CRCs, etc, and a file compressed by a chosen compression algorithm.
    
    As of 2019, there is actually only one working solution for
    compression algorithms, so it's typically raw DEFLATE stream
    (without zlib header) in all gzipped files.
    
    .. seealso::
       Source - https://www.rfc-editor.org/rfc/rfc1952
    """

    class CompressionMethods(Enum):
        deflate = 8

    class Oses(Enum):
        fat = 0
        amiga = 1
        vms = 2
        unix = 3
        vm_cms = 4
        atari_tos = 5
        hpfs = 6
        macintosh = 7
        z_system = 8
        cp_m = 9
        tops_20 = 10
        ntfs = 11
        qdos = 12
        acorn_riscos = 13
        unknown = 255
    SEQ_FIELDS = ["magic", "compression_method", "flags", "mod_time", "extra_flags", "os", "extras", "name", "comment", "header_crc16", "body", "body_crc32", "len_uncompressed"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(2)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x1F\x8B":
            raise kaitaistruct.ValidationNotEqualError(b"\x1F\x8B", self.magic, self._io, u"/seq/0")
        self._debug['compression_method']['start'] = self._io.pos()
        self.compression_method = KaitaiStream.resolve_enum(Gzip.CompressionMethods, self._io.read_u1())
        self._debug['compression_method']['end'] = self._io.pos()
        self._debug['flags']['start'] = self._io.pos()
        self.flags = Gzip.Flags(self._io, self, self._root)
        self.flags._read()
        self._debug['flags']['end'] = self._io.pos()
        self._debug['mod_time']['start'] = self._io.pos()
        self.mod_time = self._io.read_u4le()
        self._debug['mod_time']['end'] = self._io.pos()
        self._debug['extra_flags']['start'] = self._io.pos()
        _on = self.compression_method
        if _on == Gzip.CompressionMethods.deflate:
            self.extra_flags = Gzip.ExtraFlagsDeflate(self._io, self, self._root)
            self.extra_flags._read()
        self._debug['extra_flags']['end'] = self._io.pos()
        self._debug['os']['start'] = self._io.pos()
        self.os = KaitaiStream.resolve_enum(Gzip.Oses, self._io.read_u1())
        self._debug['os']['end'] = self._io.pos()
        if self.flags.has_extra:
            self._debug['extras']['start'] = self._io.pos()
            self.extras = Gzip.Extras(self._io, self, self._root)
            self.extras._read()
            self._debug['extras']['end'] = self._io.pos()

        if self.flags.has_name:
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes_term(0, False, True, True)
            self._debug['name']['end'] = self._io.pos()

        if self.flags.has_comment:
            self._debug['comment']['start'] = self._io.pos()
            self.comment = self._io.read_bytes_term(0, False, True, True)
            self._debug['comment']['end'] = self._io.pos()

        if self.flags.has_header_crc:
            self._debug['header_crc16']['start'] = self._io.pos()
            self.header_crc16 = self._io.read_u2le()
            self._debug['header_crc16']['end'] = self._io.pos()

        self._debug['body']['start'] = self._io.pos()
        self.body = self._io.read_bytes(((self._io.size() - self._io.pos()) - 8))
        self._debug['body']['end'] = self._io.pos()
        self._debug['body_crc32']['start'] = self._io.pos()
        self.body_crc32 = self._io.read_u4le()
        self._debug['body_crc32']['end'] = self._io.pos()
        self._debug['len_uncompressed']['start'] = self._io.pos()
        self.len_uncompressed = self._io.read_u4le()
        self._debug['len_uncompressed']['end'] = self._io.pos()

    class Flags(KaitaiStruct):
        SEQ_FIELDS = ["reserved1", "has_comment", "has_name", "has_extra", "has_header_crc", "is_text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(3)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['has_comment']['start'] = self._io.pos()
            self.has_comment = self._io.read_bits_int_be(1) != 0
            self._debug['has_comment']['end'] = self._io.pos()
            self._debug['has_name']['start'] = self._io.pos()
            self.has_name = self._io.read_bits_int_be(1) != 0
            self._debug['has_name']['end'] = self._io.pos()
            self._debug['has_extra']['start'] = self._io.pos()
            self.has_extra = self._io.read_bits_int_be(1) != 0
            self._debug['has_extra']['end'] = self._io.pos()
            self._debug['has_header_crc']['start'] = self._io.pos()
            self.has_header_crc = self._io.read_bits_int_be(1) != 0
            self._debug['has_header_crc']['end'] = self._io.pos()
            self._debug['is_text']['start'] = self._io.pos()
            self.is_text = self._io.read_bits_int_be(1) != 0
            self._debug['is_text']['end'] = self._io.pos()


    class ExtraFlagsDeflate(KaitaiStruct):

        class CompressionStrengths(Enum):
            best = 2
            fast = 4
        SEQ_FIELDS = ["compression_strength"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['compression_strength']['start'] = self._io.pos()
            self.compression_strength = KaitaiStream.resolve_enum(Gzip.ExtraFlagsDeflate.CompressionStrengths, self._io.read_u1())
            self._debug['compression_strength']['end'] = self._io.pos()


    class Subfields(KaitaiStruct):
        """Container for many subfields, constrained by size of stream.
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
                _t_entries = Gzip.Subfield(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class Subfield(KaitaiStruct):
        """Every subfield follows typical [TLV scheme](https://en.wikipedia.org/wiki/Type-length-value):
        
        * `id` serves role of "T"ype
        * `len_data` serves role of "L"ength
        * `data` serves role of "V"alue
        
        This way it's possible to for arbitrary parser to skip over
        subfields it does not support.
        """
        SEQ_FIELDS = ["id", "len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_u2le()
            self._debug['id']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u2le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


    class Extras(KaitaiStruct):
        SEQ_FIELDS = ["len_subfields", "subfields"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_subfields']['start'] = self._io.pos()
            self.len_subfields = self._io.read_u2le()
            self._debug['len_subfields']['end'] = self._io.pos()
            self._debug['subfields']['start'] = self._io.pos()
            self._raw_subfields = self._io.read_bytes(self.len_subfields)
            _io__raw_subfields = KaitaiStream(BytesIO(self._raw_subfields))
            self.subfields = Gzip.Subfields(_io__raw_subfields, self, self._root)
            self.subfields._read()
            self._debug['subfields']['end'] = self._io.pos()



