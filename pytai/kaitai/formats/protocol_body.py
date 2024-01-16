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
import icmp_packet
import tcp_segment
import udp_datagram
import ipv6_packet
class ProtocolBody(KaitaiStruct):
    """Protocol body represents particular payload on transport level (OSI
    layer 4).
    
    Typically this payload in encapsulated into network level (OSI layer
    3) packet, which includes "protocol number" field that would be used
    to decide what's inside the payload and how to parse it. Thanks to
    IANA's standardization effort, multiple network level use the same
    IDs for these payloads named "protocol numbers".
    
    This is effectively a "router" type: it expects to get protocol
    number as a parameter, and then invokes relevant type parser based
    on that parameter.
    
    .. seealso::
       Source - https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
    """

    class ProtocolEnum(Enum):
        hopopt = 0
        icmp = 1
        igmp = 2
        ggp = 3
        ipv4 = 4
        st = 5
        tcp = 6
        cbt = 7
        egp = 8
        igp = 9
        bbn_rcc_mon = 10
        nvp_ii = 11
        pup = 12
        argus = 13
        emcon = 14
        xnet = 15
        chaos = 16
        udp = 17
        mux = 18
        dcn_meas = 19
        hmp = 20
        prm = 21
        xns_idp = 22
        trunk_1 = 23
        trunk_2 = 24
        leaf_1 = 25
        leaf_2 = 26
        rdp = 27
        irtp = 28
        iso_tp4 = 29
        netblt = 30
        mfe_nsp = 31
        merit_inp = 32
        dccp = 33
        x_3pc = 34
        idpr = 35
        xtp = 36
        ddp = 37
        idpr_cmtp = 38
        tp_plus_plus = 39
        il = 40
        ipv6 = 41
        sdrp = 42
        ipv6_route = 43
        ipv6_frag = 44
        idrp = 45
        rsvp = 46
        gre = 47
        dsr = 48
        bna = 49
        esp = 50
        ah = 51
        i_nlsp = 52
        swipe = 53
        narp = 54
        mobile = 55
        tlsp = 56
        skip = 57
        ipv6_icmp = 58
        ipv6_nonxt = 59
        ipv6_opts = 60
        any_host_internal_protocol = 61
        cftp = 62
        any_local_network = 63
        sat_expak = 64
        kryptolan = 65
        rvd = 66
        ippc = 67
        any_distributed_file_system = 68
        sat_mon = 69
        visa = 70
        ipcv = 71
        cpnx = 72
        cphb = 73
        wsn = 74
        pvp = 75
        br_sat_mon = 76
        sun_nd = 77
        wb_mon = 78
        wb_expak = 79
        iso_ip = 80
        vmtp = 81
        secure_vmtp = 82
        vines = 83
        ttp_or_iptm = 84
        nsfnet_igp = 85
        dgp = 86
        tcf = 87
        eigrp = 88
        ospfigp = 89
        sprite_rpc = 90
        larp = 91
        mtp = 92
        ax_25 = 93
        ipip = 94
        micp = 95
        scc_sp = 96
        etherip = 97
        encap = 98
        any_private_encryption_scheme = 99
        gmtp = 100
        ifmp = 101
        pnni = 102
        pim = 103
        aris = 104
        scps = 105
        qnx = 106
        a_n = 107
        ipcomp = 108
        snp = 109
        compaq_peer = 110
        ipx_in_ip = 111
        vrrp = 112
        pgm = 113
        any_0_hop = 114
        l2tp = 115
        ddx = 116
        iatp = 117
        stp = 118
        srp = 119
        uti = 120
        smp = 121
        sm = 122
        ptp = 123
        isis_over_ipv4 = 124
        fire = 125
        crtp = 126
        crudp = 127
        sscopmce = 128
        iplt = 129
        sps = 130
        pipe = 131
        sctp = 132
        fc = 133
        rsvp_e2e_ignore = 134
        mobility_header = 135
        udplite = 136
        mpls_in_ip = 137
        manet = 138
        hip = 139
        shim6 = 140
        wesp = 141
        rohc = 142
        reserved_255 = 255
    SEQ_FIELDS = ["body"]
    def __init__(self, protocol_num, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.protocol_num = protocol_num
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['body']['start'] = self._io.pos()
        _on = self.protocol
        if _on == ProtocolBody.ProtocolEnum.ipv6_nonxt:
            self.body = ProtocolBody.NoNextHeader(self._io, self, self._root)
            self.body._read()
        elif _on == ProtocolBody.ProtocolEnum.ipv4:
            self.body = ipv4_packet.Ipv4Packet(self._io)
            self.body._read()
        elif _on == ProtocolBody.ProtocolEnum.udp:
            self.body = udp_datagram.UdpDatagram(self._io)
            self.body._read()
        elif _on == ProtocolBody.ProtocolEnum.icmp:
            self.body = icmp_packet.IcmpPacket(self._io)
            self.body._read()
        elif _on == ProtocolBody.ProtocolEnum.hopopt:
            self.body = ProtocolBody.OptionHopByHop(self._io, self, self._root)
            self.body._read()
        elif _on == ProtocolBody.ProtocolEnum.ipv6:
            self.body = ipv6_packet.Ipv6Packet(self._io)
            self.body._read()
        elif _on == ProtocolBody.ProtocolEnum.tcp:
            self.body = tcp_segment.TcpSegment(self._io)
            self.body._read()
        self._debug['body']['end'] = self._io.pos()

    class NoNextHeader(KaitaiStruct):
        """Dummy type for IPv6 "no next header" type, which signifies end of headers chain."""
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            pass


    class OptionHopByHop(KaitaiStruct):
        SEQ_FIELDS = ["next_header_type", "hdr_ext_len", "body", "next_header"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['next_header_type']['start'] = self._io.pos()
            self.next_header_type = self._io.read_u1()
            self._debug['next_header_type']['end'] = self._io.pos()
            self._debug['hdr_ext_len']['start'] = self._io.pos()
            self.hdr_ext_len = self._io.read_u1()
            self._debug['hdr_ext_len']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(((self.hdr_ext_len - 1) if self.hdr_ext_len > 0 else 1))
            self._debug['body']['end'] = self._io.pos()
            self._debug['next_header']['start'] = self._io.pos()
            self.next_header = ProtocolBody(self.next_header_type, self._io)
            self.next_header._read()
            self._debug['next_header']['end'] = self._io.pos()


    @property
    def protocol(self):
        if hasattr(self, '_m_protocol'):
            return self._m_protocol

        self._m_protocol = KaitaiStream.resolve_enum(ProtocolBody.ProtocolEnum, self.protocol_num)
        return getattr(self, '_m_protocol', None)


