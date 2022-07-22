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

class AndroidBootldrAsus(KaitaiStruct):
    """A bootloader image which only seems to have been used on a few ASUS
    devices. The encoding is ASCII, because the `releasetools.py` script
    is written using Python 2, where the default encoding is ASCII.
    
    A test file can be found in the firmware files for the "fugu" device,
    which can be downloaded from <https://developers.google.com/android/images>
    
    .. seealso::
       Source - https://android.googlesource.com/device/asus/fugu/+/android-8.1.0_r5/releasetools.py
    """
    SEQ_FIELDS = ["magic", "revision", "reserved1", "reserved2", "images"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x42\x4F\x4F\x54\x4C\x44\x52\x21":
            raise kaitaistruct.ValidationNotEqualError(b"\x42\x4F\x4F\x54\x4C\x44\x52\x21", self.magic, self._io, u"/seq/0")
        self._debug['revision']['start'] = self._io.pos()
        self.revision = self._io.read_u2le()
        self._debug['revision']['end'] = self._io.pos()
        if not self.revision >= 2:
            raise kaitaistruct.ValidationLessThanError(2, self.revision, self._io, u"/seq/1")
        self._debug['reserved1']['start'] = self._io.pos()
        self.reserved1 = self._io.read_u2le()
        self._debug['reserved1']['end'] = self._io.pos()
        self._debug['reserved2']['start'] = self._io.pos()
        self.reserved2 = self._io.read_u4le()
        self._debug['reserved2']['end'] = self._io.pos()
        self._debug['images']['start'] = self._io.pos()
        self.images = []
        for i in range(3):
            if not 'arr' in self._debug['images']:
                self._debug['images']['arr'] = []
            self._debug['images']['arr'].append({'start': self._io.pos()})
            _t_images = AndroidBootldrAsus.Image(self._io, self, self._root)
            _t_images._read()
            self.images.append(_t_images)
            self._debug['images']['arr'][i]['end'] = self._io.pos()

        self._debug['images']['end'] = self._io.pos()

    class Image(KaitaiStruct):
        SEQ_FIELDS = ["chunk_id", "len_body", "flags", "reserved1", "reserved2", "reserved3", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['chunk_id']['start'] = self._io.pos()
            self.chunk_id = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['chunk_id']['end'] = self._io.pos()
            if not  ((self.chunk_id == u"IFWI!!!!") or (self.chunk_id == u"DROIDBT!") or (self.chunk_id == u"SPLASHS!")) :
                raise kaitaistruct.ValidationNotAnyOfError(self.chunk_id, self._io, u"/types/image/seq/0")
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u4le()
            self._debug['len_body']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            _ = self.flags
            if not (_ & 1) != 0:
                raise kaitaistruct.ValidationExprError(self.flags, self._io, u"/types/image/seq/2")
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_u1()
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_u1()
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_u1()
            self._debug['reserved3']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(self.len_body)
            self._debug['body']['end'] = self._io.pos()

        @property
        def file_name(self):
            if hasattr(self, '_m_file_name'):
                return self._m_file_name

            self._m_file_name = (u"ifwi.bin" if self.chunk_id == u"IFWI!!!!" else (u"droidboot.img" if self.chunk_id == u"DROIDBT!" else (u"splashscreen.img" if self.chunk_id == u"SPLASHS!" else u"")))
            return getattr(self, '_m_file_name', None)



