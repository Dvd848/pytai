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

class BlenderBlend(KaitaiStruct):
    """Blender is an open source suite for 3D modelling, sculpting,
    animation, compositing, rendering, preparation of assets for its own
    game engine and exporting to others, etc. `.blend` is its own binary
    format that saves whole state of suite: current scene, animations,
    all software settings, extensions, etc.
    
    Internally, .blend format is a hybrid semi-self-descriptive
    format. On top level, it contains a simple header and a sequence of
    file blocks, which more or less follow typical [TLV
    pattern](https://en.wikipedia.org/wiki/Type-length-value). Pre-last
    block would be a structure with code `DNA1`, which is a essentially
    a machine-readable schema of all other structures used in this file.
    """

    class PtrSize(Enum):
        bits_64 = 45
        bits_32 = 95

    class Endian(Enum):
        be = 86
        le = 118
    SEQ_FIELDS = ["hdr", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['hdr']['start'] = self._io.pos()
        self.hdr = BlenderBlend.Header(self._io, self, self._root)
        self.hdr._read()
        self._debug['hdr']['end'] = self._io.pos()
        self._debug['blocks']['start'] = self._io.pos()
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['blocks']:
                self._debug['blocks']['arr'] = []
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _t_blocks = BlenderBlend.FileBlock(self._io, self, self._root)
            _t_blocks._read()
            self.blocks.append(_t_blocks)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['blocks']['end'] = self._io.pos()

    class DnaStruct(KaitaiStruct):
        """DNA struct contains a `type` (type name), which is specified as
        an index in types table, and sequence of fields.
        """
        SEQ_FIELDS = ["idx_type", "num_fields", "fields"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['idx_type']['start'] = self._io.pos()
            self.idx_type = self._io.read_u2le()
            self._debug['idx_type']['end'] = self._io.pos()
            self._debug['num_fields']['start'] = self._io.pos()
            self.num_fields = self._io.read_u2le()
            self._debug['num_fields']['end'] = self._io.pos()
            self._debug['fields']['start'] = self._io.pos()
            self.fields = []
            for i in range(self.num_fields):
                if not 'arr' in self._debug['fields']:
                    self._debug['fields']['arr'] = []
                self._debug['fields']['arr'].append({'start': self._io.pos()})
                _t_fields = BlenderBlend.DnaField(self._io, self, self._root)
                _t_fields._read()
                self.fields.append(_t_fields)
                self._debug['fields']['arr'][i]['end'] = self._io.pos()

            self._debug['fields']['end'] = self._io.pos()

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = self._parent.types[self.idx_type]
            return getattr(self, '_m_type', None)


    class FileBlock(KaitaiStruct):
        SEQ_FIELDS = ["code", "len_body", "mem_addr", "sdna_index", "count", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['code']['end'] = self._io.pos()
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u4le()
            self._debug['len_body']['end'] = self._io.pos()
            self._debug['mem_addr']['start'] = self._io.pos()
            self.mem_addr = self._io.read_bytes(self._root.hdr.psize)
            self._debug['mem_addr']['end'] = self._io.pos()
            self._debug['sdna_index']['start'] = self._io.pos()
            self.sdna_index = self._io.read_u4le()
            self._debug['sdna_index']['end'] = self._io.pos()
            self._debug['count']['start'] = self._io.pos()
            self.count = self._io.read_u4le()
            self._debug['count']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.code
            if _on == u"DNA1":
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = BlenderBlend.Dna1Body(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes(self.len_body)
            self._debug['body']['end'] = self._io.pos()

        @property
        def sdna_struct(self):
            if hasattr(self, '_m_sdna_struct'):
                return self._m_sdna_struct

            if self.sdna_index != 0:
                self._m_sdna_struct = self._root.sdna_structs[self.sdna_index]

            return getattr(self, '_m_sdna_struct', None)


    class Dna1Body(KaitaiStruct):
        """DNA1, also known as "Structure DNA", is a special block in
        .blend file, which contains machine-readable specifications of
        all other structures used in this .blend file.
        
        Effectively, this block contains:
        
        * a sequence of "names" (strings which represent field names)
        * a sequence of "types" (strings which represent type name)
        * a sequence of "type lengths"
        * a sequence of "structs" (which describe contents of every
          structure, referring to types and names by index)
        
        .. seealso::
           Source - https://archive.blender.org/wiki/index.php/Dev:Source/Architecture/File_Format/#Structure_DNA
        """
        SEQ_FIELDS = ["id", "name_magic", "num_names", "names", "padding_1", "type_magic", "num_types", "types", "padding_2", "tlen_magic", "lengths", "padding_3", "strc_magic", "num_structs", "structs"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_bytes(4)
            self._debug['id']['end'] = self._io.pos()
            if not self.id == b"\x53\x44\x4E\x41":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x44\x4E\x41", self.id, self._io, u"/types/dna1_body/seq/0")
            self._debug['name_magic']['start'] = self._io.pos()
            self.name_magic = self._io.read_bytes(4)
            self._debug['name_magic']['end'] = self._io.pos()
            if not self.name_magic == b"\x4E\x41\x4D\x45":
                raise kaitaistruct.ValidationNotEqualError(b"\x4E\x41\x4D\x45", self.name_magic, self._io, u"/types/dna1_body/seq/1")
            self._debug['num_names']['start'] = self._io.pos()
            self.num_names = self._io.read_u4le()
            self._debug['num_names']['end'] = self._io.pos()
            self._debug['names']['start'] = self._io.pos()
            self.names = []
            for i in range(self.num_names):
                if not 'arr' in self._debug['names']:
                    self._debug['names']['arr'] = []
                self._debug['names']['arr'].append({'start': self._io.pos()})
                self.names.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                self._debug['names']['arr'][i]['end'] = self._io.pos()

            self._debug['names']['end'] = self._io.pos()
            self._debug['padding_1']['start'] = self._io.pos()
            self.padding_1 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self._debug['padding_1']['end'] = self._io.pos()
            self._debug['type_magic']['start'] = self._io.pos()
            self.type_magic = self._io.read_bytes(4)
            self._debug['type_magic']['end'] = self._io.pos()
            if not self.type_magic == b"\x54\x59\x50\x45":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x59\x50\x45", self.type_magic, self._io, u"/types/dna1_body/seq/5")
            self._debug['num_types']['start'] = self._io.pos()
            self.num_types = self._io.read_u4le()
            self._debug['num_types']['end'] = self._io.pos()
            self._debug['types']['start'] = self._io.pos()
            self.types = []
            for i in range(self.num_types):
                if not 'arr' in self._debug['types']:
                    self._debug['types']['arr'] = []
                self._debug['types']['arr'].append({'start': self._io.pos()})
                self.types.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                self._debug['types']['arr'][i]['end'] = self._io.pos()

            self._debug['types']['end'] = self._io.pos()
            self._debug['padding_2']['start'] = self._io.pos()
            self.padding_2 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self._debug['padding_2']['end'] = self._io.pos()
            self._debug['tlen_magic']['start'] = self._io.pos()
            self.tlen_magic = self._io.read_bytes(4)
            self._debug['tlen_magic']['end'] = self._io.pos()
            if not self.tlen_magic == b"\x54\x4C\x45\x4E":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x4C\x45\x4E", self.tlen_magic, self._io, u"/types/dna1_body/seq/9")
            self._debug['lengths']['start'] = self._io.pos()
            self.lengths = []
            for i in range(self.num_types):
                if not 'arr' in self._debug['lengths']:
                    self._debug['lengths']['arr'] = []
                self._debug['lengths']['arr'].append({'start': self._io.pos()})
                self.lengths.append(self._io.read_u2le())
                self._debug['lengths']['arr'][i]['end'] = self._io.pos()

            self._debug['lengths']['end'] = self._io.pos()
            self._debug['padding_3']['start'] = self._io.pos()
            self.padding_3 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self._debug['padding_3']['end'] = self._io.pos()
            self._debug['strc_magic']['start'] = self._io.pos()
            self.strc_magic = self._io.read_bytes(4)
            self._debug['strc_magic']['end'] = self._io.pos()
            if not self.strc_magic == b"\x53\x54\x52\x43":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x54\x52\x43", self.strc_magic, self._io, u"/types/dna1_body/seq/12")
            self._debug['num_structs']['start'] = self._io.pos()
            self.num_structs = self._io.read_u4le()
            self._debug['num_structs']['end'] = self._io.pos()
            self._debug['structs']['start'] = self._io.pos()
            self.structs = []
            for i in range(self.num_structs):
                if not 'arr' in self._debug['structs']:
                    self._debug['structs']['arr'] = []
                self._debug['structs']['arr'].append({'start': self._io.pos()})
                _t_structs = BlenderBlend.DnaStruct(self._io, self, self._root)
                _t_structs._read()
                self.structs.append(_t_structs)
                self._debug['structs']['arr'][i]['end'] = self._io.pos()

            self._debug['structs']['end'] = self._io.pos()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "ptr_size_id", "endian", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(7)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x42\x4C\x45\x4E\x44\x45\x52":
                raise kaitaistruct.ValidationNotEqualError(b"\x42\x4C\x45\x4E\x44\x45\x52", self.magic, self._io, u"/types/header/seq/0")
            self._debug['ptr_size_id']['start'] = self._io.pos()
            self.ptr_size_id = KaitaiStream.resolve_enum(BlenderBlend.PtrSize, self._io.read_u1())
            self._debug['ptr_size_id']['end'] = self._io.pos()
            self._debug['endian']['start'] = self._io.pos()
            self.endian = KaitaiStream.resolve_enum(BlenderBlend.Endian, self._io.read_u1())
            self._debug['endian']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = (self._io.read_bytes(3)).decode(u"ASCII")
            self._debug['version']['end'] = self._io.pos()

        @property
        def psize(self):
            """Number of bytes that a pointer occupies."""
            if hasattr(self, '_m_psize'):
                return self._m_psize

            self._m_psize = (8 if self.ptr_size_id == BlenderBlend.PtrSize.bits_64 else 4)
            return getattr(self, '_m_psize', None)


    class DnaField(KaitaiStruct):
        SEQ_FIELDS = ["idx_type", "idx_name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['idx_type']['start'] = self._io.pos()
            self.idx_type = self._io.read_u2le()
            self._debug['idx_type']['end'] = self._io.pos()
            self._debug['idx_name']['start'] = self._io.pos()
            self.idx_name = self._io.read_u2le()
            self._debug['idx_name']['end'] = self._io.pos()

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = self._parent._parent.types[self.idx_type]
            return getattr(self, '_m_type', None)

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            self._m_name = self._parent._parent.names[self.idx_name]
            return getattr(self, '_m_name', None)


    @property
    def sdna_structs(self):
        if hasattr(self, '_m_sdna_structs'):
            return self._m_sdna_structs

        self._m_sdna_structs = self.blocks[(len(self.blocks) - 2)].body.structs
        return getattr(self, '_m_sdna_structs', None)


