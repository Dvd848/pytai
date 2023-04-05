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

class WindowsResourceFile(KaitaiStruct):
    """Windows resource file (.res) are binary bundles of
    "resources". Resource has some sort of ID (numerical or string),
    type (predefined or user-defined), and raw value. Resource files can
    be seen standalone (as .res file), or embedded inside PE executable
    (.exe, .dll) files.
    
    Typical use cases include:
    
    * providing information about the application (such as title, copyrights, etc)
    * embedding icon(s) to be displayed in file managers into .exe
    * adding non-code data into the binary, such as menus, dialog forms,
      cursor images, fonts, various misc bitmaps, and locale-aware
      strings
    
    Windows provides special API to access "resources" from a binary.
    
    Normally, resources files are created with `rc` compiler: it takes a
    .rc file (so called "resource-definition script") + all the raw
    resource binary files for input, and outputs .res file. That .res
    file can be linked into an .exe / .dll afterwards using a linker.
    
    Internally, resource file is just a sequence of individual resource
    definitions. RC tool ensures that first resource (#0) is always
    empty.
    """
    SEQ_FIELDS = ["resources"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['resources']['start'] = self._io.pos()
        self.resources = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['resources']:
                self._debug['resources']['arr'] = []
            self._debug['resources']['arr'].append({'start': self._io.pos()})
            _t_resources = WindowsResourceFile.Resource(self._io, self, self._root)
            _t_resources._read()
            self.resources.append(_t_resources)
            self._debug['resources']['arr'][len(self.resources) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['resources']['end'] = self._io.pos()

    class Resource(KaitaiStruct):
        """Each resource has a `type` and a `name`, which can be used to
        identify it, and a `value`. Both `type` and `name` can be a
        number or a string.
        
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/menurc/resourceheader
        """

        class PredefTypes(Enum):
            cursor = 1
            bitmap = 2
            icon = 3
            menu = 4
            dialog = 5
            string = 6
            fontdir = 7
            font = 8
            accelerator = 9
            rcdata = 10
            messagetable = 11
            group_cursor = 12
            group_icon = 14
            version = 16
            dlginclude = 17
            plugplay = 19
            vxd = 20
            anicursor = 21
            aniicon = 22
            html = 23
            manifest = 24
        SEQ_FIELDS = ["value_size", "header_size", "type", "name", "padding1", "format_version", "flags", "language", "value_version", "characteristics", "value", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['value_size']['start'] = self._io.pos()
            self.value_size = self._io.read_u4le()
            self._debug['value_size']['end'] = self._io.pos()
            self._debug['header_size']['start'] = self._io.pos()
            self.header_size = self._io.read_u4le()
            self._debug['header_size']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = WindowsResourceFile.UnicodeOrId(self._io, self, self._root)
            self.type._read()
            self._debug['type']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = WindowsResourceFile.UnicodeOrId(self._io, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self._debug['padding1']['end'] = self._io.pos()
            self._debug['format_version']['start'] = self._io.pos()
            self.format_version = self._io.read_u4le()
            self._debug['format_version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['language']['start'] = self._io.pos()
            self.language = self._io.read_u2le()
            self._debug['language']['end'] = self._io.pos()
            self._debug['value_version']['start'] = self._io.pos()
            self.value_version = self._io.read_u4le()
            self._debug['value_version']['end'] = self._io.pos()
            self._debug['characteristics']['start'] = self._io.pos()
            self.characteristics = self._io.read_u4le()
            self._debug['characteristics']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bytes(self.value_size)
            self._debug['value']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self.padding2 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self._debug['padding2']['end'] = self._io.pos()

        @property
        def type_as_predef(self):
            """Numeric type IDs in range of [0..0xff] are reserved for
            system usage in Windows, and there are some predefined,
            well-known values in that range. This instance allows to get
            it as enum value, if applicable.
            """
            if hasattr(self, '_m_type_as_predef'):
                return self._m_type_as_predef

            if  ((not (self.type.is_string)) and (self.type.as_numeric <= 255)) :
                self._m_type_as_predef = KaitaiStream.resolve_enum(WindowsResourceFile.Resource.PredefTypes, self.type.as_numeric)

            return getattr(self, '_m_type_as_predef', None)


    class UnicodeOrId(KaitaiStruct):
        """Resources use a special serialization of names and types: they
        can be either a number or a string.
        
        Use `is_string` to check which kind we've got here, and then use
        `as_numeric` or `as_string` to get relevant value.
        """
        SEQ_FIELDS = ["first", "as_numeric", "rest", "noop"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if self.save_pos1 >= 0:
                self._debug['first']['start'] = self._io.pos()
                self.first = self._io.read_u2le()
                self._debug['first']['end'] = self._io.pos()

            if not (self.is_string):
                self._debug['as_numeric']['start'] = self._io.pos()
                self.as_numeric = self._io.read_u2le()
                self._debug['as_numeric']['end'] = self._io.pos()

            if self.is_string:
                self._debug['rest']['start'] = self._io.pos()
                self.rest = []
                i = 0
                while True:
                    if not 'arr' in self._debug['rest']:
                        self._debug['rest']['arr'] = []
                    self._debug['rest']['arr'].append({'start': self._io.pos()})
                    _ = self._io.read_u2le()
                    self.rest.append(_)
                    self._debug['rest']['arr'][len(self.rest) - 1]['end'] = self._io.pos()
                    if _ == 0:
                        break
                    i += 1
                self._debug['rest']['end'] = self._io.pos()

            if  ((self.is_string) and (self.save_pos2 >= 0)) :
                self._debug['noop']['start'] = self._io.pos()
                self.noop = self._io.read_bytes(0)
                self._debug['noop']['end'] = self._io.pos()


        @property
        def save_pos1(self):
            if hasattr(self, '_m_save_pos1'):
                return self._m_save_pos1

            self._m_save_pos1 = self._io.pos()
            return getattr(self, '_m_save_pos1', None)

        @property
        def save_pos2(self):
            if hasattr(self, '_m_save_pos2'):
                return self._m_save_pos2

            self._m_save_pos2 = self._io.pos()
            return getattr(self, '_m_save_pos2', None)

        @property
        def is_string(self):
            if hasattr(self, '_m_is_string'):
                return self._m_is_string

            self._m_is_string = self.first != 65535
            return getattr(self, '_m_is_string', None)

        @property
        def as_string(self):
            if hasattr(self, '_m_as_string'):
                return self._m_as_string

            if self.is_string:
                _pos = self._io.pos()
                self._io.seek(self.save_pos1)
                self._debug['_m_as_string']['start'] = self._io.pos()
                self._m_as_string = (self._io.read_bytes(((self.save_pos2 - self.save_pos1) - 2))).decode(u"UTF-16LE")
                self._debug['_m_as_string']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_as_string', None)



