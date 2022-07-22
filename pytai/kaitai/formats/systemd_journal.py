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

class SystemdJournal(KaitaiStruct):
    """systemd, a popular user-space system/service management suite on Linux,
    offers logging functionality, storing incoming logs in a binary journal
    format.
    
    On live Linux system running systemd, these journals are typically located at:
    
    * /run/log/journal/machine-id/*.journal (volatile, lost after reboot)
    * /var/log/journal/machine-id/*.journal (persistent, but disabled by default on Debian / Ubuntu)
    
    .. seealso::
       Source - https://www.freedesktop.org/wiki/Software/systemd/journal-files/
    """

    class State(Enum):
        offline = 0
        online = 1
        archived = 2
    SEQ_FIELDS = ["header", "objects"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(self.len_header)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = SystemdJournal.Header(_io__raw_header, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['objects']['start'] = self._io.pos()
        self.objects = []
        for i in range(self.header.num_objects):
            if not 'arr' in self._debug['objects']:
                self._debug['objects']['arr'] = []
            self._debug['objects']['arr'].append({'start': self._io.pos()})
            _t_objects = SystemdJournal.JournalObject(self._io, self, self._root)
            _t_objects._read()
            self.objects.append(_t_objects)
            self._debug['objects']['arr'][i]['end'] = self._io.pos()

        self._debug['objects']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "compatible_flags", "incompatible_flags", "state", "reserved", "file_id", "machine_id", "boot_id", "seqnum_id", "len_header", "len_arena", "ofs_data_hash_table", "len_data_hash_table", "ofs_field_hash_table", "len_field_hash_table", "ofs_tail_object", "num_objects", "num_entries", "tail_entry_seqnum", "head_entry_seqnum", "ofs_entry_array", "head_entry_realtime", "tail_entry_realtime", "tail_entry_monotonic", "num_data", "num_fields", "num_tags", "num_entry_arrays"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(8)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x4C\x50\x4B\x53\x48\x48\x52\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x50\x4B\x53\x48\x48\x52\x48", self.signature, self._io, u"/types/header/seq/0")
            self._debug['compatible_flags']['start'] = self._io.pos()
            self.compatible_flags = self._io.read_u4le()
            self._debug['compatible_flags']['end'] = self._io.pos()
            self._debug['incompatible_flags']['start'] = self._io.pos()
            self.incompatible_flags = self._io.read_u4le()
            self._debug['incompatible_flags']['end'] = self._io.pos()
            self._debug['state']['start'] = self._io.pos()
            self.state = KaitaiStream.resolve_enum(SystemdJournal.State, self._io.read_u1())
            self._debug['state']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(7)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['file_id']['start'] = self._io.pos()
            self.file_id = self._io.read_bytes(16)
            self._debug['file_id']['end'] = self._io.pos()
            self._debug['machine_id']['start'] = self._io.pos()
            self.machine_id = self._io.read_bytes(16)
            self._debug['machine_id']['end'] = self._io.pos()
            self._debug['boot_id']['start'] = self._io.pos()
            self.boot_id = self._io.read_bytes(16)
            self._debug['boot_id']['end'] = self._io.pos()
            self._debug['seqnum_id']['start'] = self._io.pos()
            self.seqnum_id = self._io.read_bytes(16)
            self._debug['seqnum_id']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u8le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_arena']['start'] = self._io.pos()
            self.len_arena = self._io.read_u8le()
            self._debug['len_arena']['end'] = self._io.pos()
            self._debug['ofs_data_hash_table']['start'] = self._io.pos()
            self.ofs_data_hash_table = self._io.read_u8le()
            self._debug['ofs_data_hash_table']['end'] = self._io.pos()
            self._debug['len_data_hash_table']['start'] = self._io.pos()
            self.len_data_hash_table = self._io.read_u8le()
            self._debug['len_data_hash_table']['end'] = self._io.pos()
            self._debug['ofs_field_hash_table']['start'] = self._io.pos()
            self.ofs_field_hash_table = self._io.read_u8le()
            self._debug['ofs_field_hash_table']['end'] = self._io.pos()
            self._debug['len_field_hash_table']['start'] = self._io.pos()
            self.len_field_hash_table = self._io.read_u8le()
            self._debug['len_field_hash_table']['end'] = self._io.pos()
            self._debug['ofs_tail_object']['start'] = self._io.pos()
            self.ofs_tail_object = self._io.read_u8le()
            self._debug['ofs_tail_object']['end'] = self._io.pos()
            self._debug['num_objects']['start'] = self._io.pos()
            self.num_objects = self._io.read_u8le()
            self._debug['num_objects']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u8le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['tail_entry_seqnum']['start'] = self._io.pos()
            self.tail_entry_seqnum = self._io.read_u8le()
            self._debug['tail_entry_seqnum']['end'] = self._io.pos()
            self._debug['head_entry_seqnum']['start'] = self._io.pos()
            self.head_entry_seqnum = self._io.read_u8le()
            self._debug['head_entry_seqnum']['end'] = self._io.pos()
            self._debug['ofs_entry_array']['start'] = self._io.pos()
            self.ofs_entry_array = self._io.read_u8le()
            self._debug['ofs_entry_array']['end'] = self._io.pos()
            self._debug['head_entry_realtime']['start'] = self._io.pos()
            self.head_entry_realtime = self._io.read_u8le()
            self._debug['head_entry_realtime']['end'] = self._io.pos()
            self._debug['tail_entry_realtime']['start'] = self._io.pos()
            self.tail_entry_realtime = self._io.read_u8le()
            self._debug['tail_entry_realtime']['end'] = self._io.pos()
            self._debug['tail_entry_monotonic']['start'] = self._io.pos()
            self.tail_entry_monotonic = self._io.read_u8le()
            self._debug['tail_entry_monotonic']['end'] = self._io.pos()
            if not (self._io.is_eof()):
                self._debug['num_data']['start'] = self._io.pos()
                self.num_data = self._io.read_u8le()
                self._debug['num_data']['end'] = self._io.pos()

            if not (self._io.is_eof()):
                self._debug['num_fields']['start'] = self._io.pos()
                self.num_fields = self._io.read_u8le()
                self._debug['num_fields']['end'] = self._io.pos()

            if not (self._io.is_eof()):
                self._debug['num_tags']['start'] = self._io.pos()
                self.num_tags = self._io.read_u8le()
                self._debug['num_tags']['end'] = self._io.pos()

            if not (self._io.is_eof()):
                self._debug['num_entry_arrays']['start'] = self._io.pos()
                self.num_entry_arrays = self._io.read_u8le()
                self._debug['num_entry_arrays']['end'] = self._io.pos()



    class JournalObject(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.freedesktop.org/wiki/Software/systemd/journal-files/#objects
        """

        class ObjectTypes(Enum):
            unused = 0
            data = 1
            field = 2
            entry = 3
            data_hash_table = 4
            field_hash_table = 5
            entry_array = 6
            tag = 7
        SEQ_FIELDS = ["padding", "object_type", "flags", "reserved", "len_object", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(((8 - self._io.pos()) % 8))
            self._debug['padding']['end'] = self._io.pos()
            self._debug['object_type']['start'] = self._io.pos()
            self.object_type = KaitaiStream.resolve_enum(SystemdJournal.JournalObject.ObjectTypes, self._io.read_u1())
            self._debug['object_type']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(6)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['len_object']['start'] = self._io.pos()
            self.len_object = self._io.read_u8le()
            self._debug['len_object']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            _on = self.object_type
            if _on == SystemdJournal.JournalObject.ObjectTypes.data:
                self._raw_payload = self._io.read_bytes((self.len_object - 16))
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = SystemdJournal.DataObject(_io__raw_payload, self, self._root)
                self.payload._read()
            else:
                self.payload = self._io.read_bytes((self.len_object - 16))
            self._debug['payload']['end'] = self._io.pos()


    class DataObject(KaitaiStruct):
        """Data objects are designed to carry log payload, typically in
        form of a "key=value" string in `payload` attribute.
        
        .. seealso::
           Source - https://www.freedesktop.org/wiki/Software/systemd/journal-files/#dataobjects
        """
        SEQ_FIELDS = ["hash", "ofs_next_hash", "ofs_head_field", "ofs_entry", "ofs_entry_array", "num_entries", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['hash']['start'] = self._io.pos()
            self.hash = self._io.read_u8le()
            self._debug['hash']['end'] = self._io.pos()
            self._debug['ofs_next_hash']['start'] = self._io.pos()
            self.ofs_next_hash = self._io.read_u8le()
            self._debug['ofs_next_hash']['end'] = self._io.pos()
            self._debug['ofs_head_field']['start'] = self._io.pos()
            self.ofs_head_field = self._io.read_u8le()
            self._debug['ofs_head_field']['end'] = self._io.pos()
            self._debug['ofs_entry']['start'] = self._io.pos()
            self.ofs_entry = self._io.read_u8le()
            self._debug['ofs_entry']['end'] = self._io.pos()
            self._debug['ofs_entry_array']['start'] = self._io.pos()
            self.ofs_entry_array = self._io.read_u8le()
            self._debug['ofs_entry_array']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u8le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            self.payload = self._io.read_bytes_full()
            self._debug['payload']['end'] = self._io.pos()

        @property
        def next_hash(self):
            if hasattr(self, '_m_next_hash'):
                return self._m_next_hash

            if self.ofs_next_hash != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_next_hash)
                self._debug['_m_next_hash']['start'] = io.pos()
                self._m_next_hash = SystemdJournal.JournalObject(io, self, self._root)
                self._m_next_hash._read()
                self._debug['_m_next_hash']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_next_hash', None)

        @property
        def head_field(self):
            if hasattr(self, '_m_head_field'):
                return self._m_head_field

            if self.ofs_head_field != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_head_field)
                self._debug['_m_head_field']['start'] = io.pos()
                self._m_head_field = SystemdJournal.JournalObject(io, self, self._root)
                self._m_head_field._read()
                self._debug['_m_head_field']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_head_field', None)

        @property
        def entry(self):
            if hasattr(self, '_m_entry'):
                return self._m_entry

            if self.ofs_entry != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_entry)
                self._debug['_m_entry']['start'] = io.pos()
                self._m_entry = SystemdJournal.JournalObject(io, self, self._root)
                self._m_entry._read()
                self._debug['_m_entry']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_entry', None)

        @property
        def entry_array(self):
            if hasattr(self, '_m_entry_array'):
                return self._m_entry_array

            if self.ofs_entry_array != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_entry_array)
                self._debug['_m_entry_array']['start'] = io.pos()
                self._m_entry_array = SystemdJournal.JournalObject(io, self, self._root)
                self._m_entry_array._read()
                self._debug['_m_entry_array']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_entry_array', None)


    @property
    def len_header(self):
        """Header length is used to set substream size, as it thus required
        prior to declaration of header.
        """
        if hasattr(self, '_m_len_header'):
            return self._m_len_header

        _pos = self._io.pos()
        self._io.seek(88)
        self._debug['_m_len_header']['start'] = self._io.pos()
        self._m_len_header = self._io.read_u8le()
        self._debug['_m_len_header']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_len_header', None)

    @property
    def data_hash_table(self):
        if hasattr(self, '_m_data_hash_table'):
            return self._m_data_hash_table

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_data_hash_table)
        self._debug['_m_data_hash_table']['start'] = self._io.pos()
        self._m_data_hash_table = self._io.read_bytes(self.header.len_data_hash_table)
        self._debug['_m_data_hash_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_data_hash_table', None)

    @property
    def field_hash_table(self):
        if hasattr(self, '_m_field_hash_table'):
            return self._m_field_hash_table

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_field_hash_table)
        self._debug['_m_field_hash_table']['start'] = self._io.pos()
        self._m_field_hash_table = self._io.read_bytes(self.header.len_field_hash_table)
        self._debug['_m_field_hash_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_field_hash_table', None)


