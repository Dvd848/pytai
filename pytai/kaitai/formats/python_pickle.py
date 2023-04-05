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

class PythonPickle(KaitaiStruct):
    """Python Pickle format serializes Python objects to a byte stream, as a sequence
    of operations to run on the Pickle Virtual Machine.
    
    The format is mostly implementation defined, there is no formal specification.
    Pickle data types are closely coupled to the Python object model.
    Python singletons, and most builtin types (e.g. `None`, `int`,`dict`, `list`)
    are serialised using dedicated Pickle opcodes.
    Other builtin types, and all classes  (e.g. `set`, `datetime.datetime`) are
    serialised by encoding the name of a constructor callable.
    They are deserialised by importing that constructor, and calling it.
    So, unpickling an arbitrary pickle, using the Python's stdlib pickle module
    can cause arbitrary code execution.
    
    Pickle format has evolved with Python, later protocols add opcodes & types.
    Later Python releases can pickle to or unpickle from any earlier protocol.
    
    * Protocol 0: ASCII clean, no explicit version, fields are '\n' terminated.
    * Protocol 1: Binary, no explicit version, first length prefixed types.
    * Protocol 2 ([PEP 307](https://peps.python.org/pep-0307/)): Python 2.3+.
      Explicit versioning, more length prefixed types.
    * Protocol 3: Python 3.0+. Dedicated opcodes for `bytes` objects.
    * Protocol 4 ([PEP 3154](https://peps.python.org/pep-3154/)): Python 3.4+.
      Opcodes for 64 bit strings, framing, `set`.
    * Protocol 5 ([PEP 574](https://peps.python.org/pep-0574/)): Python 3.8+:
    Opcodes for `bytearray` and out of band data
    
    .. seealso::
       Source - https://github.com/python/cpython/blob/v3.8.1/Lib/pickletools.py
    """

    class Opcode(Enum):
        mark = 40
        empty_tuple = 41
        stop = 46
        pop = 48
        pop_mark = 49
        dup = 50
        binbytes = 66
        short_binbytes = 67
        float = 70
        binfloat = 71
        int = 73
        binint = 74
        binint1 = 75
        long = 76
        binint2 = 77
        none = 78
        persid = 80
        binpersid = 81
        reduce = 82
        string = 83
        binstring = 84
        short_binstring = 85
        unicode = 86
        binunicode = 88
        empty_list = 93
        append = 97
        build = 98
        global_opcode = 99
        dict = 100
        appends = 101
        get = 103
        binget = 104
        inst = 105
        long_binget = 106
        list = 108
        obj = 111
        put = 112
        binput = 113
        long_binput = 114
        setitem = 115
        tuple = 116
        setitems = 117
        empty_dict = 125
        proto = 128
        newobj = 129
        ext1 = 130
        ext2 = 131
        ext4 = 132
        tuple1 = 133
        tuple2 = 134
        tuple3 = 135
        newtrue = 136
        newfalse = 137
        long1 = 138
        long4 = 139
        short_binunicode = 140
        binunicode8 = 141
        binbytes8 = 142
        empty_set = 143
        additems = 144
        frozenset = 145
        newobj_ex = 146
        stack_global = 147
        memoize = 148
        frame = 149
        bytearray8 = 150
        next_buffer = 151
        readonly_buffer = 152
    SEQ_FIELDS = ["ops"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['ops']['start'] = self._io.pos()
        self.ops = []
        i = 0
        while True:
            if not 'arr' in self._debug['ops']:
                self._debug['ops']['arr'] = []
            self._debug['ops']['arr'].append({'start': self._io.pos()})
            _t_ops = PythonPickle.Op(self._io, self, self._root)
            _t_ops._read()
            _ = _t_ops
            self.ops.append(_)
            self._debug['ops']['arr'][len(self.ops) - 1]['end'] = self._io.pos()
            if _.code == PythonPickle.Opcode.stop:
                break
            i += 1
        self._debug['ops']['end'] = self._io.pos()

    class Unicodestring8(KaitaiStruct):
        """Length prefixed string, between 0 and 2**64-1 bytes long.
        
        Only a 64-bit build of Python would produce a pickle containing strings
        large enough to need this type. Such a pickle could not be unpickled on
        a 32-bit build of Python, because the string would be larger than
        `sys.maxsize`.
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u8le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes(self.len)).decode(u"utf8")
            self._debug['val']['end'] = self._io.pos()


    class Long1(KaitaiStruct):
        """Large signed integer, in the range -2**(8*255-1) to 2**(8*255-1)-1,
        encoded as two's complement.
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u1()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class Bytes8(KaitaiStruct):
        """Length prefixed string, between 0 and 2**64-1 bytes long.
        
        Only a 64-bit build of Python would produce a pickle containing strings
        large enough to need this type. Such a pickle could not be unpickled on
        a 32-bit build of Python, because the string would be larger than
        `sys.maxsize`.
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u8le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class Bytes1(KaitaiStruct):
        """Length prefixed byte string, between 0 and 255 bytes long."""
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u1()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class Bytes4(KaitaiStruct):
        """Length prefixed string, between 0 and 2**32-1 bytes long."""
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class NoArg(KaitaiStruct):
        """Some opcodes take no argument, this empty type is used for them."""
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            pass


    class StringnlNoescape(KaitaiStruct):
        """Unquoted string, does not contain string escapes."""
        SEQ_FIELDS = ["val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes_term(10, False, True, True)).decode(u"ascii")
            self._debug['val']['end'] = self._io.pos()


    class DecimalnlLong(KaitaiStruct):
        """Integer, encoded with the ASCII chracters [0-9-], followed by 'L'."""
        SEQ_FIELDS = ["val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes_term(10, False, True, True)).decode(u"ascii")
            self._debug['val']['end'] = self._io.pos()


    class Unicodestring4(KaitaiStruct):
        """Length prefixed string, between 0 and 2**32-1 bytes long."""
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes(self.len)).decode(u"utf8")
            self._debug['val']['end'] = self._io.pos()


    class Unicodestringnl(KaitaiStruct):
        """Unquoted string, containing Python Unicode escapes."""
        SEQ_FIELDS = ["val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes_term(10, False, True, True)).decode(u"ascii")
            self._debug['val']['end'] = self._io.pos()


    class Long4(KaitaiStruct):
        """Large signed integer, in the range -2**(8*2**32-1) to 2**(8*2**32-1)-1,
        encoded as two's complement.
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class String1(KaitaiStruct):
        """Length prefixed string, between 0 and 255 bytes long. Encoding is
        unspecified.
        
        The default Python 2.x string type (`str`) is a sequence of bytes.
        These are pickled as `string1` or `string4`, when protocol == 2.
        The bytes are written directly, no explicit encoding is performed.
        
        Python 3.x will not pickle an object as `string1` or `string4`.
        Instead, opcodes and types with a known encoding are used.
        When unpickling
        
        - `pickle.Unpickler` objects default to ASCII, which can be overriden
        - `pickletools.dis` uses latin1, and cannot be overriden
        
        .. seealso::
           Source - https://github.com/python/cpython/blob/bb8071a4cae/Lib/pickle.py#L486-L495
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u1()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class Bytearray8(KaitaiStruct):
        """Length prefixed string, between 0 and 2**64-1 bytes long.
        
        The contents are deserilised into a `bytearray` object.
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u8le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class DecimalnlShort(KaitaiStruct):
        """Integer or boolean, encoded with the ASCII characters [0-9-].
        
        The values '00' and '01' encode the Python values `False` and `True`.
        Normally a value would not contain leading '0' characters.
        """
        SEQ_FIELDS = ["val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes_term(10, False, True, True)).decode(u"ascii")
            self._debug['val']['end'] = self._io.pos()


    class Unicodestring1(KaitaiStruct):
        """Length prefixed string, between 0 and 255 bytes long."""
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u1()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes(self.len)).decode(u"utf8")
            self._debug['val']['end'] = self._io.pos()


    class Stringnl(KaitaiStruct):
        """Quoted string, possibly containing Python string escapes."""
        SEQ_FIELDS = ["val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes_term(10, False, True, True)).decode(u"ascii")
            self._debug['val']['end'] = self._io.pos()


    class StringnlNoescapePair(KaitaiStruct):
        """Pair of unquoted, unescaped strings."""
        SEQ_FIELDS = ["val1", "val2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val1']['start'] = self._io.pos()
            self.val1 = PythonPickle.StringnlNoescape(self._io, self, self._root)
            self.val1._read()
            self._debug['val1']['end'] = self._io.pos()
            self._debug['val2']['start'] = self._io.pos()
            self.val2 = PythonPickle.StringnlNoescape(self._io, self, self._root)
            self.val2._read()
            self._debug['val2']['end'] = self._io.pos()


    class String4(KaitaiStruct):
        """Length prefixed string, between 0 and 2**31-1 bytes long. Encoding is
        unspecified.
        
        Although the len field is signed, any length < 0 will raise an exception
        during unpickling.
        
        See the documentation for `string1` for further detail about encodings.
        
        .. seealso::
           Source - https://github.com/python/cpython/blob/bb8071a4cae/Lib/pickle.py#L486-L495
        """
        SEQ_FIELDS = ["len", "val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_s4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['val']['start'] = self._io.pos()
            self.val = self._io.read_bytes(self.len)
            self._debug['val']['end'] = self._io.pos()


    class Op(KaitaiStruct):
        SEQ_FIELDS = ["code", "arg"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = KaitaiStream.resolve_enum(PythonPickle.Opcode, self._io.read_u1())
            self._debug['code']['end'] = self._io.pos()
            self._debug['arg']['start'] = self._io.pos()
            _on = self.code
            if _on == PythonPickle.Opcode.ext4:
                self.arg = self._io.read_u4le()
            elif _on == PythonPickle.Opcode.tuple1:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.setitem:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.readonly_buffer:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.stop:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.ext2:
                self.arg = self._io.read_u2le()
            elif _on == PythonPickle.Opcode.empty_tuple:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.newtrue:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.long:
                self.arg = PythonPickle.DecimalnlLong(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.newobj:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.bytearray8:
                self.arg = PythonPickle.Bytearray8(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.put:
                self.arg = PythonPickle.DecimalnlShort(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.stack_global:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.pop_mark:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.append:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.newfalse:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binpersid:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.build:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.empty_dict:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.tuple2:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.long4:
                self.arg = PythonPickle.Long4(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.next_buffer:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.appends:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binbytes:
                self.arg = PythonPickle.Bytes4(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.dup:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.list:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.proto:
                self.arg = self._io.read_u1()
            elif _on == PythonPickle.Opcode.pop:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.frame:
                self.arg = self._io.read_u8le()
            elif _on == PythonPickle.Opcode.string:
                self.arg = PythonPickle.Stringnl(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binunicode:
                self.arg = PythonPickle.Unicodestring4(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.float:
                self.arg = PythonPickle.Floatnl(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.reduce:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.global_opcode:
                self.arg = PythonPickle.StringnlNoescapePair(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binput:
                self.arg = self._io.read_u1()
            elif _on == PythonPickle.Opcode.memoize:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.persid:
                self.arg = PythonPickle.StringnlNoescape(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.ext1:
                self.arg = self._io.read_u1()
            elif _on == PythonPickle.Opcode.none:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.short_binunicode:
                self.arg = PythonPickle.Unicodestring1(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.obj:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binfloat:
                self.arg = self._io.read_f8be()
            elif _on == PythonPickle.Opcode.newobj_ex:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.empty_list:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.tuple:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binunicode8:
                self.arg = PythonPickle.Unicodestring8(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binget:
                self.arg = self._io.read_u1()
            elif _on == PythonPickle.Opcode.dict:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binstring:
                self.arg = PythonPickle.String4(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.setitems:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binint2:
                self.arg = self._io.read_u2le()
            elif _on == PythonPickle.Opcode.binbytes8:
                self.arg = PythonPickle.Bytes8(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binint1:
                self.arg = self._io.read_u1()
            elif _on == PythonPickle.Opcode.inst:
                self.arg = PythonPickle.StringnlNoescapePair(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.long_binget:
                self.arg = self._io.read_u4le()
            elif _on == PythonPickle.Opcode.long_binput:
                self.arg = self._io.read_u4le()
            elif _on == PythonPickle.Opcode.int:
                self.arg = PythonPickle.DecimalnlShort(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.binint:
                self.arg = self._io.read_s4le()
            elif _on == PythonPickle.Opcode.unicode:
                self.arg = PythonPickle.Unicodestringnl(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.long1:
                self.arg = PythonPickle.Long1(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.short_binstring:
                self.arg = PythonPickle.String1(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.mark:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.frozenset:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.tuple3:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.additems:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.get:
                self.arg = PythonPickle.DecimalnlShort(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.empty_set:
                self.arg = PythonPickle.NoArg(self._io, self, self._root)
                self.arg._read()
            elif _on == PythonPickle.Opcode.short_binbytes:
                self.arg = PythonPickle.Bytes1(self._io, self, self._root)
                self.arg._read()
            self._debug['arg']['end'] = self._io.pos()


    class Floatnl(KaitaiStruct):
        """Double float, encoded with the ASCII characters [0-9.e+-], '-inf', 'inf',
        or 'nan'.
        """
        SEQ_FIELDS = ["val"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['val']['start'] = self._io.pos()
            self.val = (self._io.read_bytes_term(10, False, True, True)).decode(u"ascii")
            self._debug['val']['end'] = self._io.pos()



