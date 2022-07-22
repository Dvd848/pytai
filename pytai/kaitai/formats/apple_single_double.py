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

class AppleSingleDouble(KaitaiStruct):
    """AppleSingle and AppleDouble files are used by certain Mac
    applications (e.g. Finder) to store Mac-specific file attributes on
    filesystems that do not support that.
    
    Syntactically, both formats are the same, the only difference is how
    they are being used:
    
    * AppleSingle means that only one file will be created on external
      filesystem that will hold both the data (AKA "data fork" in Apple
      terminology), and the attributes (AKA "resource fork").
    * AppleDouble means that two files will be created: a normal file
      that keeps the data ("data fork") is kept separately from an
      auxiliary file that contains attributes ("resource fork"), which
      is kept with the same name, but starting with an extra dot and
      underscore `._` to keep it hidden.
    
    In modern practice (Mac OS X), Finder only uses AppleDouble to keep
    compatibility with other OSes, as virtually nobody outside of Mac
    understands how to access data in AppleSingle container.
    
    .. seealso::
       Source - http://kaiser-edv.de/documents/AppleSingle_AppleDouble.pdf
    """

    class FileType(Enum):
        apple_single = 333312
        apple_double = 333319
    SEQ_FIELDS = ["magic", "version", "reserved", "num_entries", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = KaitaiStream.resolve_enum(AppleSingleDouble.FileType, self._io.read_u4be())
        self._debug['magic']['end'] = self._io.pos()
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4be()
        self._debug['version']['end'] = self._io.pos()
        self._debug['reserved']['start'] = self._io.pos()
        self.reserved = self._io.read_bytes(16)
        self._debug['reserved']['end'] = self._io.pos()
        self._debug['num_entries']['start'] = self._io.pos()
        self.num_entries = self._io.read_u2be()
        self._debug['num_entries']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self.entries = []
        for i in range(self.num_entries):
            if not 'arr' in self._debug['entries']:
                self._debug['entries']['arr'] = []
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            _t_entries = AppleSingleDouble.Entry(self._io, self, self._root)
            _t_entries._read()
            self.entries.append(_t_entries)
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()

    class Entry(KaitaiStruct):

        class Types(Enum):
            data_fork = 1
            resource_fork = 2
            real_name = 3
            comment = 4
            icon_bw = 5
            icon_color = 6
            file_dates_info = 8
            finder_info = 9
            macintosh_file_info = 10
            prodos_file_info = 11
            msdos_file_info = 12
            afp_short_name = 13
            afp_file_info = 14
            afp_directory_id = 15
        SEQ_FIELDS = ["type", "ofs_body", "len_body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(AppleSingleDouble.Entry.Types, self._io.read_u4be())
            self._debug['type']['end'] = self._io.pos()
            self._debug['ofs_body']['start'] = self._io.pos()
            self.ofs_body = self._io.read_u4be()
            self._debug['ofs_body']['end'] = self._io.pos()
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u4be()
            self._debug['len_body']['end'] = self._io.pos()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            _pos = self._io.pos()
            self._io.seek(self.ofs_body)
            self._debug['_m_body']['start'] = self._io.pos()
            _on = self.type
            if _on == AppleSingleDouble.Entry.Types.finder_info:
                self._raw__m_body = self._io.read_bytes(self.len_body)
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = AppleSingleDouble.FinderInfo(_io__raw__m_body, self, self._root)
                self._m_body._read()
            else:
                self._m_body = self._io.read_bytes(self.len_body)
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_body', None)


    class FinderInfo(KaitaiStruct):
        """Information specific to Finder.
        
        .. seealso::
           older Inside Macintosh, Volume II page 84 or Volume IV page 104.
        """
        SEQ_FIELDS = ["file_type", "file_creator", "flags", "location", "folder_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['file_type']['start'] = self._io.pos()
            self.file_type = self._io.read_bytes(4)
            self._debug['file_type']['end'] = self._io.pos()
            self._debug['file_creator']['start'] = self._io.pos()
            self.file_creator = self._io.read_bytes(4)
            self._debug['file_creator']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['location']['start'] = self._io.pos()
            self.location = AppleSingleDouble.Point(self._io, self, self._root)
            self.location._read()
            self._debug['location']['end'] = self._io.pos()
            self._debug['folder_id']['start'] = self._io.pos()
            self.folder_id = self._io.read_u2be()
            self._debug['folder_id']['end'] = self._io.pos()


    class Point(KaitaiStruct):
        """Specifies 2D coordinate in QuickDraw grid."""
        SEQ_FIELDS = ["x", "y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_u2be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_u2be()
            self._debug['y']['end'] = self._io.pos()



