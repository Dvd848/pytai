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

class UefiTe(KaitaiStruct):
    """This type of executables could be found inside the UEFI firmware. The UEFI
    firmware is stored in SPI flash memory, which is a chip soldered on a
    system's motherboard. UEFI firmware is very modular: it usually contains
    dozens, if not hundreds, of executables. To store all these separates files,
    the firmware is laid out in volumes using the Firmware File System (FFS), a
    file system specifically designed to store firmware images. The volumes
    contain files that are identified by GUIDs and each of these files contain
    one or more sections holding the data. One of these sections contains the
    actual executable image. Most of the executable images follow the PE format.
    However, some of them follow the TE format.
    
    The Terse Executable (TE) image format was created as a mechanism to reduce
    the overhead of the PE/COFF headers in PE32/PE32+ images, resulting in a
    corresponding reduction of image sizes for executables running in the PI
    (Platform Initialization) Architecture environment. Reducing image size
    provides an opportunity for use of a smaller system flash part.
    
    So the TE format is basically a stripped version of PE.
    
    .. seealso::
       Source - https://uefi.org/sites/default/files/resources/PI_Spec_1_6.pdf
    """
    SEQ_FIELDS = ["te_hdr", "sections"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['te_hdr']['start'] = self._io.pos()
        self._raw_te_hdr = self._io.read_bytes(40)
        _io__raw_te_hdr = KaitaiStream(BytesIO(self._raw_te_hdr))
        self.te_hdr = UefiTe.TeHeader(_io__raw_te_hdr, self, self._root)
        self.te_hdr._read()
        self._debug['te_hdr']['end'] = self._io.pos()
        self._debug['sections']['start'] = self._io.pos()
        self.sections = []
        for i in range(self.te_hdr.num_sections):
            if not 'arr' in self._debug['sections']:
                self._debug['sections']['arr'] = []
            self._debug['sections']['arr'].append({'start': self._io.pos()})
            _t_sections = UefiTe.Section(self._io, self, self._root)
            _t_sections._read()
            self.sections.append(_t_sections)
            self._debug['sections']['arr'][i]['end'] = self._io.pos()

        self._debug['sections']['end'] = self._io.pos()

    class TeHeader(KaitaiStruct):

        class MachineType(Enum):
            unknown = 0
            i386 = 332
            r4000 = 358
            wce_mips_v2 = 361
            alpha = 388
            sh3 = 418
            sh3_dsp = 419
            sh4 = 422
            sh5 = 424
            arm = 448
            thumb = 450
            arm_nt = 452
            am33 = 467
            powerpc = 496
            powerpc_fp = 497
            ia64 = 512
            mips16 = 614
            alpha64_or_axp64 = 644
            mips_fpu = 870
            mips16_fpu = 1126
            ebc = 3772
            riscv32 = 20530
            riscv64 = 20580
            riscv128 = 20776
            loongarch32 = 25138
            loongarch64 = 25188
            amd64 = 34404
            m32r = 36929
            arm64 = 43620

        class SubsystemEnum(Enum):
            unknown = 0
            native = 1
            windows_gui = 2
            windows_cui = 3
            posix_cui = 7
            windows_ce_gui = 9
            efi_application = 10
            efi_boot_service_driver = 11
            efi_runtime_driver = 12
            efi_rom = 13
            xbox = 14
            windows_boot_application = 16
        SEQ_FIELDS = ["magic", "machine", "num_sections", "subsystem", "stripped_size", "entry_point_addr", "base_of_code", "image_base", "data_dirs"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x56\x5A":
                raise kaitaistruct.ValidationNotEqualError(b"\x56\x5A", self.magic, self._io, u"/types/te_header/seq/0")
            self._debug['machine']['start'] = self._io.pos()
            self.machine = KaitaiStream.resolve_enum(UefiTe.TeHeader.MachineType, self._io.read_u2le())
            self._debug['machine']['end'] = self._io.pos()
            self._debug['num_sections']['start'] = self._io.pos()
            self.num_sections = self._io.read_u1()
            self._debug['num_sections']['end'] = self._io.pos()
            self._debug['subsystem']['start'] = self._io.pos()
            self.subsystem = KaitaiStream.resolve_enum(UefiTe.TeHeader.SubsystemEnum, self._io.read_u1())
            self._debug['subsystem']['end'] = self._io.pos()
            self._debug['stripped_size']['start'] = self._io.pos()
            self.stripped_size = self._io.read_u2le()
            self._debug['stripped_size']['end'] = self._io.pos()
            self._debug['entry_point_addr']['start'] = self._io.pos()
            self.entry_point_addr = self._io.read_u4le()
            self._debug['entry_point_addr']['end'] = self._io.pos()
            self._debug['base_of_code']['start'] = self._io.pos()
            self.base_of_code = self._io.read_u4le()
            self._debug['base_of_code']['end'] = self._io.pos()
            self._debug['image_base']['start'] = self._io.pos()
            self.image_base = self._io.read_u8le()
            self._debug['image_base']['end'] = self._io.pos()
            self._debug['data_dirs']['start'] = self._io.pos()
            self.data_dirs = UefiTe.HeaderDataDirs(self._io, self, self._root)
            self.data_dirs._read()
            self._debug['data_dirs']['end'] = self._io.pos()


    class HeaderDataDirs(KaitaiStruct):
        SEQ_FIELDS = ["base_relocation_table", "debug"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['base_relocation_table']['start'] = self._io.pos()
            self.base_relocation_table = UefiTe.DataDir(self._io, self, self._root)
            self.base_relocation_table._read()
            self._debug['base_relocation_table']['end'] = self._io.pos()
            self._debug['debug']['start'] = self._io.pos()
            self.debug = UefiTe.DataDir(self._io, self, self._root)
            self.debug._read()
            self._debug['debug']['end'] = self._io.pos()


    class DataDir(KaitaiStruct):
        SEQ_FIELDS = ["virtual_address", "size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['virtual_address']['start'] = self._io.pos()
            self.virtual_address = self._io.read_u4le()
            self._debug['virtual_address']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()


    class Section(KaitaiStruct):
        SEQ_FIELDS = ["name", "virtual_size", "virtual_address", "size_of_raw_data", "pointer_to_raw_data", "pointer_to_relocations", "pointer_to_linenumbers", "num_relocations", "num_linenumbers", "characteristics"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 0)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['virtual_size']['start'] = self._io.pos()
            self.virtual_size = self._io.read_u4le()
            self._debug['virtual_size']['end'] = self._io.pos()
            self._debug['virtual_address']['start'] = self._io.pos()
            self.virtual_address = self._io.read_u4le()
            self._debug['virtual_address']['end'] = self._io.pos()
            self._debug['size_of_raw_data']['start'] = self._io.pos()
            self.size_of_raw_data = self._io.read_u4le()
            self._debug['size_of_raw_data']['end'] = self._io.pos()
            self._debug['pointer_to_raw_data']['start'] = self._io.pos()
            self.pointer_to_raw_data = self._io.read_u4le()
            self._debug['pointer_to_raw_data']['end'] = self._io.pos()
            self._debug['pointer_to_relocations']['start'] = self._io.pos()
            self.pointer_to_relocations = self._io.read_u4le()
            self._debug['pointer_to_relocations']['end'] = self._io.pos()
            self._debug['pointer_to_linenumbers']['start'] = self._io.pos()
            self.pointer_to_linenumbers = self._io.read_u4le()
            self._debug['pointer_to_linenumbers']['end'] = self._io.pos()
            self._debug['num_relocations']['start'] = self._io.pos()
            self.num_relocations = self._io.read_u2le()
            self._debug['num_relocations']['end'] = self._io.pos()
            self._debug['num_linenumbers']['start'] = self._io.pos()
            self.num_linenumbers = self._io.read_u2le()
            self._debug['num_linenumbers']['end'] = self._io.pos()
            self._debug['characteristics']['start'] = self._io.pos()
            self.characteristics = self._io.read_u4le()
            self._debug['characteristics']['end'] = self._io.pos()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            _pos = self._io.pos()
            self._io.seek(((self.pointer_to_raw_data - self._root.te_hdr.stripped_size) + self._root.te_hdr._io.size()))
            self._debug['_m_body']['start'] = self._io.pos()
            self._m_body = self._io.read_bytes(self.size_of_raw_data)
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_body', None)



