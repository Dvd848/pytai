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

class AndroidImg(KaitaiStruct):
    """
    .. seealso::
       Source - https://source.android.com/docs/core/architecture/bootloader/boot-image-header
    """
    SEQ_FIELDS = ["magic", "kernel", "ramdisk", "second", "tags_load", "page_size", "header_version", "os_version", "name", "cmdline", "sha", "extra_cmdline", "recovery_dtbo", "boot_header_size", "dtb"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x41\x4E\x44\x52\x4F\x49\x44\x21":
            raise kaitaistruct.ValidationNotEqualError(b"\x41\x4E\x44\x52\x4F\x49\x44\x21", self.magic, self._io, u"/seq/0")
        self._debug['kernel']['start'] = self._io.pos()
        self.kernel = AndroidImg.Load(self._io, self, self._root)
        self.kernel._read()
        self._debug['kernel']['end'] = self._io.pos()
        self._debug['ramdisk']['start'] = self._io.pos()
        self.ramdisk = AndroidImg.Load(self._io, self, self._root)
        self.ramdisk._read()
        self._debug['ramdisk']['end'] = self._io.pos()
        self._debug['second']['start'] = self._io.pos()
        self.second = AndroidImg.Load(self._io, self, self._root)
        self.second._read()
        self._debug['second']['end'] = self._io.pos()
        self._debug['tags_load']['start'] = self._io.pos()
        self.tags_load = self._io.read_u4le()
        self._debug['tags_load']['end'] = self._io.pos()
        self._debug['page_size']['start'] = self._io.pos()
        self.page_size = self._io.read_u4le()
        self._debug['page_size']['end'] = self._io.pos()
        self._debug['header_version']['start'] = self._io.pos()
        self.header_version = self._io.read_u4le()
        self._debug['header_version']['end'] = self._io.pos()
        self._debug['os_version']['start'] = self._io.pos()
        self.os_version = AndroidImg.OsVersion(self._io, self, self._root)
        self.os_version._read()
        self._debug['os_version']['end'] = self._io.pos()
        self._debug['name']['start'] = self._io.pos()
        self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ASCII")
        self._debug['name']['end'] = self._io.pos()
        self._debug['cmdline']['start'] = self._io.pos()
        self.cmdline = (KaitaiStream.bytes_terminate(self._io.read_bytes(512), 0, False)).decode(u"ASCII")
        self._debug['cmdline']['end'] = self._io.pos()
        self._debug['sha']['start'] = self._io.pos()
        self.sha = self._io.read_bytes(32)
        self._debug['sha']['end'] = self._io.pos()
        self._debug['extra_cmdline']['start'] = self._io.pos()
        self.extra_cmdline = (KaitaiStream.bytes_terminate(self._io.read_bytes(1024), 0, False)).decode(u"ASCII")
        self._debug['extra_cmdline']['end'] = self._io.pos()
        if self.header_version > 0:
            self._debug['recovery_dtbo']['start'] = self._io.pos()
            self.recovery_dtbo = AndroidImg.SizeOffset(self._io, self, self._root)
            self.recovery_dtbo._read()
            self._debug['recovery_dtbo']['end'] = self._io.pos()

        if self.header_version > 0:
            self._debug['boot_header_size']['start'] = self._io.pos()
            self.boot_header_size = self._io.read_u4le()
            self._debug['boot_header_size']['end'] = self._io.pos()

        if self.header_version > 1:
            self._debug['dtb']['start'] = self._io.pos()
            self.dtb = AndroidImg.LoadLong(self._io, self, self._root)
            self.dtb._read()
            self._debug['dtb']['end'] = self._io.pos()


    class Load(KaitaiStruct):
        SEQ_FIELDS = ["size", "addr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['addr']['start'] = self._io.pos()
            self.addr = self._io.read_u4le()
            self._debug['addr']['end'] = self._io.pos()


    class LoadLong(KaitaiStruct):
        SEQ_FIELDS = ["size", "addr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['addr']['start'] = self._io.pos()
            self.addr = self._io.read_u8le()
            self._debug['addr']['end'] = self._io.pos()


    class SizeOffset(KaitaiStruct):
        SEQ_FIELDS = ["size", "offset"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u8le()
            self._debug['offset']['end'] = self._io.pos()


    class OsVersion(KaitaiStruct):
        SEQ_FIELDS = ["version"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()

        @property
        def month(self):
            if hasattr(self, '_m_month'):
                return self._m_month

            self._m_month = (self.version & 15)
            return getattr(self, '_m_month', None)

        @property
        def patch(self):
            if hasattr(self, '_m_patch'):
                return self._m_patch

            self._m_patch = ((self.version >> 11) & 127)
            return getattr(self, '_m_patch', None)

        @property
        def year(self):
            if hasattr(self, '_m_year'):
                return self._m_year

            self._m_year = (((self.version >> 4) & 127) + 2000)
            return getattr(self, '_m_year', None)

        @property
        def major(self):
            if hasattr(self, '_m_major'):
                return self._m_major

            self._m_major = ((self.version >> 25) & 127)
            return getattr(self, '_m_major', None)

        @property
        def minor(self):
            if hasattr(self, '_m_minor'):
                return self._m_minor

            self._m_minor = ((self.version >> 18) & 127)
            return getattr(self, '_m_minor', None)


    @property
    def kernel_img(self):
        if hasattr(self, '_m_kernel_img'):
            return self._m_kernel_img

        _pos = self._io.pos()
        self._io.seek(self.page_size)
        self._debug['_m_kernel_img']['start'] = self._io.pos()
        self._m_kernel_img = self._io.read_bytes(self.kernel.size)
        self._debug['_m_kernel_img']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_kernel_img', None)

    @property
    def tags_offset(self):
        """tags offset from base."""
        if hasattr(self, '_m_tags_offset'):
            return self._m_tags_offset

        self._m_tags_offset = (self.tags_load - self.base)
        return getattr(self, '_m_tags_offset', None)

    @property
    def ramdisk_offset(self):
        """ramdisk offset from base."""
        if hasattr(self, '_m_ramdisk_offset'):
            return self._m_ramdisk_offset

        self._m_ramdisk_offset = ((self.ramdisk.addr - self.base) if self.ramdisk.addr > 0 else 0)
        return getattr(self, '_m_ramdisk_offset', None)

    @property
    def second_offset(self):
        """2nd bootloader offset from base."""
        if hasattr(self, '_m_second_offset'):
            return self._m_second_offset

        self._m_second_offset = ((self.second.addr - self.base) if self.second.addr > 0 else 0)
        return getattr(self, '_m_second_offset', None)

    @property
    def kernel_offset(self):
        """kernel offset from base."""
        if hasattr(self, '_m_kernel_offset'):
            return self._m_kernel_offset

        self._m_kernel_offset = (self.kernel.addr - self.base)
        return getattr(self, '_m_kernel_offset', None)

    @property
    def dtb_offset(self):
        """dtb offset from base."""
        if hasattr(self, '_m_dtb_offset'):
            return self._m_dtb_offset

        if self.header_version > 1:
            self._m_dtb_offset = ((self.dtb.addr - self.base) if self.dtb.addr > 0 else 0)

        return getattr(self, '_m_dtb_offset', None)

    @property
    def dtb_img(self):
        if hasattr(self, '_m_dtb_img'):
            return self._m_dtb_img

        if  ((self.header_version > 1) and (self.dtb.size > 0)) :
            _pos = self._io.pos()
            self._io.seek((((((((self.page_size + self.kernel.size) + self.ramdisk.size) + self.second.size) + self.recovery_dtbo.size) + self.page_size) - 1) // self.page_size * self.page_size))
            self._debug['_m_dtb_img']['start'] = self._io.pos()
            self._m_dtb_img = self._io.read_bytes(self.dtb.size)
            self._debug['_m_dtb_img']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_dtb_img', None)

    @property
    def ramdisk_img(self):
        if hasattr(self, '_m_ramdisk_img'):
            return self._m_ramdisk_img

        if self.ramdisk.size > 0:
            _pos = self._io.pos()
            self._io.seek(((((self.page_size + self.kernel.size) + self.page_size) - 1) // self.page_size * self.page_size))
            self._debug['_m_ramdisk_img']['start'] = self._io.pos()
            self._m_ramdisk_img = self._io.read_bytes(self.ramdisk.size)
            self._debug['_m_ramdisk_img']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_ramdisk_img', None)

    @property
    def recovery_dtbo_img(self):
        if hasattr(self, '_m_recovery_dtbo_img'):
            return self._m_recovery_dtbo_img

        if  ((self.header_version > 0) and (self.recovery_dtbo.size > 0)) :
            _pos = self._io.pos()
            self._io.seek(self.recovery_dtbo.offset)
            self._debug['_m_recovery_dtbo_img']['start'] = self._io.pos()
            self._m_recovery_dtbo_img = self._io.read_bytes(self.recovery_dtbo.size)
            self._debug['_m_recovery_dtbo_img']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_recovery_dtbo_img', None)

    @property
    def second_img(self):
        if hasattr(self, '_m_second_img'):
            return self._m_second_img

        if self.second.size > 0:
            _pos = self._io.pos()
            self._io.seek((((((self.page_size + self.kernel.size) + self.ramdisk.size) + self.page_size) - 1) // self.page_size * self.page_size))
            self._debug['_m_second_img']['start'] = self._io.pos()
            self._m_second_img = self._io.read_bytes(self.second.size)
            self._debug['_m_second_img']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_second_img', None)

    @property
    def base(self):
        """base loading address."""
        if hasattr(self, '_m_base'):
            return self._m_base

        self._m_base = (self.kernel.addr - 32768)
        return getattr(self, '_m_base', None)


