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

class WindowsEvtLog(KaitaiStruct):
    """EVT files are Windows Event Log files written by older Windows
    operating systems (2000, XP, 2003). They are used as binary log
    files by several major Windows subsystems and
    applications. Typically, several of them can be found in
    `%WINDIR%\system32\config` directory:
    
    * Application = `AppEvent.evt`
    * System = `SysEvent.evt`
    * Security = `SecEvent.evt`
    
    Alternatively, one can export any system event log as distinct .evt
    file using relevant option in Event Viewer application.
    
    A Windows application can submit an entry into these logs using
    [ReportEventA](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-reporteventa)
    function of Windows API.
    
    Internally, EVT files consist of a fixed-size header and event
    records. There are several usage scenarios (non-wrapping vs wrapping
    log files) which result in slightly different organization of
    records.
    
    .. seealso::
       Source - https://learn.microsoft.com/en-us/windows/win32/eventlog/event-log-file-format
    """
    SEQ_FIELDS = ["header", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = WindowsEvtLog.Header(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['records']['start'] = self._io.pos()
        self.records = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['records']:
                self._debug['records']['arr'] = []
            self._debug['records']['arr'].append({'start': self._io.pos()})
            _t_records = WindowsEvtLog.Record(self._io, self, self._root)
            _t_records._read()
            self.records.append(_t_records)
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['records']['end'] = self._io.pos()

    class Header(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/bb309024(v=vs.85)
        """
        SEQ_FIELDS = ["len_header", "magic", "version_major", "version_minor", "ofs_start", "ofs_end", "cur_rec_idx", "oldest_rec_idx", "len_file_max", "flags", "retention", "len_header_2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4C\x66\x4C\x65":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x66\x4C\x65", self.magic, self._io, u"/types/header/seq/1")
            self._debug['version_major']['start'] = self._io.pos()
            self.version_major = self._io.read_u4le()
            self._debug['version_major']['end'] = self._io.pos()
            self._debug['version_minor']['start'] = self._io.pos()
            self.version_minor = self._io.read_u4le()
            self._debug['version_minor']['end'] = self._io.pos()
            self._debug['ofs_start']['start'] = self._io.pos()
            self.ofs_start = self._io.read_u4le()
            self._debug['ofs_start']['end'] = self._io.pos()
            self._debug['ofs_end']['start'] = self._io.pos()
            self.ofs_end = self._io.read_u4le()
            self._debug['ofs_end']['end'] = self._io.pos()
            self._debug['cur_rec_idx']['start'] = self._io.pos()
            self.cur_rec_idx = self._io.read_u4le()
            self._debug['cur_rec_idx']['end'] = self._io.pos()
            self._debug['oldest_rec_idx']['start'] = self._io.pos()
            self.oldest_rec_idx = self._io.read_u4le()
            self._debug['oldest_rec_idx']['end'] = self._io.pos()
            self._debug['len_file_max']['start'] = self._io.pos()
            self.len_file_max = self._io.read_u4le()
            self._debug['len_file_max']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = WindowsEvtLog.Header.Flags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['retention']['start'] = self._io.pos()
            self.retention = self._io.read_u4le()
            self._debug['retention']['end'] = self._io.pos()
            self._debug['len_header_2']['start'] = self._io.pos()
            self.len_header_2 = self._io.read_u4le()
            self._debug['len_header_2']['end'] = self._io.pos()

        class Flags(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "archive", "log_full", "wrap", "dirty"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_bits_int_be(28)
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['archive']['start'] = self._io.pos()
                self.archive = self._io.read_bits_int_be(1) != 0
                self._debug['archive']['end'] = self._io.pos()
                self._debug['log_full']['start'] = self._io.pos()
                self.log_full = self._io.read_bits_int_be(1) != 0
                self._debug['log_full']['end'] = self._io.pos()
                self._debug['wrap']['start'] = self._io.pos()
                self.wrap = self._io.read_bits_int_be(1) != 0
                self._debug['wrap']['end'] = self._io.pos()
                self._debug['dirty']['start'] = self._io.pos()
                self.dirty = self._io.read_bits_int_be(1) != 0
                self._debug['dirty']['end'] = self._io.pos()



    class Record(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-eventlogrecord
        """
        SEQ_FIELDS = ["len_record", "type", "body", "len_record2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_record']['start'] = self._io.pos()
            self.len_record = self._io.read_u4le()
            self._debug['len_record']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u4le()
            self._debug['type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.type
            if _on == 1699505740:
                self._raw_body = self._io.read_bytes((self.len_record - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = WindowsEvtLog.RecordBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == 286331153:
                self._raw_body = self._io.read_bytes((self.len_record - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = WindowsEvtLog.CursorRecordBody(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes((self.len_record - 12))
            self._debug['body']['end'] = self._io.pos()
            self._debug['len_record2']['start'] = self._io.pos()
            self.len_record2 = self._io.read_u4le()
            self._debug['len_record2']['end'] = self._io.pos()


    class RecordBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-eventlogrecord
        """

        class EventTypes(Enum):
            error = 1
            audit_failure = 2
            audit_success = 3
            info = 4
            warning = 5
        SEQ_FIELDS = ["idx", "time_generated", "time_written", "event_id", "event_type", "num_strings", "event_category", "reserved", "ofs_strings", "len_user_sid", "ofs_user_sid", "len_data", "ofs_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_u4le()
            self._debug['idx']['end'] = self._io.pos()
            self._debug['time_generated']['start'] = self._io.pos()
            self.time_generated = self._io.read_u4le()
            self._debug['time_generated']['end'] = self._io.pos()
            self._debug['time_written']['start'] = self._io.pos()
            self.time_written = self._io.read_u4le()
            self._debug['time_written']['end'] = self._io.pos()
            self._debug['event_id']['start'] = self._io.pos()
            self.event_id = self._io.read_u4le()
            self._debug['event_id']['end'] = self._io.pos()
            self._debug['event_type']['start'] = self._io.pos()
            self.event_type = KaitaiStream.resolve_enum(WindowsEvtLog.RecordBody.EventTypes, self._io.read_u2le())
            self._debug['event_type']['end'] = self._io.pos()
            self._debug['num_strings']['start'] = self._io.pos()
            self.num_strings = self._io.read_u2le()
            self._debug['num_strings']['end'] = self._io.pos()
            self._debug['event_category']['start'] = self._io.pos()
            self.event_category = self._io.read_u2le()
            self._debug['event_category']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(6)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['ofs_strings']['start'] = self._io.pos()
            self.ofs_strings = self._io.read_u4le()
            self._debug['ofs_strings']['end'] = self._io.pos()
            self._debug['len_user_sid']['start'] = self._io.pos()
            self.len_user_sid = self._io.read_u4le()
            self._debug['len_user_sid']['end'] = self._io.pos()
            self._debug['ofs_user_sid']['start'] = self._io.pos()
            self.ofs_user_sid = self._io.read_u4le()
            self._debug['ofs_user_sid']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()

        @property
        def user_sid(self):
            if hasattr(self, '_m_user_sid'):
                return self._m_user_sid

            _pos = self._io.pos()
            self._io.seek((self.ofs_user_sid - 8))
            self._debug['_m_user_sid']['start'] = self._io.pos()
            self._m_user_sid = self._io.read_bytes(self.len_user_sid)
            self._debug['_m_user_sid']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_user_sid', None)

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek((self.ofs_data - 8))
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)


    class CursorRecordBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://forensics.wiki/windows_event_log_(evt)/#cursor-record
        """
        SEQ_FIELDS = ["magic", "ofs_first_record", "ofs_next_record", "idx_next_record", "idx_first_record"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(12)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x22\x22\x22\x22\x33\x33\x33\x33\x44\x44\x44\x44":
                raise kaitaistruct.ValidationNotEqualError(b"\x22\x22\x22\x22\x33\x33\x33\x33\x44\x44\x44\x44", self.magic, self._io, u"/types/cursor_record_body/seq/0")
            self._debug['ofs_first_record']['start'] = self._io.pos()
            self.ofs_first_record = self._io.read_u4le()
            self._debug['ofs_first_record']['end'] = self._io.pos()
            self._debug['ofs_next_record']['start'] = self._io.pos()
            self.ofs_next_record = self._io.read_u4le()
            self._debug['ofs_next_record']['end'] = self._io.pos()
            self._debug['idx_next_record']['start'] = self._io.pos()
            self.idx_next_record = self._io.read_u4le()
            self._debug['idx_next_record']['end'] = self._io.pos()
            self._debug['idx_first_record']['start'] = self._io.pos()
            self.idx_first_record = self._io.read_u4le()
            self._debug['idx_first_record']['end'] = self._io.pos()



