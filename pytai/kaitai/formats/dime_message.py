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

class DimeMessage(KaitaiStruct):
    """Direct Internet Message Encapsulation (DIME)
    is an old Microsoft specification for sending and receiving
    SOAP messages along with additional attachments,
    like binary files, XML fragments, and even other
    SOAP messages, using standard transport protocols like HTTP.
    
    Sample file: `curl -LO
    https://github.com/kaitai-io/kaitai_struct_formats/files/5894723/scanner_withoptions.dump.gz
    && gunzip scanner_withoptions.dump.gz`
    
    .. seealso::
       Source - https://datatracker.ietf.org/doc/html/draft-nielsen-dime-02
    
    
    .. seealso::
       Source - https://learn.microsoft.com/en-us/archive/msdn-magazine/2002/december/sending-files-attachments-and-soap-messages-via-dime
    
    
    .. seealso::
       Source - http://imrannazar.com/Parsing-the-DIME-Message-Format
    """

    class TypeFormats(Enum):
        unchanged = 0
        media_type = 1
        absolute_uri = 2
        unknown = 3
        none = 4
    SEQ_FIELDS = ["records"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['records']['start'] = self._io.pos()
        self.records = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['records']:
                self._debug['records']['arr'] = []
            self._debug['records']['arr'].append({'start': self._io.pos()})
            _t_records = DimeMessage.Record(self._io, self, self._root)
            _t_records._read()
            self.records.append(_t_records)
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['records']['end'] = self._io.pos()

    class Padding(KaitaiStruct):
        """padding to the next 4-byte boundary."""
        SEQ_FIELDS = ["boundary_padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['boundary_padding']['start'] = self._io.pos()
            self.boundary_padding = self._io.read_bytes((-(self._io.pos()) % 4))
            self._debug['boundary_padding']['end'] = self._io.pos()


    class OptionField(KaitaiStruct):
        """the option field of the record."""
        SEQ_FIELDS = ["option_elements"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['option_elements']['start'] = self._io.pos()
            self.option_elements = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['option_elements']:
                    self._debug['option_elements']['arr'] = []
                self._debug['option_elements']['arr'].append({'start': self._io.pos()})
                _t_option_elements = DimeMessage.OptionElement(self._io, self, self._root)
                _t_option_elements._read()
                self.option_elements.append(_t_option_elements)
                self._debug['option_elements']['arr'][len(self.option_elements) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['option_elements']['end'] = self._io.pos()


    class OptionElement(KaitaiStruct):
        """one element of the option field."""
        SEQ_FIELDS = ["element_format", "len_element", "element_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['element_format']['start'] = self._io.pos()
            self.element_format = self._io.read_u2be()
            self._debug['element_format']['end'] = self._io.pos()
            self._debug['len_element']['start'] = self._io.pos()
            self.len_element = self._io.read_u2be()
            self._debug['len_element']['end'] = self._io.pos()
            self._debug['element_data']['start'] = self._io.pos()
            self.element_data = self._io.read_bytes(self.len_element)
            self._debug['element_data']['end'] = self._io.pos()


    class Record(KaitaiStruct):
        """each individual fragment of the message."""
        SEQ_FIELDS = ["version", "is_first_record", "is_last_record", "is_chunk_record", "type_format", "reserved", "len_options", "len_id", "len_type", "len_data", "options", "options_padding", "id", "id_padding", "type", "type_padding", "data", "data_padding"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bits_int_be(5)
            self._debug['version']['end'] = self._io.pos()
            self._debug['is_first_record']['start'] = self._io.pos()
            self.is_first_record = self._io.read_bits_int_be(1) != 0
            self._debug['is_first_record']['end'] = self._io.pos()
            self._debug['is_last_record']['start'] = self._io.pos()
            self.is_last_record = self._io.read_bits_int_be(1) != 0
            self._debug['is_last_record']['end'] = self._io.pos()
            self._debug['is_chunk_record']['start'] = self._io.pos()
            self.is_chunk_record = self._io.read_bits_int_be(1) != 0
            self._debug['is_chunk_record']['end'] = self._io.pos()
            self._debug['type_format']['start'] = self._io.pos()
            self.type_format = KaitaiStream.resolve_enum(DimeMessage.TypeFormats, self._io.read_bits_int_be(4))
            self._debug['type_format']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bits_int_be(4)
            self._debug['reserved']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['len_options']['start'] = self._io.pos()
            self.len_options = self._io.read_u2be()
            self._debug['len_options']['end'] = self._io.pos()
            self._debug['len_id']['start'] = self._io.pos()
            self.len_id = self._io.read_u2be()
            self._debug['len_id']['end'] = self._io.pos()
            self._debug['len_type']['start'] = self._io.pos()
            self.len_type = self._io.read_u2be()
            self._debug['len_type']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self._raw_options = self._io.read_bytes(self.len_options)
            _io__raw_options = KaitaiStream(BytesIO(self._raw_options))
            self.options = DimeMessage.OptionField(_io__raw_options, self, self._root)
            self.options._read()
            self._debug['options']['end'] = self._io.pos()
            self._debug['options_padding']['start'] = self._io.pos()
            self.options_padding = DimeMessage.Padding(self._io, self, self._root)
            self.options_padding._read()
            self._debug['options_padding']['end'] = self._io.pos()
            self._debug['id']['start'] = self._io.pos()
            self.id = (self._io.read_bytes(self.len_id)).decode(u"ASCII")
            self._debug['id']['end'] = self._io.pos()
            self._debug['id_padding']['start'] = self._io.pos()
            self.id_padding = DimeMessage.Padding(self._io, self, self._root)
            self.id_padding._read()
            self._debug['id_padding']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = (self._io.read_bytes(self.len_type)).decode(u"ASCII")
            self._debug['type']['end'] = self._io.pos()
            self._debug['type_padding']['start'] = self._io.pos()
            self.type_padding = DimeMessage.Padding(self._io, self, self._root)
            self.type_padding._read()
            self._debug['type_padding']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()
            self._debug['data_padding']['start'] = self._io.pos()
            self.data_padding = DimeMessage.Padding(self._io, self, self._root)
            self.data_padding._read()
            self._debug['data_padding']['end'] = self._io.pos()



