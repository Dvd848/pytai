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


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class DosDatetime(KaitaiStruct):
    """MS-DOS date and time are packed 16-bit values that specify local date/time.
    The time is always stored in the current UTC time offset set on the computer
    which created the file. Note that the daylight saving time (DST) shifts
    also change the UTC time offset.
    
    For example, if you pack two files A and B into a ZIP archive, file A last modified
    at 2020-03-29 00:59 UTC+00:00 (GMT) and file B at 2020-03-29 02:00 UTC+01:00 (BST),
    the file modification times saved in MS-DOS format in the ZIP file will vary depending
    on whether the computer packing the files is set to GMT or BST at the time of ZIP creation.
    
      - If set to GMT:
          - file A: 2020-03-29 00:59 (UTC+00:00)
          - file B: 2020-03-29 01:00 (UTC+00:00)
      - If set to BST:
          - file A: 2020-03-29 01:59 (UTC+01:00)
          - file B: 2020-03-29 02:00 (UTC+01:00)
    
    It follows that you are unable to determine the actual last modified time
    of any file stored in the ZIP archive, if you don't know the locale time
    setting of the computer at the time it created the ZIP.
    
    This format is used in some data formats from the MS-DOS era, for example:
    
      - [zip](/zip/)
      - [rar](/rar/)
      - [vfat](/vfat/) (FAT12)
      - [lzh](/lzh/)
      - [cab](http://justsolve.archiveteam.org/wiki/Cabinet)
    
    .. seealso::
       Source - https://learn.microsoft.com/en-us/windows/win32/sysinfo/ms-dos-date-and-time
    
    
    .. seealso::
       Source - https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-dosdatetimetofiletime
    
    
    .. seealso::
       DosDateTimeToFileTime - https://github.com/reactos/reactos/blob/c6b64448ce4/dll/win32/kernel32/client/time.c#L82-L87
    
    
    .. seealso::
       page 25/34 - https://download.microsoft.com/download/0/8/4/084c452b-b772-4fe5-89bb-a0cbf082286a/fatgen103.doc
    """
    SEQ_FIELDS = ["time", "date"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['time']['start'] = self._io.pos()
        self.time = DosDatetime.Time(self._io, self, self._root)
        self.time._read()
        self._debug['time']['end'] = self._io.pos()
        self._debug['date']['start'] = self._io.pos()
        self.date = DosDatetime.Date(self._io, self, self._root)
        self.date._read()
        self._debug['date']['end'] = self._io.pos()

    class Time(KaitaiStruct):
        SEQ_FIELDS = ["second_div_2", "minute", "hour"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['second_div_2']['start'] = self._io.pos()
            self.second_div_2 = self._io.read_bits_int_le(5)
            self._debug['second_div_2']['end'] = self._io.pos()
            if not self.second_div_2 <= 29:
                raise kaitaistruct.ValidationGreaterThanError(29, self.second_div_2, self._io, u"/types/time/seq/0")
            self._debug['minute']['start'] = self._io.pos()
            self.minute = self._io.read_bits_int_le(6)
            self._debug['minute']['end'] = self._io.pos()
            if not self.minute <= 59:
                raise kaitaistruct.ValidationGreaterThanError(59, self.minute, self._io, u"/types/time/seq/1")
            self._debug['hour']['start'] = self._io.pos()
            self.hour = self._io.read_bits_int_le(5)
            self._debug['hour']['end'] = self._io.pos()
            if not self.hour <= 23:
                raise kaitaistruct.ValidationGreaterThanError(23, self.hour, self._io, u"/types/time/seq/2")

        @property
        def second(self):
            if hasattr(self, '_m_second'):
                return self._m_second

            self._m_second = (2 * self.second_div_2)
            return getattr(self, '_m_second', None)

        @property
        def padded_second(self):
            if hasattr(self, '_m_padded_second'):
                return self._m_padded_second

            self._m_padded_second = (u"0" if self.second <= 9 else u"") + str(self.second)
            return getattr(self, '_m_padded_second', None)

        @property
        def padded_minute(self):
            if hasattr(self, '_m_padded_minute'):
                return self._m_padded_minute

            self._m_padded_minute = (u"0" if self.minute <= 9 else u"") + str(self.minute)
            return getattr(self, '_m_padded_minute', None)

        @property
        def padded_hour(self):
            if hasattr(self, '_m_padded_hour'):
                return self._m_padded_hour

            self._m_padded_hour = (u"0" if self.hour <= 9 else u"") + str(self.hour)
            return getattr(self, '_m_padded_hour', None)


    class Date(KaitaiStruct):
        SEQ_FIELDS = ["day", "month", "year_minus_1980"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['day']['start'] = self._io.pos()
            self.day = self._io.read_bits_int_le(5)
            self._debug['day']['end'] = self._io.pos()
            if not self.day >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.day, self._io, u"/types/date/seq/0")
            self._debug['month']['start'] = self._io.pos()
            self.month = self._io.read_bits_int_le(4)
            self._debug['month']['end'] = self._io.pos()
            if not self.month >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.month, self._io, u"/types/date/seq/1")
            if not self.month <= 12:
                raise kaitaistruct.ValidationGreaterThanError(12, self.month, self._io, u"/types/date/seq/1")
            self._debug['year_minus_1980']['start'] = self._io.pos()
            self.year_minus_1980 = self._io.read_bits_int_le(7)
            self._debug['year_minus_1980']['end'] = self._io.pos()

        @property
        def year(self):
            """only years from 1980 to 2107 (1980 + 127) can be represented."""
            if hasattr(self, '_m_year'):
                return self._m_year

            self._m_year = (1980 + self.year_minus_1980)
            return getattr(self, '_m_year', None)

        @property
        def padded_day(self):
            if hasattr(self, '_m_padded_day'):
                return self._m_padded_day

            self._m_padded_day = (u"0" if self.day <= 9 else u"") + str(self.day)
            return getattr(self, '_m_padded_day', None)

        @property
        def padded_month(self):
            if hasattr(self, '_m_padded_month'):
                return self._m_padded_month

            self._m_padded_month = (u"0" if self.month <= 9 else u"") + str(self.month)
            return getattr(self, '_m_padded_month', None)

        @property
        def padded_year(self):
            if hasattr(self, '_m_padded_year'):
                return self._m_padded_year

            self._m_padded_year = (u"0" + (u"0" + (u"0" if self.year <= 9 else u"") if self.year <= 99 else u"") if self.year <= 999 else u"") + str(self.year)
            return getattr(self, '_m_padded_year', None)



