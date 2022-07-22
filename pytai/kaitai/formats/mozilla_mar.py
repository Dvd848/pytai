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

class MozillaMar(KaitaiStruct):
    """Mozilla ARchive file is Mozilla's own archive format to distribute software updates.
    Test files can be found on Mozilla's FTP site, for example:
    
    <http://ftp.mozilla.org/pub/firefox/nightly/partials/>
    
    .. seealso::
       Source - https://wiki.mozilla.org/Software_Update:MAR
    """

    class SignatureAlgorithms(Enum):
        rsa_pkcs1_sha1 = 1
        rsa_pkcs1_sha384 = 2

    class BlockIdentifiers(Enum):
        product_information = 1
    SEQ_FIELDS = ["magic", "ofs_index", "file_size", "len_signatures", "signatures", "len_additional_sections", "additional_sections"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x4D\x41\x52\x31":
            raise kaitaistruct.ValidationNotEqualError(b"\x4D\x41\x52\x31", self.magic, self._io, u"/seq/0")
        self._debug['ofs_index']['start'] = self._io.pos()
        self.ofs_index = self._io.read_u4be()
        self._debug['ofs_index']['end'] = self._io.pos()
        self._debug['file_size']['start'] = self._io.pos()
        self.file_size = self._io.read_u8be()
        self._debug['file_size']['end'] = self._io.pos()
        self._debug['len_signatures']['start'] = self._io.pos()
        self.len_signatures = self._io.read_u4be()
        self._debug['len_signatures']['end'] = self._io.pos()
        self._debug['signatures']['start'] = self._io.pos()
        self.signatures = []
        for i in range(self.len_signatures):
            if not 'arr' in self._debug['signatures']:
                self._debug['signatures']['arr'] = []
            self._debug['signatures']['arr'].append({'start': self._io.pos()})
            _t_signatures = MozillaMar.Signature(self._io, self, self._root)
            _t_signatures._read()
            self.signatures.append(_t_signatures)
            self._debug['signatures']['arr'][i]['end'] = self._io.pos()

        self._debug['signatures']['end'] = self._io.pos()
        self._debug['len_additional_sections']['start'] = self._io.pos()
        self.len_additional_sections = self._io.read_u4be()
        self._debug['len_additional_sections']['end'] = self._io.pos()
        self._debug['additional_sections']['start'] = self._io.pos()
        self.additional_sections = []
        for i in range(self.len_additional_sections):
            if not 'arr' in self._debug['additional_sections']:
                self._debug['additional_sections']['arr'] = []
            self._debug['additional_sections']['arr'].append({'start': self._io.pos()})
            _t_additional_sections = MozillaMar.AdditionalSection(self._io, self, self._root)
            _t_additional_sections._read()
            self.additional_sections.append(_t_additional_sections)
            self._debug['additional_sections']['arr'][i]['end'] = self._io.pos()

        self._debug['additional_sections']['end'] = self._io.pos()

    class MarIndex(KaitaiStruct):
        SEQ_FIELDS = ["len_index", "index_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_index']['start'] = self._io.pos()
            self.len_index = self._io.read_u4be()
            self._debug['len_index']['end'] = self._io.pos()
            self._debug['index_entries']['start'] = self._io.pos()
            self._raw_index_entries = self._io.read_bytes(self.len_index)
            _io__raw_index_entries = KaitaiStream(BytesIO(self._raw_index_entries))
            self.index_entries = MozillaMar.IndexEntries(_io__raw_index_entries, self, self._root)
            self.index_entries._read()
            self._debug['index_entries']['end'] = self._io.pos()


    class IndexEntries(KaitaiStruct):
        SEQ_FIELDS = ["index_entry"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['index_entry']['start'] = self._io.pos()
            self.index_entry = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['index_entry']:
                    self._debug['index_entry']['arr'] = []
                self._debug['index_entry']['arr'].append({'start': self._io.pos()})
                _t_index_entry = MozillaMar.IndexEntry(self._io, self, self._root)
                _t_index_entry._read()
                self.index_entry.append(_t_index_entry)
                self._debug['index_entry']['arr'][len(self.index_entry) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['index_entry']['end'] = self._io.pos()


    class Signature(KaitaiStruct):
        SEQ_FIELDS = ["algorithm", "len_signature", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['algorithm']['start'] = self._io.pos()
            self.algorithm = KaitaiStream.resolve_enum(MozillaMar.SignatureAlgorithms, self._io.read_u4be())
            self._debug['algorithm']['end'] = self._io.pos()
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u4be()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()


    class ProductInformationBlock(KaitaiStruct):
        SEQ_FIELDS = ["mar_channel_name", "product_version"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['mar_channel_name']['start'] = self._io.pos()
            self.mar_channel_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"UTF-8")
            self._debug['mar_channel_name']['end'] = self._io.pos()
            self._debug['product_version']['start'] = self._io.pos()
            self.product_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['product_version']['end'] = self._io.pos()


    class IndexEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_content", "len_content", "flags", "file_name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['ofs_content']['start'] = self._io.pos()
            self.ofs_content = self._io.read_u4be()
            self._debug['ofs_content']['end'] = self._io.pos()
            self._debug['len_content']['start'] = self._io.pos()
            self.len_content = self._io.read_u4be()
            self._debug['len_content']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['file_name']['end'] = self._io.pos()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_content)
            self._debug['_m_body']['start'] = io.pos()
            self._m_body = io.read_bytes(self.len_content)
            self._debug['_m_body']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_body', None)


    class AdditionalSection(KaitaiStruct):
        SEQ_FIELDS = ["len_block", "block_identifier", "bytes"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_block']['start'] = self._io.pos()
            self.len_block = self._io.read_u4be()
            self._debug['len_block']['end'] = self._io.pos()
            self._debug['block_identifier']['start'] = self._io.pos()
            self.block_identifier = KaitaiStream.resolve_enum(MozillaMar.BlockIdentifiers, self._io.read_u4be())
            self._debug['block_identifier']['end'] = self._io.pos()
            self._debug['bytes']['start'] = self._io.pos()
            _on = self.block_identifier
            if _on == MozillaMar.BlockIdentifiers.product_information:
                self._raw_bytes = self._io.read_bytes(((self.len_block - 4) - 4))
                _io__raw_bytes = KaitaiStream(BytesIO(self._raw_bytes))
                self.bytes = MozillaMar.ProductInformationBlock(_io__raw_bytes, self, self._root)
                self.bytes._read()
            else:
                self.bytes = self._io.read_bytes(((self.len_block - 4) - 4))
            self._debug['bytes']['end'] = self._io.pos()


    @property
    def index(self):
        if hasattr(self, '_m_index'):
            return self._m_index

        _pos = self._io.pos()
        self._io.seek(self.ofs_index)
        self._debug['_m_index']['start'] = self._io.pos()
        self._m_index = MozillaMar.MarIndex(self._io, self, self._root)
        self._m_index._read()
        self._debug['_m_index']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_index', None)


