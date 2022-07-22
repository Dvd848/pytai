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

class FalloutDat(KaitaiStruct):

    class Compression(Enum):
        none = 32
        lzss = 64
    SEQ_FIELDS = ["folder_count", "unknown1", "unknown2", "timestamp", "folder_names", "folders"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['folder_count']['start'] = self._io.pos()
        self.folder_count = self._io.read_u4be()
        self._debug['folder_count']['end'] = self._io.pos()
        self._debug['unknown1']['start'] = self._io.pos()
        self.unknown1 = self._io.read_u4be()
        self._debug['unknown1']['end'] = self._io.pos()
        self._debug['unknown2']['start'] = self._io.pos()
        self.unknown2 = self._io.read_u4be()
        self._debug['unknown2']['end'] = self._io.pos()
        self._debug['timestamp']['start'] = self._io.pos()
        self.timestamp = self._io.read_u4be()
        self._debug['timestamp']['end'] = self._io.pos()
        self._debug['folder_names']['start'] = self._io.pos()
        self.folder_names = []
        for i in range(self.folder_count):
            if not 'arr' in self._debug['folder_names']:
                self._debug['folder_names']['arr'] = []
            self._debug['folder_names']['arr'].append({'start': self._io.pos()})
            _t_folder_names = FalloutDat.Pstr(self._io, self, self._root)
            _t_folder_names._read()
            self.folder_names.append(_t_folder_names)
            self._debug['folder_names']['arr'][i]['end'] = self._io.pos()

        self._debug['folder_names']['end'] = self._io.pos()
        self._debug['folders']['start'] = self._io.pos()
        self.folders = []
        for i in range(self.folder_count):
            if not 'arr' in self._debug['folders']:
                self._debug['folders']['arr'] = []
            self._debug['folders']['arr'].append({'start': self._io.pos()})
            _t_folders = FalloutDat.Folder(self._io, self, self._root)
            _t_folders._read()
            self.folders.append(_t_folders)
            self._debug['folders']['arr'][i]['end'] = self._io.pos()

        self._debug['folders']['end'] = self._io.pos()

    class Pstr(KaitaiStruct):
        SEQ_FIELDS = ["size", "str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u1()
            self._debug['size']['end'] = self._io.pos()
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes(self.size)).decode(u"ASCII")
            self._debug['str']['end'] = self._io.pos()


    class Folder(KaitaiStruct):
        SEQ_FIELDS = ["file_count", "unknown", "flags", "timestamp", "files"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['file_count']['start'] = self._io.pos()
            self.file_count = self._io.read_u4be()
            self._debug['file_count']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_u4be()
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_u4be()
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['files']['start'] = self._io.pos()
            self.files = []
            for i in range(self.file_count):
                if not 'arr' in self._debug['files']:
                    self._debug['files']['arr'] = []
                self._debug['files']['arr'].append({'start': self._io.pos()})
                _t_files = FalloutDat.File(self._io, self, self._root)
                _t_files._read()
                self.files.append(_t_files)
                self._debug['files']['arr'][i]['end'] = self._io.pos()

            self._debug['files']['end'] = self._io.pos()


    class File(KaitaiStruct):
        SEQ_FIELDS = ["name", "flags", "offset", "size_unpacked", "size_packed"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = FalloutDat.Pstr(self._io, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(FalloutDat.Compression, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4be()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['size_unpacked']['start'] = self._io.pos()
            self.size_unpacked = self._io.read_u4be()
            self._debug['size_unpacked']['end'] = self._io.pos()
            self._debug['size_packed']['start'] = self._io.pos()
            self.size_packed = self._io.read_u4be()
            self._debug['size_packed']['end'] = self._io.pos()

        @property
        def contents(self):
            if hasattr(self, '_m_contents'):
                return self._m_contents

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._debug['_m_contents']['start'] = io.pos()
            self._m_contents = io.read_bytes((self.size_unpacked if self.flags == FalloutDat.Compression.none else self.size_packed))
            self._debug['_m_contents']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_contents', None)



