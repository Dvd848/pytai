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

class Quake2Md2(KaitaiStruct):
    """The MD2 format is used for 3D animated models in id Sofware's Quake II.
    
    A model consists of named `frames`, each with the same number of `vertices`
    (`vertices_per_frame`). Each such vertex has a `position` and `normal` in
    model space. Each vertex has the same topological "meaning" across frames, in
    terms of triangle and texture info; it just varies in position and normal for
    animation purposes.
    
    How the vertices form triangles is defined via disjoint `triangles` or via
    `gl_cmds` (which allows strip and fan topology). Each triangle contains three
    `vertex_indices` into frame vertices, and three `tex_point_indices` into
    global `tex_coords`. Each texture point has pixel coords `s_px` and `t_px`
    ranging from 0 to `skin_{width,height}_px` respectively, along with
    `{s,t}_normalized` ranging from 0 to 1 for your convenience.
    
    A GL command has a `primitive` type (`TRIANGLE_FAN` or `TRIANGLE_STRIP`) along
    with some `vertices`. Each GL vertex contains `tex_coords_normalized` from 0
    to 1, and a `vertex_index` into frame vertices.
    
    A model may also contain `skins`, which are just file paths to PCX images.
    However, this is empty for many models, in which case it is up to the client
    (e.g. Q2PRO) to offer skins some other way (e.g. by similar filename in the
    current directory).
    
    There are 198 `frames` in total, partitioned into a fixed set of ranges used
    for different animations. Each frame has a standard `name` for humans, but the
    client just uses their index and the name can be arbitrary. The name, start
    frame index and frame count of each animation can be looked up in the arrays
    `anim_names`, `anim_start_indices`, and `anim_num_frames` respectively. This
    information is summarized in the following table:
    
    ```
    |   INDEX  |    NAME | SUFFIX | NOTES                                                  |
    |:--------:|--------:|:-------|:-------------------------------------------------------|
    |    0-39  |   stand | 01-40  | Idle animation                                         |
    |   40-45  |     run | 1-6    | Full run cycle                                         |
    |   46-53  |  attack | 1-8    | Shoot, reload; some weapons just repeat 1st few frames |
    |   54-57  |   pain1 | 01-04  | Q2Pro also uses this for switching weapons             |
    |   58-61  |   pain2 | 01-04  |                                                        |
    |   62-65  |   pain3 | 01-04  |                                                        |
    |   66-71  |    jump | 1-6    | Starts at height and lands on feet                     |
    |   72-83  |    flip | 01-12  | Flipoff, i.e. middle finger                            |
    |   84-94  |  salute | 01-11  |                                                        |
    |   95-111 |   taunt | 01-17  |                                                        |
    |  112-122 |    wave | 01-11  | Q2Pro plays this backwards for a handgrenade toss      |
    |  123-134 |   point | 01-12  |                                                        |
    |  135-153 |  crstnd | 01-19  | Idle while crouching                                   |
    |  154-159 |  crwalk | 1-6    |                                                        |
    |  160-168 | crattak | 1-9    |                                                        |
    |  169-172 |  crpain | 1-4    |                                                        |
    |  173-177 | crdeath | 1-5    |                                                        |
    |  178-183 |  death1 | 01-06  |                                                        |
    |  184-189 |  death2 | 01-06  |                                                        |
    |  190-197 |  death3 | 01-08  |                                                        |
    ```
    
    The above are filled in for player models; for the separate weapon models,
    the final frame is 173 "g_view" (unknown purpose) since weapons aren't shown
    during death animations. `a_grenades.md2`, the handgrenade weapon model, is
    the same except that the `wave` frames are blank (according to the default
    female model files). This is likely due to its dual use as a grenade throw
    animation where this model must leave the player's model.
    
    .. seealso::
       Source - https://icculus.org/~phaethon/q3a/formats/md2-schoenblum.html
    
    
    .. seealso::
       Source - http://tfc.duke.free.fr/coding/md2-specs-en.html
    
    
    .. seealso::
       Source - http://tastyspleen.net/~panjoo/downloads/quake2_model_frames.html
    
    
    .. seealso::
       Source - http://wiki.polycount.com/wiki/OldSiteResourcesQuake2FramesList
    """

    class GlPrimitive(Enum):
        triangle_strip = 0
        triangle_fan = 1
    SEQ_FIELDS = ["magic", "version", "skin_width_px", "skin_height_px", "bytes_per_frame", "num_skins", "vertices_per_frame", "num_tex_coords", "num_triangles", "num_gl_cmds", "num_frames", "ofs_skins", "ofs_tex_coords", "ofs_triangles", "ofs_frames", "ofs_gl_cmds", "ofs_eof"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x49\x44\x50\x32":
            raise kaitaistruct.ValidationNotEqualError(b"\x49\x44\x50\x32", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 8:
            raise kaitaistruct.ValidationNotEqualError(8, self.version, self._io, u"/seq/1")
        self._debug['skin_width_px']['start'] = self._io.pos()
        self.skin_width_px = self._io.read_u4le()
        self._debug['skin_width_px']['end'] = self._io.pos()
        self._debug['skin_height_px']['start'] = self._io.pos()
        self.skin_height_px = self._io.read_u4le()
        self._debug['skin_height_px']['end'] = self._io.pos()
        self._debug['bytes_per_frame']['start'] = self._io.pos()
        self.bytes_per_frame = self._io.read_u4le()
        self._debug['bytes_per_frame']['end'] = self._io.pos()
        self._debug['num_skins']['start'] = self._io.pos()
        self.num_skins = self._io.read_u4le()
        self._debug['num_skins']['end'] = self._io.pos()
        self._debug['vertices_per_frame']['start'] = self._io.pos()
        self.vertices_per_frame = self._io.read_u4le()
        self._debug['vertices_per_frame']['end'] = self._io.pos()
        self._debug['num_tex_coords']['start'] = self._io.pos()
        self.num_tex_coords = self._io.read_u4le()
        self._debug['num_tex_coords']['end'] = self._io.pos()
        self._debug['num_triangles']['start'] = self._io.pos()
        self.num_triangles = self._io.read_u4le()
        self._debug['num_triangles']['end'] = self._io.pos()
        self._debug['num_gl_cmds']['start'] = self._io.pos()
        self.num_gl_cmds = self._io.read_u4le()
        self._debug['num_gl_cmds']['end'] = self._io.pos()
        self._debug['num_frames']['start'] = self._io.pos()
        self.num_frames = self._io.read_u4le()
        self._debug['num_frames']['end'] = self._io.pos()
        self._debug['ofs_skins']['start'] = self._io.pos()
        self.ofs_skins = self._io.read_u4le()
        self._debug['ofs_skins']['end'] = self._io.pos()
        self._debug['ofs_tex_coords']['start'] = self._io.pos()
        self.ofs_tex_coords = self._io.read_u4le()
        self._debug['ofs_tex_coords']['end'] = self._io.pos()
        self._debug['ofs_triangles']['start'] = self._io.pos()
        self.ofs_triangles = self._io.read_u4le()
        self._debug['ofs_triangles']['end'] = self._io.pos()
        self._debug['ofs_frames']['start'] = self._io.pos()
        self.ofs_frames = self._io.read_u4le()
        self._debug['ofs_frames']['end'] = self._io.pos()
        self._debug['ofs_gl_cmds']['start'] = self._io.pos()
        self.ofs_gl_cmds = self._io.read_u4le()
        self._debug['ofs_gl_cmds']['end'] = self._io.pos()
        self._debug['ofs_eof']['start'] = self._io.pos()
        self.ofs_eof = self._io.read_u4le()
        self._debug['ofs_eof']['end'] = self._io.pos()

    class Vertex(KaitaiStruct):
        SEQ_FIELDS = ["position", "normal_index"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['position']['start'] = self._io.pos()
            self.position = Quake2Md2.CompressedVec(self._io, self, self._root)
            self.position._read()
            self._debug['position']['end'] = self._io.pos()
            self._debug['normal_index']['start'] = self._io.pos()
            self.normal_index = self._io.read_u1()
            self._debug['normal_index']['end'] = self._io.pos()

        @property
        def normal(self):
            if hasattr(self, '_m_normal'):
                return self._m_normal

            self._m_normal = self._root.anorms_table[self.normal_index]
            return getattr(self, '_m_normal', None)


    class CompressedVec(KaitaiStruct):
        SEQ_FIELDS = ["x_compressed", "y_compressed", "z_compressed"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x_compressed']['start'] = self._io.pos()
            self.x_compressed = self._io.read_u1()
            self._debug['x_compressed']['end'] = self._io.pos()
            self._debug['y_compressed']['start'] = self._io.pos()
            self.y_compressed = self._io.read_u1()
            self._debug['y_compressed']['end'] = self._io.pos()
            self._debug['z_compressed']['start'] = self._io.pos()
            self.z_compressed = self._io.read_u1()
            self._debug['z_compressed']['end'] = self._io.pos()

        @property
        def x(self):
            if hasattr(self, '_m_x'):
                return self._m_x

            self._m_x = ((self.x_compressed * self._parent._parent.scale.x) + self._parent._parent.translate.x)
            return getattr(self, '_m_x', None)

        @property
        def y(self):
            if hasattr(self, '_m_y'):
                return self._m_y

            self._m_y = ((self.y_compressed * self._parent._parent.scale.y) + self._parent._parent.translate.y)
            return getattr(self, '_m_y', None)

        @property
        def z(self):
            if hasattr(self, '_m_z'):
                return self._m_z

            self._m_z = ((self.z_compressed * self._parent._parent.scale.z) + self._parent._parent.translate.z)
            return getattr(self, '_m_z', None)


    class Triangle(KaitaiStruct):
        SEQ_FIELDS = ["vertex_indices", "tex_point_indices"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['vertex_indices']['start'] = self._io.pos()
            self.vertex_indices = []
            for i in range(3):
                if not 'arr' in self._debug['vertex_indices']:
                    self._debug['vertex_indices']['arr'] = []
                self._debug['vertex_indices']['arr'].append({'start': self._io.pos()})
                self.vertex_indices.append(self._io.read_u2le())
                self._debug['vertex_indices']['arr'][i]['end'] = self._io.pos()

            self._debug['vertex_indices']['end'] = self._io.pos()
            self._debug['tex_point_indices']['start'] = self._io.pos()
            self.tex_point_indices = []
            for i in range(3):
                if not 'arr' in self._debug['tex_point_indices']:
                    self._debug['tex_point_indices']['arr'] = []
                self._debug['tex_point_indices']['arr'].append({'start': self._io.pos()})
                self.tex_point_indices.append(self._io.read_u2le())
                self._debug['tex_point_indices']['arr'][i]['end'] = self._io.pos()

            self._debug['tex_point_indices']['end'] = self._io.pos()


    class Frame(KaitaiStruct):
        SEQ_FIELDS = ["scale", "translate", "name", "vertices"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['scale']['start'] = self._io.pos()
            self.scale = Quake2Md2.Vec3f(self._io, self, self._root)
            self.scale._read()
            self._debug['scale']['end'] = self._io.pos()
            self._debug['translate']['start'] = self._io.pos()
            self.translate = Quake2Md2.Vec3f(self._io, self, self._root)
            self.translate._read()
            self._debug['translate']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ascii")
            self._debug['name']['end'] = self._io.pos()
            self._debug['vertices']['start'] = self._io.pos()
            self.vertices = []
            for i in range(self._root.vertices_per_frame):
                if not 'arr' in self._debug['vertices']:
                    self._debug['vertices']['arr'] = []
                self._debug['vertices']['arr'].append({'start': self._io.pos()})
                _t_vertices = Quake2Md2.Vertex(self._io, self, self._root)
                _t_vertices._read()
                self.vertices.append(_t_vertices)
                self._debug['vertices']['arr'][i]['end'] = self._io.pos()

            self._debug['vertices']['end'] = self._io.pos()


    class GlCmdsList(KaitaiStruct):
        SEQ_FIELDS = ["items"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            if not (self._io.is_eof()):
                self._debug['items']['start'] = self._io.pos()
                self.items = []
                i = 0
                while True:
                    if not 'arr' in self._debug['items']:
                        self._debug['items']['arr'] = []
                    self._debug['items']['arr'].append({'start': self._io.pos()})
                    _t_items = Quake2Md2.GlCmd(self._io, self, self._root)
                    _t_items._read()
                    _ = _t_items
                    self.items.append(_)
                    self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                    if _.cmd_num_vertices == 0:
                        break
                    i += 1
                self._debug['items']['end'] = self._io.pos()



    class TexPoint(KaitaiStruct):
        SEQ_FIELDS = ["s_px", "t_px"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['s_px']['start'] = self._io.pos()
            self.s_px = self._io.read_u2le()
            self._debug['s_px']['end'] = self._io.pos()
            self._debug['t_px']['start'] = self._io.pos()
            self.t_px = self._io.read_u2le()
            self._debug['t_px']['end'] = self._io.pos()

        @property
        def s_normalized(self):
            if hasattr(self, '_m_s_normalized'):
                return self._m_s_normalized

            self._m_s_normalized = ((self.s_px + 0.0) / self._root.skin_width_px)
            return getattr(self, '_m_s_normalized', None)

        @property
        def t_normalized(self):
            if hasattr(self, '_m_t_normalized'):
                return self._m_t_normalized

            self._m_t_normalized = ((self.t_px + 0.0) / self._root.skin_height_px)
            return getattr(self, '_m_t_normalized', None)


    class Vec3f(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4le()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4le()
            self._debug['z']['end'] = self._io.pos()


    class GlVertex(KaitaiStruct):
        SEQ_FIELDS = ["tex_coords_normalized", "vertex_index"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['tex_coords_normalized']['start'] = self._io.pos()
            self.tex_coords_normalized = []
            for i in range(2):
                if not 'arr' in self._debug['tex_coords_normalized']:
                    self._debug['tex_coords_normalized']['arr'] = []
                self._debug['tex_coords_normalized']['arr'].append({'start': self._io.pos()})
                self.tex_coords_normalized.append(self._io.read_f4le())
                self._debug['tex_coords_normalized']['arr'][i]['end'] = self._io.pos()

            self._debug['tex_coords_normalized']['end'] = self._io.pos()
            self._debug['vertex_index']['start'] = self._io.pos()
            self.vertex_index = self._io.read_u4le()
            self._debug['vertex_index']['end'] = self._io.pos()


    class GlCmd(KaitaiStruct):
        SEQ_FIELDS = ["cmd_num_vertices", "vertices"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['cmd_num_vertices']['start'] = self._io.pos()
            self.cmd_num_vertices = self._io.read_s4le()
            self._debug['cmd_num_vertices']['end'] = self._io.pos()
            self._debug['vertices']['start'] = self._io.pos()
            self.vertices = []
            for i in range(self.num_vertices):
                if not 'arr' in self._debug['vertices']:
                    self._debug['vertices']['arr'] = []
                self._debug['vertices']['arr'].append({'start': self._io.pos()})
                _t_vertices = Quake2Md2.GlVertex(self._io, self, self._root)
                _t_vertices._read()
                self.vertices.append(_t_vertices)
                self._debug['vertices']['arr'][i]['end'] = self._io.pos()

            self._debug['vertices']['end'] = self._io.pos()

        @property
        def num_vertices(self):
            if hasattr(self, '_m_num_vertices'):
                return self._m_num_vertices

            self._m_num_vertices = (-(self.cmd_num_vertices) if self.cmd_num_vertices < 0 else self.cmd_num_vertices)
            return getattr(self, '_m_num_vertices', None)

        @property
        def primitive(self):
            if hasattr(self, '_m_primitive'):
                return self._m_primitive

            self._m_primitive = (Quake2Md2.GlPrimitive.triangle_fan if self.cmd_num_vertices < 0 else Quake2Md2.GlPrimitive.triangle_strip)
            return getattr(self, '_m_primitive', None)


    @property
    def anim_num_frames(self):
        if hasattr(self, '_m_anim_num_frames'):
            return self._m_anim_num_frames

        self._m_anim_num_frames = b"\x28\x06\x08\x04\x04\x04\x06\x0C\x0B\x11\x0B\x0C\x13\x06\x09\x04\x05\x06\x06\x08"
        return getattr(self, '_m_anim_num_frames', None)

    @property
    def anorms_table(self):
        """
        .. seealso::
           Quake anorms.h - https://github.com/skullernet/q2pro/blob/f4faabd/src/common/math.c#L80
           from
        """
        if hasattr(self, '_m_anorms_table'):
            return self._m_anorms_table

        self._m_anorms_table = [[-0.525731, 0.000000, 0.850651], [-0.442863, 0.238856, 0.864188], [-0.295242, 0.000000, 0.955423], [-0.309017, 0.500000, 0.809017], [-0.162460, 0.262866, 0.951056], [0.000000, 0.000000, 1.000000], [0.000000, 0.850651, 0.525731], [-0.147621, 0.716567, 0.681718], [0.147621, 0.716567, 0.681718], [0.000000, 0.525731, 0.850651], [0.309017, 0.500000, 0.809017], [0.525731, 0.000000, 0.850651], [0.295242, 0.000000, 0.955423], [0.442863, 0.238856, 0.864188], [0.162460, 0.262866, 0.951056], [-0.681718, 0.147621, 0.716567], [-0.809017, 0.309017, 0.500000], [-0.587785, 0.425325, 0.688191], [-0.850651, 0.525731, 0.000000], [-0.864188, 0.442863, 0.238856], [-0.716567, 0.681718, 0.147621], [-0.688191, 0.587785, 0.425325], [-0.500000, 0.809017, 0.309017], [-0.238856, 0.864188, 0.442863], [-0.425325, 0.688191, 0.587785], [-0.716567, 0.681718, -0.147621], [-0.500000, 0.809017, -0.309017], [-0.525731, 0.850651, 0.000000], [0.000000, 0.850651, -0.525731], [-0.238856, 0.864188, -0.442863], [0.000000, 0.955423, -0.295242], [-0.262866, 0.951056, -0.162460], [0.000000, 1.000000, 0.000000], [0.000000, 0.955423, 0.295242], [-0.262866, 0.951056, 0.162460], [0.238856, 0.864188, 0.442863], [0.262866, 0.951056, 0.162460], [0.500000, 0.809017, 0.309017], [0.238856, 0.864188, -0.442863], [0.262866, 0.951056, -0.162460], [0.500000, 0.809017, -0.309017], [0.850651, 0.525731, 0.000000], [0.716567, 0.681718, 0.147621], [0.716567, 0.681718, -0.147621], [0.525731, 0.850651, 0.000000], [0.425325, 0.688191, 0.587785], [0.864188, 0.442863, 0.238856], [0.688191, 0.587785, 0.425325], [0.809017, 0.309017, 0.500000], [0.681718, 0.147621, 0.716567], [0.587785, 0.425325, 0.688191], [0.955423, 0.295242, 0.000000], [1.000000, 0.000000, 0.000000], [0.951056, 0.162460, 0.262866], [0.850651, -0.525731, 0.000000], [0.955423, -0.295242, 0.000000], [0.864188, -0.442863, 0.238856], [0.951056, -0.162460, 0.262866], [0.809017, -0.309017, 0.500000], [0.681718, -0.147621, 0.716567], [0.850651, 0.000000, 0.525731], [0.864188, 0.442863, -0.238856], [0.809017, 0.309017, -0.500000], [0.951056, 0.162460, -0.262866], [0.525731, 0.000000, -0.850651], [0.681718, 0.147621, -0.716567], [0.681718, -0.147621, -0.716567], [0.850651, 0.000000, -0.525731], [0.809017, -0.309017, -0.500000], [0.864188, -0.442863, -0.238856], [0.951056, -0.162460, -0.262866], [0.147621, 0.716567, -0.681718], [0.309017, 0.500000, -0.809017], [0.425325, 0.688191, -0.587785], [0.442863, 0.238856, -0.864188], [0.587785, 0.425325, -0.688191], [0.688191, 0.587785, -0.425325], [-0.147621, 0.716567, -0.681718], [-0.309017, 0.500000, -0.809017], [0.000000, 0.525731, -0.850651], [-0.525731, 0.000000, -0.850651], [-0.442863, 0.238856, -0.864188], [-0.295242, 0.000000, -0.955423], [-0.162460, 0.262866, -0.951056], [0.000000, 0.000000, -1.000000], [0.295242, 0.000000, -0.955423], [0.162460, 0.262866, -0.951056], [-0.442863, -0.238856, -0.864188], [-0.309017, -0.500000, -0.809017], [-0.162460, -0.262866, -0.951056], [0.000000, -0.850651, -0.525731], [-0.147621, -0.716567, -0.681718], [0.147621, -0.716567, -0.681718], [0.000000, -0.525731, -0.850651], [0.309017, -0.500000, -0.809017], [0.442863, -0.238856, -0.864188], [0.162460, -0.262866, -0.951056], [0.238856, -0.864188, -0.442863], [0.500000, -0.809017, -0.309017], [0.425325, -0.688191, -0.587785], [0.716567, -0.681718, -0.147621], [0.688191, -0.587785, -0.425325], [0.587785, -0.425325, -0.688191], [0.000000, -0.955423, -0.295242], [0.000000, -1.000000, 0.000000], [0.262866, -0.951056, -0.162460], [0.000000, -0.850651, 0.525731], [0.000000, -0.955423, 0.295242], [0.238856, -0.864188, 0.442863], [0.262866, -0.951056, 0.162460], [0.500000, -0.809017, 0.309017], [0.716567, -0.681718, 0.147621], [0.525731, -0.850651, 0.000000], [-0.238856, -0.864188, -0.442863], [-0.500000, -0.809017, -0.309017], [-0.262866, -0.951056, -0.162460], [-0.850651, -0.525731, 0.000000], [-0.716567, -0.681718, -0.147621], [-0.716567, -0.681718, 0.147621], [-0.525731, -0.850651, 0.000000], [-0.500000, -0.809017, 0.309017], [-0.238856, -0.864188, 0.442863], [-0.262866, -0.951056, 0.162460], [-0.864188, -0.442863, 0.238856], [-0.809017, -0.309017, 0.500000], [-0.688191, -0.587785, 0.425325], [-0.681718, -0.147621, 0.716567], [-0.442863, -0.238856, 0.864188], [-0.587785, -0.425325, 0.688191], [-0.309017, -0.500000, 0.809017], [-0.147621, -0.716567, 0.681718], [-0.425325, -0.688191, 0.587785], [-0.162460, -0.262866, 0.951056], [0.442863, -0.238856, 0.864188], [0.162460, -0.262866, 0.951056], [0.309017, -0.500000, 0.809017], [0.147621, -0.716567, 0.681718], [0.000000, -0.525731, 0.850651], [0.425325, -0.688191, 0.587785], [0.587785, -0.425325, 0.688191], [0.688191, -0.587785, 0.425325], [-0.955423, 0.295242, 0.000000], [-0.951056, 0.162460, 0.262866], [-1.000000, 0.000000, 0.000000], [-0.850651, 0.000000, 0.525731], [-0.955423, -0.295242, 0.000000], [-0.951056, -0.162460, 0.262866], [-0.864188, 0.442863, -0.238856], [-0.951056, 0.162460, -0.262866], [-0.809017, 0.309017, -0.500000], [-0.864188, -0.442863, -0.238856], [-0.951056, -0.162460, -0.262866], [-0.809017, -0.309017, -0.500000], [-0.681718, 0.147621, -0.716567], [-0.681718, -0.147621, -0.716567], [-0.850651, 0.000000, -0.525731], [-0.688191, 0.587785, -0.425325], [-0.587785, 0.425325, -0.688191], [-0.425325, 0.688191, -0.587785], [-0.425325, -0.688191, -0.587785], [-0.587785, -0.425325, -0.688191], [-0.688191, -0.587785, -0.425325]]
        return getattr(self, '_m_anorms_table', None)

    @property
    def tex_coords(self):
        if hasattr(self, '_m_tex_coords'):
            return self._m_tex_coords

        _pos = self._io.pos()
        self._io.seek(self.ofs_tex_coords)
        self._debug['_m_tex_coords']['start'] = self._io.pos()
        self._m_tex_coords = []
        for i in range(self.num_tex_coords):
            if not 'arr' in self._debug['_m_tex_coords']:
                self._debug['_m_tex_coords']['arr'] = []
            self._debug['_m_tex_coords']['arr'].append({'start': self._io.pos()})
            _t__m_tex_coords = Quake2Md2.TexPoint(self._io, self, self._root)
            _t__m_tex_coords._read()
            self._m_tex_coords.append(_t__m_tex_coords)
            self._debug['_m_tex_coords']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_tex_coords']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_tex_coords', None)

    @property
    def triangles(self):
        if hasattr(self, '_m_triangles'):
            return self._m_triangles

        _pos = self._io.pos()
        self._io.seek(self.ofs_triangles)
        self._debug['_m_triangles']['start'] = self._io.pos()
        self._m_triangles = []
        for i in range(self.num_triangles):
            if not 'arr' in self._debug['_m_triangles']:
                self._debug['_m_triangles']['arr'] = []
            self._debug['_m_triangles']['arr'].append({'start': self._io.pos()})
            _t__m_triangles = Quake2Md2.Triangle(self._io, self, self._root)
            _t__m_triangles._read()
            self._m_triangles.append(_t__m_triangles)
            self._debug['_m_triangles']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_triangles']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_triangles', None)

    @property
    def frames(self):
        if hasattr(self, '_m_frames'):
            return self._m_frames

        _pos = self._io.pos()
        self._io.seek(self.ofs_frames)
        self._debug['_m_frames']['start'] = self._io.pos()
        self._raw__m_frames = []
        self._m_frames = []
        for i in range(self.num_frames):
            if not 'arr' in self._debug['_m_frames']:
                self._debug['_m_frames']['arr'] = []
            self._debug['_m_frames']['arr'].append({'start': self._io.pos()})
            self._raw__m_frames.append(self._io.read_bytes(self.bytes_per_frame))
            _io__raw__m_frames = KaitaiStream(BytesIO(self._raw__m_frames[i]))
            _t__m_frames = Quake2Md2.Frame(_io__raw__m_frames, self, self._root)
            _t__m_frames._read()
            self._m_frames.append(_t__m_frames)
            self._debug['_m_frames']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_frames']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_frames', None)

    @property
    def anim_names(self):
        if hasattr(self, '_m_anim_names'):
            return self._m_anim_names

        self._m_anim_names = [u"stand", u"run", u"attack", u"pain1", u"pain2", u"pain3", u"jump", u"flip", u"salute", u"taunt", u"wave", u"point", u"crstnd", u"crwalk", u"crattak", u"crpain", u"crdeath", u"death1", u"death2", u"death3"]
        return getattr(self, '_m_anim_names', None)

    @property
    def gl_cmds(self):
        if hasattr(self, '_m_gl_cmds'):
            return self._m_gl_cmds

        _pos = self._io.pos()
        self._io.seek(self.ofs_gl_cmds)
        self._debug['_m_gl_cmds']['start'] = self._io.pos()
        self._raw__m_gl_cmds = self._io.read_bytes((4 * self.num_gl_cmds))
        _io__raw__m_gl_cmds = KaitaiStream(BytesIO(self._raw__m_gl_cmds))
        self._m_gl_cmds = Quake2Md2.GlCmdsList(_io__raw__m_gl_cmds, self, self._root)
        self._m_gl_cmds._read()
        self._debug['_m_gl_cmds']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_gl_cmds', None)

    @property
    def skins(self):
        if hasattr(self, '_m_skins'):
            return self._m_skins

        _pos = self._io.pos()
        self._io.seek(self.ofs_skins)
        self._debug['_m_skins']['start'] = self._io.pos()
        self._m_skins = []
        for i in range(self.num_skins):
            if not 'arr' in self._debug['_m_skins']:
                self._debug['_m_skins']['arr'] = []
            self._debug['_m_skins']['arr'].append({'start': self._io.pos()})
            self._m_skins.append((KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ascii"))
            self._debug['_m_skins']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_skins']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_skins', None)

    @property
    def anim_start_indices(self):
        if hasattr(self, '_m_anim_start_indices'):
            return self._m_anim_start_indices

        self._m_anim_start_indices = b"\x00\x28\x2E\x36\x3A\x3E\x42\x48\x54\x5F\x70\x7B\x87\x9A\xA0\xA9\xAD\xB2\xB8\xBE"
        return getattr(self, '_m_anim_start_indices', None)


