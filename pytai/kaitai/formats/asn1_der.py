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

class Asn1Der(KaitaiStruct):
    """ASN.1 (Abstract Syntax Notation One) DER (Distinguished Encoding
    Rules) is a standard-backed serialization scheme used in many
    different use-cases. Particularly popular usage scenarios are X.509
    certificates and some telecommunication / networking protocols.
    
    DER is self-describing encoding scheme which allows representation
    of simple, atomic data elements, such as strings and numbers, and
    complex objects, such as sequences of other elements.
    
    DER is a subset of BER (Basic Encoding Rules), with an emphasis on
    being non-ambiguous: there's always exactly one canonical way to
    encode a data structure defined in terms of ASN.1 using DER.
    
    This spec allows full parsing of format syntax, but to understand
    the semantics, one would typically require a dictionary of Object
    Identifiers (OIDs), to match OID bodies against some human-readable
    list of constants. OIDs are covered by many different standards,
    so typically it's simpler to use a pre-compiled list of them, such
    as:
    
    * <https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.cfg>
    * <http://oid-info.com/>
    * <https://www.alvestrand.no/objectid/top.html>
    
    .. seealso::
       Source - https://www.itu.int/itu-t/recommendations/rec.aspx?rec=12483&lang=en
    """

    class TypeTag(Enum):
        end_of_content = 0
        boolean = 1
        integer = 2
        bit_string = 3
        octet_string = 4
        null_value = 5
        object_id = 6
        object_descriptor = 7
        external = 8
        real = 9
        enumerated = 10
        embedded_pdv = 11
        utf8string = 12
        relative_oid = 13
        sequence_10 = 16
        printable_string = 19
        ia5string = 22
        sequence_30 = 48
        set = 49
    SEQ_FIELDS = ["type_tag", "len", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['type_tag']['start'] = self._io.pos()
        self.type_tag = KaitaiStream.resolve_enum(Asn1Der.TypeTag, self._io.read_u1())
        self._debug['type_tag']['end'] = self._io.pos()
        self._debug['len']['start'] = self._io.pos()
        self.len = Asn1Der.LenEncoded(self._io, self, self._root)
        self.len._read()
        self._debug['len']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        _on = self.type_tag
        if _on == Asn1Der.TypeTag.printable_string:
            self._raw_body = self._io.read_bytes(self.len.result)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Asn1Der.BodyPrintableString(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == Asn1Der.TypeTag.sequence_10:
            self._raw_body = self._io.read_bytes(self.len.result)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Asn1Der.BodySequence(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == Asn1Der.TypeTag.set:
            self._raw_body = self._io.read_bytes(self.len.result)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Asn1Der.BodySequence(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == Asn1Der.TypeTag.sequence_30:
            self._raw_body = self._io.read_bytes(self.len.result)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Asn1Der.BodySequence(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == Asn1Der.TypeTag.utf8string:
            self._raw_body = self._io.read_bytes(self.len.result)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Asn1Der.BodyUtf8string(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == Asn1Der.TypeTag.object_id:
            self._raw_body = self._io.read_bytes(self.len.result)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Asn1Der.BodyObjectId(_io__raw_body, self, self._root)
            self.body._read()
        else:
            self.body = self._io.read_bytes(self.len.result)
        self._debug['body']['end'] = self._io.pos()

    class BodySequence(KaitaiStruct):
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
                _t_entries = Asn1Der(self._io)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class BodyUtf8string(KaitaiStruct):
        SEQ_FIELDS = ["str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._debug['str']['end'] = self._io.pos()


    class BodyObjectId(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/seccertenroll/about-object-identifier
        """
        SEQ_FIELDS = ["first_and_second", "rest"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['first_and_second']['start'] = self._io.pos()
            self.first_and_second = self._io.read_u1()
            self._debug['first_and_second']['end'] = self._io.pos()
            self._debug['rest']['start'] = self._io.pos()
            self.rest = self._io.read_bytes_full()
            self._debug['rest']['end'] = self._io.pos()

        @property
        def first(self):
            if hasattr(self, '_m_first'):
                return self._m_first

            self._m_first = self.first_and_second // 40
            return getattr(self, '_m_first', None)

        @property
        def second(self):
            if hasattr(self, '_m_second'):
                return self._m_second

            self._m_second = (self.first_and_second % 40)
            return getattr(self, '_m_second', None)


    class LenEncoded(KaitaiStruct):
        SEQ_FIELDS = ["b1", "int2", "int1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['b1']['start'] = self._io.pos()
            self.b1 = self._io.read_u1()
            self._debug['b1']['end'] = self._io.pos()
            if self.b1 == 130:
                self._debug['int2']['start'] = self._io.pos()
                self.int2 = self._io.read_u2be()
                self._debug['int2']['end'] = self._io.pos()

            if self.b1 == 129:
                self._debug['int1']['start'] = self._io.pos()
                self.int1 = self._io.read_u1()
                self._debug['int1']['end'] = self._io.pos()


        @property
        def result(self):
            if hasattr(self, '_m_result'):
                return self._m_result

            self._m_result = (self.int1 if self.b1 == 129 else (self.int2 if self.b1 == 130 else self.b1))
            return getattr(self, '_m_result', None)


    class BodyPrintableString(KaitaiStruct):
        SEQ_FIELDS = ["str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes_full()).decode(u"ASCII")
            self._debug['str']['end'] = self._io.pos()



