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

class Wmf(KaitaiStruct):
    """WMF (Windows Metafile) is a relatively early vector image format
    introduced for Microsoft Windows in 1990.
    
    Inside, it provides a serialized list of Windows GDI (Graphics
    Device Interface) function calls, which, if played back, result in
    an image being drawn on a given surface (display, off-screen buffer,
    printer, etc).
    
    .. seealso::
       Source - https://www.loc.gov/preservation/digital/formats/digformatspecs/WindowsMetafileFormat(wmf)Specification.pdf
    """

    class Func(Enum):
        eof = 0
        savedc = 30
        realizepalette = 53
        setpalentries = 55
        createpalette = 247
        setbkmode = 258
        setmapmode = 259
        setrop2 = 260
        setrelabs = 261
        setpolyfillmode = 262
        setstretchbltmode = 263
        settextcharextra = 264
        restoredc = 295
        invertregion = 298
        paintregion = 299
        selectclipregion = 300
        selectobject = 301
        settextalign = 302
        resizepalette = 313
        dibcreatepatternbrush = 322
        setlayout = 329
        deleteobject = 496
        createpatternbrush = 505
        setbkcolor = 513
        settextcolor = 521
        settextjustification = 522
        setwindoworg = 523
        setwindowext = 524
        setviewportorg = 525
        setviewportext = 526
        offsetwindoworg = 527
        offsetviewportorg = 529
        lineto = 531
        moveto = 532
        offsetcliprgn = 544
        fillregion = 552
        setmapperflags = 561
        selectpalette = 564
        createpenindirect = 762
        createfontindirect = 763
        createbrushindirect = 764
        polygon = 804
        polyline = 805
        scalewindowext = 1040
        scaleviewportext = 1042
        excludecliprect = 1045
        intersectcliprect = 1046
        ellipse = 1048
        floodfill = 1049
        rectangle = 1051
        setpixel = 1055
        frameregion = 1065
        animatepalette = 1078
        textout = 1313
        polypolygon = 1336
        extfloodfill = 1352
        roundrect = 1564
        patblt = 1565
        escape = 1574
        createregion = 1791
        arc = 2071
        pie = 2074
        chord = 2096
        bitblt = 2338
        dibbitblt = 2368
        exttextout = 2610
        stretchblt = 2851
        dibstretchblt = 2881
        setdibtodev = 3379
        stretchdib = 3907

    class BinRasterOp(Enum):
        black = 1
        notmergepen = 2
        masknotpen = 3
        notcopypen = 4
        maskpennot = 5
        not = 6
        xorpen = 7
        notmaskpen = 8
        maskpen = 9
        notxorpen = 10
        nop = 11
        mergenotpen = 12
        copypen = 13
        mergepennot = 14
        mergepen = 15
        white = 16

    class MixMode(Enum):
        transparent = 1
        opaque = 2

    class PolyFillMode(Enum):
        alternate = 1
        winding = 2
    SEQ_FIELDS = ["special_header", "header", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['special_header']['start'] = self._io.pos()
        self.special_header = Wmf.SpecialHeader(self._io, self, self._root)
        self.special_header._read()
        self._debug['special_header']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self.header = Wmf.Header(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['records']['start'] = self._io.pos()
        self.records = []
        i = 0
        while True:
            if not 'arr' in self._debug['records']:
                self._debug['records']['arr'] = []
            self._debug['records']['arr'].append({'start': self._io.pos()})
            _t_records = Wmf.Record(self._io, self, self._root)
            _t_records._read()
            _ = _t_records
            self.records.append(_)
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            if _.function == Wmf.Func.eof:
                break
            i += 1
        self._debug['records']['end'] = self._io.pos()

    class ParamsSetwindoworg(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.31
        """
        SEQ_FIELDS = ["y", "x"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_s2le()
            self._debug['y']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_s2le()
            self._debug['x']['end'] = self._io.pos()


    class ParamsSetbkmode(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.15
        """
        SEQ_FIELDS = ["bk_mode"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bk_mode']['start'] = self._io.pos()
            self.bk_mode = KaitaiStream.resolve_enum(Wmf.MixMode, self._io.read_u2le())
            self._debug['bk_mode']['end'] = self._io.pos()


    class PointS(KaitaiStruct):
        """
        .. seealso::
           section 2.2.1.12
        """
        SEQ_FIELDS = ["x", "y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_s2le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_s2le()
            self._debug['y']['end'] = self._io.pos()


    class ParamsSetwindowext(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.30
        """
        SEQ_FIELDS = ["y", "x"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_s2le()
            self._debug['y']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_s2le()
            self._debug['x']['end'] = self._io.pos()


    class ParamsPolygon(KaitaiStruct):
        """
        .. seealso::
           section 2.3.3.15 = params_polyline
        """
        SEQ_FIELDS = ["num_points", "points"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_points']['start'] = self._io.pos()
            self.num_points = self._io.read_s2le()
            self._debug['num_points']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.num_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = Wmf.PointS(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()


    class Header(KaitaiStruct):

        class MetafileType(Enum):
            memory_metafile = 1
            disk_metafile = 2
        SEQ_FIELDS = ["metafile_type", "header_size", "version", "size", "number_of_objects", "max_record", "number_of_members"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['metafile_type']['start'] = self._io.pos()
            self.metafile_type = KaitaiStream.resolve_enum(Wmf.Header.MetafileType, self._io.read_u2le())
            self._debug['metafile_type']['end'] = self._io.pos()
            self._debug['header_size']['start'] = self._io.pos()
            self.header_size = self._io.read_u2le()
            self._debug['header_size']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['number_of_objects']['start'] = self._io.pos()
            self.number_of_objects = self._io.read_u2le()
            self._debug['number_of_objects']['end'] = self._io.pos()
            self._debug['max_record']['start'] = self._io.pos()
            self.max_record = self._io.read_u4le()
            self._debug['max_record']['end'] = self._io.pos()
            self._debug['number_of_members']['start'] = self._io.pos()
            self.number_of_members = self._io.read_u2le()
            self._debug['number_of_members']['end'] = self._io.pos()


    class ColorRef(KaitaiStruct):
        """
        .. seealso::
           section 2.2.1.7
        """
        SEQ_FIELDS = ["red", "green", "blue", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['red']['start'] = self._io.pos()
            self.red = self._io.read_u1()
            self._debug['red']['end'] = self._io.pos()
            self._debug['green']['start'] = self._io.pos()
            self.green = self._io.read_u1()
            self._debug['green']['end'] = self._io.pos()
            self._debug['blue']['start'] = self._io.pos()
            self.blue = self._io.read_u1()
            self._debug['blue']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u1()
            self._debug['reserved']['end'] = self._io.pos()


    class ParamsSetrop2(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.22
        """
        SEQ_FIELDS = ["draw_mode"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['draw_mode']['start'] = self._io.pos()
            self.draw_mode = KaitaiStream.resolve_enum(Wmf.BinRasterOp, self._io.read_u2le())
            self._debug['draw_mode']['end'] = self._io.pos()


    class ParamsSetpolyfillmode(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.20
        """
        SEQ_FIELDS = ["poly_fill_mode"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['poly_fill_mode']['start'] = self._io.pos()
            self.poly_fill_mode = KaitaiStream.resolve_enum(Wmf.PolyFillMode, self._io.read_u2le())
            self._debug['poly_fill_mode']['end'] = self._io.pos()


    class ParamsPolyline(KaitaiStruct):
        """
        .. seealso::
           section 2.3.3.14
        """
        SEQ_FIELDS = ["num_points", "points"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_points']['start'] = self._io.pos()
            self.num_points = self._io.read_s2le()
            self._debug['num_points']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.num_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = Wmf.PointS(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()


    class SpecialHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "handle", "left", "top", "right", "bottom", "inch", "reserved", "checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xD7\xCD\xC6\x9A":
                raise kaitaistruct.ValidationNotEqualError(b"\xD7\xCD\xC6\x9A", self.magic, self._io, u"/types/special_header/seq/0")
            self._debug['handle']['start'] = self._io.pos()
            self.handle = self._io.read_bytes(2)
            self._debug['handle']['end'] = self._io.pos()
            if not self.handle == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.handle, self._io, u"/types/special_header/seq/1")
            self._debug['left']['start'] = self._io.pos()
            self.left = self._io.read_s2le()
            self._debug['left']['end'] = self._io.pos()
            self._debug['top']['start'] = self._io.pos()
            self.top = self._io.read_s2le()
            self._debug['top']['end'] = self._io.pos()
            self._debug['right']['start'] = self._io.pos()
            self.right = self._io.read_s2le()
            self._debug['right']['end'] = self._io.pos()
            self._debug['bottom']['start'] = self._io.pos()
            self.bottom = self._io.read_s2le()
            self._debug['bottom']['end'] = self._io.pos()
            self._debug['inch']['start'] = self._io.pos()
            self.inch = self._io.read_u2le()
            self._debug['inch']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved, self._io, u"/types/special_header/seq/7")
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u2le()
            self._debug['checksum']['end'] = self._io.pos()


    class Record(KaitaiStruct):
        SEQ_FIELDS = ["size", "function", "params"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['function']['start'] = self._io.pos()
            self.function = KaitaiStream.resolve_enum(Wmf.Func, self._io.read_u2le())
            self._debug['function']['end'] = self._io.pos()
            self._debug['params']['start'] = self._io.pos()
            _on = self.function
            if _on == Wmf.Func.setbkmode:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetbkmode(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.polygon:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsPolygon(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.setbkcolor:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ColorRef(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.setpolyfillmode:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetpolyfillmode(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.setwindoworg:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetwindoworg(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.setrop2:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetrop2(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.setwindowext:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetwindowext(_io__raw_params, self, self._root)
                self.params._read()
            elif _on == Wmf.Func.polyline:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsPolyline(_io__raw_params, self, self._root)
                self.params._read()
            else:
                self.params = self._io.read_bytes(((self.size - 3) * 2))
            self._debug['params']['end'] = self._io.pos()



