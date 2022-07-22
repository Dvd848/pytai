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

class TrDosImage(KaitaiStruct):
    """.trd file is a raw dump of TR-DOS (ZX-Spectrum) floppy. .trd files are
    headerless and contain consequent "logical tracks", each logical track
    consists of 16 256-byte sectors.
    
    Logical tracks are defined the same way as used by TR-DOS: for single-side
    floppies it's just a physical track number, for two-side floppies sides are
    interleaved, i.e. logical_track_num = (physical_track_num << 1) | side
    
    So, this format definition is more for TR-DOS filesystem than for .trd files,
    which are formatless.
    
    Strings (file names, disk label, disk password) are padded with spaces and use
    ZX Spectrum character set, including UDGs, block drawing chars and Basic
    tokens. ASCII range is mostly standard ASCII, with few characters (^, `, DEL)
    replaced with (up arrow, pound, copyright symbol).
    
    .trd file can be smaller than actual floppy disk, if last logical tracks are
    empty (contain no file data) they can be omitted.
    """

    class DiskType(Enum):
        type_80_tracks_double_side = 22
        type_40_tracks_double_side = 23
        type_80_tracks_single_side = 24
        type_40_tracks_single_side = 25
    SEQ_FIELDS = ["files"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['files']['start'] = self._io.pos()
        self.files = []
        i = 0
        while True:
            if not 'arr' in self._debug['files']:
                self._debug['files']['arr'] = []
            self._debug['files']['arr'].append({'start': self._io.pos()})
            _t_files = TrDosImage.File(self._io, self, self._root)
            _t_files._read()
            _ = _t_files
            self.files.append(_)
            self._debug['files']['arr'][len(self.files) - 1]['end'] = self._io.pos()
            if _.is_terminator:
                break
            i += 1
        self._debug['files']['end'] = self._io.pos()

    class VolumeInfo(KaitaiStruct):
        SEQ_FIELDS = ["catalog_end", "unused", "first_free_sector_sector", "first_free_sector_track", "disk_type", "num_files", "num_free_sectors", "tr_dos_id", "unused_2", "password", "unused_3", "num_deleted_files", "label", "unused_4"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['catalog_end']['start'] = self._io.pos()
            self.catalog_end = self._io.read_bytes(1)
            self._debug['catalog_end']['end'] = self._io.pos()
            if not self.catalog_end == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.catalog_end, self._io, u"/types/volume_info/seq/0")
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(224)
            self._debug['unused']['end'] = self._io.pos()
            self._debug['first_free_sector_sector']['start'] = self._io.pos()
            self.first_free_sector_sector = self._io.read_u1()
            self._debug['first_free_sector_sector']['end'] = self._io.pos()
            self._debug['first_free_sector_track']['start'] = self._io.pos()
            self.first_free_sector_track = self._io.read_u1()
            self._debug['first_free_sector_track']['end'] = self._io.pos()
            self._debug['disk_type']['start'] = self._io.pos()
            self.disk_type = KaitaiStream.resolve_enum(TrDosImage.DiskType, self._io.read_u1())
            self._debug['disk_type']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u1()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['num_free_sectors']['start'] = self._io.pos()
            self.num_free_sectors = self._io.read_u2le()
            self._debug['num_free_sectors']['end'] = self._io.pos()
            self._debug['tr_dos_id']['start'] = self._io.pos()
            self.tr_dos_id = self._io.read_bytes(1)
            self._debug['tr_dos_id']['end'] = self._io.pos()
            if not self.tr_dos_id == b"\x10":
                raise kaitaistruct.ValidationNotEqualError(b"\x10", self.tr_dos_id, self._io, u"/types/volume_info/seq/7")
            self._debug['unused_2']['start'] = self._io.pos()
            self.unused_2 = self._io.read_bytes(2)
            self._debug['unused_2']['end'] = self._io.pos()
            self._debug['password']['start'] = self._io.pos()
            self.password = self._io.read_bytes(9)
            self._debug['password']['end'] = self._io.pos()
            self._debug['unused_3']['start'] = self._io.pos()
            self.unused_3 = self._io.read_bytes(1)
            self._debug['unused_3']['end'] = self._io.pos()
            self._debug['num_deleted_files']['start'] = self._io.pos()
            self.num_deleted_files = self._io.read_u1()
            self._debug['num_deleted_files']['end'] = self._io.pos()
            self._debug['label']['start'] = self._io.pos()
            self.label = self._io.read_bytes(8)
            self._debug['label']['end'] = self._io.pos()
            self._debug['unused_4']['start'] = self._io.pos()
            self.unused_4 = self._io.read_bytes(3)
            self._debug['unused_4']['end'] = self._io.pos()

        @property
        def num_tracks(self):
            if hasattr(self, '_m_num_tracks'):
                return self._m_num_tracks

            self._m_num_tracks = (40 if (self.disk_type.value & 1) != 0 else 80)
            return getattr(self, '_m_num_tracks', None)

        @property
        def num_sides(self):
            if hasattr(self, '_m_num_sides'):
                return self._m_num_sides

            self._m_num_sides = (1 if (self.disk_type.value & 8) != 0 else 2)
            return getattr(self, '_m_num_sides', None)


    class PositionAndLengthCode(KaitaiStruct):
        SEQ_FIELDS = ["start_address", "length"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['start_address']['start'] = self._io.pos()
            self.start_address = self._io.read_u2le()
            self._debug['start_address']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u2le()
            self._debug['length']['end'] = self._io.pos()


    class Filename(KaitaiStruct):
        SEQ_FIELDS = ["name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(8)
            self._debug['name']['end'] = self._io.pos()

        @property
        def first_byte(self):
            if hasattr(self, '_m_first_byte'):
                return self._m_first_byte

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_first_byte']['start'] = self._io.pos()
            self._m_first_byte = self._io.read_u1()
            self._debug['_m_first_byte']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_first_byte', None)


    class PositionAndLengthPrint(KaitaiStruct):
        SEQ_FIELDS = ["extent_no", "reserved", "length"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['extent_no']['start'] = self._io.pos()
            self.extent_no = self._io.read_u1()
            self._debug['extent_no']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u1()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u2le()
            self._debug['length']['end'] = self._io.pos()


    class PositionAndLengthGeneric(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "length"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u2le()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u2le()
            self._debug['length']['end'] = self._io.pos()


    class PositionAndLengthBasic(KaitaiStruct):
        SEQ_FIELDS = ["program_and_data_length", "program_length"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['program_and_data_length']['start'] = self._io.pos()
            self.program_and_data_length = self._io.read_u2le()
            self._debug['program_and_data_length']['end'] = self._io.pos()
            self._debug['program_length']['start'] = self._io.pos()
            self.program_length = self._io.read_u2le()
            self._debug['program_length']['end'] = self._io.pos()


    class File(KaitaiStruct):
        SEQ_FIELDS = ["name", "extension", "position_and_length", "length_sectors", "starting_sector", "starting_track"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self._raw_name = self._io.read_bytes(8)
            _io__raw_name = KaitaiStream(BytesIO(self._raw_name))
            self.name = TrDosImage.Filename(_io__raw_name, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()
            self._debug['extension']['start'] = self._io.pos()
            self.extension = self._io.read_u1()
            self._debug['extension']['end'] = self._io.pos()
            self._debug['position_and_length']['start'] = self._io.pos()
            _on = self.extension
            if _on == 66:
                self.position_and_length = TrDosImage.PositionAndLengthBasic(self._io, self, self._root)
                self.position_and_length._read()
            elif _on == 67:
                self.position_and_length = TrDosImage.PositionAndLengthCode(self._io, self, self._root)
                self.position_and_length._read()
            elif _on == 35:
                self.position_and_length = TrDosImage.PositionAndLengthPrint(self._io, self, self._root)
                self.position_and_length._read()
            else:
                self.position_and_length = TrDosImage.PositionAndLengthGeneric(self._io, self, self._root)
                self.position_and_length._read()
            self._debug['position_and_length']['end'] = self._io.pos()
            self._debug['length_sectors']['start'] = self._io.pos()
            self.length_sectors = self._io.read_u1()
            self._debug['length_sectors']['end'] = self._io.pos()
            self._debug['starting_sector']['start'] = self._io.pos()
            self.starting_sector = self._io.read_u1()
            self._debug['starting_sector']['end'] = self._io.pos()
            self._debug['starting_track']['start'] = self._io.pos()
            self.starting_track = self._io.read_u1()
            self._debug['starting_track']['end'] = self._io.pos()

        @property
        def is_deleted(self):
            if hasattr(self, '_m_is_deleted'):
                return self._m_is_deleted

            self._m_is_deleted = self.name.first_byte == 1
            return getattr(self, '_m_is_deleted', None)

        @property
        def is_terminator(self):
            if hasattr(self, '_m_is_terminator'):
                return self._m_is_terminator

            self._m_is_terminator = self.name.first_byte == 0
            return getattr(self, '_m_is_terminator', None)

        @property
        def contents(self):
            if hasattr(self, '_m_contents'):
                return self._m_contents

            _pos = self._io.pos()
            self._io.seek((((self.starting_track * 256) * 16) + (self.starting_sector * 256)))
            self._debug['_m_contents']['start'] = self._io.pos()
            self._m_contents = self._io.read_bytes((self.length_sectors * 256))
            self._debug['_m_contents']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_contents', None)


    @property
    def volume_info(self):
        if hasattr(self, '_m_volume_info'):
            return self._m_volume_info

        _pos = self._io.pos()
        self._io.seek(2048)
        self._debug['_m_volume_info']['start'] = self._io.pos()
        self._m_volume_info = TrDosImage.VolumeInfo(self._io, self, self._root)
        self._m_volume_info._read()
        self._debug['_m_volume_info']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_volume_info', None)


