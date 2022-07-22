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

import protocol_body
class Ipv4Packet(KaitaiStruct):
    SEQ_FIELDS = ["b1", "b2", "total_length", "identification", "b67", "ttl", "protocol", "header_checksum", "src_ip_addr", "dst_ip_addr", "options", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['b1']['start'] = self._io.pos()
        self.b1 = self._io.read_u1()
        self._debug['b1']['end'] = self._io.pos()
        self._debug['b2']['start'] = self._io.pos()
        self.b2 = self._io.read_u1()
        self._debug['b2']['end'] = self._io.pos()
        self._debug['total_length']['start'] = self._io.pos()
        self.total_length = self._io.read_u2be()
        self._debug['total_length']['end'] = self._io.pos()
        self._debug['identification']['start'] = self._io.pos()
        self.identification = self._io.read_u2be()
        self._debug['identification']['end'] = self._io.pos()
        self._debug['b67']['start'] = self._io.pos()
        self.b67 = self._io.read_u2be()
        self._debug['b67']['end'] = self._io.pos()
        self._debug['ttl']['start'] = self._io.pos()
        self.ttl = self._io.read_u1()
        self._debug['ttl']['end'] = self._io.pos()
        self._debug['protocol']['start'] = self._io.pos()
        self.protocol = self._io.read_u1()
        self._debug['protocol']['end'] = self._io.pos()
        self._debug['header_checksum']['start'] = self._io.pos()
        self.header_checksum = self._io.read_u2be()
        self._debug['header_checksum']['end'] = self._io.pos()
        self._debug['src_ip_addr']['start'] = self._io.pos()
        self.src_ip_addr = self._io.read_bytes(4)
        self._debug['src_ip_addr']['end'] = self._io.pos()
        self._debug['dst_ip_addr']['start'] = self._io.pos()
        self.dst_ip_addr = self._io.read_bytes(4)
        self._debug['dst_ip_addr']['end'] = self._io.pos()
        self._debug['options']['start'] = self._io.pos()
        self._raw_options = self._io.read_bytes((self.ihl_bytes - 20))
        _io__raw_options = KaitaiStream(BytesIO(self._raw_options))
        self.options = Ipv4Packet.Ipv4Options(_io__raw_options, self, self._root)
        self.options._read()
        self._debug['options']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        self._raw_body = self._io.read_bytes((self.total_length - self.ihl_bytes))
        _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
        self.body = protocol_body.ProtocolBody(self.protocol, _io__raw_body)
        self.body._read()
        self._debug['body']['end'] = self._io.pos()

    class Ipv4Options(KaitaiStruct):
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
                _t_entries = Ipv4Packet.Ipv4Option(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class Ipv4Option(KaitaiStruct):
        SEQ_FIELDS = ["b1", "len", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['b1']['start'] = self._io.pos()
            self.b1 = self._io.read_u1()
            self._debug['b1']['end'] = self._io.pos()
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u1()
            self._debug['len']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(((self.len - 2) if self.len > 2 else 0))
            self._debug['body']['end'] = self._io.pos()

        @property
        def copy(self):
            if hasattr(self, '_m_copy'):
                return self._m_copy

            self._m_copy = ((self.b1 & 128) >> 7)
            return getattr(self, '_m_copy', None)

        @property
        def opt_class(self):
            if hasattr(self, '_m_opt_class'):
                return self._m_opt_class

            self._m_opt_class = ((self.b1 & 96) >> 5)
            return getattr(self, '_m_opt_class', None)

        @property
        def number(self):
            if hasattr(self, '_m_number'):
                return self._m_number

            self._m_number = (self.b1 & 31)
            return getattr(self, '_m_number', None)


    @property
    def version(self):
        if hasattr(self, '_m_version'):
            return self._m_version

        self._m_version = ((self.b1 & 240) >> 4)
        return getattr(self, '_m_version', None)

    @property
    def ihl(self):
        if hasattr(self, '_m_ihl'):
            return self._m_ihl

        self._m_ihl = (self.b1 & 15)
        return getattr(self, '_m_ihl', None)

    @property
    def ihl_bytes(self):
        if hasattr(self, '_m_ihl_bytes'):
            return self._m_ihl_bytes

        self._m_ihl_bytes = (self.ihl * 4)
        return getattr(self, '_m_ihl_bytes', None)


