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

class CpioOldLe(KaitaiStruct):
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
        while not self._io.is_eof():
            if not 'arr' in self._debug['files']:
                self._debug['files']['arr'] = []
            self._debug['files']['arr'].append({'start': self._io.pos()})
            _t_files = CpioOldLe.File(self._io, self, self._root)
            _t_files._read()
            self.files.append(_t_files)
            self._debug['files']['arr'][len(self.files) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['files']['end'] = self._io.pos()

    class File(KaitaiStruct):
        SEQ_FIELDS = ["header", "path_name", "string_terminator", "path_name_padding", "file_data", "file_data_padding", "end_of_file_padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = CpioOldLe.FileHeader(self._io, self, self._root)
            self.header._read()
            self._debug['header']['end'] = self._io.pos()
            self._debug['path_name']['start'] = self._io.pos()
            self.path_name = self._io.read_bytes((self.header.path_name_size - 1))
            self._debug['path_name']['end'] = self._io.pos()
            self._debug['string_terminator']['start'] = self._io.pos()
            self.string_terminator = self._io.read_bytes(1)
            self._debug['string_terminator']['end'] = self._io.pos()
            if not self.string_terminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.string_terminator, self._io, u"/types/file/seq/2")
            if (self.header.path_name_size % 2) == 1:
                self._debug['path_name_padding']['start'] = self._io.pos()
                self.path_name_padding = self._io.read_bytes(1)
                self._debug['path_name_padding']['end'] = self._io.pos()
                if not self.path_name_padding == b"\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00", self.path_name_padding, self._io, u"/types/file/seq/3")

            self._debug['file_data']['start'] = self._io.pos()
            self.file_data = self._io.read_bytes(self.header.file_size.value)
            self._debug['file_data']['end'] = self._io.pos()
            if (self.header.file_size.value % 2) == 1:
                self._debug['file_data_padding']['start'] = self._io.pos()
                self.file_data_padding = self._io.read_bytes(1)
                self._debug['file_data_padding']['end'] = self._io.pos()
                if not self.file_data_padding == b"\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00", self.file_data_padding, self._io, u"/types/file/seq/5")

            if  ((self.path_name == b"\x54\x52\x41\x49\x4C\x45\x52\x21\x21\x21") and (self.header.file_size.value == 0)) :
                self._debug['end_of_file_padding']['start'] = self._io.pos()
                self.end_of_file_padding = self._io.read_bytes_full()
                self._debug['end_of_file_padding']['end'] = self._io.pos()



    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "device_number", "inode_number", "mode", "user_id", "group_id", "number_of_links", "r_device_number", "modification_time", "path_name_size", "file_size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xC7\x71":
                raise kaitaistruct.ValidationNotEqualError(b"\xC7\x71", self.magic, self._io, u"/types/file_header/seq/0")
            self._debug['device_number']['start'] = self._io.pos()
            self.device_number = self._io.read_u2le()
            self._debug['device_number']['end'] = self._io.pos()
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u2le()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u2le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['user_id']['start'] = self._io.pos()
            self.user_id = self._io.read_u2le()
            self._debug['user_id']['end'] = self._io.pos()
            self._debug['group_id']['start'] = self._io.pos()
            self.group_id = self._io.read_u2le()
            self._debug['group_id']['end'] = self._io.pos()
            self._debug['number_of_links']['start'] = self._io.pos()
            self.number_of_links = self._io.read_u2le()
            self._debug['number_of_links']['end'] = self._io.pos()
            self._debug['r_device_number']['start'] = self._io.pos()
            self.r_device_number = self._io.read_u2le()
            self._debug['r_device_number']['end'] = self._io.pos()
            self._debug['modification_time']['start'] = self._io.pos()
            self.modification_time = CpioOldLe.FourByteUnsignedInteger(self._io, self, self._root)
            self.modification_time._read()
            self._debug['modification_time']['end'] = self._io.pos()
            self._debug['path_name_size']['start'] = self._io.pos()
            self.path_name_size = self._io.read_u2le()
            self._debug['path_name_size']['end'] = self._io.pos()
            self._debug['file_size']['start'] = self._io.pos()
            self.file_size = CpioOldLe.FourByteUnsignedInteger(self._io, self, self._root)
            self.file_size._read()
            self._debug['file_size']['end'] = self._io.pos()


    class FourByteUnsignedInteger(KaitaiStruct):
        SEQ_FIELDS = ["most_significant_bits", "least_significant_bits"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['most_significant_bits']['start'] = self._io.pos()
            self.most_significant_bits = self._io.read_u2le()
            self._debug['most_significant_bits']['end'] = self._io.pos()
            self._debug['least_significant_bits']['start'] = self._io.pos()
            self.least_significant_bits = self._io.read_u2le()
            self._debug['least_significant_bits']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.least_significant_bits + (self.most_significant_bits << 16))
            return getattr(self, '_m_value', None)



