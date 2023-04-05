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

class Luks(KaitaiStruct):
    """Linux Unified Key Setup (LUKS) is a format specification for storing disk
    encryption parameters and up to 8 user keys (which can unlock the master key).
    
    .. seealso::
       Source - https://gitlab.com/cryptsetup/cryptsetup/-/wikis/LUKS-standard/on-disk-format.pdf
    """
    SEQ_FIELDS = ["partition_header"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['partition_header']['start'] = self._io.pos()
        self.partition_header = Luks.PartitionHeader(self._io, self, self._root)
        self.partition_header._read()
        self._debug['partition_header']['end'] = self._io.pos()

    class PartitionHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "cipher_name_specification", "cipher_mode_specification", "hash_specification", "payload_offset", "number_of_key_bytes", "master_key_checksum", "master_key_salt_parameter", "master_key_iterations_parameter", "uuid", "key_slots"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(6)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4C\x55\x4B\x53\xBA\xBE":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x55\x4B\x53\xBA\xBE", self.magic, self._io, u"/types/partition_header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(2)
            self._debug['version']['end'] = self._io.pos()
            if not self.version == b"\x00\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x01", self.version, self._io, u"/types/partition_header/seq/1")
            self._debug['cipher_name_specification']['start'] = self._io.pos()
            self.cipher_name_specification = (self._io.read_bytes(32)).decode(u"ASCII")
            self._debug['cipher_name_specification']['end'] = self._io.pos()
            self._debug['cipher_mode_specification']['start'] = self._io.pos()
            self.cipher_mode_specification = (self._io.read_bytes(32)).decode(u"ASCII")
            self._debug['cipher_mode_specification']['end'] = self._io.pos()
            self._debug['hash_specification']['start'] = self._io.pos()
            self.hash_specification = (self._io.read_bytes(32)).decode(u"ASCII")
            self._debug['hash_specification']['end'] = self._io.pos()
            self._debug['payload_offset']['start'] = self._io.pos()
            self.payload_offset = self._io.read_u4be()
            self._debug['payload_offset']['end'] = self._io.pos()
            self._debug['number_of_key_bytes']['start'] = self._io.pos()
            self.number_of_key_bytes = self._io.read_u4be()
            self._debug['number_of_key_bytes']['end'] = self._io.pos()
            self._debug['master_key_checksum']['start'] = self._io.pos()
            self.master_key_checksum = self._io.read_bytes(20)
            self._debug['master_key_checksum']['end'] = self._io.pos()
            self._debug['master_key_salt_parameter']['start'] = self._io.pos()
            self.master_key_salt_parameter = self._io.read_bytes(32)
            self._debug['master_key_salt_parameter']['end'] = self._io.pos()
            self._debug['master_key_iterations_parameter']['start'] = self._io.pos()
            self.master_key_iterations_parameter = self._io.read_u4be()
            self._debug['master_key_iterations_parameter']['end'] = self._io.pos()
            self._debug['uuid']['start'] = self._io.pos()
            self.uuid = (self._io.read_bytes(40)).decode(u"ASCII")
            self._debug['uuid']['end'] = self._io.pos()
            self._debug['key_slots']['start'] = self._io.pos()
            self.key_slots = []
            for i in range(8):
                if not 'arr' in self._debug['key_slots']:
                    self._debug['key_slots']['arr'] = []
                self._debug['key_slots']['arr'].append({'start': self._io.pos()})
                _t_key_slots = Luks.PartitionHeader.KeySlot(self._io, self, self._root)
                _t_key_slots._read()
                self.key_slots.append(_t_key_slots)
                self._debug['key_slots']['arr'][i]['end'] = self._io.pos()

            self._debug['key_slots']['end'] = self._io.pos()

        class KeySlot(KaitaiStruct):

            class KeySlotStates(Enum):
                disabled_key_slot = 57005
                enabled_key_slot = 11301363
            SEQ_FIELDS = ["state_of_key_slot", "iteration_parameter", "salt_parameter", "start_sector_of_key_material", "number_of_anti_forensic_stripes"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['state_of_key_slot']['start'] = self._io.pos()
                self.state_of_key_slot = KaitaiStream.resolve_enum(Luks.PartitionHeader.KeySlot.KeySlotStates, self._io.read_u4be())
                self._debug['state_of_key_slot']['end'] = self._io.pos()
                self._debug['iteration_parameter']['start'] = self._io.pos()
                self.iteration_parameter = self._io.read_u4be()
                self._debug['iteration_parameter']['end'] = self._io.pos()
                self._debug['salt_parameter']['start'] = self._io.pos()
                self.salt_parameter = self._io.read_bytes(32)
                self._debug['salt_parameter']['end'] = self._io.pos()
                self._debug['start_sector_of_key_material']['start'] = self._io.pos()
                self.start_sector_of_key_material = self._io.read_u4be()
                self._debug['start_sector_of_key_material']['end'] = self._io.pos()
                self._debug['number_of_anti_forensic_stripes']['start'] = self._io.pos()
                self.number_of_anti_forensic_stripes = self._io.read_u4be()
                self._debug['number_of_anti_forensic_stripes']['end'] = self._io.pos()

            @property
            def key_material(self):
                if hasattr(self, '_m_key_material'):
                    return self._m_key_material

                _pos = self._io.pos()
                self._io.seek((self.start_sector_of_key_material * 512))
                self._debug['_m_key_material']['start'] = self._io.pos()
                self._m_key_material = self._io.read_bytes((self._parent.number_of_key_bytes * self.number_of_anti_forensic_stripes))
                self._debug['_m_key_material']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_key_material', None)



    @property
    def payload(self):
        if hasattr(self, '_m_payload'):
            return self._m_payload

        _pos = self._io.pos()
        self._io.seek((self.partition_header.payload_offset * 512))
        self._debug['_m_payload']['start'] = self._io.pos()
        self._m_payload = self._io.read_bytes_full()
        self._debug['_m_payload']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_payload', None)


