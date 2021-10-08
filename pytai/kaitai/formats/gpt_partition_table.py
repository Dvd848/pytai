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

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GptPartitionTable(KaitaiStruct):
    """
    .. seealso::
       Source - https://en.wikipedia.org/wiki/GUID_Partition_Table
    """
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        pass

    class PartitionEntry(KaitaiStruct):
        SEQ_FIELDS = ["type_guid", "guid", "first_lba", "last_lba", "attributes", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type_guid']['start'] = self._io.pos()
            self.type_guid = self._io.read_bytes(16)
            self._debug['type_guid']['end'] = self._io.pos()
            self._debug['guid']['start'] = self._io.pos()
            self.guid = self._io.read_bytes(16)
            self._debug['guid']['end'] = self._io.pos()
            self._debug['first_lba']['start'] = self._io.pos()
            self.first_lba = self._io.read_u8le()
            self._debug['first_lba']['end'] = self._io.pos()
            self._debug['last_lba']['start'] = self._io.pos()
            self.last_lba = self._io.read_u8le()
            self._debug['last_lba']['end'] = self._io.pos()
            self._debug['attributes']['start'] = self._io.pos()
            self.attributes = self._io.read_u8le()
            self._debug['attributes']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(72)).decode(u"UTF-16LE")
            self._debug['name']['end'] = self._io.pos()


    class PartitionHeader(KaitaiStruct):
        SEQ_FIELDS = ["signature", "revision", "header_size", "crc32_header", "reserved", "current_lba", "backup_lba", "first_usable_lba", "last_usable_lba", "disk_guid", "entries_start", "entries_count", "entries_size", "crc32_array"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(8)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x45\x46\x49\x20\x50\x41\x52\x54":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x46\x49\x20\x50\x41\x52\x54", self.signature, self._io, u"/types/partition_header/seq/0")
            self._debug['revision']['start'] = self._io.pos()
            self.revision = self._io.read_u4le()
            self._debug['revision']['end'] = self._io.pos()
            self._debug['header_size']['start'] = self._io.pos()
            self.header_size = self._io.read_u4le()
            self._debug['header_size']['end'] = self._io.pos()
            self._debug['crc32_header']['start'] = self._io.pos()
            self.crc32_header = self._io.read_u4le()
            self._debug['crc32_header']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4le()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['current_lba']['start'] = self._io.pos()
            self.current_lba = self._io.read_u8le()
            self._debug['current_lba']['end'] = self._io.pos()
            self._debug['backup_lba']['start'] = self._io.pos()
            self.backup_lba = self._io.read_u8le()
            self._debug['backup_lba']['end'] = self._io.pos()
            self._debug['first_usable_lba']['start'] = self._io.pos()
            self.first_usable_lba = self._io.read_u8le()
            self._debug['first_usable_lba']['end'] = self._io.pos()
            self._debug['last_usable_lba']['start'] = self._io.pos()
            self.last_usable_lba = self._io.read_u8le()
            self._debug['last_usable_lba']['end'] = self._io.pos()
            self._debug['disk_guid']['start'] = self._io.pos()
            self.disk_guid = self._io.read_bytes(16)
            self._debug['disk_guid']['end'] = self._io.pos()
            self._debug['entries_start']['start'] = self._io.pos()
            self.entries_start = self._io.read_u8le()
            self._debug['entries_start']['end'] = self._io.pos()
            self._debug['entries_count']['start'] = self._io.pos()
            self.entries_count = self._io.read_u4le()
            self._debug['entries_count']['end'] = self._io.pos()
            self._debug['entries_size']['start'] = self._io.pos()
            self.entries_size = self._io.read_u4le()
            self._debug['entries_size']['end'] = self._io.pos()
            self._debug['crc32_array']['start'] = self._io.pos()
            self.crc32_array = self._io.read_u4le()
            self._debug['crc32_array']['end'] = self._io.pos()

        @property
        def entries(self):
            if hasattr(self, '_m_entries'):
                return self._m_entries if hasattr(self, '_m_entries') else None

            io = self._root._io
            _pos = io.pos()
            io.seek((self.entries_start * self._root.sector_size))
            self._debug['_m_entries']['start'] = io.pos()
            self._raw__m_entries = [None] * (self.entries_count)
            self._m_entries = [None] * (self.entries_count)
            for i in range(self.entries_count):
                if not 'arr' in self._debug['_m_entries']:
                    self._debug['_m_entries']['arr'] = []
                self._debug['_m_entries']['arr'].append({'start': io.pos()})
                self._raw__m_entries[i] = io.read_bytes(self.entries_size)
                _io__raw__m_entries = KaitaiStream(BytesIO(self._raw__m_entries[i]))
                _t__m_entries = GptPartitionTable.PartitionEntry(_io__raw__m_entries, self, self._root)
                _t__m_entries._read()
                self._m_entries[i] = _t__m_entries
                self._debug['_m_entries']['arr'][i]['end'] = io.pos()

            self._debug['_m_entries']['end'] = io.pos()
            io.seek(_pos)
            return self._m_entries if hasattr(self, '_m_entries') else None


    @property
    def sector_size(self):
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size if hasattr(self, '_m_sector_size') else None

        self._m_sector_size = 512
        return self._m_sector_size if hasattr(self, '_m_sector_size') else None

    @property
    def primary(self):
        if hasattr(self, '_m_primary'):
            return self._m_primary if hasattr(self, '_m_primary') else None

        io = self._root._io
        _pos = io.pos()
        io.seek(self._root.sector_size)
        self._debug['_m_primary']['start'] = io.pos()
        self._m_primary = GptPartitionTable.PartitionHeader(io, self, self._root)
        self._m_primary._read()
        self._debug['_m_primary']['end'] = io.pos()
        io.seek(_pos)
        return self._m_primary if hasattr(self, '_m_primary') else None

    @property
    def backup(self):
        if hasattr(self, '_m_backup'):
            return self._m_backup if hasattr(self, '_m_backup') else None

        io = self._root._io
        _pos = io.pos()
        io.seek((self._io.size() - self._root.sector_size))
        self._debug['_m_backup']['start'] = io.pos()
        self._m_backup = GptPartitionTable.PartitionHeader(io, self, self._root)
        self._m_backup._read()
        self._debug['_m_backup']['end'] = io.pos()
        io.seek(_pos)
        return self._m_backup if hasattr(self, '_m_backup') else None


