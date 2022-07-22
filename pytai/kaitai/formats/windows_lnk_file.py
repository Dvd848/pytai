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

import windows_shell_items
class WindowsLnkFile(KaitaiStruct):
    """Windows .lnk files (AKA "shell link" file) are most frequently used
    in Windows shell to create "shortcuts" to another files, usually for
    purposes of running a program from some other directory, sometimes
    with certain preconfigured arguments and some other options.
    
    .. seealso::
       Source - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
    """

    class WindowState(Enum):
        normal = 1
        maximized = 3
        min_no_active = 7

    class DriveTypes(Enum):
        unknown = 0
        no_root_dir = 1
        removable = 2
        fixed = 3
        remote = 4
        cdrom = 5
        ramdisk = 6
    SEQ_FIELDS = ["header", "target_id_list", "info", "name", "rel_path", "work_dir", "arguments", "icon_location"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = WindowsLnkFile.FileHeader(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        if self.header.flags.has_link_target_id_list:
            self._debug['target_id_list']['start'] = self._io.pos()
            self.target_id_list = WindowsLnkFile.LinkTargetIdList(self._io, self, self._root)
            self.target_id_list._read()
            self._debug['target_id_list']['end'] = self._io.pos()

        if self.header.flags.has_link_info:
            self._debug['info']['start'] = self._io.pos()
            self.info = WindowsLnkFile.LinkInfo(self._io, self, self._root)
            self.info._read()
            self._debug['info']['end'] = self._io.pos()

        if self.header.flags.has_name:
            self._debug['name']['start'] = self._io.pos()
            self.name = WindowsLnkFile.StringData(self._io, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()

        if self.header.flags.has_rel_path:
            self._debug['rel_path']['start'] = self._io.pos()
            self.rel_path = WindowsLnkFile.StringData(self._io, self, self._root)
            self.rel_path._read()
            self._debug['rel_path']['end'] = self._io.pos()

        if self.header.flags.has_work_dir:
            self._debug['work_dir']['start'] = self._io.pos()
            self.work_dir = WindowsLnkFile.StringData(self._io, self, self._root)
            self.work_dir._read()
            self._debug['work_dir']['end'] = self._io.pos()

        if self.header.flags.has_arguments:
            self._debug['arguments']['start'] = self._io.pos()
            self.arguments = WindowsLnkFile.StringData(self._io, self, self._root)
            self.arguments._read()
            self._debug['arguments']['end'] = self._io.pos()

        if self.header.flags.has_icon_location:
            self._debug['icon_location']['start'] = self._io.pos()
            self.icon_location = WindowsLnkFile.StringData(self._io, self, self._root)
            self.icon_location._read()
            self._debug['icon_location']['end'] = self._io.pos()


    class LinkTargetIdList(KaitaiStruct):
        """
        .. seealso::
           Section 2.2 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        SEQ_FIELDS = ["len_id_list", "id_list"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_id_list']['start'] = self._io.pos()
            self.len_id_list = self._io.read_u2le()
            self._debug['len_id_list']['end'] = self._io.pos()
            self._debug['id_list']['start'] = self._io.pos()
            self._raw_id_list = self._io.read_bytes(self.len_id_list)
            _io__raw_id_list = KaitaiStream(BytesIO(self._raw_id_list))
            self.id_list = windows_shell_items.WindowsShellItems(_io__raw_id_list)
            self.id_list._read()
            self._debug['id_list']['end'] = self._io.pos()


    class StringData(KaitaiStruct):
        SEQ_FIELDS = ["chars_str", "str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['chars_str']['start'] = self._io.pos()
            self.chars_str = self._io.read_u2le()
            self._debug['chars_str']['end'] = self._io.pos()
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes((self.chars_str * 2))).decode(u"UTF-16LE")
            self._debug['str']['end'] = self._io.pos()


    class LinkInfo(KaitaiStruct):
        """
        .. seealso::
           Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        SEQ_FIELDS = ["len_all", "all"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_all']['start'] = self._io.pos()
            self.len_all = self._io.read_u4le()
            self._debug['len_all']['end'] = self._io.pos()
            self._debug['all']['start'] = self._io.pos()
            self._raw_all = self._io.read_bytes((self.len_all - 4))
            _io__raw_all = KaitaiStream(BytesIO(self._raw_all))
            self.all = WindowsLnkFile.LinkInfo.All(_io__raw_all, self, self._root)
            self.all._read()
            self._debug['all']['end'] = self._io.pos()

        class VolumeIdBody(KaitaiStruct):
            """
            .. seealso::
               Section 2.3.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            SEQ_FIELDS = ["drive_type", "drive_serial_number", "ofs_volume_label", "ofs_volume_label_unicode"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['drive_type']['start'] = self._io.pos()
                self.drive_type = KaitaiStream.resolve_enum(WindowsLnkFile.DriveTypes, self._io.read_u4le())
                self._debug['drive_type']['end'] = self._io.pos()
                self._debug['drive_serial_number']['start'] = self._io.pos()
                self.drive_serial_number = self._io.read_u4le()
                self._debug['drive_serial_number']['end'] = self._io.pos()
                self._debug['ofs_volume_label']['start'] = self._io.pos()
                self.ofs_volume_label = self._io.read_u4le()
                self._debug['ofs_volume_label']['end'] = self._io.pos()
                if self.is_unicode:
                    self._debug['ofs_volume_label_unicode']['start'] = self._io.pos()
                    self.ofs_volume_label_unicode = self._io.read_u4le()
                    self._debug['ofs_volume_label_unicode']['end'] = self._io.pos()


            @property
            def is_unicode(self):
                if hasattr(self, '_m_is_unicode'):
                    return self._m_is_unicode

                self._m_is_unicode = self.ofs_volume_label == 20
                return getattr(self, '_m_is_unicode', None)

            @property
            def volume_label_ansi(self):
                if hasattr(self, '_m_volume_label_ansi'):
                    return self._m_volume_label_ansi

                if not (self.is_unicode):
                    _pos = self._io.pos()
                    self._io.seek((self.ofs_volume_label - 4))
                    self._debug['_m_volume_label_ansi']['start'] = self._io.pos()
                    self._m_volume_label_ansi = (self._io.read_bytes_term(0, False, True, True)).decode(u"cp437")
                    self._debug['_m_volume_label_ansi']['end'] = self._io.pos()
                    self._io.seek(_pos)

                return getattr(self, '_m_volume_label_ansi', None)


        class All(KaitaiStruct):
            """
            .. seealso::
               Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            SEQ_FIELDS = ["len_header", "header"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['len_header']['start'] = self._io.pos()
                self.len_header = self._io.read_u4le()
                self._debug['len_header']['end'] = self._io.pos()
                self._debug['header']['start'] = self._io.pos()
                self._raw_header = self._io.read_bytes((self.len_header - 8))
                _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
                self.header = WindowsLnkFile.LinkInfo.Header(_io__raw_header, self, self._root)
                self.header._read()
                self._debug['header']['end'] = self._io.pos()

            @property
            def volume_id(self):
                if hasattr(self, '_m_volume_id'):
                    return self._m_volume_id

                if self.header.flags.has_volume_id_and_local_base_path:
                    _pos = self._io.pos()
                    self._io.seek((self.header.ofs_volume_id - 4))
                    self._debug['_m_volume_id']['start'] = self._io.pos()
                    self._m_volume_id = WindowsLnkFile.LinkInfo.VolumeIdSpec(self._io, self, self._root)
                    self._m_volume_id._read()
                    self._debug['_m_volume_id']['end'] = self._io.pos()
                    self._io.seek(_pos)

                return getattr(self, '_m_volume_id', None)

            @property
            def local_base_path(self):
                if hasattr(self, '_m_local_base_path'):
                    return self._m_local_base_path

                if self.header.flags.has_volume_id_and_local_base_path:
                    _pos = self._io.pos()
                    self._io.seek((self.header.ofs_local_base_path - 4))
                    self._debug['_m_local_base_path']['start'] = self._io.pos()
                    self._m_local_base_path = self._io.read_bytes_term(0, False, True, True)
                    self._debug['_m_local_base_path']['end'] = self._io.pos()
                    self._io.seek(_pos)

                return getattr(self, '_m_local_base_path', None)


        class VolumeIdSpec(KaitaiStruct):
            """
            .. seealso::
               Section 2.3.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            SEQ_FIELDS = ["len_all", "body"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['len_all']['start'] = self._io.pos()
                self.len_all = self._io.read_u4le()
                self._debug['len_all']['end'] = self._io.pos()
                self._debug['body']['start'] = self._io.pos()
                self._raw_body = self._io.read_bytes((self.len_all - 4))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = WindowsLnkFile.LinkInfo.VolumeIdBody(_io__raw_body, self, self._root)
                self.body._read()
                self._debug['body']['end'] = self._io.pos()


        class LinkInfoFlags(KaitaiStruct):
            """
            .. seealso::
               Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            SEQ_FIELDS = ["reserved1", "has_common_net_rel_link", "has_volume_id_and_local_base_path", "reserved2"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved1']['start'] = self._io.pos()
                self.reserved1 = self._io.read_bits_int_be(6)
                self._debug['reserved1']['end'] = self._io.pos()
                self._debug['has_common_net_rel_link']['start'] = self._io.pos()
                self.has_common_net_rel_link = self._io.read_bits_int_be(1) != 0
                self._debug['has_common_net_rel_link']['end'] = self._io.pos()
                self._debug['has_volume_id_and_local_base_path']['start'] = self._io.pos()
                self.has_volume_id_and_local_base_path = self._io.read_bits_int_be(1) != 0
                self._debug['has_volume_id_and_local_base_path']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_bits_int_be(24)
                self._debug['reserved2']['end'] = self._io.pos()


        class Header(KaitaiStruct):
            """
            .. seealso::
               Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            SEQ_FIELDS = ["flags", "ofs_volume_id", "ofs_local_base_path", "ofs_common_net_rel_link", "ofs_common_path_suffix", "ofs_local_base_path_unicode", "ofs_common_path_suffix_unicode"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['flags']['start'] = self._io.pos()
                self.flags = WindowsLnkFile.LinkInfo.LinkInfoFlags(self._io, self, self._root)
                self.flags._read()
                self._debug['flags']['end'] = self._io.pos()
                self._debug['ofs_volume_id']['start'] = self._io.pos()
                self.ofs_volume_id = self._io.read_u4le()
                self._debug['ofs_volume_id']['end'] = self._io.pos()
                self._debug['ofs_local_base_path']['start'] = self._io.pos()
                self.ofs_local_base_path = self._io.read_u4le()
                self._debug['ofs_local_base_path']['end'] = self._io.pos()
                self._debug['ofs_common_net_rel_link']['start'] = self._io.pos()
                self.ofs_common_net_rel_link = self._io.read_u4le()
                self._debug['ofs_common_net_rel_link']['end'] = self._io.pos()
                self._debug['ofs_common_path_suffix']['start'] = self._io.pos()
                self.ofs_common_path_suffix = self._io.read_u4le()
                self._debug['ofs_common_path_suffix']['end'] = self._io.pos()
                if not (self._io.is_eof()):
                    self._debug['ofs_local_base_path_unicode']['start'] = self._io.pos()
                    self.ofs_local_base_path_unicode = self._io.read_u4le()
                    self._debug['ofs_local_base_path_unicode']['end'] = self._io.pos()

                if not (self._io.is_eof()):
                    self._debug['ofs_common_path_suffix_unicode']['start'] = self._io.pos()
                    self.ofs_common_path_suffix_unicode = self._io.read_u4le()
                    self._debug['ofs_common_path_suffix_unicode']['end'] = self._io.pos()




    class LinkFlags(KaitaiStruct):
        """
        .. seealso::
           Section 2.1.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        SEQ_FIELDS = ["is_unicode", "has_icon_location", "has_arguments", "has_work_dir", "has_rel_path", "has_name", "has_link_info", "has_link_target_id_list", "_unnamed8", "reserved", "keep_local_id_list_for_unc_target", "_unnamed11"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['is_unicode']['start'] = self._io.pos()
            self.is_unicode = self._io.read_bits_int_be(1) != 0
            self._debug['is_unicode']['end'] = self._io.pos()
            self._debug['has_icon_location']['start'] = self._io.pos()
            self.has_icon_location = self._io.read_bits_int_be(1) != 0
            self._debug['has_icon_location']['end'] = self._io.pos()
            self._debug['has_arguments']['start'] = self._io.pos()
            self.has_arguments = self._io.read_bits_int_be(1) != 0
            self._debug['has_arguments']['end'] = self._io.pos()
            self._debug['has_work_dir']['start'] = self._io.pos()
            self.has_work_dir = self._io.read_bits_int_be(1) != 0
            self._debug['has_work_dir']['end'] = self._io.pos()
            self._debug['has_rel_path']['start'] = self._io.pos()
            self.has_rel_path = self._io.read_bits_int_be(1) != 0
            self._debug['has_rel_path']['end'] = self._io.pos()
            self._debug['has_name']['start'] = self._io.pos()
            self.has_name = self._io.read_bits_int_be(1) != 0
            self._debug['has_name']['end'] = self._io.pos()
            self._debug['has_link_info']['start'] = self._io.pos()
            self.has_link_info = self._io.read_bits_int_be(1) != 0
            self._debug['has_link_info']['end'] = self._io.pos()
            self._debug['has_link_target_id_list']['start'] = self._io.pos()
            self.has_link_target_id_list = self._io.read_bits_int_be(1) != 0
            self._debug['has_link_target_id_list']['end'] = self._io.pos()
            self._debug['_unnamed8']['start'] = self._io.pos()
            self._unnamed8 = self._io.read_bits_int_be(16)
            self._debug['_unnamed8']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bits_int_be(5)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['keep_local_id_list_for_unc_target']['start'] = self._io.pos()
            self.keep_local_id_list_for_unc_target = self._io.read_bits_int_be(1) != 0
            self._debug['keep_local_id_list_for_unc_target']['end'] = self._io.pos()
            self._debug['_unnamed11']['start'] = self._io.pos()
            self._unnamed11 = self._io.read_bits_int_be(2)
            self._debug['_unnamed11']['end'] = self._io.pos()


    class FileHeader(KaitaiStruct):
        """
        .. seealso::
           Section 2.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        SEQ_FIELDS = ["len_header", "link_clsid", "flags", "file_attrs", "time_creation", "time_access", "time_write", "target_file_size", "icon_index", "show_command", "hotkey", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_bytes(4)
            self._debug['len_header']['end'] = self._io.pos()
            if not self.len_header == b"\x4C\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x00\x00\x00", self.len_header, self._io, u"/types/file_header/seq/0")
            self._debug['link_clsid']['start'] = self._io.pos()
            self.link_clsid = self._io.read_bytes(16)
            self._debug['link_clsid']['end'] = self._io.pos()
            if not self.link_clsid == b"\x01\x14\x02\x00\x00\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x01\x14\x02\x00\x00\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x46", self.link_clsid, self._io, u"/types/file_header/seq/1")
            self._debug['flags']['start'] = self._io.pos()
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = WindowsLnkFile.LinkFlags(_io__raw_flags, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['file_attrs']['start'] = self._io.pos()
            self.file_attrs = self._io.read_u4le()
            self._debug['file_attrs']['end'] = self._io.pos()
            self._debug['time_creation']['start'] = self._io.pos()
            self.time_creation = self._io.read_u8le()
            self._debug['time_creation']['end'] = self._io.pos()
            self._debug['time_access']['start'] = self._io.pos()
            self.time_access = self._io.read_u8le()
            self._debug['time_access']['end'] = self._io.pos()
            self._debug['time_write']['start'] = self._io.pos()
            self.time_write = self._io.read_u8le()
            self._debug['time_write']['end'] = self._io.pos()
            self._debug['target_file_size']['start'] = self._io.pos()
            self.target_file_size = self._io.read_u4le()
            self._debug['target_file_size']['end'] = self._io.pos()
            self._debug['icon_index']['start'] = self._io.pos()
            self.icon_index = self._io.read_s4le()
            self._debug['icon_index']['end'] = self._io.pos()
            self._debug['show_command']['start'] = self._io.pos()
            self.show_command = KaitaiStream.resolve_enum(WindowsLnkFile.WindowState, self._io.read_u4le())
            self._debug['show_command']['end'] = self._io.pos()
            self._debug['hotkey']['start'] = self._io.pos()
            self.hotkey = self._io.read_u2le()
            self._debug['hotkey']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(10)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.reserved, self._io, u"/types/file_header/seq/11")



