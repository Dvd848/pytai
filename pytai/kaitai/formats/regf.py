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
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Regf(KaitaiStruct):
    """This spec allows to parse files used by Microsoft Windows family of
    operating systems to store parts of its "registry". "Registry" is a
    hierarchical database that is used to store system settings (global
    configuration, per-user, per-application configuration, etc).
    
    Typically, registry files are stored in:
    
    * System-wide: several files in `%SystemRoot%\System32\Config\`
    * User-wide:
      * `%USERPROFILE%\Ntuser.dat`
      * `%USERPROFILE%\Local Settings\Application Data\Microsoft\Windows\Usrclass.dat` (localized, Windows 2000, Server 2003 and Windows XP)
      * `%USERPROFILE%\AppData\Local\Microsoft\Windows\Usrclass.dat` (non-localized, Windows Vista and later)
    
    Note that one typically can't access files directly on a mounted
    filesystem with a running Windows OS.
    
    .. seealso::
       Source - https://github.com/libyal/libregf/blob/main/documentation/Windows%20NT%20Registry%20File%20(REGF)%20format.asciidoc
    """
    SEQ_FIELDS = ["header", "hive_bins"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Regf.FileHeader(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['hive_bins']['start'] = self._io.pos()
        self._raw_hive_bins = []
        self.hive_bins = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['hive_bins']:
                self._debug['hive_bins']['arr'] = []
            self._debug['hive_bins']['arr'].append({'start': self._io.pos()})
            self._raw_hive_bins.append(self._io.read_bytes(4096))
            _io__raw_hive_bins = KaitaiStream(BytesIO(self._raw_hive_bins[-1]))
            _t_hive_bins = Regf.HiveBin(_io__raw_hive_bins, self, self._root)
            _t_hive_bins._read()
            self.hive_bins.append(_t_hive_bins)
            self._debug['hive_bins']['arr'][len(self.hive_bins) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['hive_bins']['end'] = self._io.pos()

    class Filetime(KaitaiStruct):
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u8le()
            self._debug['value']['end'] = self._io.pos()


    class HiveBin(KaitaiStruct):
        SEQ_FIELDS = ["header", "cells"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Regf.HiveBinHeader(self._io, self, self._root)
            self.header._read()
            self._debug['header']['end'] = self._io.pos()
            self._debug['cells']['start'] = self._io.pos()
            self.cells = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['cells']:
                    self._debug['cells']['arr'] = []
                self._debug['cells']['arr'].append({'start': self._io.pos()})
                _t_cells = Regf.HiveBinCell(self._io, self, self._root)
                _t_cells._read()
                self.cells.append(_t_cells)
                self._debug['cells']['arr'][len(self.cells) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['cells']['end'] = self._io.pos()


    class HiveBinHeader(KaitaiStruct):
        SEQ_FIELDS = ["signature", "offset", "size", "unknown1", "unknown2", "timestamp", "unknown4"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x68\x62\x69\x6E":
                raise kaitaistruct.ValidationNotEqualError(b"\x68\x62\x69\x6E", self.signature, self._io, u"/types/hive_bin_header/seq/0")
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4le()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u4le()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = Regf.Filetime(self._io, self, self._root)
            self.timestamp._read()
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_u4le()
            self._debug['unknown4']['end'] = self._io.pos()


    class HiveBinCell(KaitaiStruct):
        SEQ_FIELDS = ["cell_size_raw", "identifier", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['cell_size_raw']['start'] = self._io.pos()
            self.cell_size_raw = self._io.read_s4le()
            self._debug['cell_size_raw']['end'] = self._io.pos()
            self._debug['identifier']['start'] = self._io.pos()
            self.identifier = (self._io.read_bytes(2)).decode(u"ascii")
            self._debug['identifier']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.identifier
            if _on == u"li":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.SubKeyListLi(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == u"vk":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.SubKeyListVk(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == u"lf":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.SubKeyListLhLf(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == u"ri":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.SubKeyListRi(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == u"lh":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.SubKeyListLhLf(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == u"nk":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.NamedKey(_io__raw_data, self, self._root)
                self.data._read()
            elif _on == u"sk":
                self._raw_data = self._io.read_bytes(((self.cell_size - 2) - 4))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Regf.HiveBinCell.SubKeyListSk(_io__raw_data, self, self._root)
                self.data._read()
            else:
                self.data = self._io.read_bytes(((self.cell_size - 2) - 4))
            self._debug['data']['end'] = self._io.pos()

        class SubKeyListVk(KaitaiStruct):

            class DataTypeEnum(Enum):
                reg_none = 0
                reg_sz = 1
                reg_expand_sz = 2
                reg_binary = 3
                reg_dword = 4
                reg_dword_big_endian = 5
                reg_link = 6
                reg_multi_sz = 7
                reg_resource_list = 8
                reg_full_resource_descriptor = 9
                reg_resource_requirements_list = 10
                reg_qword = 11

            class VkFlags(Enum):
                value_comp_name = 1
            SEQ_FIELDS = ["value_name_size", "data_size", "data_offset", "data_type", "flags", "padding", "value_name"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['value_name_size']['start'] = self._io.pos()
                self.value_name_size = self._io.read_u2le()
                self._debug['value_name_size']['end'] = self._io.pos()
                self._debug['data_size']['start'] = self._io.pos()
                self.data_size = self._io.read_u4le()
                self._debug['data_size']['end'] = self._io.pos()
                self._debug['data_offset']['start'] = self._io.pos()
                self.data_offset = self._io.read_u4le()
                self._debug['data_offset']['end'] = self._io.pos()
                self._debug['data_type']['start'] = self._io.pos()
                self.data_type = KaitaiStream.resolve_enum(Regf.HiveBinCell.SubKeyListVk.DataTypeEnum, self._io.read_u4le())
                self._debug['data_type']['end'] = self._io.pos()
                self._debug['flags']['start'] = self._io.pos()
                self.flags = KaitaiStream.resolve_enum(Regf.HiveBinCell.SubKeyListVk.VkFlags, self._io.read_u2le())
                self._debug['flags']['end'] = self._io.pos()
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_u2le()
                self._debug['padding']['end'] = self._io.pos()
                if self.flags == Regf.HiveBinCell.SubKeyListVk.VkFlags.value_comp_name:
                    self._debug['value_name']['start'] = self._io.pos()
                    self.value_name = (self._io.read_bytes(self.value_name_size)).decode(u"ascii")
                    self._debug['value_name']['end'] = self._io.pos()



        class SubKeyListLhLf(KaitaiStruct):
            SEQ_FIELDS = ["count", "items"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['count']['start'] = self._io.pos()
                self.count = self._io.read_u2le()
                self._debug['count']['end'] = self._io.pos()
                self._debug['items']['start'] = self._io.pos()
                self.items = []
                for i in range(self.count):
                    if not 'arr' in self._debug['items']:
                        self._debug['items']['arr'] = []
                    self._debug['items']['arr'].append({'start': self._io.pos()})
                    _t_items = Regf.HiveBinCell.SubKeyListLhLf.Item(self._io, self, self._root)
                    _t_items._read()
                    self.items.append(_t_items)
                    self._debug['items']['arr'][i]['end'] = self._io.pos()

                self._debug['items']['end'] = self._io.pos()

            class Item(KaitaiStruct):
                SEQ_FIELDS = ["named_key_offset", "hash_value"]
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._debug = collections.defaultdict(dict)

                def _read(self):
                    self._debug['named_key_offset']['start'] = self._io.pos()
                    self.named_key_offset = self._io.read_u4le()
                    self._debug['named_key_offset']['end'] = self._io.pos()
                    self._debug['hash_value']['start'] = self._io.pos()
                    self.hash_value = self._io.read_u4le()
                    self._debug['hash_value']['end'] = self._io.pos()



        class SubKeyListSk(KaitaiStruct):
            SEQ_FIELDS = ["unknown1", "previous_security_key_offset", "next_security_key_offset", "reference_count"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['unknown1']['start'] = self._io.pos()
                self.unknown1 = self._io.read_u2le()
                self._debug['unknown1']['end'] = self._io.pos()
                self._debug['previous_security_key_offset']['start'] = self._io.pos()
                self.previous_security_key_offset = self._io.read_u4le()
                self._debug['previous_security_key_offset']['end'] = self._io.pos()
                self._debug['next_security_key_offset']['start'] = self._io.pos()
                self.next_security_key_offset = self._io.read_u4le()
                self._debug['next_security_key_offset']['end'] = self._io.pos()
                self._debug['reference_count']['start'] = self._io.pos()
                self.reference_count = self._io.read_u4le()
                self._debug['reference_count']['end'] = self._io.pos()


        class SubKeyListLi(KaitaiStruct):
            SEQ_FIELDS = ["count", "items"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['count']['start'] = self._io.pos()
                self.count = self._io.read_u2le()
                self._debug['count']['end'] = self._io.pos()
                self._debug['items']['start'] = self._io.pos()
                self.items = []
                for i in range(self.count):
                    if not 'arr' in self._debug['items']:
                        self._debug['items']['arr'] = []
                    self._debug['items']['arr'].append({'start': self._io.pos()})
                    _t_items = Regf.HiveBinCell.SubKeyListLi.Item(self._io, self, self._root)
                    _t_items._read()
                    self.items.append(_t_items)
                    self._debug['items']['arr'][i]['end'] = self._io.pos()

                self._debug['items']['end'] = self._io.pos()

            class Item(KaitaiStruct):
                SEQ_FIELDS = ["named_key_offset"]
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._debug = collections.defaultdict(dict)

                def _read(self):
                    self._debug['named_key_offset']['start'] = self._io.pos()
                    self.named_key_offset = self._io.read_u4le()
                    self._debug['named_key_offset']['end'] = self._io.pos()



        class NamedKey(KaitaiStruct):

            class NkFlags(Enum):
                key_is_volatile = 1
                key_hive_exit = 2
                key_hive_entry = 4
                key_no_delete = 8
                key_sym_link = 16
                key_comp_name = 32
                key_prefef_handle = 64
                key_virt_mirrored = 128
                key_virt_target = 256
                key_virtual_store = 512
                unknown1 = 4096
                unknown2 = 16384
            SEQ_FIELDS = ["flags", "last_key_written_date_and_time", "unknown1", "parent_key_offset", "number_of_sub_keys", "number_of_volatile_sub_keys", "sub_keys_list_offset", "number_of_values", "values_list_offset", "security_key_offset", "class_name_offset", "largest_sub_key_name_size", "largest_sub_key_class_name_size", "largest_value_name_size", "largest_value_data_size", "unknown2", "key_name_size", "class_name_size", "unknown_string_size", "unknown_string"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['flags']['start'] = self._io.pos()
                self.flags = KaitaiStream.resolve_enum(Regf.HiveBinCell.NamedKey.NkFlags, self._io.read_u2le())
                self._debug['flags']['end'] = self._io.pos()
                self._debug['last_key_written_date_and_time']['start'] = self._io.pos()
                self.last_key_written_date_and_time = Regf.Filetime(self._io, self, self._root)
                self.last_key_written_date_and_time._read()
                self._debug['last_key_written_date_and_time']['end'] = self._io.pos()
                self._debug['unknown1']['start'] = self._io.pos()
                self.unknown1 = self._io.read_u4le()
                self._debug['unknown1']['end'] = self._io.pos()
                self._debug['parent_key_offset']['start'] = self._io.pos()
                self.parent_key_offset = self._io.read_u4le()
                self._debug['parent_key_offset']['end'] = self._io.pos()
                self._debug['number_of_sub_keys']['start'] = self._io.pos()
                self.number_of_sub_keys = self._io.read_u4le()
                self._debug['number_of_sub_keys']['end'] = self._io.pos()
                self._debug['number_of_volatile_sub_keys']['start'] = self._io.pos()
                self.number_of_volatile_sub_keys = self._io.read_u4le()
                self._debug['number_of_volatile_sub_keys']['end'] = self._io.pos()
                self._debug['sub_keys_list_offset']['start'] = self._io.pos()
                self.sub_keys_list_offset = self._io.read_u4le()
                self._debug['sub_keys_list_offset']['end'] = self._io.pos()
                self._debug['number_of_values']['start'] = self._io.pos()
                self.number_of_values = self._io.read_u4le()
                self._debug['number_of_values']['end'] = self._io.pos()
                self._debug['values_list_offset']['start'] = self._io.pos()
                self.values_list_offset = self._io.read_u4le()
                self._debug['values_list_offset']['end'] = self._io.pos()
                self._debug['security_key_offset']['start'] = self._io.pos()
                self.security_key_offset = self._io.read_u4le()
                self._debug['security_key_offset']['end'] = self._io.pos()
                self._debug['class_name_offset']['start'] = self._io.pos()
                self.class_name_offset = self._io.read_u4le()
                self._debug['class_name_offset']['end'] = self._io.pos()
                self._debug['largest_sub_key_name_size']['start'] = self._io.pos()
                self.largest_sub_key_name_size = self._io.read_u4le()
                self._debug['largest_sub_key_name_size']['end'] = self._io.pos()
                self._debug['largest_sub_key_class_name_size']['start'] = self._io.pos()
                self.largest_sub_key_class_name_size = self._io.read_u4le()
                self._debug['largest_sub_key_class_name_size']['end'] = self._io.pos()
                self._debug['largest_value_name_size']['start'] = self._io.pos()
                self.largest_value_name_size = self._io.read_u4le()
                self._debug['largest_value_name_size']['end'] = self._io.pos()
                self._debug['largest_value_data_size']['start'] = self._io.pos()
                self.largest_value_data_size = self._io.read_u4le()
                self._debug['largest_value_data_size']['end'] = self._io.pos()
                self._debug['unknown2']['start'] = self._io.pos()
                self.unknown2 = self._io.read_u4le()
                self._debug['unknown2']['end'] = self._io.pos()
                self._debug['key_name_size']['start'] = self._io.pos()
                self.key_name_size = self._io.read_u2le()
                self._debug['key_name_size']['end'] = self._io.pos()
                self._debug['class_name_size']['start'] = self._io.pos()
                self.class_name_size = self._io.read_u2le()
                self._debug['class_name_size']['end'] = self._io.pos()
                self._debug['unknown_string_size']['start'] = self._io.pos()
                self.unknown_string_size = self._io.read_u4le()
                self._debug['unknown_string_size']['end'] = self._io.pos()
                self._debug['unknown_string']['start'] = self._io.pos()
                self.unknown_string = (self._io.read_bytes(self.unknown_string_size)).decode(u"ascii")
                self._debug['unknown_string']['end'] = self._io.pos()


        class SubKeyListRi(KaitaiStruct):
            SEQ_FIELDS = ["count", "items"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['count']['start'] = self._io.pos()
                self.count = self._io.read_u2le()
                self._debug['count']['end'] = self._io.pos()
                self._debug['items']['start'] = self._io.pos()
                self.items = []
                for i in range(self.count):
                    if not 'arr' in self._debug['items']:
                        self._debug['items']['arr'] = []
                    self._debug['items']['arr'].append({'start': self._io.pos()})
                    _t_items = Regf.HiveBinCell.SubKeyListRi.Item(self._io, self, self._root)
                    _t_items._read()
                    self.items.append(_t_items)
                    self._debug['items']['arr'][i]['end'] = self._io.pos()

                self._debug['items']['end'] = self._io.pos()

            class Item(KaitaiStruct):
                SEQ_FIELDS = ["sub_key_list_offset"]
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._debug = collections.defaultdict(dict)

                def _read(self):
                    self._debug['sub_key_list_offset']['start'] = self._io.pos()
                    self.sub_key_list_offset = self._io.read_u4le()
                    self._debug['sub_key_list_offset']['end'] = self._io.pos()



        @property
        def cell_size(self):
            if hasattr(self, '_m_cell_size'):
                return self._m_cell_size

            self._m_cell_size = ((-1 if self.cell_size_raw < 0 else 1) * self.cell_size_raw)
            return getattr(self, '_m_cell_size', None)

        @property
        def is_allocated(self):
            if hasattr(self, '_m_is_allocated'):
                return self._m_is_allocated

            self._m_is_allocated = self.cell_size_raw < 0
            return getattr(self, '_m_is_allocated', None)


    class FileHeader(KaitaiStruct):

        class FileType(Enum):
            normal = 0
            transaction_log = 1

        class FileFormat(Enum):
            direct_memory_load = 1
        SEQ_FIELDS = ["signature", "primary_sequence_number", "secondary_sequence_number", "last_modification_date_and_time", "major_version", "minor_version", "type", "format", "root_key_offset", "hive_bins_data_size", "clustering_factor", "unknown1", "unknown2", "checksum", "reserved", "boot_type", "boot_recover"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x72\x65\x67\x66":
                raise kaitaistruct.ValidationNotEqualError(b"\x72\x65\x67\x66", self.signature, self._io, u"/types/file_header/seq/0")
            self._debug['primary_sequence_number']['start'] = self._io.pos()
            self.primary_sequence_number = self._io.read_u4le()
            self._debug['primary_sequence_number']['end'] = self._io.pos()
            self._debug['secondary_sequence_number']['start'] = self._io.pos()
            self.secondary_sequence_number = self._io.read_u4le()
            self._debug['secondary_sequence_number']['end'] = self._io.pos()
            self._debug['last_modification_date_and_time']['start'] = self._io.pos()
            self.last_modification_date_and_time = Regf.Filetime(self._io, self, self._root)
            self.last_modification_date_and_time._read()
            self._debug['last_modification_date_and_time']['end'] = self._io.pos()
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u4le()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u4le()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Regf.FileHeader.FileType, self._io.read_u4le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['format']['start'] = self._io.pos()
            self.format = KaitaiStream.resolve_enum(Regf.FileHeader.FileFormat, self._io.read_u4le())
            self._debug['format']['end'] = self._io.pos()
            self._debug['root_key_offset']['start'] = self._io.pos()
            self.root_key_offset = self._io.read_u4le()
            self._debug['root_key_offset']['end'] = self._io.pos()
            self._debug['hive_bins_data_size']['start'] = self._io.pos()
            self.hive_bins_data_size = self._io.read_u4le()
            self._debug['hive_bins_data_size']['end'] = self._io.pos()
            self._debug['clustering_factor']['start'] = self._io.pos()
            self.clustering_factor = self._io.read_u4le()
            self._debug['clustering_factor']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(64)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_bytes(396)
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4le()
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(3576)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['boot_type']['start'] = self._io.pos()
            self.boot_type = self._io.read_u4le()
            self._debug['boot_type']['end'] = self._io.pos()
            self._debug['boot_recover']['start'] = self._io.pos()
            self.boot_recover = self._io.read_u4le()
            self._debug['boot_recover']['end'] = self._io.pos()



