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

class ChromePak(KaitaiStruct):
    """Format mostly used by Google Chrome and various Android apps to store
    resources such as translated strings, help messages and images.
    
    .. seealso::
       Source - https://web.archive.org/web/20220126211447/https://dev.chromium.org/developers/design-documents/linuxresourcesandlocalizedstrings
    
    
    .. seealso::
       Source - https://chromium.googlesource.com/chromium/src/tools/grit/+/3c36f27/grit/format/data_pack.py
    
    
    .. seealso::
       Source - https://chromium.googlesource.com/chromium/src/tools/grit/+/8a23eae/grit/format/data_pack.py
    """

    class Encodings(Enum):
        binary = 0
        utf8 = 1
        utf16 = 2
    SEQ_FIELDS = ["version", "num_resources_v4", "encoding", "v5_part", "resources", "aliases"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not  ((self.version == 4) or (self.version == 5)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/0")
        if self.version == 4:
            self._debug['num_resources_v4']['start'] = self._io.pos()
            self.num_resources_v4 = self._io.read_u4le()
            self._debug['num_resources_v4']['end'] = self._io.pos()

        self._debug['encoding']['start'] = self._io.pos()
        self.encoding = KaitaiStream.resolve_enum(ChromePak.Encodings, self._io.read_u1())
        self._debug['encoding']['end'] = self._io.pos()
        if self.version == 5:
            self._debug['v5_part']['start'] = self._io.pos()
            self.v5_part = ChromePak.HeaderV5Part(self._io, self, self._root)
            self.v5_part._read()
            self._debug['v5_part']['end'] = self._io.pos()

        self._debug['resources']['start'] = self._io.pos()
        self.resources = []
        for i in range((self.num_resources + 1)):
            if not 'arr' in self._debug['resources']:
                self._debug['resources']['arr'] = []
            self._debug['resources']['arr'].append({'start': self._io.pos()})
            _t_resources = ChromePak.Resource(i, i < self.num_resources, self._io, self, self._root)
            _t_resources._read()
            self.resources.append(_t_resources)
            self._debug['resources']['arr'][i]['end'] = self._io.pos()

        self._debug['resources']['end'] = self._io.pos()
        self._debug['aliases']['start'] = self._io.pos()
        self.aliases = []
        for i in range(self.num_aliases):
            if not 'arr' in self._debug['aliases']:
                self._debug['aliases']['arr'] = []
            self._debug['aliases']['arr'].append({'start': self._io.pos()})
            _t_aliases = ChromePak.Alias(self._io, self, self._root)
            _t_aliases._read()
            self.aliases.append(_t_aliases)
            self._debug['aliases']['arr'][i]['end'] = self._io.pos()

        self._debug['aliases']['end'] = self._io.pos()

    class HeaderV5Part(KaitaiStruct):
        SEQ_FIELDS = ["encoding_padding", "num_resources", "num_aliases"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['encoding_padding']['start'] = self._io.pos()
            self.encoding_padding = self._io.read_bytes(3)
            self._debug['encoding_padding']['end'] = self._io.pos()
            self._debug['num_resources']['start'] = self._io.pos()
            self.num_resources = self._io.read_u2le()
            self._debug['num_resources']['end'] = self._io.pos()
            self._debug['num_aliases']['start'] = self._io.pos()
            self.num_aliases = self._io.read_u2le()
            self._debug['num_aliases']['end'] = self._io.pos()


    class Resource(KaitaiStruct):
        SEQ_FIELDS = ["id", "ofs_body"]
        def __init__(self, idx, has_body, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.idx = idx
            self.has_body = has_body
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_u2le()
            self._debug['id']['end'] = self._io.pos()
            self._debug['ofs_body']['start'] = self._io.pos()
            self.ofs_body = self._io.read_u4le()
            self._debug['ofs_body']['end'] = self._io.pos()

        @property
        def len_body(self):
            """MUST NOT be accessed until the next `resource` is parsed."""
            if hasattr(self, '_m_len_body'):
                return self._m_len_body

            if self.has_body:
                self._m_len_body = (self._parent.resources[(self.idx + 1)].ofs_body - self.ofs_body)

            return getattr(self, '_m_len_body', None)

        @property
        def body(self):
            """MUST NOT be accessed until the next `resource` is parsed."""
            if hasattr(self, '_m_body'):
                return self._m_body

            if self.has_body:
                _pos = self._io.pos()
                self._io.seek(self.ofs_body)
                self._debug['_m_body']['start'] = self._io.pos()
                self._m_body = self._io.read_bytes(self.len_body)
                self._debug['_m_body']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_body', None)


    class Alias(KaitaiStruct):
        SEQ_FIELDS = ["id", "resource_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_u2le()
            self._debug['id']['end'] = self._io.pos()
            self._debug['resource_idx']['start'] = self._io.pos()
            self.resource_idx = self._io.read_u2le()
            self._debug['resource_idx']['end'] = self._io.pos()
            if not self.resource_idx <= (self._parent.num_resources - 1):
                raise kaitaistruct.ValidationGreaterThanError((self._parent.num_resources - 1), self.resource_idx, self._io, u"/types/alias/seq/1")

        @property
        def resource(self):
            if hasattr(self, '_m_resource'):
                return self._m_resource

            self._m_resource = self._parent.resources[self.resource_idx]
            return getattr(self, '_m_resource', None)


    @property
    def num_resources(self):
        if hasattr(self, '_m_num_resources'):
            return self._m_num_resources

        self._m_num_resources = (self.v5_part.num_resources if self.version == 5 else self.num_resources_v4)
        return getattr(self, '_m_num_resources', None)

    @property
    def num_aliases(self):
        if hasattr(self, '_m_num_aliases'):
            return self._m_num_aliases

        self._m_num_aliases = (self.v5_part.num_aliases if self.version == 5 else 0)
        return getattr(self, '_m_num_aliases', None)


