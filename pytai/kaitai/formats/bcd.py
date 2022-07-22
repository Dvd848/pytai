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

class Bcd(KaitaiStruct):
    """BCD (Binary Coded Decimals) is a common way to encode integer
    numbers in a way that makes human-readable output somewhat
    simpler. In this encoding scheme, every decimal digit is encoded as
    either a single byte (8 bits), or a nibble (half of a byte, 4
    bits). This obviously wastes a lot of bits, but it makes translation
    into human-readable string much easier than traditional
    binary-to-decimal conversion process, which includes lots of
    divisions by 10.
    
    For example, encoding integer 31337 in 8-digit, 8 bits per digit,
    big endian order of digits BCD format yields
    
    ```
    00 00 00 03 01 03 03 07
    ```
    
    Encoding the same integer as 8-digit, 4 bits per digit, little
    endian order BCD format would yield:
    
    ```
    73 31 30 00
    ```
    
    Using this type of encoding in Kaitai Struct is pretty
    straightforward: one calls for this type, specifying desired
    encoding parameters, and gets result using either `as_int` or
    `as_str` attributes.
    """
    SEQ_FIELDS = ["digits"]
    def __init__(self, num_digits, bits_per_digit, is_le, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.num_digits = num_digits
        self.bits_per_digit = bits_per_digit
        self.is_le = is_le
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['digits']['start'] = self._io.pos()
        self.digits = []
        for i in range(self.num_digits):
            if not 'arr' in self._debug['digits']:
                self._debug['digits']['arr'] = []
            self._debug['digits']['arr'].append({'start': self._io.pos()})
            _on = self.bits_per_digit
            if _on == 4:
                if not 'arr' in self._debug['digits']:
                    self._debug['digits']['arr'] = []
                self._debug['digits']['arr'].append({'start': self._io.pos()})
                self.digits.append(self._io.read_bits_int_be(4))
                self._debug['digits']['arr'][i]['end'] = self._io.pos()
            elif _on == 8:
                if not 'arr' in self._debug['digits']:
                    self._debug['digits']['arr'] = []
                self._debug['digits']['arr'].append({'start': self._io.pos()})
                self.digits.append(self._io.read_u1())
                self._debug['digits']['arr'][i]['end'] = self._io.pos()
            self._debug['digits']['arr'][i]['end'] = self._io.pos()

        self._debug['digits']['end'] = self._io.pos()

    @property
    def as_int(self):
        """Value of this BCD number as integer. Endianness would be selected based on `is_le` parameter given."""
        if hasattr(self, '_m_as_int'):
            return self._m_as_int

        self._m_as_int = (self.as_int_le if self.is_le else self.as_int_be)
        return getattr(self, '_m_as_int', None)

    @property
    def as_int_le(self):
        """Value of this BCD number as integer (treating digit order as little-endian)."""
        if hasattr(self, '_m_as_int_le'):
            return self._m_as_int_le

        self._m_as_int_le = (self.digits[0] + (0 if self.num_digits < 2 else ((self.digits[1] * 10) + (0 if self.num_digits < 3 else ((self.digits[2] * 100) + (0 if self.num_digits < 4 else ((self.digits[3] * 1000) + (0 if self.num_digits < 5 else ((self.digits[4] * 10000) + (0 if self.num_digits < 6 else ((self.digits[5] * 100000) + (0 if self.num_digits < 7 else ((self.digits[6] * 1000000) + (0 if self.num_digits < 8 else (self.digits[7] * 10000000)))))))))))))))
        return getattr(self, '_m_as_int_le', None)

    @property
    def last_idx(self):
        """Index of last digit (0-based)."""
        if hasattr(self, '_m_last_idx'):
            return self._m_last_idx

        self._m_last_idx = (self.num_digits - 1)
        return getattr(self, '_m_last_idx', None)

    @property
    def as_int_be(self):
        """Value of this BCD number as integer (treating digit order as big-endian)."""
        if hasattr(self, '_m_as_int_be'):
            return self._m_as_int_be

        self._m_as_int_be = (self.digits[self.last_idx] + (0 if self.num_digits < 2 else ((self.digits[(self.last_idx - 1)] * 10) + (0 if self.num_digits < 3 else ((self.digits[(self.last_idx - 2)] * 100) + (0 if self.num_digits < 4 else ((self.digits[(self.last_idx - 3)] * 1000) + (0 if self.num_digits < 5 else ((self.digits[(self.last_idx - 4)] * 10000) + (0 if self.num_digits < 6 else ((self.digits[(self.last_idx - 5)] * 100000) + (0 if self.num_digits < 7 else ((self.digits[(self.last_idx - 6)] * 1000000) + (0 if self.num_digits < 8 else (self.digits[(self.last_idx - 7)] * 10000000)))))))))))))))
        return getattr(self, '_m_as_int_be', None)


