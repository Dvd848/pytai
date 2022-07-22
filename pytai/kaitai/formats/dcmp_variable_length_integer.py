# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This file was compiled from a KSY format file downloaded from:
# https://github.com/kaitai-io/kaitai_struct_formats


# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class DcmpVariableLengthInteger(KaitaiStruct):
    """A variable-length integer,
    in the format used by the 0xfe chunks in the `'dcmp' (0)` and `'dcmp' (1)` resource compression formats.
    See the dcmp_0 and dcmp_1 specs for more information about these compression formats.
    
    This variable-length integer format can store an integer `x` in any of the following ways:
    
    * In a single byte,
      if `0 <= x <= 0x7f`
      (7-bit unsigned integer)
    * In 2 bytes,
      if `-0x4000 <= x <= 0x3eff`
      (15-bit signed integer with the highest `0x100` values unavailable)
    * In 5 bytes, if `-0x80000000 <= x <= 0x7fffffff`
      (32-bit signed integer)
    
    In practice,
    values are always stored in the smallest possible format,
    but technically any of the larger formats could be used as well.
    
    .. seealso::
       Source - https://github.com/dgelessus/python-rsrcfork/blob/f891a6e/src/rsrcfork/compress/common.py
    """
    SEQ_FIELDS = ["first", "more"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['first']['start'] = self._io.pos()
        self.first = self._io.read_u1()
        self._debug['first']['end'] = self._io.pos()
        if self.first >= 128:
            self._debug['more']['start'] = self._io.pos()
            _on = self.first
            if _on == 255:
                self.more = self._io.read_s4be()
            else:
                self.more = self._io.read_u1()
            self._debug['more']['end'] = self._io.pos()


    @property
    def value(self):
        """The decoded value of the variable-length integer.
        """
        if hasattr(self, '_m_value'):
            return self._m_value

        self._m_value = (self.more if self.first == 255 else ((((self.first << 8) | self.more) - 49152) if self.first >= 128 else self.first))
        return getattr(self, '_m_value', None)


