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

class AndroidSuper(KaitaiStruct):
    """The metadata stored by Android at the beginning of a "super" partition, which
    is what it calls a disk partition that holds one or more Dynamic Partitions.
    Dynamic Partitions do more or less the same thing that LVM does on Linux,
    allowing Android to map ranges of non-contiguous extents to a single logical
    device. This metadata holds that mapping.
    
    .. seealso::
       Source - https://source.android.com/docs/core/ota/dynamic_partitions
    
    
    .. seealso::
       Source - https://android.googlesource.com/platform/system/core/+/refs/tags/android-11.0.0_r8/fs_mgr/liblp/include/liblp/metadata_format.h
    """
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        pass

    class Root(KaitaiStruct):
        SEQ_FIELDS = ["primary_geometry", "backup_geometry", "primary_metadata", "backup_metadata"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['primary_geometry']['start'] = self._io.pos()
            self._raw_primary_geometry = self._io.read_bytes(4096)
            _io__raw_primary_geometry = KaitaiStream(BytesIO(self._raw_primary_geometry))
            self.primary_geometry = AndroidSuper.Geometry(_io__raw_primary_geometry, self, self._root)
            self.primary_geometry._read()
            self._debug['primary_geometry']['end'] = self._io.pos()
            self._debug['backup_geometry']['start'] = self._io.pos()
            self._raw_backup_geometry = self._io.read_bytes(4096)
            _io__raw_backup_geometry = KaitaiStream(BytesIO(self._raw_backup_geometry))
            self.backup_geometry = AndroidSuper.Geometry(_io__raw_backup_geometry, self, self._root)
            self.backup_geometry._read()
            self._debug['backup_geometry']['end'] = self._io.pos()
            self._debug['primary_metadata']['start'] = self._io.pos()
            self._raw_primary_metadata = []
            self.primary_metadata = []
            for i in range(self.primary_geometry.metadata_slot_count):
                if not 'arr' in self._debug['primary_metadata']:
                    self._debug['primary_metadata']['arr'] = []
                self._debug['primary_metadata']['arr'].append({'start': self._io.pos()})
                self._raw_primary_metadata.append(self._io.read_bytes(self.primary_geometry.metadata_max_size))
                _io__raw_primary_metadata = KaitaiStream(BytesIO(self._raw_primary_metadata[i]))
                _t_primary_metadata = AndroidSuper.Metadata(_io__raw_primary_metadata, self, self._root)
                _t_primary_metadata._read()
                self.primary_metadata.append(_t_primary_metadata)
                self._debug['primary_metadata']['arr'][i]['end'] = self._io.pos()

            self._debug['primary_metadata']['end'] = self._io.pos()
            self._debug['backup_metadata']['start'] = self._io.pos()
            self._raw_backup_metadata = []
            self.backup_metadata = []
            for i in range(self.primary_geometry.metadata_slot_count):
                if not 'arr' in self._debug['backup_metadata']:
                    self._debug['backup_metadata']['arr'] = []
                self._debug['backup_metadata']['arr'].append({'start': self._io.pos()})
                self._raw_backup_metadata.append(self._io.read_bytes(self.primary_geometry.metadata_max_size))
                _io__raw_backup_metadata = KaitaiStream(BytesIO(self._raw_backup_metadata[i]))
                _t_backup_metadata = AndroidSuper.Metadata(_io__raw_backup_metadata, self, self._root)
                _t_backup_metadata._read()
                self.backup_metadata.append(_t_backup_metadata)
                self._debug['backup_metadata']['arr'][i]['end'] = self._io.pos()

            self._debug['backup_metadata']['end'] = self._io.pos()


    class Geometry(KaitaiStruct):
        SEQ_FIELDS = ["magic", "struct_size", "checksum", "metadata_max_size", "metadata_slot_count", "logical_block_size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x67\x44\x6C\x61":
                raise kaitaistruct.ValidationNotEqualError(b"\x67\x44\x6C\x61", self.magic, self._io, u"/types/geometry/seq/0")
            self._debug['struct_size']['start'] = self._io.pos()
            self.struct_size = self._io.read_u4le()
            self._debug['struct_size']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_bytes(32)
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['metadata_max_size']['start'] = self._io.pos()
            self.metadata_max_size = self._io.read_u4le()
            self._debug['metadata_max_size']['end'] = self._io.pos()
            self._debug['metadata_slot_count']['start'] = self._io.pos()
            self.metadata_slot_count = self._io.read_u4le()
            self._debug['metadata_slot_count']['end'] = self._io.pos()
            self._debug['logical_block_size']['start'] = self._io.pos()
            self.logical_block_size = self._io.read_u4le()
            self._debug['logical_block_size']['end'] = self._io.pos()


    class Metadata(KaitaiStruct):

        class TableKind(Enum):
            partitions = 0
            extents = 1
            groups = 2
            block_devices = 3
        SEQ_FIELDS = ["magic", "major_version", "minor_version", "header_size", "header_checksum", "tables_size", "tables_checksum", "partitions", "extents", "groups", "block_devices"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x30\x50\x4C\x41":
                raise kaitaistruct.ValidationNotEqualError(b"\x30\x50\x4C\x41", self.magic, self._io, u"/types/metadata/seq/0")
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u2le()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u2le()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['header_size']['start'] = self._io.pos()
            self.header_size = self._io.read_u4le()
            self._debug['header_size']['end'] = self._io.pos()
            self._debug['header_checksum']['start'] = self._io.pos()
            self.header_checksum = self._io.read_bytes(32)
            self._debug['header_checksum']['end'] = self._io.pos()
            self._debug['tables_size']['start'] = self._io.pos()
            self.tables_size = self._io.read_u4le()
            self._debug['tables_size']['end'] = self._io.pos()
            self._debug['tables_checksum']['start'] = self._io.pos()
            self.tables_checksum = self._io.read_bytes(32)
            self._debug['tables_checksum']['end'] = self._io.pos()
            self._debug['partitions']['start'] = self._io.pos()
            self.partitions = AndroidSuper.Metadata.TableDescriptor(AndroidSuper.Metadata.TableKind.partitions, self._io, self, self._root)
            self.partitions._read()
            self._debug['partitions']['end'] = self._io.pos()
            self._debug['extents']['start'] = self._io.pos()
            self.extents = AndroidSuper.Metadata.TableDescriptor(AndroidSuper.Metadata.TableKind.extents, self._io, self, self._root)
            self.extents._read()
            self._debug['extents']['end'] = self._io.pos()
            self._debug['groups']['start'] = self._io.pos()
            self.groups = AndroidSuper.Metadata.TableDescriptor(AndroidSuper.Metadata.TableKind.groups, self._io, self, self._root)
            self.groups._read()
            self._debug['groups']['end'] = self._io.pos()
            self._debug['block_devices']['start'] = self._io.pos()
            self.block_devices = AndroidSuper.Metadata.TableDescriptor(AndroidSuper.Metadata.TableKind.block_devices, self._io, self, self._root)
            self.block_devices._read()
            self._debug['block_devices']['end'] = self._io.pos()

        class BlockDevice(KaitaiStruct):
            SEQ_FIELDS = ["first_logical_sector", "alignment", "alignment_offset", "size", "partition_name", "flag_slot_suffixed", "flags_reserved"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['first_logical_sector']['start'] = self._io.pos()
                self.first_logical_sector = self._io.read_u8le()
                self._debug['first_logical_sector']['end'] = self._io.pos()
                self._debug['alignment']['start'] = self._io.pos()
                self.alignment = self._io.read_u4le()
                self._debug['alignment']['end'] = self._io.pos()
                self._debug['alignment_offset']['start'] = self._io.pos()
                self.alignment_offset = self._io.read_u4le()
                self._debug['alignment_offset']['end'] = self._io.pos()
                self._debug['size']['start'] = self._io.pos()
                self.size = self._io.read_u8le()
                self._debug['size']['end'] = self._io.pos()
                self._debug['partition_name']['start'] = self._io.pos()
                self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
                self._debug['partition_name']['end'] = self._io.pos()
                self._debug['flag_slot_suffixed']['start'] = self._io.pos()
                self.flag_slot_suffixed = self._io.read_bits_int_le(1) != 0
                self._debug['flag_slot_suffixed']['end'] = self._io.pos()
                self._debug['flags_reserved']['start'] = self._io.pos()
                self.flags_reserved = self._io.read_bits_int_le(31)
                self._debug['flags_reserved']['end'] = self._io.pos()


        class Extent(KaitaiStruct):

            class TargetType(Enum):
                linear = 0
                zero = 1
            SEQ_FIELDS = ["num_sectors", "target_type", "target_data", "target_source"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['num_sectors']['start'] = self._io.pos()
                self.num_sectors = self._io.read_u8le()
                self._debug['num_sectors']['end'] = self._io.pos()
                self._debug['target_type']['start'] = self._io.pos()
                self.target_type = KaitaiStream.resolve_enum(AndroidSuper.Metadata.Extent.TargetType, self._io.read_u4le())
                self._debug['target_type']['end'] = self._io.pos()
                self._debug['target_data']['start'] = self._io.pos()
                self.target_data = self._io.read_u8le()
                self._debug['target_data']['end'] = self._io.pos()
                self._debug['target_source']['start'] = self._io.pos()
                self.target_source = self._io.read_u4le()
                self._debug['target_source']['end'] = self._io.pos()


        class TableDescriptor(KaitaiStruct):
            SEQ_FIELDS = ["offset", "num_entries", "entry_size"]
            def __init__(self, kind, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.kind = kind
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['offset']['start'] = self._io.pos()
                self.offset = self._io.read_u4le()
                self._debug['offset']['end'] = self._io.pos()
                self._debug['num_entries']['start'] = self._io.pos()
                self.num_entries = self._io.read_u4le()
                self._debug['num_entries']['end'] = self._io.pos()
                self._debug['entry_size']['start'] = self._io.pos()
                self.entry_size = self._io.read_u4le()
                self._debug['entry_size']['end'] = self._io.pos()

            @property
            def table(self):
                if hasattr(self, '_m_table'):
                    return self._m_table

                _pos = self._io.pos()
                self._io.seek((self._parent.header_size + self.offset))
                self._debug['_m_table']['start'] = self._io.pos()
                self._raw__m_table = []
                self._m_table = []
                for i in range(self.num_entries):
                    if not 'arr' in self._debug['_m_table']:
                        self._debug['_m_table']['arr'] = []
                    self._debug['_m_table']['arr'].append({'start': self._io.pos()})
                    _on = self.kind
                    if _on == AndroidSuper.Metadata.TableKind.partitions:
                        if not 'arr' in self._debug['_m_table']:
                            self._debug['_m_table']['arr'] = []
                        self._debug['_m_table']['arr'].append({'start': self._io.pos()})
                        self._raw__m_table.append(self._io.read_bytes(self.entry_size))
                        _io__raw__m_table = KaitaiStream(BytesIO(self._raw__m_table[i]))
                        _t__m_table = AndroidSuper.Metadata.Partition(_io__raw__m_table, self, self._root)
                        _t__m_table._read()
                        self._m_table.append(_t__m_table)
                        self._debug['_m_table']['arr'][i]['end'] = self._io.pos()
                    elif _on == AndroidSuper.Metadata.TableKind.extents:
                        if not 'arr' in self._debug['_m_table']:
                            self._debug['_m_table']['arr'] = []
                        self._debug['_m_table']['arr'].append({'start': self._io.pos()})
                        self._raw__m_table.append(self._io.read_bytes(self.entry_size))
                        _io__raw__m_table = KaitaiStream(BytesIO(self._raw__m_table[i]))
                        _t__m_table = AndroidSuper.Metadata.Extent(_io__raw__m_table, self, self._root)
                        _t__m_table._read()
                        self._m_table.append(_t__m_table)
                        self._debug['_m_table']['arr'][i]['end'] = self._io.pos()
                    elif _on == AndroidSuper.Metadata.TableKind.groups:
                        if not 'arr' in self._debug['_m_table']:
                            self._debug['_m_table']['arr'] = []
                        self._debug['_m_table']['arr'].append({'start': self._io.pos()})
                        self._raw__m_table.append(self._io.read_bytes(self.entry_size))
                        _io__raw__m_table = KaitaiStream(BytesIO(self._raw__m_table[i]))
                        _t__m_table = AndroidSuper.Metadata.Group(_io__raw__m_table, self, self._root)
                        _t__m_table._read()
                        self._m_table.append(_t__m_table)
                        self._debug['_m_table']['arr'][i]['end'] = self._io.pos()
                    elif _on == AndroidSuper.Metadata.TableKind.block_devices:
                        if not 'arr' in self._debug['_m_table']:
                            self._debug['_m_table']['arr'] = []
                        self._debug['_m_table']['arr'].append({'start': self._io.pos()})
                        self._raw__m_table.append(self._io.read_bytes(self.entry_size))
                        _io__raw__m_table = KaitaiStream(BytesIO(self._raw__m_table[i]))
                        _t__m_table = AndroidSuper.Metadata.BlockDevice(_io__raw__m_table, self, self._root)
                        _t__m_table._read()
                        self._m_table.append(_t__m_table)
                        self._debug['_m_table']['arr'][i]['end'] = self._io.pos()
                    else:
                        if not 'arr' in self._debug['_m_table']:
                            self._debug['_m_table']['arr'] = []
                        self._debug['_m_table']['arr'].append({'start': self._io.pos()})
                        self._m_table.append(self._io.read_bytes(self.entry_size))
                        self._debug['_m_table']['arr'][i]['end'] = self._io.pos()
                    self._debug['_m_table']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_table']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_table', None)


        class Partition(KaitaiStruct):
            SEQ_FIELDS = ["name", "attr_readonly", "attr_slot_suffixed", "attr_updated", "attr_disabled", "attrs_reserved", "first_extent_index", "num_extents", "group_index"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['name']['start'] = self._io.pos()
                self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
                self._debug['name']['end'] = self._io.pos()
                self._debug['attr_readonly']['start'] = self._io.pos()
                self.attr_readonly = self._io.read_bits_int_le(1) != 0
                self._debug['attr_readonly']['end'] = self._io.pos()
                self._debug['attr_slot_suffixed']['start'] = self._io.pos()
                self.attr_slot_suffixed = self._io.read_bits_int_le(1) != 0
                self._debug['attr_slot_suffixed']['end'] = self._io.pos()
                self._debug['attr_updated']['start'] = self._io.pos()
                self.attr_updated = self._io.read_bits_int_le(1) != 0
                self._debug['attr_updated']['end'] = self._io.pos()
                self._debug['attr_disabled']['start'] = self._io.pos()
                self.attr_disabled = self._io.read_bits_int_le(1) != 0
                self._debug['attr_disabled']['end'] = self._io.pos()
                self._debug['attrs_reserved']['start'] = self._io.pos()
                self.attrs_reserved = self._io.read_bits_int_le(28)
                self._debug['attrs_reserved']['end'] = self._io.pos()
                self._io.align_to_byte()
                self._debug['first_extent_index']['start'] = self._io.pos()
                self.first_extent_index = self._io.read_u4le()
                self._debug['first_extent_index']['end'] = self._io.pos()
                self._debug['num_extents']['start'] = self._io.pos()
                self.num_extents = self._io.read_u4le()
                self._debug['num_extents']['end'] = self._io.pos()
                self._debug['group_index']['start'] = self._io.pos()
                self.group_index = self._io.read_u4le()
                self._debug['group_index']['end'] = self._io.pos()


        class Group(KaitaiStruct):
            SEQ_FIELDS = ["name", "flag_slot_suffixed", "flags_reserved", "maximum_size"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['name']['start'] = self._io.pos()
                self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
                self._debug['name']['end'] = self._io.pos()
                self._debug['flag_slot_suffixed']['start'] = self._io.pos()
                self.flag_slot_suffixed = self._io.read_bits_int_le(1) != 0
                self._debug['flag_slot_suffixed']['end'] = self._io.pos()
                self._debug['flags_reserved']['start'] = self._io.pos()
                self.flags_reserved = self._io.read_bits_int_le(31)
                self._debug['flags_reserved']['end'] = self._io.pos()
                self._io.align_to_byte()
                self._debug['maximum_size']['start'] = self._io.pos()
                self.maximum_size = self._io.read_u8le()
                self._debug['maximum_size']['end'] = self._io.pos()



    @property
    def root(self):
        if hasattr(self, '_m_root'):
            return self._m_root

        _pos = self._io.pos()
        self._io.seek(4096)
        self._debug['_m_root']['start'] = self._io.pos()
        self._m_root = AndroidSuper.Root(self._io, self, self._root)
        self._m_root._read()
        self._debug['_m_root']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_root', None)


