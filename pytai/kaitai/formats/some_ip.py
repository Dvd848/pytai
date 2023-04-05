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

import some_ip_sd
class SomeIp(KaitaiStruct):
    """SOME/IP (Scalable service-Oriented MiddlewarE over IP) is an automotive/embedded
    communication protocol which supports remoteprocedure calls, event notifications
    and the underlying serialization/wire format.
    
    .. seealso::
       Source - https://www.autosar.org/fileadmin/standards/foundation/19-11/AUTOSAR_PRS_SOMEIPProtocol.pdf
    """
    SEQ_FIELDS = ["header", "payload"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = SomeIp.Header(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['payload']['start'] = self._io.pos()
        _on = self.header.message_id.value
        if _on == 4294934784:
            self._raw_payload = self._io.read_bytes((self.header.length - 8))
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = some_ip_sd.SomeIpSd(_io__raw_payload)
            self.payload._read()
        else:
            self.payload = self._io.read_bytes((self.header.length - 8))
        self._debug['payload']['end'] = self._io.pos()

    class Header(KaitaiStruct):

        class MessageTypeEnum(Enum):
            request = 0
            request_no_return = 1
            notification = 2
            request_ack = 64
            request_no_return_ack = 65
            notification_ack = 66
            response = 128
            error = 129
            response_ack = 192
            error_ack = 193

        class ReturnCodeEnum(Enum):
            ok = 0
            not_ok = 1
            unknown_service = 2
            unknown_method = 3
            not_ready = 4
            not_reachable = 5
            time_out = 6
            wrong_protocol_version = 7
            wrong_interface_version = 8
            malformed_message = 9
            wrong_message_type = 10
        SEQ_FIELDS = ["message_id", "length", "request_id", "protocol_version", "interface_version", "message_type", "return_code"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['message_id']['start'] = self._io.pos()
            self._raw_message_id = self._io.read_bytes(4)
            _io__raw_message_id = KaitaiStream(BytesIO(self._raw_message_id))
            self.message_id = SomeIp.Header.MessageId(_io__raw_message_id, self, self._root)
            self.message_id._read()
            self._debug['message_id']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u4be()
            self._debug['length']['end'] = self._io.pos()
            self._debug['request_id']['start'] = self._io.pos()
            self._raw_request_id = self._io.read_bytes(4)
            _io__raw_request_id = KaitaiStream(BytesIO(self._raw_request_id))
            self.request_id = SomeIp.Header.RequestId(_io__raw_request_id, self, self._root)
            self.request_id._read()
            self._debug['request_id']['end'] = self._io.pos()
            self._debug['protocol_version']['start'] = self._io.pos()
            self.protocol_version = self._io.read_u1()
            self._debug['protocol_version']['end'] = self._io.pos()
            self._debug['interface_version']['start'] = self._io.pos()
            self.interface_version = self._io.read_u1()
            self._debug['interface_version']['end'] = self._io.pos()
            self._debug['message_type']['start'] = self._io.pos()
            self.message_type = KaitaiStream.resolve_enum(SomeIp.Header.MessageTypeEnum, self._io.read_u1())
            self._debug['message_type']['end'] = self._io.pos()
            self._debug['return_code']['start'] = self._io.pos()
            self.return_code = KaitaiStream.resolve_enum(SomeIp.Header.ReturnCodeEnum, self._io.read_u1())
            self._debug['return_code']['end'] = self._io.pos()

        class MessageId(KaitaiStruct):
            """[PRS_SOMEIP_00035] The assignment of the Message ID shall be up to
            the user. However, the Message ID shall be unique for the whole
            system (i.e. the vehicle). TheMessage ID is similar to a CAN ID and
            should be handled via a comparable process.
            [PRS_SOMEIP_00038] Message IDs of method calls shall be structured in
            the ID with 2^16 services with 2^15 methods.
            
            .. seealso::
               AUTOSAR_PRS_SOMEIPProtocol.pdf 4.1.1.1  Message ID
            """
            SEQ_FIELDS = ["service_id", "sub_id", "method_id", "event_id"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['service_id']['start'] = self._io.pos()
                self.service_id = self._io.read_u2be()
                self._debug['service_id']['end'] = self._io.pos()
                self._debug['sub_id']['start'] = self._io.pos()
                self.sub_id = self._io.read_bits_int_be(1) != 0
                self._debug['sub_id']['end'] = self._io.pos()
                if self.sub_id == False:
                    self._debug['method_id']['start'] = self._io.pos()
                    self.method_id = self._io.read_bits_int_be(15)
                    self._debug['method_id']['end'] = self._io.pos()

                if self.sub_id == True:
                    self._debug['event_id']['start'] = self._io.pos()
                    self.event_id = self._io.read_bits_int_be(15)
                    self._debug['event_id']['end'] = self._io.pos()


            @property
            def value(self):
                """The value provides the undissected Message ID."""
                if hasattr(self, '_m_value'):
                    return self._m_value

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_value']['start'] = self._io.pos()
                self._m_value = self._io.read_u4be()
                self._debug['_m_value']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_value', None)


        class RequestId(KaitaiStruct):
            """The Request ID allows a provider and subscriber to differentiate
            multiple parallel usesof the same method, event, getter or setter.
            
            .. seealso::
               AUTOSAR_PRS_SOMEIPProtocol.pdf - section 4.1.1.3  Request ID
            """
            SEQ_FIELDS = ["client_id", "session_id"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['client_id']['start'] = self._io.pos()
                self.client_id = self._io.read_u2be()
                self._debug['client_id']['end'] = self._io.pos()
                self._debug['session_id']['start'] = self._io.pos()
                self.session_id = self._io.read_u2be()
                self._debug['session_id']['end'] = self._io.pos()

            @property
            def value(self):
                """The value provides the undissected Request ID."""
                if hasattr(self, '_m_value'):
                    return self._m_value

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_value']['start'] = self._io.pos()
                self._m_value = self._io.read_u4be()
                self._debug['_m_value']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_value', None)


        @property
        def is_valid_service_discovery(self):
            """auxillary value.
            
            .. seealso::
               AUTOSAR_PRS_SOMEIPServiceDiscoveryProtocol.pdf - section 4.1.2.1 General Requirements
            """
            if hasattr(self, '_m_is_valid_service_discovery'):
                return self._m_is_valid_service_discovery

            self._m_is_valid_service_discovery =  ((self.message_id.value == 4294934784) and (self.protocol_version == 1) and (self.interface_version == 1) and (self.message_type == SomeIp.Header.MessageTypeEnum.notification) and (self.return_code == SomeIp.Header.ReturnCodeEnum.ok)) 
            return getattr(self, '_m_is_valid_service_discovery', None)



