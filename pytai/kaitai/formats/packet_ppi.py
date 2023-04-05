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

import ethernet_frame
class PacketPpi(KaitaiStruct):
    """PPI is a standard for link layer packet encapsulation, proposed as
    generic extensible container to store both captured in-band data and
    out-of-band data. Originally it was developed to provide 802.11n
    radio information, but can be used for other purposes as well.
    
    Sample capture:
    <https://wiki.wireshark.org/uploads/27707187aeb30df68e70c8fb9d614981/http.cap>
    
    .. seealso::
       PPI header format spec, section 3 - https://web.archive.org/web/20090206112419/https://www.cacetech.com/documents/PPI_Header_format_1.0.1.pdf
    """

    class PfhType(Enum):
        radio_802_11_common = 2
        radio_802_11n_mac_ext = 3
        radio_802_11n_mac_phy_ext = 4
        spectrum_map = 5
        process_info = 6
        capture_info = 7

    class Linktype(Enum):
        null_linktype = 0
        ethernet = 1
        ax25 = 3
        ieee802_5 = 6
        arcnet_bsd = 7
        slip = 8
        ppp = 9
        fddi = 10
        ppp_hdlc = 50
        ppp_ether = 51
        atm_rfc1483 = 100
        raw = 101
        c_hdlc = 104
        ieee802_11 = 105
        frelay = 107
        loop = 108
        linux_sll = 113
        ltalk = 114
        pflog = 117
        ieee802_11_prism = 119
        ip_over_fc = 122
        sunatm = 123
        ieee802_11_radiotap = 127
        arcnet_linux = 129
        apple_ip_over_ieee1394 = 138
        mtp2_with_phdr = 139
        mtp2 = 140
        mtp3 = 141
        sccp = 142
        docsis = 143
        linux_irda = 144
        user0 = 147
        user1 = 148
        user2 = 149
        user3 = 150
        user4 = 151
        user5 = 152
        user6 = 153
        user7 = 154
        user8 = 155
        user9 = 156
        user10 = 157
        user11 = 158
        user12 = 159
        user13 = 160
        user14 = 161
        user15 = 162
        ieee802_11_avs = 163
        bacnet_ms_tp = 165
        ppp_pppd = 166
        gprs_llc = 169
        gpf_t = 170
        gpf_f = 171
        linux_lapd = 177
        bluetooth_hci_h4 = 187
        usb_linux = 189
        ppi = 192
        ieee802_15_4 = 195
        sita = 196
        erf = 197
        bluetooth_hci_h4_with_phdr = 201
        ax25_kiss = 202
        lapd = 203
        ppp_with_dir = 204
        c_hdlc_with_dir = 205
        frelay_with_dir = 206
        ipmb_linux = 209
        ieee802_15_4_nonask_phy = 215
        usb_linux_mmapped = 220
        fc_2 = 224
        fc_2_with_frame_delims = 225
        ipnet = 226
        can_socketcan = 227
        ipv4 = 228
        ipv6 = 229
        ieee802_15_4_nofcs = 230
        dbus = 231
        dvb_ci = 235
        mux27010 = 236
        stanag_5066_d_pdu = 237
        nflog = 239
        netanalyzer = 240
        netanalyzer_transparent = 241
        ipoib = 242
        mpeg_2_ts = 243
        ng40 = 244
        nfc_llcp = 245
        infiniband = 247
        sctp = 248
        usbpcap = 249
        rtac_serial = 250
        bluetooth_le_ll = 251
        netlink = 253
        bluetooth_linux_monitor = 254
        bluetooth_bredr_bb = 255
        bluetooth_le_ll_with_phdr = 256
        profibus_dl = 257
        pktap = 258
        epon = 259
        ipmi_hpm_2 = 260
        zwave_r1_r2 = 261
        zwave_r3 = 262
        wattstopper_dlm = 263
        iso_14443 = 264
    SEQ_FIELDS = ["header", "fields", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = PacketPpi.PacketPpiHeader(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['fields']['start'] = self._io.pos()
        self._raw_fields = self._io.read_bytes((self.header.pph_len - 8))
        _io__raw_fields = KaitaiStream(BytesIO(self._raw_fields))
        self.fields = PacketPpi.PacketPpiFields(_io__raw_fields, self, self._root)
        self.fields._read()
        self._debug['fields']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        _on = self.header.pph_dlt
        if _on == PacketPpi.Linktype.ppi:
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = PacketPpi(_io__raw_body)
            self.body._read()
        elif _on == PacketPpi.Linktype.ethernet:
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = ethernet_frame.EthernetFrame(_io__raw_body)
            self.body._read()
        else:
            self.body = self._io.read_bytes_full()
        self._debug['body']['end'] = self._io.pos()

    class PacketPpiFields(KaitaiStruct):
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
                _t_entries = PacketPpi.PacketPpiField(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class Radio80211nMacExtBody(KaitaiStruct):
        """
        .. seealso::
           PPI header format spec, section 4.1.3 - https://web.archive.org/web/20090206112419/https://www.cacetech.com/documents/PPI_Header_format_1.0.1.pdf
        """
        SEQ_FIELDS = ["flags", "a_mpdu_id", "num_delimiters", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = PacketPpi.MacFlags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['a_mpdu_id']['start'] = self._io.pos()
            self.a_mpdu_id = self._io.read_u4le()
            self._debug['a_mpdu_id']['end'] = self._io.pos()
            self._debug['num_delimiters']['start'] = self._io.pos()
            self.num_delimiters = self._io.read_u1()
            self._debug['num_delimiters']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(3)
            self._debug['reserved']['end'] = self._io.pos()


    class MacFlags(KaitaiStruct):
        SEQ_FIELDS = ["unused1", "aggregate_delimiter", "more_aggregates", "aggregate", "dup_rx", "rx_short_guard", "is_ht_40", "greenfield", "unused2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['unused1']['start'] = self._io.pos()
            self.unused1 = self._io.read_bits_int_be(1) != 0
            self._debug['unused1']['end'] = self._io.pos()
            self._debug['aggregate_delimiter']['start'] = self._io.pos()
            self.aggregate_delimiter = self._io.read_bits_int_be(1) != 0
            self._debug['aggregate_delimiter']['end'] = self._io.pos()
            self._debug['more_aggregates']['start'] = self._io.pos()
            self.more_aggregates = self._io.read_bits_int_be(1) != 0
            self._debug['more_aggregates']['end'] = self._io.pos()
            self._debug['aggregate']['start'] = self._io.pos()
            self.aggregate = self._io.read_bits_int_be(1) != 0
            self._debug['aggregate']['end'] = self._io.pos()
            self._debug['dup_rx']['start'] = self._io.pos()
            self.dup_rx = self._io.read_bits_int_be(1) != 0
            self._debug['dup_rx']['end'] = self._io.pos()
            self._debug['rx_short_guard']['start'] = self._io.pos()
            self.rx_short_guard = self._io.read_bits_int_be(1) != 0
            self._debug['rx_short_guard']['end'] = self._io.pos()
            self._debug['is_ht_40']['start'] = self._io.pos()
            self.is_ht_40 = self._io.read_bits_int_be(1) != 0
            self._debug['is_ht_40']['end'] = self._io.pos()
            self._debug['greenfield']['start'] = self._io.pos()
            self.greenfield = self._io.read_bits_int_be(1) != 0
            self._debug['greenfield']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['unused2']['start'] = self._io.pos()
            self.unused2 = self._io.read_bytes(3)
            self._debug['unused2']['end'] = self._io.pos()


    class PacketPpiHeader(KaitaiStruct):
        """
        .. seealso::
           PPI header format spec, section 3.1 - https://web.archive.org/web/20090206112419/https://www.cacetech.com/documents/PPI_Header_format_1.0.1.pdf
        """
        SEQ_FIELDS = ["pph_version", "pph_flags", "pph_len", "pph_dlt"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['pph_version']['start'] = self._io.pos()
            self.pph_version = self._io.read_u1()
            self._debug['pph_version']['end'] = self._io.pos()
            self._debug['pph_flags']['start'] = self._io.pos()
            self.pph_flags = self._io.read_u1()
            self._debug['pph_flags']['end'] = self._io.pos()
            self._debug['pph_len']['start'] = self._io.pos()
            self.pph_len = self._io.read_u2le()
            self._debug['pph_len']['end'] = self._io.pos()
            self._debug['pph_dlt']['start'] = self._io.pos()
            self.pph_dlt = KaitaiStream.resolve_enum(PacketPpi.Linktype, self._io.read_u4le())
            self._debug['pph_dlt']['end'] = self._io.pos()


    class Radio80211CommonBody(KaitaiStruct):
        """
        .. seealso::
           PPI header format spec, section 4.1.2 - https://web.archive.org/web/20090206112419/https://www.cacetech.com/documents/PPI_Header_format_1.0.1.pdf
        """
        SEQ_FIELDS = ["tsf_timer", "flags", "rate", "channel_freq", "channel_flags", "fhss_hopset", "fhss_pattern", "dbm_antsignal", "dbm_antnoise"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['tsf_timer']['start'] = self._io.pos()
            self.tsf_timer = self._io.read_u8le()
            self._debug['tsf_timer']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['rate']['start'] = self._io.pos()
            self.rate = self._io.read_u2le()
            self._debug['rate']['end'] = self._io.pos()
            self._debug['channel_freq']['start'] = self._io.pos()
            self.channel_freq = self._io.read_u2le()
            self._debug['channel_freq']['end'] = self._io.pos()
            self._debug['channel_flags']['start'] = self._io.pos()
            self.channel_flags = self._io.read_u2le()
            self._debug['channel_flags']['end'] = self._io.pos()
            self._debug['fhss_hopset']['start'] = self._io.pos()
            self.fhss_hopset = self._io.read_u1()
            self._debug['fhss_hopset']['end'] = self._io.pos()
            self._debug['fhss_pattern']['start'] = self._io.pos()
            self.fhss_pattern = self._io.read_u1()
            self._debug['fhss_pattern']['end'] = self._io.pos()
            self._debug['dbm_antsignal']['start'] = self._io.pos()
            self.dbm_antsignal = self._io.read_s1()
            self._debug['dbm_antsignal']['end'] = self._io.pos()
            self._debug['dbm_antnoise']['start'] = self._io.pos()
            self.dbm_antnoise = self._io.read_s1()
            self._debug['dbm_antnoise']['end'] = self._io.pos()


    class PacketPpiField(KaitaiStruct):
        """
        .. seealso::
           PPI header format spec, section 3.1 - https://web.archive.org/web/20090206112419/https://www.cacetech.com/documents/PPI_Header_format_1.0.1.pdf
        """
        SEQ_FIELDS = ["pfh_type", "pfh_datalen", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['pfh_type']['start'] = self._io.pos()
            self.pfh_type = KaitaiStream.resolve_enum(PacketPpi.PfhType, self._io.read_u2le())
            self._debug['pfh_type']['end'] = self._io.pos()
            self._debug['pfh_datalen']['start'] = self._io.pos()
            self.pfh_datalen = self._io.read_u2le()
            self._debug['pfh_datalen']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.pfh_type
            if _on == PacketPpi.PfhType.radio_802_11_common:
                self._raw_body = self._io.read_bytes(self.pfh_datalen)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PacketPpi.Radio80211CommonBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == PacketPpi.PfhType.radio_802_11n_mac_ext:
                self._raw_body = self._io.read_bytes(self.pfh_datalen)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PacketPpi.Radio80211nMacExtBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == PacketPpi.PfhType.radio_802_11n_mac_phy_ext:
                self._raw_body = self._io.read_bytes(self.pfh_datalen)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PacketPpi.Radio80211nMacPhyExtBody(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes(self.pfh_datalen)
            self._debug['body']['end'] = self._io.pos()


    class Radio80211nMacPhyExtBody(KaitaiStruct):
        """
        .. seealso::
           PPI header format spec, section 4.1.4 - https://web.archive.org/web/20090206112419/https://www.cacetech.com/documents/PPI_Header_format_1.0.1.pdf
        """
        SEQ_FIELDS = ["flags", "a_mpdu_id", "num_delimiters", "mcs", "num_streams", "rssi_combined", "rssi_ant_ctl", "rssi_ant_ext", "ext_channel_freq", "ext_channel_flags", "rf_signal_noise", "evm"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = PacketPpi.MacFlags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['a_mpdu_id']['start'] = self._io.pos()
            self.a_mpdu_id = self._io.read_u4le()
            self._debug['a_mpdu_id']['end'] = self._io.pos()
            self._debug['num_delimiters']['start'] = self._io.pos()
            self.num_delimiters = self._io.read_u1()
            self._debug['num_delimiters']['end'] = self._io.pos()
            self._debug['mcs']['start'] = self._io.pos()
            self.mcs = self._io.read_u1()
            self._debug['mcs']['end'] = self._io.pos()
            self._debug['num_streams']['start'] = self._io.pos()
            self.num_streams = self._io.read_u1()
            self._debug['num_streams']['end'] = self._io.pos()
            self._debug['rssi_combined']['start'] = self._io.pos()
            self.rssi_combined = self._io.read_u1()
            self._debug['rssi_combined']['end'] = self._io.pos()
            self._debug['rssi_ant_ctl']['start'] = self._io.pos()
            self.rssi_ant_ctl = []
            for i in range(4):
                if not 'arr' in self._debug['rssi_ant_ctl']:
                    self._debug['rssi_ant_ctl']['arr'] = []
                self._debug['rssi_ant_ctl']['arr'].append({'start': self._io.pos()})
                self.rssi_ant_ctl.append(self._io.read_u1())
                self._debug['rssi_ant_ctl']['arr'][i]['end'] = self._io.pos()

            self._debug['rssi_ant_ctl']['end'] = self._io.pos()
            self._debug['rssi_ant_ext']['start'] = self._io.pos()
            self.rssi_ant_ext = []
            for i in range(4):
                if not 'arr' in self._debug['rssi_ant_ext']:
                    self._debug['rssi_ant_ext']['arr'] = []
                self._debug['rssi_ant_ext']['arr'].append({'start': self._io.pos()})
                self.rssi_ant_ext.append(self._io.read_u1())
                self._debug['rssi_ant_ext']['arr'][i]['end'] = self._io.pos()

            self._debug['rssi_ant_ext']['end'] = self._io.pos()
            self._debug['ext_channel_freq']['start'] = self._io.pos()
            self.ext_channel_freq = self._io.read_u2le()
            self._debug['ext_channel_freq']['end'] = self._io.pos()
            self._debug['ext_channel_flags']['start'] = self._io.pos()
            self.ext_channel_flags = PacketPpi.Radio80211nMacPhyExtBody.ChannelFlags(self._io, self, self._root)
            self.ext_channel_flags._read()
            self._debug['ext_channel_flags']['end'] = self._io.pos()
            self._debug['rf_signal_noise']['start'] = self._io.pos()
            self.rf_signal_noise = []
            for i in range(4):
                if not 'arr' in self._debug['rf_signal_noise']:
                    self._debug['rf_signal_noise']['arr'] = []
                self._debug['rf_signal_noise']['arr'].append({'start': self._io.pos()})
                _t_rf_signal_noise = PacketPpi.Radio80211nMacPhyExtBody.SignalNoise(self._io, self, self._root)
                _t_rf_signal_noise._read()
                self.rf_signal_noise.append(_t_rf_signal_noise)
                self._debug['rf_signal_noise']['arr'][i]['end'] = self._io.pos()

            self._debug['rf_signal_noise']['end'] = self._io.pos()
            self._debug['evm']['start'] = self._io.pos()
            self.evm = []
            for i in range(4):
                if not 'arr' in self._debug['evm']:
                    self._debug['evm']['arr'] = []
                self._debug['evm']['arr'].append({'start': self._io.pos()})
                self.evm.append(self._io.read_u4le())
                self._debug['evm']['arr'][i]['end'] = self._io.pos()

            self._debug['evm']['end'] = self._io.pos()

        class ChannelFlags(KaitaiStruct):
            SEQ_FIELDS = ["spectrum_2ghz", "ofdm", "cck", "turbo", "unused", "gfsk", "dyn_cck_ofdm", "only_passive_scan", "spectrum_5ghz"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['spectrum_2ghz']['start'] = self._io.pos()
                self.spectrum_2ghz = self._io.read_bits_int_be(1) != 0
                self._debug['spectrum_2ghz']['end'] = self._io.pos()
                self._debug['ofdm']['start'] = self._io.pos()
                self.ofdm = self._io.read_bits_int_be(1) != 0
                self._debug['ofdm']['end'] = self._io.pos()
                self._debug['cck']['start'] = self._io.pos()
                self.cck = self._io.read_bits_int_be(1) != 0
                self._debug['cck']['end'] = self._io.pos()
                self._debug['turbo']['start'] = self._io.pos()
                self.turbo = self._io.read_bits_int_be(1) != 0
                self._debug['turbo']['end'] = self._io.pos()
                self._debug['unused']['start'] = self._io.pos()
                self.unused = self._io.read_bits_int_be(8)
                self._debug['unused']['end'] = self._io.pos()
                self._debug['gfsk']['start'] = self._io.pos()
                self.gfsk = self._io.read_bits_int_be(1) != 0
                self._debug['gfsk']['end'] = self._io.pos()
                self._debug['dyn_cck_ofdm']['start'] = self._io.pos()
                self.dyn_cck_ofdm = self._io.read_bits_int_be(1) != 0
                self._debug['dyn_cck_ofdm']['end'] = self._io.pos()
                self._debug['only_passive_scan']['start'] = self._io.pos()
                self.only_passive_scan = self._io.read_bits_int_be(1) != 0
                self._debug['only_passive_scan']['end'] = self._io.pos()
                self._debug['spectrum_5ghz']['start'] = self._io.pos()
                self.spectrum_5ghz = self._io.read_bits_int_be(1) != 0
                self._debug['spectrum_5ghz']['end'] = self._io.pos()


        class SignalNoise(KaitaiStruct):
            """RF signal + noise pair at a single antenna."""
            SEQ_FIELDS = ["signal", "noise"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['signal']['start'] = self._io.pos()
                self.signal = self._io.read_s1()
                self._debug['signal']['end'] = self._io.pos()
                self._debug['noise']['start'] = self._io.pos()
                self.noise = self._io.read_s1()
                self._debug['noise']['end'] = self._io.pos()




