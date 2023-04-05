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

class SomeIpSdOptions(KaitaiStruct):
    """FormatOptions are used to transport additional information to the entries.
    This includes forinstance the information how a service instance is
    reachable (IP-Address, TransportProtocol, Port Number).
    
    .. seealso::
       section 4.1.2.4 Options Format - https://www.autosar.org/fileadmin/standards/foundation/19-11/AUTOSAR_PRS_SOMEIPServiceDiscoveryProtocol.pdf
       -
    """
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
            _t_entries = SomeIpSdOptions.SdOption(self._io, self, self._root)
            _t_entries._read()
            self.entries.append(_t_entries)
            self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['entries']['end'] = self._io.pos()

    class SdOption(KaitaiStruct):

        class OptionTypes(Enum):
            configuration_option = 1
            load_balancing_option = 2
            ipv4_endpoint_option = 4
            ipv6_endpoint_option = 6
            ipv4_multicast_option = 20
            ipv6_multicast_option = 22
            ipv4_sd_endpoint_option = 36
            ipv6_sd_endpoint_option = 38
        SEQ_FIELDS = ["header", "content"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = SomeIpSdOptions.SdOption.SdOptionHeader(self._io, self, self._root)
            self.header._read()
            self._debug['header']['end'] = self._io.pos()
            self._debug['content']['start'] = self._io.pos()
            _on = self.header.type
            if _on == SomeIpSdOptions.SdOption.OptionTypes.load_balancing_option:
                self.content = SomeIpSdOptions.SdOption.SdLoadBalancingOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.configuration_option:
                self.content = SomeIpSdOptions.SdOption.SdConfigurationOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.ipv4_sd_endpoint_option:
                self.content = SomeIpSdOptions.SdOption.SdIpv4SdEndpointOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.ipv4_endpoint_option:
                self.content = SomeIpSdOptions.SdOption.SdIpv4EndpointOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.ipv6_sd_endpoint_option:
                self.content = SomeIpSdOptions.SdOption.SdIpv6SdEndpointOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.ipv4_multicast_option:
                self.content = SomeIpSdOptions.SdOption.SdIpv4MulticastOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.ipv6_endpoint_option:
                self.content = SomeIpSdOptions.SdOption.SdIpv6EndpointOption(self._io, self, self._root)
                self.content._read()
            elif _on == SomeIpSdOptions.SdOption.OptionTypes.ipv6_multicast_option:
                self.content = SomeIpSdOptions.SdOption.SdIpv6MulticastOption(self._io, self, self._root)
                self.content._read()
            self._debug['content']['end'] = self._io.pos()

        class SdOptionHeader(KaitaiStruct):
            SEQ_FIELDS = ["length", "type"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u2be()
                self._debug['length']['end'] = self._io.pos()
                self._debug['type']['start'] = self._io.pos()
                self.type = KaitaiStream.resolve_enum(SomeIpSdOptions.SdOption.OptionTypes, self._io.read_u1())
                self._debug['type']['end'] = self._io.pos()


        class SdConfigString(KaitaiStruct):
            SEQ_FIELDS = ["length", "config"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u1()
                self._debug['length']['end'] = self._io.pos()
                if self.length != 0:
                    self._debug['config']['start'] = self._io.pos()
                    self._raw_config = self._io.read_bytes(self.length)
                    _io__raw_config = KaitaiStream(BytesIO(self._raw_config))
                    self.config = SomeIpSdOptions.SdOption.SdConfigKvPair(_io__raw_config, self, self._root)
                    self.config._read()
                    self._debug['config']['end'] = self._io.pos()



        class SdConfigStringsContainer(KaitaiStruct):
            SEQ_FIELDS = ["config_strings"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['config_strings']['start'] = self._io.pos()
                self.config_strings = []
                i = 0
                while not self._io.is_eof():
                    if not 'arr' in self._debug['config_strings']:
                        self._debug['config_strings']['arr'] = []
                    self._debug['config_strings']['arr'].append({'start': self._io.pos()})
                    _t_config_strings = SomeIpSdOptions.SdOption.SdConfigString(self._io, self, self._root)
                    _t_config_strings._read()
                    self.config_strings.append(_t_config_strings)
                    self._debug['config_strings']['arr'][len(self.config_strings) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['config_strings']['end'] = self._io.pos()


        class SdConfigurationOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "configurations"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['configurations']['start'] = self._io.pos()
                self._raw_configurations = self._io.read_bytes((self._parent.header.length - 1))
                _io__raw_configurations = KaitaiStream(BytesIO(self._raw_configurations))
                self.configurations = SomeIpSdOptions.SdOption.SdConfigStringsContainer(_io__raw_configurations, self, self._root)
                self.configurations._read()
                self._debug['configurations']['end'] = self._io.pos()


        class SdIpv4MulticastOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "address", "reserved2", "l4_protocol", "port"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['address']['start'] = self._io.pos()
                self.address = self._io.read_bytes(4)
                self._debug['address']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_u1()
                self._debug['reserved2']['end'] = self._io.pos()
                self._debug['l4_protocol']['start'] = self._io.pos()
                self.l4_protocol = self._io.read_u1()
                self._debug['l4_protocol']['end'] = self._io.pos()
                self._debug['port']['start'] = self._io.pos()
                self.port = self._io.read_u2be()
                self._debug['port']['end'] = self._io.pos()


        class SdIpv4SdEndpointOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "address", "reserved2", "l4_protocol", "port"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['address']['start'] = self._io.pos()
                self.address = self._io.read_bytes(4)
                self._debug['address']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_u1()
                self._debug['reserved2']['end'] = self._io.pos()
                self._debug['l4_protocol']['start'] = self._io.pos()
                self.l4_protocol = self._io.read_u1()
                self._debug['l4_protocol']['end'] = self._io.pos()
                self._debug['port']['start'] = self._io.pos()
                self.port = self._io.read_u2be()
                self._debug['port']['end'] = self._io.pos()


        class SdIpv6MulticastOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "address", "reserved2", "l4_protocol", "port"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['address']['start'] = self._io.pos()
                self.address = self._io.read_bytes(16)
                self._debug['address']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_u1()
                self._debug['reserved2']['end'] = self._io.pos()
                self._debug['l4_protocol']['start'] = self._io.pos()
                self.l4_protocol = self._io.read_u1()
                self._debug['l4_protocol']['end'] = self._io.pos()
                self._debug['port']['start'] = self._io.pos()
                self.port = self._io.read_u2be()
                self._debug['port']['end'] = self._io.pos()


        class SdConfigKvPair(KaitaiStruct):
            SEQ_FIELDS = ["key", "value"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['key']['start'] = self._io.pos()
                self.key = (self._io.read_bytes_term(61, False, True, True)).decode(u"ASCII")
                self._debug['key']['end'] = self._io.pos()
                self._debug['value']['start'] = self._io.pos()
                self.value = (self._io.read_bytes_full()).decode(u"ASCII")
                self._debug['value']['end'] = self._io.pos()


        class SdIpv6SdEndpointOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "address", "reserved2", "l4_protocol", "port"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['address']['start'] = self._io.pos()
                self.address = self._io.read_bytes(16)
                self._debug['address']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_u1()
                self._debug['reserved2']['end'] = self._io.pos()
                self._debug['l4_protocol']['start'] = self._io.pos()
                self.l4_protocol = self._io.read_u1()
                self._debug['l4_protocol']['end'] = self._io.pos()
                self._debug['port']['start'] = self._io.pos()
                self.port = self._io.read_u2be()
                self._debug['port']['end'] = self._io.pos()


        class SdIpv4EndpointOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "address", "reserved2", "l4_protocol", "port"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['address']['start'] = self._io.pos()
                self.address = self._io.read_bytes(4)
                self._debug['address']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_u1()
                self._debug['reserved2']['end'] = self._io.pos()
                self._debug['l4_protocol']['start'] = self._io.pos()
                self.l4_protocol = self._io.read_u1()
                self._debug['l4_protocol']['end'] = self._io.pos()
                self._debug['port']['start'] = self._io.pos()
                self.port = self._io.read_u2be()
                self._debug['port']['end'] = self._io.pos()


        class SdIpv6EndpointOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "address", "reserved2", "l4_protocol", "port"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['address']['start'] = self._io.pos()
                self.address = self._io.read_bytes(16)
                self._debug['address']['end'] = self._io.pos()
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_u1()
                self._debug['reserved2']['end'] = self._io.pos()
                self._debug['l4_protocol']['start'] = self._io.pos()
                self.l4_protocol = self._io.read_u1()
                self._debug['l4_protocol']['end'] = self._io.pos()
                self._debug['port']['start'] = self._io.pos()
                self.port = self._io.read_u2be()
                self._debug['port']['end'] = self._io.pos()


        class SdLoadBalancingOption(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "priority", "weight"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u1()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['priority']['start'] = self._io.pos()
                self.priority = self._io.read_u2be()
                self._debug['priority']['end'] = self._io.pos()
                self._debug['weight']['start'] = self._io.pos()
                self.weight = self._io.read_u2be()
                self._debug['weight']['end'] = self._io.pos()




