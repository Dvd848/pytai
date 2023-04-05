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

class ZxSpectrumTap(KaitaiStruct):
    """TAP files are used by emulators of ZX Spectrum computer (released in
    1982 by Sinclair Research). TAP file stores blocks of data as if
    they are written to magnetic tape, which was used as primary media
    for ZX Spectrum. Contents of this file can be viewed as a very
    simple linear filesystem, storing named files with some basic
    metainformation prepended as a header.
    
    .. seealso::
       Source - https://sinclair.wiki.zxnet.co.uk/wiki/TAP_format
    """

    class FlagEnum(Enum):
        header = 0
        data = 255

    class HeaderTypeEnum(Enum):
        program = 0
        num_array = 1
        char_array = 2
        bytes = 3
    SEQ_FIELDS = ["blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['blocks']['start'] = self._io.pos()
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['blocks']:
                self._debug['blocks']['arr'] = []
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _t_blocks = ZxSpectrumTap.Block(self._io, self, self._root)
            _t_blocks._read()
            self.blocks.append(_t_blocks)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['blocks']['end'] = self._io.pos()

    class Block(KaitaiStruct):
        SEQ_FIELDS = ["len_block", "flag", "header", "data", "headerless_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_block']['start'] = self._io.pos()
            self.len_block = self._io.read_u2le()
            self._debug['len_block']['end'] = self._io.pos()
            self._debug['flag']['start'] = self._io.pos()
            self.flag = KaitaiStream.resolve_enum(ZxSpectrumTap.FlagEnum, self._io.read_u1())
            self._debug['flag']['end'] = self._io.pos()
            if  ((self.len_block == 19) and (self.flag == ZxSpectrumTap.FlagEnum.header)) :
                self._debug['header']['start'] = self._io.pos()
                self.header = ZxSpectrumTap.Header(self._io, self, self._root)
                self.header._read()
                self._debug['header']['end'] = self._io.pos()

            if self.len_block == 19:
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes((self.header.len_data + 4))
                self._debug['data']['end'] = self._io.pos()

            if self.flag == ZxSpectrumTap.FlagEnum.data:
                self._debug['headerless_data']['start'] = self._io.pos()
                self.headerless_data = self._io.read_bytes((self.len_block - 1))
                self._debug['headerless_data']['end'] = self._io.pos()



    class ProgramParams(KaitaiStruct):
        SEQ_FIELDS = ["autostart_line", "len_program"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['autostart_line']['start'] = self._io.pos()
            self.autostart_line = self._io.read_u2le()
            self._debug['autostart_line']['end'] = self._io.pos()
            self._debug['len_program']['start'] = self._io.pos()
            self.len_program = self._io.read_u2le()
            self._debug['len_program']['end'] = self._io.pos()


    class BytesParams(KaitaiStruct):
        SEQ_FIELDS = ["start_address", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['start_address']['start'] = self._io.pos()
            self.start_address = self._io.read_u2le()
            self._debug['start_address']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(2)
            self._debug['reserved']['end'] = self._io.pos()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["header_type", "filename", "len_data", "params", "checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header_type']['start'] = self._io.pos()
            self.header_type = KaitaiStream.resolve_enum(ZxSpectrumTap.HeaderTypeEnum, self._io.read_u1())
            self._debug['header_type']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = KaitaiStream.bytes_strip_right(self._io.read_bytes(10), 32)
            self._debug['filename']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u2le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['params']['start'] = self._io.pos()
            _on = self.header_type
            if _on == ZxSpectrumTap.HeaderTypeEnum.program:
                self.params = ZxSpectrumTap.ProgramParams(self._io, self, self._root)
                self.params._read()
            elif _on == ZxSpectrumTap.HeaderTypeEnum.num_array:
                self.params = ZxSpectrumTap.ArrayParams(self._io, self, self._root)
                self.params._read()
            elif _on == ZxSpectrumTap.HeaderTypeEnum.char_array:
                self.params = ZxSpectrumTap.ArrayParams(self._io, self, self._root)
                self.params._read()
            elif _on == ZxSpectrumTap.HeaderTypeEnum.bytes:
                self.params = ZxSpectrumTap.BytesParams(self._io, self, self._root)
                self.params._read()
            self._debug['params']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u1()
            self._debug['checksum']['end'] = self._io.pos()


    class ArrayParams(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "var_name", "reserved1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u1()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['var_name']['start'] = self._io.pos()
            self.var_name = self._io.read_u1()
            self._debug['var_name']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(2)
            self._debug['reserved1']['end'] = self._io.pos()
            if not self.reserved1 == b"\x00\x80":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x80", self.reserved1, self._io, u"/types/array_params/seq/2")



