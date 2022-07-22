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

class ShapefileMain(KaitaiStruct):

    class ShapeType(Enum):
        null_shape = 0
        point = 1
        poly_line = 3
        polygon = 5
        multi_point = 8
        point_z = 11
        poly_line_z = 13
        polygon_z = 15
        multi_point_z = 18
        point_m = 21
        poly_line_m = 23
        polygon_m = 25
        multi_point_m = 28
        multi_patch = 31

    class PartType(Enum):
        triangle_strip = 0
        triangle_fan = 1
        outer_ring = 2
        inner_ring = 3
        first_ring = 4
        ring = 5
    SEQ_FIELDS = ["header", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = ShapefileMain.FileHeader(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['records']['start'] = self._io.pos()
        self.records = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['records']:
                self._debug['records']['arr'] = []
            self._debug['records']['arr'].append({'start': self._io.pos()})
            _t_records = ShapefileMain.Record(self._io, self, self._root)
            _t_records._read()
            self.records.append(_t_records)
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['records']['end'] = self._io.pos()

    class MultiPointM(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_points", "points", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()


    class BoundingBoxXYZM(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "m"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.x._read()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.y._read()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.z._read()
            self._debug['z']['end'] = self._io.pos()
            self._debug['m']['start'] = self._io.pos()
            self.m = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m._read()
            self._debug['m']['end'] = self._io.pos()


    class Point(KaitaiStruct):
        SEQ_FIELDS = ["x", "y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f8le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f8le()
            self._debug['y']['end'] = self._io.pos()


    class Polygon(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "points"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()


    class BoundsMinMax(KaitaiStruct):
        SEQ_FIELDS = ["min", "max"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['min']['start'] = self._io.pos()
            self.min = self._io.read_f8le()
            self._debug['min']['end'] = self._io.pos()
            self._debug['max']['start'] = self._io.pos()
            self.max = self._io.read_f8le()
            self._debug['max']['end'] = self._io.pos()


    class PolyLine(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "points"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()


    class MultiPointZ(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_points", "points", "z_range", "z_values", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['z_range']['start'] = self._io.pos()
            self.z_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.z_range._read()
            self._debug['z_range']['end'] = self._io.pos()
            self._debug['z_values']['start'] = self._io.pos()
            self.z_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['z_values']:
                    self._debug['z_values']['arr'] = []
                self._debug['z_values']['arr'].append({'start': self._io.pos()})
                self.z_values.append(self._io.read_f8le())
                self._debug['z_values']['arr'][i]['end'] = self._io.pos()

            self._debug['z_values']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()


    class PolyLineZ(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "points", "z_range", "z_values", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['z_range']['start'] = self._io.pos()
            self.z_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.z_range._read()
            self._debug['z_range']['end'] = self._io.pos()
            self._debug['z_values']['start'] = self._io.pos()
            self.z_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['z_values']:
                    self._debug['z_values']['arr'] = []
                self._debug['z_values']['arr'].append({'start': self._io.pos()})
                self.z_values.append(self._io.read_f8le())
                self._debug['z_values']['arr'][i]['end'] = self._io.pos()

            self._debug['z_values']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()


    class PolygonZ(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "points", "z_range", "z_values", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['z_range']['start'] = self._io.pos()
            self.z_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.z_range._read()
            self._debug['z_range']['end'] = self._io.pos()
            self._debug['z_values']['start'] = self._io.pos()
            self.z_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['z_values']:
                    self._debug['z_values']['arr'] = []
                self._debug['z_values']['arr'].append({'start': self._io.pos()})
                self.z_values.append(self._io.read_f8le())
                self._debug['z_values']['arr'][i]['end'] = self._io.pos()

            self._debug['z_values']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()


    class BoundingBoxXY(KaitaiStruct):
        SEQ_FIELDS = ["x", "y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.x._read()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.y._read()
            self._debug['y']['end'] = self._io.pos()


    class PointM(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "m"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f8le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f8le()
            self._debug['y']['end'] = self._io.pos()
            self._debug['m']['start'] = self._io.pos()
            self.m = self._io.read_f8le()
            self._debug['m']['end'] = self._io.pos()


    class PolygonM(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "points", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()


    class RecordHeader(KaitaiStruct):
        SEQ_FIELDS = ["record_number", "content_length"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['record_number']['start'] = self._io.pos()
            self.record_number = self._io.read_s4be()
            self._debug['record_number']['end'] = self._io.pos()
            self._debug['content_length']['start'] = self._io.pos()
            self.content_length = self._io.read_s4be()
            self._debug['content_length']['end'] = self._io.pos()


    class MultiPoint(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_points", "points"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["file_code", "unused_field_1", "unused_field_2", "unused_field_3", "unused_field_4", "unused_field_5", "file_length", "version", "shape_type", "bounding_box"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['file_code']['start'] = self._io.pos()
            self.file_code = self._io.read_bytes(4)
            self._debug['file_code']['end'] = self._io.pos()
            if not self.file_code == b"\x00\x00\x27\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x27\x0A", self.file_code, self._io, u"/types/file_header/seq/0")
            self._debug['unused_field_1']['start'] = self._io.pos()
            self.unused_field_1 = self._io.read_bytes(4)
            self._debug['unused_field_1']['end'] = self._io.pos()
            if not self.unused_field_1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.unused_field_1, self._io, u"/types/file_header/seq/1")
            self._debug['unused_field_2']['start'] = self._io.pos()
            self.unused_field_2 = self._io.read_bytes(4)
            self._debug['unused_field_2']['end'] = self._io.pos()
            if not self.unused_field_2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.unused_field_2, self._io, u"/types/file_header/seq/2")
            self._debug['unused_field_3']['start'] = self._io.pos()
            self.unused_field_3 = self._io.read_bytes(4)
            self._debug['unused_field_3']['end'] = self._io.pos()
            if not self.unused_field_3 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.unused_field_3, self._io, u"/types/file_header/seq/3")
            self._debug['unused_field_4']['start'] = self._io.pos()
            self.unused_field_4 = self._io.read_bytes(4)
            self._debug['unused_field_4']['end'] = self._io.pos()
            if not self.unused_field_4 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.unused_field_4, self._io, u"/types/file_header/seq/4")
            self._debug['unused_field_5']['start'] = self._io.pos()
            self.unused_field_5 = self._io.read_bytes(4)
            self._debug['unused_field_5']['end'] = self._io.pos()
            if not self.unused_field_5 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.unused_field_5, self._io, u"/types/file_header/seq/5")
            self._debug['file_length']['start'] = self._io.pos()
            self.file_length = self._io.read_s4be()
            self._debug['file_length']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(4)
            self._debug['version']['end'] = self._io.pos()
            if not self.version == b"\xE8\x03\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\xE8\x03\x00\x00", self.version, self._io, u"/types/file_header/seq/7")
            self._debug['shape_type']['start'] = self._io.pos()
            self.shape_type = KaitaiStream.resolve_enum(ShapefileMain.ShapeType, self._io.read_s4le())
            self._debug['shape_type']['end'] = self._io.pos()
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXYZM(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()


    class PointZ(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "m"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f8le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f8le()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f8le()
            self._debug['z']['end'] = self._io.pos()
            self._debug['m']['start'] = self._io.pos()
            self.m = self._io.read_f8le()
            self._debug['m']['end'] = self._io.pos()


    class Record(KaitaiStruct):
        SEQ_FIELDS = ["header", "contents"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = ShapefileMain.RecordHeader(self._io, self, self._root)
            self.header._read()
            self._debug['header']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            self.contents = ShapefileMain.RecordContents(self._io, self, self._root)
            self.contents._read()
            self._debug['contents']['end'] = self._io.pos()


    class RecordContents(KaitaiStruct):
        SEQ_FIELDS = ["shape_type", "shape_parameters"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['shape_type']['start'] = self._io.pos()
            self.shape_type = KaitaiStream.resolve_enum(ShapefileMain.ShapeType, self._io.read_s4le())
            self._debug['shape_type']['end'] = self._io.pos()
            if self.shape_type != ShapefileMain.ShapeType.null_shape:
                self._debug['shape_parameters']['start'] = self._io.pos()
                _on = self.shape_type
                if _on == ShapefileMain.ShapeType.poly_line_z:
                    self.shape_parameters = ShapefileMain.PolyLineZ(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.multi_patch:
                    self.shape_parameters = ShapefileMain.MultiPatch(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.poly_line_m:
                    self.shape_parameters = ShapefileMain.PolyLineM(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.polygon:
                    self.shape_parameters = ShapefileMain.Polygon(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.polygon_z:
                    self.shape_parameters = ShapefileMain.PolygonZ(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.point_z:
                    self.shape_parameters = ShapefileMain.PointZ(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.poly_line:
                    self.shape_parameters = ShapefileMain.PolyLine(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.point_m:
                    self.shape_parameters = ShapefileMain.PointM(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.polygon_m:
                    self.shape_parameters = ShapefileMain.PolygonM(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.multi_point:
                    self.shape_parameters = ShapefileMain.MultiPoint(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.point:
                    self.shape_parameters = ShapefileMain.Point(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.multi_point_m:
                    self.shape_parameters = ShapefileMain.MultiPointM(self._io, self, self._root)
                    self.shape_parameters._read()
                elif _on == ShapefileMain.ShapeType.multi_point_z:
                    self.shape_parameters = ShapefileMain.MultiPointZ(self._io, self, self._root)
                    self.shape_parameters._read()
                self._debug['shape_parameters']['end'] = self._io.pos()



    class MultiPatch(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "part_types", "points", "z_range", "z_values", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['part_types']['start'] = self._io.pos()
            self.part_types = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['part_types']:
                    self._debug['part_types']['arr'] = []
                self._debug['part_types']['arr'].append({'start': self._io.pos()})
                self.part_types.append(KaitaiStream.resolve_enum(ShapefileMain.PartType, self._io.read_s4le()))
                self._debug['part_types']['arr'][i]['end'] = self._io.pos()

            self._debug['part_types']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['z_range']['start'] = self._io.pos()
            self.z_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.z_range._read()
            self._debug['z_range']['end'] = self._io.pos()
            self._debug['z_values']['start'] = self._io.pos()
            self.z_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['z_values']:
                    self._debug['z_values']['arr'] = []
                self._debug['z_values']['arr'].append({'start': self._io.pos()})
                self.z_values.append(self._io.read_f8le())
                self._debug['z_values']['arr'][i]['end'] = self._io.pos()

            self._debug['z_values']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()


    class PolyLineM(KaitaiStruct):
        SEQ_FIELDS = ["bounding_box", "number_of_parts", "number_of_points", "parts", "points", "m_range", "m_values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = ShapefileMain.BoundingBoxXY(self._io, self, self._root)
            self.bounding_box._read()
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['number_of_parts']['start'] = self._io.pos()
            self.number_of_parts = self._io.read_s4le()
            self._debug['number_of_parts']['end'] = self._io.pos()
            self._debug['number_of_points']['start'] = self._io.pos()
            self.number_of_points = self._io.read_s4le()
            self._debug['number_of_points']['end'] = self._io.pos()
            self._debug['parts']['start'] = self._io.pos()
            self.parts = []
            for i in range(self.number_of_parts):
                if not 'arr' in self._debug['parts']:
                    self._debug['parts']['arr'] = []
                self._debug['parts']['arr'].append({'start': self._io.pos()})
                self.parts.append(self._io.read_s4le())
                self._debug['parts']['arr'][i]['end'] = self._io.pos()

            self._debug['parts']['end'] = self._io.pos()
            self._debug['points']['start'] = self._io.pos()
            self.points = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['points']:
                    self._debug['points']['arr'] = []
                self._debug['points']['arr'].append({'start': self._io.pos()})
                _t_points = ShapefileMain.Point(self._io, self, self._root)
                _t_points._read()
                self.points.append(_t_points)
                self._debug['points']['arr'][i]['end'] = self._io.pos()

            self._debug['points']['end'] = self._io.pos()
            self._debug['m_range']['start'] = self._io.pos()
            self.m_range = ShapefileMain.BoundsMinMax(self._io, self, self._root)
            self.m_range._read()
            self._debug['m_range']['end'] = self._io.pos()
            self._debug['m_values']['start'] = self._io.pos()
            self.m_values = []
            for i in range(self.number_of_points):
                if not 'arr' in self._debug['m_values']:
                    self._debug['m_values']['arr'] = []
                self._debug['m_values']['arr'].append({'start': self._io.pos()})
                self.m_values.append(self._io.read_f8le())
                self._debug['m_values']['arr'][i]['end'] = self._io.pos()

            self._debug['m_values']['end'] = self._io.pos()



