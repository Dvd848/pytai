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
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SshPublicKey(KaitaiStruct):
    """SSH public keys are encoded in a special binary format, typically represented
    to end users as either one-liner OpenSSH format or multi-line PEM format
    (commerical SSH). Text wrapper carries extra information about user who
    created the key, comment, etc, but the inner binary is always base64-encoded
    and follows the same internal format.
    
    This format spec deals with this internal binary format (called "blob" in
    openssh sources) only. Buffer is expected to be raw binary and not base64-d.
    Implementation closely follows code in OpenSSH.
    
    .. seealso::
       Source - https://github.com/openssh/openssh-portable/blob/master/sshkey.c#L1970
    """
    SEQ_FIELDS = ["key_name", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['key_name']['start'] = self._io.pos()
        self.key_name = SshPublicKey.Cstring(self._io, self, self._root)
        self.key_name._read()
        self._debug['key_name']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        _on = self.key_name.value
        if _on == u"ssh-rsa":
            self.body = SshPublicKey.KeyRsa(self._io, self, self._root)
            self.body._read()
        elif _on == u"ecdsa-sha2-nistp256":
            self.body = SshPublicKey.KeyEcdsa(self._io, self, self._root)
            self.body._read()
        elif _on == u"ssh-ed25519":
            self.body = SshPublicKey.KeyEd25519(self._io, self, self._root)
            self.body._read()
        elif _on == u"ssh-dss":
            self.body = SshPublicKey.KeyDsa(self._io, self, self._root)
            self.body._read()
        self._debug['body']['end'] = self._io.pos()

    class KeyRsa(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshkey.c#L2011-L2028
        """
        SEQ_FIELDS = ["rsa_e", "rsa_n"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['rsa_e']['start'] = self._io.pos()
            self.rsa_e = SshPublicKey.Bignum2(self._io, self, self._root)
            self.rsa_e._read()
            self._debug['rsa_e']['end'] = self._io.pos()
            self._debug['rsa_n']['start'] = self._io.pos()
            self.rsa_n = SshPublicKey.Bignum2(self._io, self, self._root)
            self.rsa_n._read()
            self._debug['rsa_n']['end'] = self._io.pos()

        @property
        def key_length(self):
            """Key length in bits."""
            if hasattr(self, '_m_key_length'):
                return self._m_key_length if hasattr(self, '_m_key_length') else None

            self._m_key_length = self.rsa_n.length_in_bits
            return self._m_key_length if hasattr(self, '_m_key_length') else None


    class KeyEd25519(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshkey.c#L2111-L2124
        """
        SEQ_FIELDS = ["len_pk", "pk"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_pk']['start'] = self._io.pos()
            self.len_pk = self._io.read_u4be()
            self._debug['len_pk']['end'] = self._io.pos()
            self._debug['pk']['start'] = self._io.pos()
            self.pk = self._io.read_bytes(self.len_pk)
            self._debug['pk']['end'] = self._io.pos()


    class KeyEcdsa(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshkey.c#L2060-L2103
        """
        SEQ_FIELDS = ["curve_name", "ec"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['curve_name']['start'] = self._io.pos()
            self.curve_name = SshPublicKey.Cstring(self._io, self, self._root)
            self.curve_name._read()
            self._debug['curve_name']['end'] = self._io.pos()
            self._debug['ec']['start'] = self._io.pos()
            self.ec = SshPublicKey.EllipticCurve(self._io, self, self._root)
            self.ec._read()
            self._debug['ec']['end'] = self._io.pos()


    class Cstring(KaitaiStruct):
        """A integer-prefixed string designed to be read using `sshbuf_get_cstring`
        and written by `sshbuf_put_cstring` routines in ssh sources. Name is an
        obscure misnomer, as typically "C string" means a null-terminated string.
        
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshbuf-getput-basic.c#L181
        """
        SEQ_FIELDS = ["len", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4be()
            self._debug['len']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = (self._io.read_bytes(self.len)).decode(u"ASCII")
            self._debug['value']['end'] = self._io.pos()


    class KeyDsa(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshkey.c#L2036-L2051
        """
        SEQ_FIELDS = ["dsa_p", "dsa_q", "dsa_g", "dsa_pub_key"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['dsa_p']['start'] = self._io.pos()
            self.dsa_p = SshPublicKey.Bignum2(self._io, self, self._root)
            self.dsa_p._read()
            self._debug['dsa_p']['end'] = self._io.pos()
            self._debug['dsa_q']['start'] = self._io.pos()
            self.dsa_q = SshPublicKey.Bignum2(self._io, self, self._root)
            self.dsa_q._read()
            self._debug['dsa_q']['end'] = self._io.pos()
            self._debug['dsa_g']['start'] = self._io.pos()
            self.dsa_g = SshPublicKey.Bignum2(self._io, self, self._root)
            self.dsa_g._read()
            self._debug['dsa_g']['end'] = self._io.pos()
            self._debug['dsa_pub_key']['start'] = self._io.pos()
            self.dsa_pub_key = SshPublicKey.Bignum2(self._io, self, self._root)
            self.dsa_pub_key._read()
            self._debug['dsa_pub_key']['end'] = self._io.pos()


    class EllipticCurve(KaitaiStruct):
        """Elliptic curve dump format used by ssh. In OpenSSH code, the following
        routines are used to read/write it:
        
        * sshbuf_get_ec
        * get_ec
        
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshbuf-getput-crypto.c#L90
           https://github.com/openssh/openssh-portable/blob/master/sshbuf-getput-crypto.c#L76
        """
        SEQ_FIELDS = ["len", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4be()
            self._debug['len']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(self.len)
            self._debug['body']['end'] = self._io.pos()


    class Bignum2(KaitaiStruct):
        """Big integers serialization format used by ssh, v2. In the code, the following
        routines are used to read/write it:
        
        * sshbuf_get_bignum2
        * sshbuf_get_bignum2_bytes_direct
        * sshbuf_put_bignum2
        * sshbuf_get_bignum2_bytes_direct
        
        .. seealso::
           Source - https://github.com/openssh/openssh-portable/blob/master/sshbuf-getput-crypto.c#L35
           https://github.com/openssh/openssh-portable/blob/master/sshbuf-getput-basic.c#L431
        """
        SEQ_FIELDS = ["len", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4be()
            self._debug['len']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(self.len)
            self._debug['body']['end'] = self._io.pos()

        @property
        def length_in_bits(self):
            """Length of big integer in bits. In OpenSSH sources, this corresponds to
            `BN_num_bits` function.
            """
            if hasattr(self, '_m_length_in_bits'):
                return self._m_length_in_bits if hasattr(self, '_m_length_in_bits') else None

            self._m_length_in_bits = ((self.len - 1) * 8)
            return self._m_length_in_bits if hasattr(self, '_m_length_in_bits') else None



