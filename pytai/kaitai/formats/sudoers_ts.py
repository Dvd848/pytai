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

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SudoersTs(KaitaiStruct):
    """This spec can be used to parse sudo time stamp files located in directories
    such as /run/sudo/ts/$USER or /var/lib/sudo/ts/$USER.
    
    .. seealso::
       Source - https://www.sudo.ws/man/1.8.27/sudoers_timestamp.man.html
    """

    class TsType(Enum):
        global = 1
        tty = 2
        ppid = 3
        lockexcl = 4
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
            _t_records = SudoersTs.Record(self._io, self, self._root)
            _t_records._read()
            self.records.append(_t_records)
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['records']['end'] = self._io.pos()

    class RecordV2(KaitaiStruct):
        SEQ_FIELDS = ["type", "flags", "auth_uid", "sid", "start_time", "ts", "ttydev", "ppid"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(SudoersTs.TsType, self._io.read_u2le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = SudoersTs.TsFlag(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['auth_uid']['start'] = self._io.pos()
            self.auth_uid = self._io.read_u4le()
            self._debug['auth_uid']['end'] = self._io.pos()
            self._debug['sid']['start'] = self._io.pos()
            self.sid = self._io.read_u4le()
            self._debug['sid']['end'] = self._io.pos()
            self._debug['start_time']['start'] = self._io.pos()
            self.start_time = SudoersTs.Timespec(self._io, self, self._root)
            self.start_time._read()
            self._debug['start_time']['end'] = self._io.pos()
            self._debug['ts']['start'] = self._io.pos()
            self.ts = SudoersTs.Timespec(self._io, self, self._root)
            self.ts._read()
            self._debug['ts']['end'] = self._io.pos()
            if self.type == SudoersTs.TsType.tty:
                self._debug['ttydev']['start'] = self._io.pos()
                self.ttydev = self._io.read_u4le()
                self._debug['ttydev']['end'] = self._io.pos()

            if self.type == SudoersTs.TsType.ppid:
                self._debug['ppid']['start'] = self._io.pos()
                self.ppid = self._io.read_u4le()
                self._debug['ppid']['end'] = self._io.pos()



    class TsFlag(KaitaiStruct):
        SEQ_FIELDS = ["reserved0", "anyuid", "disabled", "reserved1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved0']['start'] = self._io.pos()
            self.reserved0 = self._io.read_bits_int_be(6)
            self._debug['reserved0']['end'] = self._io.pos()
            self._debug['anyuid']['start'] = self._io.pos()
            self.anyuid = self._io.read_bits_int_be(1) != 0
            self._debug['anyuid']['end'] = self._io.pos()
            self._debug['disabled']['start'] = self._io.pos()
            self.disabled = self._io.read_bits_int_be(1) != 0
            self._debug['disabled']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(8)
            self._debug['reserved1']['end'] = self._io.pos()


    class RecordV1(KaitaiStruct):
        SEQ_FIELDS = ["type", "flags", "auth_uid", "sid", "ts", "ttydev", "ppid"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(SudoersTs.TsType, self._io.read_u2le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = SudoersTs.TsFlag(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['auth_uid']['start'] = self._io.pos()
            self.auth_uid = self._io.read_u4le()
            self._debug['auth_uid']['end'] = self._io.pos()
            self._debug['sid']['start'] = self._io.pos()
            self.sid = self._io.read_u4le()
            self._debug['sid']['end'] = self._io.pos()
            self._debug['ts']['start'] = self._io.pos()
            self.ts = SudoersTs.Timespec(self._io, self, self._root)
            self.ts._read()
            self._debug['ts']['end'] = self._io.pos()
            if self.type == SudoersTs.TsType.tty:
                self._debug['ttydev']['start'] = self._io.pos()
                self.ttydev = self._io.read_u4le()
                self._debug['ttydev']['end'] = self._io.pos()

            if self.type == SudoersTs.TsType.ppid:
                self._debug['ppid']['start'] = self._io.pos()
                self.ppid = self._io.read_u4le()
                self._debug['ppid']['end'] = self._io.pos()



    class Timespec(KaitaiStruct):
        SEQ_FIELDS = ["sec", "nsec"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['sec']['start'] = self._io.pos()
            self.sec = self._io.read_s8le()
            self._debug['sec']['end'] = self._io.pos()
            self._debug['nsec']['start'] = self._io.pos()
            self.nsec = self._io.read_s8le()
            self._debug['nsec']['end'] = self._io.pos()


    class Record(KaitaiStruct):
        SEQ_FIELDS = ["version", "len_record", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_record']['start'] = self._io.pos()
            self.len_record = self._io.read_u2le()
            self._debug['len_record']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            _on = self.version
            if _on == 1:
                self._raw_payload = self._io.read_bytes((self.len_record - 4))
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = SudoersTs.RecordV1(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == 2:
                self._raw_payload = self._io.read_bytes((self.len_record - 4))
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = SudoersTs.RecordV2(_io__raw_payload, self, self._root)
                self.payload._read()
            else:
                self.payload = self._io.read_bytes((self.len_record - 4))
            self._debug['payload']['end'] = self._io.pos()



