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

class ApmPartitionTable(KaitaiStruct):
    """
    .. seealso::
       Source - https://en.wikipedia.org/wiki/Apple_Partition_Map
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
        SEQ_FIELDS = ["magic", "reserved_1", "number_of_partitions", "partition_start", "partition_size", "partition_name", "partition_type", "data_start", "data_size", "partition_status", "boot_code_start", "boot_code_size", "boot_loader_address", "reserved_2", "boot_code_entry", "reserved_3", "boot_code_cksum", "processor_type"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x50\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x4D", self.magic, self._io, u"/types/partition_entry/seq/0")
            self._debug['reserved_1']['start'] = self._io.pos()
            self.reserved_1 = self._io.read_bytes(2)
            self._debug['reserved_1']['end'] = self._io.pos()
            self._debug['number_of_partitions']['start'] = self._io.pos()
            self.number_of_partitions = self._io.read_u4be()
            self._debug['number_of_partitions']['end'] = self._io.pos()
            self._debug['partition_start']['start'] = self._io.pos()
            self.partition_start = self._io.read_u4be()
            self._debug['partition_start']['end'] = self._io.pos()
            self._debug['partition_size']['start'] = self._io.pos()
            self.partition_size = self._io.read_u4be()
            self._debug['partition_size']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['partition_type']['start'] = self._io.pos()
            self.partition_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self._debug['partition_type']['end'] = self._io.pos()
            self._debug['data_start']['start'] = self._io.pos()
            self.data_start = self._io.read_u4be()
            self._debug['data_start']['end'] = self._io.pos()
            self._debug['data_size']['start'] = self._io.pos()
            self.data_size = self._io.read_u4be()
            self._debug['data_size']['end'] = self._io.pos()
            self._debug['partition_status']['start'] = self._io.pos()
            self.partition_status = self._io.read_u4be()
            self._debug['partition_status']['end'] = self._io.pos()
            self._debug['boot_code_start']['start'] = self._io.pos()
            self.boot_code_start = self._io.read_u4be()
            self._debug['boot_code_start']['end'] = self._io.pos()
            self._debug['boot_code_size']['start'] = self._io.pos()
            self.boot_code_size = self._io.read_u4be()
            self._debug['boot_code_size']['end'] = self._io.pos()
            self._debug['boot_loader_address']['start'] = self._io.pos()
            self.boot_loader_address = self._io.read_u4be()
            self._debug['boot_loader_address']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_bytes(4)
            self._debug['reserved_2']['end'] = self._io.pos()
            self._debug['boot_code_entry']['start'] = self._io.pos()
            self.boot_code_entry = self._io.read_u4be()
            self._debug['boot_code_entry']['end'] = self._io.pos()
            self._debug['reserved_3']['start'] = self._io.pos()
            self.reserved_3 = self._io.read_bytes(4)
            self._debug['reserved_3']['end'] = self._io.pos()
            self._debug['boot_code_cksum']['start'] = self._io.pos()
            self.boot_code_cksum = self._io.read_u4be()
            self._debug['boot_code_cksum']['end'] = self._io.pos()
            self._debug['processor_type']['start'] = self._io.pos()
            self.processor_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ascii")
            self._debug['processor_type']['end'] = self._io.pos()

        @property
        def partition(self):
            if hasattr(self, '_m_partition'):
                return self._m_partition

            if (self.partition_status & 1) != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek((self.partition_start * self._root.sector_size))
                self._debug['_m_partition']['start'] = io.pos()
                self._m_partition = io.read_bytes((self.partition_size * self._root.sector_size))
                self._debug['_m_partition']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_partition', None)

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek((self.data_start * self._root.sector_size))
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes((self.data_size * self._root.sector_size))
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)

        @property
        def boot_code(self):
            if hasattr(self, '_m_boot_code'):
                return self._m_boot_code

            io = self._root._io
            _pos = io.pos()
            io.seek((self.boot_code_start * self._root.sector_size))
            self._debug['_m_boot_code']['start'] = io.pos()
            self._m_boot_code = io.read_bytes(self.boot_code_size)
            self._debug['_m_boot_code']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_boot_code', None)


    @property
    def sector_size(self):
        """0x200 (512) bytes for disks, 0x1000 (4096) bytes is not supported by APM
        0x800 (2048) bytes for CDROM
        """
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size

        self._m_sector_size = 512
        return getattr(self, '_m_sector_size', None)

    @property
    def partition_lookup(self):
        """Every partition entry contains the number of partition entries.
        We parse the first entry, to know how many to parse, including the first one.
        No logic is given what to do if other entries have a different number.
        """
        if hasattr(self, '_m_partition_lookup'):
            return self._m_partition_lookup

        io = self._root._io
        _pos = io.pos()
        io.seek(self._root.sector_size)
        self._debug['_m_partition_lookup']['start'] = io.pos()
        self._raw__m_partition_lookup = io.read_bytes(self.sector_size)
        _io__raw__m_partition_lookup = KaitaiStream(BytesIO(self._raw__m_partition_lookup))
        self._m_partition_lookup = ApmPartitionTable.PartitionEntry(_io__raw__m_partition_lookup, self, self._root)
        self._m_partition_lookup._read()
        self._debug['_m_partition_lookup']['end'] = io.pos()
        io.seek(_pos)
        return getattr(self, '_m_partition_lookup', None)

    @property
    def partition_entries(self):
        if hasattr(self, '_m_partition_entries'):
            return self._m_partition_entries

        io = self._root._io
        _pos = io.pos()
        io.seek(self._root.sector_size)
        self._debug['_m_partition_entries']['start'] = io.pos()
        self._raw__m_partition_entries = []
        self._m_partition_entries = []
        for i in range(self._root.partition_lookup.number_of_partitions):
            if not 'arr' in self._debug['_m_partition_entries']:
                self._debug['_m_partition_entries']['arr'] = []
            self._debug['_m_partition_entries']['arr'].append({'start': io.pos()})
            self._raw__m_partition_entries.append(io.read_bytes(self.sector_size))
            _io__raw__m_partition_entries = KaitaiStream(BytesIO(self._raw__m_partition_entries[i]))
            _t__m_partition_entries = ApmPartitionTable.PartitionEntry(_io__raw__m_partition_entries, self, self._root)
            _t__m_partition_entries._read()
            self._m_partition_entries.append(_t__m_partition_entries)
            self._debug['_m_partition_entries']['arr'][i]['end'] = io.pos()

        self._debug['_m_partition_entries']['end'] = io.pos()
        io.seek(_pos)
        return getattr(self, '_m_partition_entries', None)


