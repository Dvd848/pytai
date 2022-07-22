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

import ipv4_packet
import ipv6_packet
class EthernetFrame(KaitaiStruct):
    """Ethernet frame is a OSI data link layer (layer 2) protocol data unit
    for Ethernet networks. In practice, many other networks and/or
    in-file dumps adopted the same format for encapsulation purposes.
    
    .. seealso::
       Source - https://ieeexplore.ieee.org/document/7428776
    """

    class EtherTypeEnum(Enum):
        ipv4 = 2048
        x_75_internet = 2049
        nbs_internet = 2050
        ecma_internet = 2051
        chaosnet = 2052
        x_25_level_3 = 2053
        arp = 2054
        ieee_802_1q_tpid = 33024
        ipv6 = 34525
    SEQ_FIELDS = ["dst_mac", "src_mac", "ether_type_1", "tci", "ether_type_2", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['dst_mac']['start'] = self._io.pos()
        self.dst_mac = self._io.read_bytes(6)
        self._debug['dst_mac']['end'] = self._io.pos()
        self._debug['src_mac']['start'] = self._io.pos()
        self.src_mac = self._io.read_bytes(6)
        self._debug['src_mac']['end'] = self._io.pos()
        self._debug['ether_type_1']['start'] = self._io.pos()
        self.ether_type_1 = KaitaiStream.resolve_enum(EthernetFrame.EtherTypeEnum, self._io.read_u2be())
        self._debug['ether_type_1']['end'] = self._io.pos()
        if self.ether_type_1 == EthernetFrame.EtherTypeEnum.ieee_802_1q_tpid:
            self._debug['tci']['start'] = self._io.pos()
            self.tci = EthernetFrame.TagControlInfo(self._io, self, self._root)
            self.tci._read()
            self._debug['tci']['end'] = self._io.pos()

        if self.ether_type_1 == EthernetFrame.EtherTypeEnum.ieee_802_1q_tpid:
            self._debug['ether_type_2']['start'] = self._io.pos()
            self.ether_type_2 = KaitaiStream.resolve_enum(EthernetFrame.EtherTypeEnum, self._io.read_u2be())
            self._debug['ether_type_2']['end'] = self._io.pos()

        self._debug['body']['start'] = self._io.pos()
        _on = self.ether_type
        if _on == EthernetFrame.EtherTypeEnum.ipv4:
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = ipv4_packet.Ipv4Packet(_io__raw_body)
            self.body._read()
        elif _on == EthernetFrame.EtherTypeEnum.ipv6:
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = ipv6_packet.Ipv6Packet(_io__raw_body)
            self.body._read()
        else:
            self.body = self._io.read_bytes_full()
        self._debug['body']['end'] = self._io.pos()

    class TagControlInfo(KaitaiStruct):
        """Tag Control Information (TCI) is an extension of IEEE 802.1Q to
        support VLANs on normal IEEE 802.3 Ethernet network.
        """
        SEQ_FIELDS = ["priority", "drop_eligible", "vlan_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['priority']['start'] = self._io.pos()
            self.priority = self._io.read_bits_int_be(3)
            self._debug['priority']['end'] = self._io.pos()
            self._debug['drop_eligible']['start'] = self._io.pos()
            self.drop_eligible = self._io.read_bits_int_be(1) != 0
            self._debug['drop_eligible']['end'] = self._io.pos()
            self._debug['vlan_id']['start'] = self._io.pos()
            self.vlan_id = self._io.read_bits_int_be(12)
            self._debug['vlan_id']['end'] = self._io.pos()


    @property
    def ether_type(self):
        """Ether type can be specied in several places in the frame. If
        first location bears special marker (0x8100), then it is not the
        real ether frame yet, an additional payload (`tci`) is expected
        and real ether type is upcoming next.
        """
        if hasattr(self, '_m_ether_type'):
            return self._m_ether_type

        self._m_ether_type = (self.ether_type_2 if self.ether_type_1 == EthernetFrame.EtherTypeEnum.ieee_802_1q_tpid else self.ether_type_1)
        return getattr(self, '_m_ether_type', None)


