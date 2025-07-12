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

class EfivarSignatureList(KaitaiStruct):
    """Parse UEFI variables db and dbx that contain signatures, certificates and
    hashes. On a Linux system using UEFI, these variables are readable from:
    
    ```
    /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f
    /sys/firmware/efi/efivars/dbDefault-8be4df61-93ca-11d2-aa0d-00e098032b8c
    /sys/firmware/efi/efivars/dbx-d719b2cb-3d3a-4596-a3bc-dad00e67656f
    /sys/firmware/efi/efivars/dbxDefault-8be4df61-93ca-11d2-aa0d-00e098032b8c
    ```
    
    Note:
    
    * `d719b2cb-3d3a-4596-a3bc-dad00e67656f` is defined as `EFI_IMAGE_SECURITY_DATABASE_GUID`
    * `8be4df61-93ca-11d2-aa0d-00e098032b8c` is defined as `EFI_GLOBAL_VARIABLE`
    
    Each file contains an EFI attribute (32-bit integer) followed by a list of
    `EFI_SIGNATURE_LIST` structures.
    
    .. seealso::
       Source - https://uefi.org/sites/default/files/resources/UEFI_Spec_2_8_final.pdf
    """
    SEQ_FIELDS = ["var_attributes", "signatures"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['var_attributes']['start'] = self._io.pos()
        self.var_attributes = EfivarSignatureList.EfiVarAttr(self._io, self, self._root)
        self.var_attributes._read()
        self._debug['var_attributes']['end'] = self._io.pos()
        self._debug['signatures']['start'] = self._io.pos()
        self.signatures = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['signatures']:
                self._debug['signatures']['arr'] = []
            self._debug['signatures']['arr'].append({'start': self._io.pos()})
            _t_signatures = EfivarSignatureList.SignatureList(self._io, self, self._root)
            _t_signatures._read()
            self.signatures.append(_t_signatures)
            self._debug['signatures']['arr'][len(self.signatures) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['signatures']['end'] = self._io.pos()

    class SignatureList(KaitaiStruct):
        """
        .. seealso::
           EFI_SIGNATURE_LIST
        """
        SEQ_FIELDS = ["signature_type", "len_signature_list", "len_signature_header", "len_signature", "header", "signatures"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['signature_type']['start'] = self._io.pos()
            self.signature_type = self._io.read_bytes(16)
            self._debug['signature_type']['end'] = self._io.pos()
            self._debug['len_signature_list']['start'] = self._io.pos()
            self.len_signature_list = self._io.read_u4le()
            self._debug['len_signature_list']['end'] = self._io.pos()
            self._debug['len_signature_header']['start'] = self._io.pos()
            self.len_signature_header = self._io.read_u4le()
            self._debug['len_signature_header']['end'] = self._io.pos()
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u4le()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['header']['start'] = self._io.pos()
            self.header = self._io.read_bytes(self.len_signature_header)
            self._debug['header']['end'] = self._io.pos()
            if self.len_signature > 0:
                self._debug['signatures']['start'] = self._io.pos()
                self._raw_signatures = []
                self.signatures = []
                for i in range(((self.len_signature_list - self.len_signature_header) - 28) // self.len_signature):
                    if not 'arr' in self._debug['signatures']:
                        self._debug['signatures']['arr'] = []
                    self._debug['signatures']['arr'].append({'start': self._io.pos()})
                    self._raw_signatures.append(self._io.read_bytes(self.len_signature))
                    _io__raw_signatures = KaitaiStream(BytesIO(self._raw_signatures[i]))
                    _t_signatures = EfivarSignatureList.SignatureData(_io__raw_signatures, self, self._root)
                    _t_signatures._read()
                    self.signatures.append(_t_signatures)
                    self._debug['signatures']['arr'][i]['end'] = self._io.pos()

                self._debug['signatures']['end'] = self._io.pos()


        @property
        def is_cert_sha512_x509(self):
            """SHA512 hash of an X.509 certificate's To-Be-Signed contents, and a time of revocation.
            
            .. seealso::
               EFI_CERT_X509_SHA512_GUID
            """
            if hasattr(self, '_m_is_cert_sha512_x509'):
                return self._m_is_cert_sha512_x509

            self._m_is_cert_sha512_x509 = self.signature_type == b"\x63\xBF\x6D\x44\x02\x25\xDA\x4C\xBC\xFA\x24\x65\xD2\xB0\xFE\x9D"
            return getattr(self, '_m_is_cert_sha512_x509', None)

        @property
        def is_cert_sha224(self):
            """SHA-224 hash.
            
            .. seealso::
               EFI_CERT_SHA224_GUID
            """
            if hasattr(self, '_m_is_cert_sha224'):
                return self._m_is_cert_sha224

            self._m_is_cert_sha224 = self.signature_type == b"\x33\x52\x6E\x0B\x5C\xA6\xC9\x44\x94\x07\xD9\xAB\x83\xBF\xC8\xBD"
            return getattr(self, '_m_is_cert_sha224', None)

        @property
        def is_cert_x509(self):
            """X.509 certificate.
            
            .. seealso::
               EFI_CERT_X509_GUID
            """
            if hasattr(self, '_m_is_cert_x509'):
                return self._m_is_cert_x509

            self._m_is_cert_x509 = self.signature_type == b"\xA1\x59\xC0\xA5\xE4\x94\xA7\x4A\x87\xB5\xAB\x15\x5C\x2B\xF0\x72"
            return getattr(self, '_m_is_cert_x509', None)

        @property
        def is_cert_sha256_x509(self):
            """SHA256 hash of an X.509 certificate's To-Be-Signed contents, and a time of revocation.
            
            .. seealso::
               EFI_CERT_X509_SHA256_GUID
            """
            if hasattr(self, '_m_is_cert_sha256_x509'):
                return self._m_is_cert_sha256_x509

            self._m_is_cert_sha256_x509 = self.signature_type == b"\x92\xA4\xD2\x3B\xC0\x96\x79\x40\xB4\x20\xFC\xF9\x8E\xF1\x03\xED"
            return getattr(self, '_m_is_cert_sha256_x509', None)

        @property
        def is_cert_rsa2048_key(self):
            """RSA-2048 key (only the modulus since the public key exponent is known to be 0x10001).
            
            .. seealso::
               EFI_CERT_RSA2048_GUID
            """
            if hasattr(self, '_m_is_cert_rsa2048_key'):
                return self._m_is_cert_rsa2048_key

            self._m_is_cert_rsa2048_key = self.signature_type == b"\xE8\x66\x57\x3C\x9C\x26\x34\x4E\xAA\x14\xED\x77\x6E\x85\xB3\xB6"
            return getattr(self, '_m_is_cert_rsa2048_key', None)

        @property
        def is_cert_sha512(self):
            """SHA-512 hash.
            
            .. seealso::
               EFI_CERT_SHA512_GUID
            """
            if hasattr(self, '_m_is_cert_sha512'):
                return self._m_is_cert_sha512

            self._m_is_cert_sha512 = self.signature_type == b"\xAE\x0F\x3E\x09\xC4\xA6\x50\x4F\x9F\x1B\xD4\x1E\x2B\x89\xC1\x9A"
            return getattr(self, '_m_is_cert_sha512', None)

        @property
        def is_cert_sha384(self):
            """SHA-384 hash.
            
            .. seealso::
               EFI_CERT_SHA384_GUID
            """
            if hasattr(self, '_m_is_cert_sha384'):
                return self._m_is_cert_sha384

            self._m_is_cert_sha384 = self.signature_type == b"\x07\x53\x3E\xFF\xD0\x9F\xC9\x48\x85\xF1\x8A\xD5\x6C\x70\x1E\x01"
            return getattr(self, '_m_is_cert_sha384', None)

        @property
        def is_cert_sha1(self):
            """SHA-1 hash.
            
            .. seealso::
               EFI_CERT_SHA1_GUID
            """
            if hasattr(self, '_m_is_cert_sha1'):
                return self._m_is_cert_sha1

            self._m_is_cert_sha1 = self.signature_type == b"\x12\xA5\x6C\x82\x10\xCF\xC9\x4A\xB1\x87\xBE\x01\x49\x66\x31\xBD"
            return getattr(self, '_m_is_cert_sha1', None)

        @property
        def is_cert_rsa2048_sha1(self):
            """RSA-2048 signature of a SHA-1 hash.
            
            .. seealso::
               EFI_CERT_RSA2048_SHA1_GUID
            """
            if hasattr(self, '_m_is_cert_rsa2048_sha1'):
                return self._m_is_cert_rsa2048_sha1

            self._m_is_cert_rsa2048_sha1 = self.signature_type == b"\x4F\x44\xF8\x67\x43\x87\xF1\x48\xA3\x28\x1E\xAA\xB8\x73\x60\x80"
            return getattr(self, '_m_is_cert_rsa2048_sha1', None)

        @property
        def is_cert_sha256(self):
            """SHA-256 hash.
            
            .. seealso::
               EFI_CERT_SHA256_GUID
            """
            if hasattr(self, '_m_is_cert_sha256'):
                return self._m_is_cert_sha256

            self._m_is_cert_sha256 = self.signature_type == b"\x26\x16\xC4\xC1\x4C\x50\x92\x40\xAC\xA9\x41\xF9\x36\x93\x43\x28"
            return getattr(self, '_m_is_cert_sha256', None)

        @property
        def is_cert_sha384_x509(self):
            """SHA384 hash of an X.509 certificate's To-Be-Signed contents, and a time of revocation.
            
            .. seealso::
               EFI_CERT_X509_SHA384_GUID
            """
            if hasattr(self, '_m_is_cert_sha384_x509'):
                return self._m_is_cert_sha384_x509

            self._m_is_cert_sha384_x509 = self.signature_type == b"\x6E\x87\x76\x70\xC2\x80\xE6\x4E\xAA\xD2\x28\xB3\x49\xA6\x86\x5B"
            return getattr(self, '_m_is_cert_sha384_x509', None)

        @property
        def is_cert_rsa2048_sha256(self):
            """RSA-2048 signature of a SHA-256 hash.
            
            .. seealso::
               EFI_CERT_RSA2048_SHA256_GUID
            """
            if hasattr(self, '_m_is_cert_rsa2048_sha256'):
                return self._m_is_cert_rsa2048_sha256

            self._m_is_cert_rsa2048_sha256 = self.signature_type == b"\x90\x61\xB3\xE2\x9B\x87\x3D\x4A\xAD\x8D\xF2\xE7\xBB\xA3\x27\x84"
            return getattr(self, '_m_is_cert_rsa2048_sha256', None)

        @property
        def is_cert_der_pkcs7(self):
            """DER-encoded PKCS #7 version 1.5 [RFC2315].
            
            .. seealso::
               EFI_CERT_TYPE_PKCS7_GUID
            """
            if hasattr(self, '_m_is_cert_der_pkcs7'):
                return self._m_is_cert_der_pkcs7

            self._m_is_cert_der_pkcs7 = self.signature_type == b"\x9D\xD2\xAF\x4A\xDF\x68\xEE\x49\x8A\xA9\x34\x7D\x37\x56\x65\xA7"
            return getattr(self, '_m_is_cert_der_pkcs7', None)


    class SignatureData(KaitaiStruct):
        """
        .. seealso::
           EFI_SIGNATURE_DATA
        """
        SEQ_FIELDS = ["owner", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['owner']['start'] = self._io.pos()
            self.owner = self._io.read_bytes(16)
            self._debug['owner']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


    class EfiVarAttr(KaitaiStruct):
        """Attributes of a UEFI variable."""
        SEQ_FIELDS = ["enhanced_authenticated_access", "append_write", "time_based_authenticated_write_access", "authenticated_write_access", "hardware_error_record", "runtime_access", "bootservice_access", "non_volatile", "reserved1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['enhanced_authenticated_access']['start'] = self._io.pos()
            self.enhanced_authenticated_access = self._io.read_bits_int_be(1) != 0
            self._debug['enhanced_authenticated_access']['end'] = self._io.pos()
            self._debug['append_write']['start'] = self._io.pos()
            self.append_write = self._io.read_bits_int_be(1) != 0
            self._debug['append_write']['end'] = self._io.pos()
            self._debug['time_based_authenticated_write_access']['start'] = self._io.pos()
            self.time_based_authenticated_write_access = self._io.read_bits_int_be(1) != 0
            self._debug['time_based_authenticated_write_access']['end'] = self._io.pos()
            self._debug['authenticated_write_access']['start'] = self._io.pos()
            self.authenticated_write_access = self._io.read_bits_int_be(1) != 0
            self._debug['authenticated_write_access']['end'] = self._io.pos()
            self._debug['hardware_error_record']['start'] = self._io.pos()
            self.hardware_error_record = self._io.read_bits_int_be(1) != 0
            self._debug['hardware_error_record']['end'] = self._io.pos()
            self._debug['runtime_access']['start'] = self._io.pos()
            self.runtime_access = self._io.read_bits_int_be(1) != 0
            self._debug['runtime_access']['end'] = self._io.pos()
            self._debug['bootservice_access']['start'] = self._io.pos()
            self.bootservice_access = self._io.read_bits_int_be(1) != 0
            self._debug['bootservice_access']['end'] = self._io.pos()
            self._debug['non_volatile']['start'] = self._io.pos()
            self.non_volatile = self._io.read_bits_int_be(1) != 0
            self._debug['non_volatile']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(24)
            self._debug['reserved1']['end'] = self._io.pos()



