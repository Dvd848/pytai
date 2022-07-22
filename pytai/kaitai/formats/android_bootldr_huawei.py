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

class AndroidBootldrHuawei(KaitaiStruct):
    """Format of `bootloader-*.img` files found in factory images of certain Android devices from Huawei:
    
    * Nexus 6P "angler": [sample][sample-angler] ([other samples][others-angler]),
      [releasetools.py](https://android.googlesource.com/device/huawei/angler/+/cf92cd8/releasetools.py#29)
    
    [sample-angler]: https://androidfilehost.com/?fid=11410963190603870158 "bootloader-angler-angler-03.84.img"
    [others-angler]: https://androidfilehost.com/?w=search&s=bootloader-angler&type=files
    
    All image versions can be found in factory images at
    <https://developers.google.com/android/images> for the specific device. To
    avoid having to download an entire ZIP archive when you only need one file
    from it, install [remotezip](https://github.com/gtsystem/python-remotezip) and
    use its [command line
    tool](https://github.com/gtsystem/python-remotezip#command-line-tool) to list
    members in the archive and then to download only the file you want.
    
    .. seealso::
       Source - https://android.googlesource.com/device/huawei/angler/+/673cfb9/releasetools.py
    
    
    .. seealso::
       Source - https://source.codeaurora.org/quic/la/device/qcom/common/tree/meta_image/meta_format.h?h=LA.UM.6.1.1&id=a68d284aee85
    
    
    .. seealso::
       Source - https://source.codeaurora.org/quic/la/device/qcom/common/tree/meta_image/meta_image.c?h=LA.UM.6.1.1&id=a68d284aee85
    """
    SEQ_FIELDS = ["meta_header", "header_ext", "image_header"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['meta_header']['start'] = self._io.pos()
        self.meta_header = AndroidBootldrHuawei.MetaHdr(self._io, self, self._root)
        self.meta_header._read()
        self._debug['meta_header']['end'] = self._io.pos()
        self._debug['header_ext']['start'] = self._io.pos()
        self.header_ext = self._io.read_bytes((self.meta_header.len_meta_header - 76))
        self._debug['header_ext']['end'] = self._io.pos()
        self._debug['image_header']['start'] = self._io.pos()
        self._raw_image_header = self._io.read_bytes(self.meta_header.len_image_header)
        _io__raw_image_header = KaitaiStream(BytesIO(self._raw_image_header))
        self.image_header = AndroidBootldrHuawei.ImageHdr(_io__raw_image_header, self, self._root)
        self.image_header._read()
        self._debug['image_header']['end'] = self._io.pos()

    class MetaHdr(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "image_version", "len_meta_header", "len_image_header"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x3C\xD6\x1A\xCE":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\xD6\x1A\xCE", self.magic, self._io, u"/types/meta_hdr/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = AndroidBootldrHuawei.Version(self._io, self, self._root)
            self.version._read()
            self._debug['version']['end'] = self._io.pos()
            self._debug['image_version']['start'] = self._io.pos()
            self.image_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ASCII")
            self._debug['image_version']['end'] = self._io.pos()
            self._debug['len_meta_header']['start'] = self._io.pos()
            self.len_meta_header = self._io.read_u2le()
            self._debug['len_meta_header']['end'] = self._io.pos()
            self._debug['len_image_header']['start'] = self._io.pos()
            self.len_image_header = self._io.read_u2le()
            self._debug['len_image_header']['end'] = self._io.pos()


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
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()


    class ImageHdr(KaitaiStruct):
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
                _t_entries = AndroidBootldrHuawei.ImageHdrEntry(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class ImageHdrEntry(KaitaiStruct):
        SEQ_FIELDS = ["name", "ofs_body", "len_body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(72), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['ofs_body']['start'] = self._io.pos()
            self.ofs_body = self._io.read_u4le()
            self._debug['ofs_body']['end'] = self._io.pos()
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u4le()
            self._debug['len_body']['end'] = self._io.pos()

        @property
        def is_used(self):
            """
            .. seealso::
               Source - https://source.codeaurora.org/quic/la/device/qcom/common/tree/meta_image/meta_image.c?h=LA.UM.6.1.1&id=a68d284aee85#n119
            """
            if hasattr(self, '_m_is_used'):
                return self._m_is_used

            self._m_is_used =  ((self.ofs_body != 0) and (self.len_body != 0)) 
            return getattr(self, '_m_is_used', None)

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            if self.is_used:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_body)
                self._debug['_m_body']['start'] = io.pos()
                self._m_body = io.read_bytes(self.len_body)
                self._debug['_m_body']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_body', None)



