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

class Dtb(KaitaiStruct):
    """Also referred to as Devicetree Blob (DTB). It is a flat binary encoding
    of data (primarily devicetree data, although other data is possible as well).
    The data is internally stored as a tree of named nodes and properties. Nodes
    contain properties and child nodes, while properties are name-value pairs.
    
    The Devicetree Blobs (`.dtb` files) are compiled from the Devicetree Source
    files (`.dts`) through the Devicetree compiler (DTC).
    
    On Linux systems that support this, the blobs can be accessed in
    `/sys/firmware/fdt`:
    
    * <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-firmware-ofw>
    
    The encoding of strings used in the `strings_block` and `structure_block` is
    actually a subset of ASCII:
    
    <https://devicetree-specification.readthedocs.io/en/v0.3/devicetree-basics.html#node-names>
    
    Example files:
    
    * <https://github.com/qemu/qemu/tree/master/pc-bios>
    
    .. seealso::
       Source - https://devicetree-specification.readthedocs.io/en/v0.3/flattened-format.html
    
    
    .. seealso::
       Source - https://elinux.org/images/f/f4/Elc2013_Fernandes.pdf
    """

    class Fdt(Enum):
        begin_node = 1
        end_node = 2
        prop = 3
        nop = 4
        end = 9
    SEQ_FIELDS = ["magic", "total_size", "ofs_structure_block", "ofs_strings_block", "ofs_memory_reservation_block", "version", "min_compatible_version", "boot_cpuid_phys", "len_strings_block", "len_structure_block"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xD0\x0D\xFE\xED":
            raise kaitaistruct.ValidationNotEqualError(b"\xD0\x0D\xFE\xED", self.magic, self._io, u"/seq/0")
        self._debug['total_size']['start'] = self._io.pos()
        self.total_size = self._io.read_u4be()
        self._debug['total_size']['end'] = self._io.pos()
        self._debug['ofs_structure_block']['start'] = self._io.pos()
        self.ofs_structure_block = self._io.read_u4be()
        self._debug['ofs_structure_block']['end'] = self._io.pos()
        self._debug['ofs_strings_block']['start'] = self._io.pos()
        self.ofs_strings_block = self._io.read_u4be()
        self._debug['ofs_strings_block']['end'] = self._io.pos()
        self._debug['ofs_memory_reservation_block']['start'] = self._io.pos()
        self.ofs_memory_reservation_block = self._io.read_u4be()
        self._debug['ofs_memory_reservation_block']['end'] = self._io.pos()
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4be()
        self._debug['version']['end'] = self._io.pos()
        self._debug['min_compatible_version']['start'] = self._io.pos()
        self.min_compatible_version = self._io.read_u4be()
        self._debug['min_compatible_version']['end'] = self._io.pos()
        if not self.min_compatible_version <= self.version:
            raise kaitaistruct.ValidationGreaterThanError(self.version, self.min_compatible_version, self._io, u"/seq/6")
        self._debug['boot_cpuid_phys']['start'] = self._io.pos()
        self.boot_cpuid_phys = self._io.read_u4be()
        self._debug['boot_cpuid_phys']['end'] = self._io.pos()
        self._debug['len_strings_block']['start'] = self._io.pos()
        self.len_strings_block = self._io.read_u4be()
        self._debug['len_strings_block']['end'] = self._io.pos()
        self._debug['len_structure_block']['start'] = self._io.pos()
        self.len_structure_block = self._io.read_u4be()
        self._debug['len_structure_block']['end'] = self._io.pos()

    class MemoryBlock(KaitaiStruct):
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
                _t_entries = Dtb.MemoryBlockEntry(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class FdtBlock(KaitaiStruct):
        SEQ_FIELDS = ["nodes"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['nodes']['start'] = self._io.pos()
            self.nodes = []
            i = 0
            while True:
                if not 'arr' in self._debug['nodes']:
                    self._debug['nodes']['arr'] = []
                self._debug['nodes']['arr'].append({'start': self._io.pos()})
                _t_nodes = Dtb.FdtNode(self._io, self, self._root)
                _t_nodes._read()
                _ = _t_nodes
                self.nodes.append(_)
                self._debug['nodes']['arr'][len(self.nodes) - 1]['end'] = self._io.pos()
                if _.type == Dtb.Fdt.end:
                    break
                i += 1
            self._debug['nodes']['end'] = self._io.pos()


    class MemoryBlockEntry(KaitaiStruct):
        SEQ_FIELDS = ["address", "size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['address']['start'] = self._io.pos()
            self.address = self._io.read_u8be()
            self._debug['address']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u8be()
            self._debug['size']['end'] = self._io.pos()


    class Strings(KaitaiStruct):
        SEQ_FIELDS = ["strings"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['strings']['start'] = self._io.pos()
            self.strings = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['strings']:
                    self._debug['strings']['arr'] = []
                self._debug['strings']['arr'].append({'start': self._io.pos()})
                self.strings.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
                self._debug['strings']['arr'][len(self.strings) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['strings']['end'] = self._io.pos()


    class FdtProp(KaitaiStruct):
        SEQ_FIELDS = ["len_property", "ofs_name", "property", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_property']['start'] = self._io.pos()
            self.len_property = self._io.read_u4be()
            self._debug['len_property']['end'] = self._io.pos()
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u4be()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['property']['start'] = self._io.pos()
            self.property = self._io.read_bytes(self.len_property)
            self._debug['property']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes((-(self._io.pos()) % 4))
            self._debug['padding']['end'] = self._io.pos()

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            io = self._root.strings_block._io
            _pos = io.pos()
            io.seek(self.ofs_name)
            self._debug['_m_name']['start'] = io.pos()
            self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_name']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_name', None)


    class FdtNode(KaitaiStruct):
        SEQ_FIELDS = ["type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Dtb.Fdt, self._io.read_u4be())
            self._debug['type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.type
            if _on == Dtb.Fdt.begin_node:
                self.body = Dtb.FdtBeginNode(self._io, self, self._root)
                self.body._read()
            elif _on == Dtb.Fdt.prop:
                self.body = Dtb.FdtProp(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()


    class FdtBeginNode(KaitaiStruct):
        SEQ_FIELDS = ["name", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes((-(self._io.pos()) % 4))
            self._debug['padding']['end'] = self._io.pos()


    @property
    def memory_reservation_block(self):
        if hasattr(self, '_m_memory_reservation_block'):
            return self._m_memory_reservation_block

        _pos = self._io.pos()
        self._io.seek(self.ofs_memory_reservation_block)
        self._debug['_m_memory_reservation_block']['start'] = self._io.pos()
        self._raw__m_memory_reservation_block = self._io.read_bytes((self.ofs_structure_block - self.ofs_memory_reservation_block))
        _io__raw__m_memory_reservation_block = KaitaiStream(BytesIO(self._raw__m_memory_reservation_block))
        self._m_memory_reservation_block = Dtb.MemoryBlock(_io__raw__m_memory_reservation_block, self, self._root)
        self._m_memory_reservation_block._read()
        self._debug['_m_memory_reservation_block']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_memory_reservation_block', None)

    @property
    def structure_block(self):
        if hasattr(self, '_m_structure_block'):
            return self._m_structure_block

        _pos = self._io.pos()
        self._io.seek(self.ofs_structure_block)
        self._debug['_m_structure_block']['start'] = self._io.pos()
        self._raw__m_structure_block = self._io.read_bytes(self.len_structure_block)
        _io__raw__m_structure_block = KaitaiStream(BytesIO(self._raw__m_structure_block))
        self._m_structure_block = Dtb.FdtBlock(_io__raw__m_structure_block, self, self._root)
        self._m_structure_block._read()
        self._debug['_m_structure_block']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_structure_block', None)

    @property
    def strings_block(self):
        if hasattr(self, '_m_strings_block'):
            return self._m_strings_block

        _pos = self._io.pos()
        self._io.seek(self.ofs_strings_block)
        self._debug['_m_strings_block']['start'] = self._io.pos()
        self._raw__m_strings_block = self._io.read_bytes(self.len_strings_block)
        _io__raw__m_strings_block = KaitaiStream(BytesIO(self._raw__m_strings_block))
        self._m_strings_block = Dtb.Strings(_io__raw__m_strings_block, self, self._root)
        self._m_strings_block._read()
        self._debug['_m_strings_block']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_strings_block', None)


