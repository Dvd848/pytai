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

class Id3v23(KaitaiStruct):
    """
    .. seealso::
       Source - https://id3.org/id3v2.3.0
    """
    SEQ_FIELDS = ["tag"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['tag']['start'] = self._io.pos()
        self.tag = Id3v23.Tag(self._io, self, self._root)
        self.tag._read()
        self._debug['tag']['end'] = self._io.pos()

    class U1beSynchsafe(KaitaiStruct):
        SEQ_FIELDS = ["padding", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bits_int_be(1) != 0
            self._debug['padding']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bits_int_be(7)
            self._debug['value']['end'] = self._io.pos()


    class U2beSynchsafe(KaitaiStruct):
        SEQ_FIELDS = ["byte0", "byte1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['byte0']['start'] = self._io.pos()
            self.byte0 = Id3v23.U1beSynchsafe(self._io, self, self._root)
            self.byte0._read()
            self._debug['byte0']['end'] = self._io.pos()
            self._debug['byte1']['start'] = self._io.pos()
            self.byte1 = Id3v23.U1beSynchsafe(self._io, self, self._root)
            self.byte1._read()
            self._debug['byte1']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.byte0.value << 7) | self.byte1.value)
            return getattr(self, '_m_value', None)


    class Tag(KaitaiStruct):
        """
        .. seealso::
           Section 3. ID3v2 overview
        """
        SEQ_FIELDS = ["header", "header_ex", "frames", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Id3v23.Header(self._io, self, self._root)
            self.header._read()
            self._debug['header']['end'] = self._io.pos()
            if self.header.flags.flag_headerex:
                self._debug['header_ex']['start'] = self._io.pos()
                self.header_ex = Id3v23.HeaderEx(self._io, self, self._root)
                self.header_ex._read()
                self._debug['header_ex']['end'] = self._io.pos()

            self._debug['frames']['start'] = self._io.pos()
            self.frames = []
            i = 0
            while True:
                if not 'arr' in self._debug['frames']:
                    self._debug['frames']['arr'] = []
                self._debug['frames']['arr'].append({'start': self._io.pos()})
                _t_frames = Id3v23.Frame(self._io, self, self._root)
                _t_frames._read()
                _ = _t_frames
                self.frames.append(_)
                self._debug['frames']['arr'][len(self.frames) - 1]['end'] = self._io.pos()
                if  (((self._io.pos() + _.size) > self.header.size.value) or (_.is_invalid)) :
                    break
                i += 1
            self._debug['frames']['end'] = self._io.pos()
            if self.header.flags.flag_headerex:
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes((self.header_ex.padding_size - self._io.pos()))
                self._debug['padding']['end'] = self._io.pos()



    class U4beSynchsafe(KaitaiStruct):
        SEQ_FIELDS = ["short0", "short1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['short0']['start'] = self._io.pos()
            self.short0 = Id3v23.U2beSynchsafe(self._io, self, self._root)
            self.short0._read()
            self._debug['short0']['end'] = self._io.pos()
            self._debug['short1']['start'] = self._io.pos()
            self.short1 = Id3v23.U2beSynchsafe(self._io, self, self._root)
            self.short1._read()
            self._debug['short1']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.short0.value << 14) | self.short1.value)
            return getattr(self, '_m_value', None)


    class Frame(KaitaiStruct):
        """
        .. seealso::
           Section 3.3. ID3v2 frame overview
        """
        SEQ_FIELDS = ["id", "size", "flags", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['id']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4be()
            self._debug['size']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = Id3v23.Frame.Flags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.size)
            self._debug['data']['end'] = self._io.pos()

        class Flags(KaitaiStruct):
            SEQ_FIELDS = ["flag_discard_alter_tag", "flag_discard_alter_file", "flag_read_only", "reserved1", "flag_compressed", "flag_encrypted", "flag_grouping", "reserved2"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['flag_discard_alter_tag']['start'] = self._io.pos()
                self.flag_discard_alter_tag = self._io.read_bits_int_be(1) != 0
                self._debug['flag_discard_alter_tag']['end'] = self._io.pos()
                self._debug['flag_discard_alter_file']['start'] = self._io.pos()
                self.flag_discard_alter_file = self._io.read_bits_int_be(1) != 0
                self._debug['flag_discard_alter_file']['end'] = self._io.pos()
                self._debug['flag_read_only']['start'] = self._io.pos()
                self.flag_read_only = self._io.read_bits_int_be(1) != 0
                self._debug['flag_read_only']['end'] = self._io.pos()
                self._debug['reserved1']['start'] = self._io.pos()
                self.reserved1 = self._io.read_bits_int_be(5)
                self._debug['reserved1']['end'] = self._io.pos()
                self._debug['flag_compressed']['start'] = self._io.pos()
                self.flag_compressed = self._io.read_bits_int_be(1) != 0
                self._debug['flag_compressed']['end'] = self._io.pos()
                self._debug['flag_encrypted']['start'] = self._io.pos()
                self.flag_encrypted = self._io.read_bits_int_be(1) != 0
                self._debug['flag_encrypted']['end'] = self._io.pos()
                self._debug['flag_grouping']['start'] = self._io.pos()
                self.flag_grouping = self._io.read_bits_int_be(1) != 0
                self._debug['flag_grouping']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_bits_int_be(5)
                self._debug['reserved2']['end'] = self._io.pos()


        @property
        def is_invalid(self):
            if hasattr(self, '_m_is_invalid'):
                return self._m_is_invalid

            self._m_is_invalid = self.id == u"\000\000\000\000"
            return getattr(self, '_m_is_invalid', None)


    class HeaderEx(KaitaiStruct):
        """ID3v2 extended header.
        
        .. seealso::
           Section 3.2. ID3v2 extended header
        """
        SEQ_FIELDS = ["size", "flags_ex", "padding_size", "crc"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4be()
            self._debug['size']['end'] = self._io.pos()
            self._debug['flags_ex']['start'] = self._io.pos()
            self.flags_ex = Id3v23.HeaderEx.FlagsEx(self._io, self, self._root)
            self.flags_ex._read()
            self._debug['flags_ex']['end'] = self._io.pos()
            self._debug['padding_size']['start'] = self._io.pos()
            self.padding_size = self._io.read_u4be()
            self._debug['padding_size']['end'] = self._io.pos()
            if self.flags_ex.flag_crc:
                self._debug['crc']['start'] = self._io.pos()
                self.crc = self._io.read_u4be()
                self._debug['crc']['end'] = self._io.pos()


        class FlagsEx(KaitaiStruct):
            SEQ_FIELDS = ["flag_crc", "reserved"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['flag_crc']['start'] = self._io.pos()
                self.flag_crc = self._io.read_bits_int_be(1) != 0
                self._debug['flag_crc']['end'] = self._io.pos()
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_bits_int_be(15)
                self._debug['reserved']['end'] = self._io.pos()



    class Header(KaitaiStruct):
        """ID3v2 fixed header.
        
        .. seealso::
           Section 3.1. ID3v2 header
        """
        SEQ_FIELDS = ["magic", "version_major", "version_revision", "flags", "size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(3)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x49\x44\x33":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x44\x33", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version_major']['start'] = self._io.pos()
            self.version_major = self._io.read_u1()
            self._debug['version_major']['end'] = self._io.pos()
            self._debug['version_revision']['start'] = self._io.pos()
            self.version_revision = self._io.read_u1()
            self._debug['version_revision']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = Id3v23.Header.Flags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = Id3v23.U4beSynchsafe(self._io, self, self._root)
            self.size._read()
            self._debug['size']['end'] = self._io.pos()

        class Flags(KaitaiStruct):
            SEQ_FIELDS = ["flag_unsynchronization", "flag_headerex", "flag_experimental", "reserved"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['flag_unsynchronization']['start'] = self._io.pos()
                self.flag_unsynchronization = self._io.read_bits_int_be(1) != 0
                self._debug['flag_unsynchronization']['end'] = self._io.pos()
                self._debug['flag_headerex']['start'] = self._io.pos()
                self.flag_headerex = self._io.read_bits_int_be(1) != 0
                self._debug['flag_headerex']['end'] = self._io.pos()
                self._debug['flag_experimental']['start'] = self._io.pos()
                self.flag_experimental = self._io.read_bits_int_be(1) != 0
                self._debug['flag_experimental']['end'] = self._io.pos()
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_bits_int_be(5)
                self._debug['reserved']['end'] = self._io.pos()




