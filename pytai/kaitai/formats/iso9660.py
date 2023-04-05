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

class Iso9660(KaitaiStruct):
    """ISO9660 is standard filesystem used on read-only optical discs
    (mostly CD-ROM). The standard was based on earlier High Sierra
    Format (HSF), proposed for CD-ROMs in 1985, and, after several
    revisions, it was accepted as ISO9960:1998.
    
    The format emphasizes portability (thus having pretty minimal
    features and very conservative file names standards) and sequential
    access (which favors disc devices with relatively slow rotation
    speed).
    """
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        pass

    class VolDescPrimary(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.osdev.org/ISO_9660#The_Primary_Volume_Descriptor
        """
        SEQ_FIELDS = ["unused1", "system_id", "volume_id", "unused2", "vol_space_size", "unused3", "vol_set_size", "vol_seq_num", "logical_block_size", "path_table_size", "lba_path_table_le", "lba_opt_path_table_le", "lba_path_table_be", "lba_opt_path_table_be", "root_dir", "vol_set_id", "publisher_id", "data_preparer_id", "application_id", "copyright_file_id", "abstract_file_id", "bibliographic_file_id", "vol_create_datetime", "vol_mod_datetime", "vol_expire_datetime", "vol_effective_datetime", "file_structure_version", "unused4", "application_area"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['unused1']['start'] = self._io.pos()
            self.unused1 = self._io.read_bytes(1)
            self._debug['unused1']['end'] = self._io.pos()
            if not self.unused1 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.unused1, self._io, u"/types/vol_desc_primary/seq/0")
            self._debug['system_id']['start'] = self._io.pos()
            self.system_id = (self._io.read_bytes(32)).decode(u"UTF-8")
            self._debug['system_id']['end'] = self._io.pos()
            self._debug['volume_id']['start'] = self._io.pos()
            self.volume_id = (self._io.read_bytes(32)).decode(u"UTF-8")
            self._debug['volume_id']['end'] = self._io.pos()
            self._debug['unused2']['start'] = self._io.pos()
            self.unused2 = self._io.read_bytes(8)
            self._debug['unused2']['end'] = self._io.pos()
            if not self.unused2 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.unused2, self._io, u"/types/vol_desc_primary/seq/3")
            self._debug['vol_space_size']['start'] = self._io.pos()
            self.vol_space_size = Iso9660.U4bi(self._io, self, self._root)
            self.vol_space_size._read()
            self._debug['vol_space_size']['end'] = self._io.pos()
            self._debug['unused3']['start'] = self._io.pos()
            self.unused3 = self._io.read_bytes(32)
            self._debug['unused3']['end'] = self._io.pos()
            if not self.unused3 == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.unused3, self._io, u"/types/vol_desc_primary/seq/5")
            self._debug['vol_set_size']['start'] = self._io.pos()
            self.vol_set_size = Iso9660.U2bi(self._io, self, self._root)
            self.vol_set_size._read()
            self._debug['vol_set_size']['end'] = self._io.pos()
            self._debug['vol_seq_num']['start'] = self._io.pos()
            self.vol_seq_num = Iso9660.U2bi(self._io, self, self._root)
            self.vol_seq_num._read()
            self._debug['vol_seq_num']['end'] = self._io.pos()
            self._debug['logical_block_size']['start'] = self._io.pos()
            self.logical_block_size = Iso9660.U2bi(self._io, self, self._root)
            self.logical_block_size._read()
            self._debug['logical_block_size']['end'] = self._io.pos()
            self._debug['path_table_size']['start'] = self._io.pos()
            self.path_table_size = Iso9660.U4bi(self._io, self, self._root)
            self.path_table_size._read()
            self._debug['path_table_size']['end'] = self._io.pos()
            self._debug['lba_path_table_le']['start'] = self._io.pos()
            self.lba_path_table_le = self._io.read_u4le()
            self._debug['lba_path_table_le']['end'] = self._io.pos()
            self._debug['lba_opt_path_table_le']['start'] = self._io.pos()
            self.lba_opt_path_table_le = self._io.read_u4le()
            self._debug['lba_opt_path_table_le']['end'] = self._io.pos()
            self._debug['lba_path_table_be']['start'] = self._io.pos()
            self.lba_path_table_be = self._io.read_u4be()
            self._debug['lba_path_table_be']['end'] = self._io.pos()
            self._debug['lba_opt_path_table_be']['start'] = self._io.pos()
            self.lba_opt_path_table_be = self._io.read_u4be()
            self._debug['lba_opt_path_table_be']['end'] = self._io.pos()
            self._debug['root_dir']['start'] = self._io.pos()
            self._raw_root_dir = self._io.read_bytes(34)
            _io__raw_root_dir = KaitaiStream(BytesIO(self._raw_root_dir))
            self.root_dir = Iso9660.DirEntry(_io__raw_root_dir, self, self._root)
            self.root_dir._read()
            self._debug['root_dir']['end'] = self._io.pos()
            self._debug['vol_set_id']['start'] = self._io.pos()
            self.vol_set_id = (self._io.read_bytes(128)).decode(u"UTF-8")
            self._debug['vol_set_id']['end'] = self._io.pos()
            self._debug['publisher_id']['start'] = self._io.pos()
            self.publisher_id = (self._io.read_bytes(128)).decode(u"UTF-8")
            self._debug['publisher_id']['end'] = self._io.pos()
            self._debug['data_preparer_id']['start'] = self._io.pos()
            self.data_preparer_id = (self._io.read_bytes(128)).decode(u"UTF-8")
            self._debug['data_preparer_id']['end'] = self._io.pos()
            self._debug['application_id']['start'] = self._io.pos()
            self.application_id = (self._io.read_bytes(128)).decode(u"UTF-8")
            self._debug['application_id']['end'] = self._io.pos()
            self._debug['copyright_file_id']['start'] = self._io.pos()
            self.copyright_file_id = (self._io.read_bytes(38)).decode(u"UTF-8")
            self._debug['copyright_file_id']['end'] = self._io.pos()
            self._debug['abstract_file_id']['start'] = self._io.pos()
            self.abstract_file_id = (self._io.read_bytes(36)).decode(u"UTF-8")
            self._debug['abstract_file_id']['end'] = self._io.pos()
            self._debug['bibliographic_file_id']['start'] = self._io.pos()
            self.bibliographic_file_id = (self._io.read_bytes(37)).decode(u"UTF-8")
            self._debug['bibliographic_file_id']['end'] = self._io.pos()
            self._debug['vol_create_datetime']['start'] = self._io.pos()
            self.vol_create_datetime = Iso9660.DecDatetime(self._io, self, self._root)
            self.vol_create_datetime._read()
            self._debug['vol_create_datetime']['end'] = self._io.pos()
            self._debug['vol_mod_datetime']['start'] = self._io.pos()
            self.vol_mod_datetime = Iso9660.DecDatetime(self._io, self, self._root)
            self.vol_mod_datetime._read()
            self._debug['vol_mod_datetime']['end'] = self._io.pos()
            self._debug['vol_expire_datetime']['start'] = self._io.pos()
            self.vol_expire_datetime = Iso9660.DecDatetime(self._io, self, self._root)
            self.vol_expire_datetime._read()
            self._debug['vol_expire_datetime']['end'] = self._io.pos()
            self._debug['vol_effective_datetime']['start'] = self._io.pos()
            self.vol_effective_datetime = Iso9660.DecDatetime(self._io, self, self._root)
            self.vol_effective_datetime._read()
            self._debug['vol_effective_datetime']['end'] = self._io.pos()
            self._debug['file_structure_version']['start'] = self._io.pos()
            self.file_structure_version = self._io.read_u1()
            self._debug['file_structure_version']['end'] = self._io.pos()
            self._debug['unused4']['start'] = self._io.pos()
            self.unused4 = self._io.read_u1()
            self._debug['unused4']['end'] = self._io.pos()
            self._debug['application_area']['start'] = self._io.pos()
            self.application_area = self._io.read_bytes(512)
            self._debug['application_area']['end'] = self._io.pos()

        @property
        def path_table(self):
            if hasattr(self, '_m_path_table'):
                return self._m_path_table

            _pos = self._io.pos()
            self._io.seek((self.lba_path_table_le * self._root.sector_size))
            self._debug['_m_path_table']['start'] = self._io.pos()
            self._raw__m_path_table = self._io.read_bytes(self.path_table_size.le)
            _io__raw__m_path_table = KaitaiStream(BytesIO(self._raw__m_path_table))
            self._m_path_table = Iso9660.PathTableLe(_io__raw__m_path_table, self, self._root)
            self._m_path_table._read()
            self._debug['_m_path_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_path_table', None)


    class VolDescBootRecord(KaitaiStruct):
        SEQ_FIELDS = ["boot_system_id", "boot_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['boot_system_id']['start'] = self._io.pos()
            self.boot_system_id = (self._io.read_bytes(32)).decode(u"UTF-8")
            self._debug['boot_system_id']['end'] = self._io.pos()
            self._debug['boot_id']['start'] = self._io.pos()
            self.boot_id = (self._io.read_bytes(32)).decode(u"UTF-8")
            self._debug['boot_id']['end'] = self._io.pos()


    class Datetime(KaitaiStruct):
        SEQ_FIELDS = ["year", "month", "day", "hour", "minute", "sec", "timezone"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['year']['start'] = self._io.pos()
            self.year = self._io.read_u1()
            self._debug['year']['end'] = self._io.pos()
            self._debug['month']['start'] = self._io.pos()
            self.month = self._io.read_u1()
            self._debug['month']['end'] = self._io.pos()
            self._debug['day']['start'] = self._io.pos()
            self.day = self._io.read_u1()
            self._debug['day']['end'] = self._io.pos()
            self._debug['hour']['start'] = self._io.pos()
            self.hour = self._io.read_u1()
            self._debug['hour']['end'] = self._io.pos()
            self._debug['minute']['start'] = self._io.pos()
            self.minute = self._io.read_u1()
            self._debug['minute']['end'] = self._io.pos()
            self._debug['sec']['start'] = self._io.pos()
            self.sec = self._io.read_u1()
            self._debug['sec']['end'] = self._io.pos()
            self._debug['timezone']['start'] = self._io.pos()
            self.timezone = self._io.read_u1()
            self._debug['timezone']['end'] = self._io.pos()


    class DirEntry(KaitaiStruct):
        SEQ_FIELDS = ["len", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u1()
            self._debug['len']['end'] = self._io.pos()
            if self.len > 0:
                self._debug['body']['start'] = self._io.pos()
                self._raw_body = self._io.read_bytes((self.len - 1))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Iso9660.DirEntryBody(_io__raw_body, self, self._root)
                self.body._read()
                self._debug['body']['end'] = self._io.pos()



    class VolDesc(KaitaiStruct):
        SEQ_FIELDS = ["type", "magic", "version", "vol_desc_boot_record", "vol_desc_primary"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u1()
            self._debug['type']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(5)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x43\x44\x30\x30\x31":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x44\x30\x30\x31", self.magic, self._io, u"/types/vol_desc/seq/1")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            if self.type == 0:
                self._debug['vol_desc_boot_record']['start'] = self._io.pos()
                self.vol_desc_boot_record = Iso9660.VolDescBootRecord(self._io, self, self._root)
                self.vol_desc_boot_record._read()
                self._debug['vol_desc_boot_record']['end'] = self._io.pos()

            if self.type == 1:
                self._debug['vol_desc_primary']['start'] = self._io.pos()
                self.vol_desc_primary = Iso9660.VolDescPrimary(self._io, self, self._root)
                self.vol_desc_primary._read()
                self._debug['vol_desc_primary']['end'] = self._io.pos()



    class PathTableEntryLe(KaitaiStruct):
        SEQ_FIELDS = ["len_dir_name", "len_ext_attr_rec", "lba_extent", "parent_dir_idx", "dir_name", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_dir_name']['start'] = self._io.pos()
            self.len_dir_name = self._io.read_u1()
            self._debug['len_dir_name']['end'] = self._io.pos()
            self._debug['len_ext_attr_rec']['start'] = self._io.pos()
            self.len_ext_attr_rec = self._io.read_u1()
            self._debug['len_ext_attr_rec']['end'] = self._io.pos()
            self._debug['lba_extent']['start'] = self._io.pos()
            self.lba_extent = self._io.read_u4le()
            self._debug['lba_extent']['end'] = self._io.pos()
            self._debug['parent_dir_idx']['start'] = self._io.pos()
            self.parent_dir_idx = self._io.read_u2le()
            self._debug['parent_dir_idx']['end'] = self._io.pos()
            self._debug['dir_name']['start'] = self._io.pos()
            self.dir_name = (self._io.read_bytes(self.len_dir_name)).decode(u"UTF-8")
            self._debug['dir_name']['end'] = self._io.pos()
            if (self.len_dir_name % 2) == 1:
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_u1()
                self._debug['padding']['end'] = self._io.pos()



    class DirEntries(KaitaiStruct):
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
            while True:
                if not 'arr' in self._debug['entries']:
                    self._debug['entries']['arr'] = []
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _t_entries = Iso9660.DirEntry(self._io, self, self._root)
                _t_entries._read()
                _ = _t_entries
                self.entries.append(_)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                if _.len == 0:
                    break
                i += 1
            self._debug['entries']['end'] = self._io.pos()


    class U4bi(KaitaiStruct):
        SEQ_FIELDS = ["le", "be"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['le']['start'] = self._io.pos()
            self.le = self._io.read_u4le()
            self._debug['le']['end'] = self._io.pos()
            self._debug['be']['start'] = self._io.pos()
            self.be = self._io.read_u4be()
            self._debug['be']['end'] = self._io.pos()


    class U2bi(KaitaiStruct):
        SEQ_FIELDS = ["le", "be"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['le']['start'] = self._io.pos()
            self.le = self._io.read_u2le()
            self._debug['le']['end'] = self._io.pos()
            self._debug['be']['start'] = self._io.pos()
            self.be = self._io.read_u2be()
            self._debug['be']['end'] = self._io.pos()


    class PathTableLe(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.osdev.org/ISO_9660#The_Path_Table
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
                _t_entries = Iso9660.PathTableEntryLe(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class DecDatetime(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.osdev.org/ISO_9660#Date.2Ftime_format
        """
        SEQ_FIELDS = ["year", "month", "day", "hour", "minute", "sec", "sec_hundreds", "timezone"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['year']['start'] = self._io.pos()
            self.year = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['year']['end'] = self._io.pos()
            self._debug['month']['start'] = self._io.pos()
            self.month = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['month']['end'] = self._io.pos()
            self._debug['day']['start'] = self._io.pos()
            self.day = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['day']['end'] = self._io.pos()
            self._debug['hour']['start'] = self._io.pos()
            self.hour = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['hour']['end'] = self._io.pos()
            self._debug['minute']['start'] = self._io.pos()
            self.minute = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['minute']['end'] = self._io.pos()
            self._debug['sec']['start'] = self._io.pos()
            self.sec = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['sec']['end'] = self._io.pos()
            self._debug['sec_hundreds']['start'] = self._io.pos()
            self.sec_hundreds = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['sec_hundreds']['end'] = self._io.pos()
            self._debug['timezone']['start'] = self._io.pos()
            self.timezone = self._io.read_u1()
            self._debug['timezone']['end'] = self._io.pos()


    class DirEntryBody(KaitaiStruct):
        SEQ_FIELDS = ["len_ext_attr_rec", "lba_extent", "size_extent", "datetime", "file_flags", "file_unit_size", "interleave_gap_size", "vol_seq_num", "len_file_name", "file_name", "padding", "rest"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_ext_attr_rec']['start'] = self._io.pos()
            self.len_ext_attr_rec = self._io.read_u1()
            self._debug['len_ext_attr_rec']['end'] = self._io.pos()
            self._debug['lba_extent']['start'] = self._io.pos()
            self.lba_extent = Iso9660.U4bi(self._io, self, self._root)
            self.lba_extent._read()
            self._debug['lba_extent']['end'] = self._io.pos()
            self._debug['size_extent']['start'] = self._io.pos()
            self.size_extent = Iso9660.U4bi(self._io, self, self._root)
            self.size_extent._read()
            self._debug['size_extent']['end'] = self._io.pos()
            self._debug['datetime']['start'] = self._io.pos()
            self.datetime = Iso9660.Datetime(self._io, self, self._root)
            self.datetime._read()
            self._debug['datetime']['end'] = self._io.pos()
            self._debug['file_flags']['start'] = self._io.pos()
            self.file_flags = self._io.read_u1()
            self._debug['file_flags']['end'] = self._io.pos()
            self._debug['file_unit_size']['start'] = self._io.pos()
            self.file_unit_size = self._io.read_u1()
            self._debug['file_unit_size']['end'] = self._io.pos()
            self._debug['interleave_gap_size']['start'] = self._io.pos()
            self.interleave_gap_size = self._io.read_u1()
            self._debug['interleave_gap_size']['end'] = self._io.pos()
            self._debug['vol_seq_num']['start'] = self._io.pos()
            self.vol_seq_num = Iso9660.U2bi(self._io, self, self._root)
            self.vol_seq_num._read()
            self._debug['vol_seq_num']['end'] = self._io.pos()
            self._debug['len_file_name']['start'] = self._io.pos()
            self.len_file_name = self._io.read_u1()
            self._debug['len_file_name']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = (self._io.read_bytes(self.len_file_name)).decode(u"UTF-8")
            self._debug['file_name']['end'] = self._io.pos()
            if (self.len_file_name % 2) == 0:
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_u1()
                self._debug['padding']['end'] = self._io.pos()

            self._debug['rest']['start'] = self._io.pos()
            self.rest = self._io.read_bytes_full()
            self._debug['rest']['end'] = self._io.pos()

        @property
        def extent_as_dir(self):
            if hasattr(self, '_m_extent_as_dir'):
                return self._m_extent_as_dir

            if (self.file_flags & 2) != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek((self.lba_extent.le * self._root.sector_size))
                self._debug['_m_extent_as_dir']['start'] = io.pos()
                self._raw__m_extent_as_dir = io.read_bytes(self.size_extent.le)
                _io__raw__m_extent_as_dir = KaitaiStream(BytesIO(self._raw__m_extent_as_dir))
                self._m_extent_as_dir = Iso9660.DirEntries(_io__raw__m_extent_as_dir, self, self._root)
                self._m_extent_as_dir._read()
                self._debug['_m_extent_as_dir']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_extent_as_dir', None)

        @property
        def extent_as_file(self):
            if hasattr(self, '_m_extent_as_file'):
                return self._m_extent_as_file

            if (self.file_flags & 2) == 0:
                io = self._root._io
                _pos = io.pos()
                io.seek((self.lba_extent.le * self._root.sector_size))
                self._debug['_m_extent_as_file']['start'] = io.pos()
                self._m_extent_as_file = io.read_bytes(self.size_extent.le)
                self._debug['_m_extent_as_file']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_extent_as_file', None)


    @property
    def sector_size(self):
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size

        self._m_sector_size = 2048
        return getattr(self, '_m_sector_size', None)

    @property
    def primary_vol_desc(self):
        if hasattr(self, '_m_primary_vol_desc'):
            return self._m_primary_vol_desc

        _pos = self._io.pos()
        self._io.seek((16 * self.sector_size))
        self._debug['_m_primary_vol_desc']['start'] = self._io.pos()
        self._m_primary_vol_desc = Iso9660.VolDesc(self._io, self, self._root)
        self._m_primary_vol_desc._read()
        self._debug['_m_primary_vol_desc']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_primary_vol_desc', None)


