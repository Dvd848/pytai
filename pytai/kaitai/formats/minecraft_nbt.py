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

class MinecraftNbt(KaitaiStruct):
    """A structured binary format native to Minecraft for saving game data and transferring
    it over the network (in multiplayer), such as player data
    ([`<player>.dat`](https://minecraft.wiki/w/Player.dat_format); contains
    e.g. player's inventory and location), saved worlds
    ([`level.dat`](
      https://minecraft.wiki/w/Java_Edition_level_format#level.dat_format
    ) and [Chunk format](https://minecraft.wiki/w/Chunk_format#NBT_structure)),
    list of saved multiplayer servers
    ([`servers.dat`](https://minecraft.wiki/w/Servers.dat_format)) and so on -
    see <https://minecraft.wiki/w/NBT_format#Uses>.
    
    The entire file should be _gzip_-compressed (in accordance with the original
    specification [NBT.txt](
      https://web.archive.org/web/20110723210920/https://www.minecraft.net/docs/NBT.txt
    ) by Notch), but can also be compressed with _zlib_ or uncompressed.
    
    This spec can only handle uncompressed NBT data, so be sure to first detect
    what type of data you are dealing with. You can use the Unix `file` command
    to do this (`file-5.20` or later is required; older versions do not recognize
    _zlib_-compressed data and return `application/octet-stream` instead):
    
    ```shell
    file --brief --mime-type input-unknown.nbt
    ```
    
    If it says:
    
      * `application/x-gzip` or `application/gzip` (since `file-5.37`), you can decompress it by
        * `gunzip -c input-gzip.nbt > output.nbt` or
        * `python3 -c "import sys, gzip; sys.stdout.buffer.write(
          gzip.decompress(sys.stdin.buffer.read()) )" < input-gzip.nbt > output.nbt`
      * `application/zlib`, you can use
        * `openssl zlib -d -in input-zlib.nbt -out output.nbt` (does not work on most systems)
        * `python3 -c "import sys, zlib; sys.stdout.buffer.write(
          zlib.decompress(sys.stdin.buffer.read()) )" < input-zlib.nbt > output.nbt`
      * something else (especially `image/x-pcx` and `application/octet-stream`),
        it is most likely already uncompressed.
    
    The file `output.nbt` generated by one of the above commands can already be
    processed with this Kaitai Struct specification.
    
    This spec **only** implements the Java edition format. There is also
    a [Bedrock edition](https://wiki.vg/NBT#Bedrock_edition) NBT format,
    which uses little-endian encoding and has a few other differences, but it isn't
    as popular as the Java edition format.
    
    **Implementation note:** strings in `TAG_String` are incorrectly decoded with
    standard UTF-8, while they are encoded in [**Modified UTF-8**](
      https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html#modified-utf-8
    ) (MUTF-8). That's because MUTF-8 is not supported natively by most target
    languages, and thus one must use external libraries to achieve a fully-compliant
    decoder. But decoding in standard UTF-8 is still better than nothing, and
    it usually works fine.
    
    All Unicode code points with incompatible representations in MUTF-8 and UTF-8 are
    U+0000 (_NUL_), U+D800-U+DFFF (_High_ and _Low Surrogates_) and U+10000-U+10FFFF
    (all _Supplementary_ Planes; includes e.g. emoticons, pictograms).
    A _MUTF-8_-encoded string containing these code points cannot be successfully
    decoded as UTF-8. The behavior in this case depends on the target language -
    usually an exception is thrown, or the bytes that are not valid UTF-8
    are replaced or ignored.
    
    **Sample files:**
    
      * <https://wiki.vg/NBT#Download>
      * <https://github.com/twoolie/NBT/blob/f9e892e/tests/world_test/data/scoreboard.dat>
      * <https://github.com/chmod222/cNBT/tree/3f74b69/testdata>
      * <https://github.com/PistonDevelopers/hematite_nbt/tree/0b85f89/tests>
    
    .. seealso::
       Source - https://wiki.vg/NBT
    
    
    .. seealso::
       Source - https://web.archive.org/web/20110723210920/https://www.minecraft.net/docs/NBT.txt
    
    
    .. seealso::
       Source - https://minecraft.wiki/w/NBT_format
    """

    class Tag(Enum):
        end = 0
        byte = 1
        short = 2
        int = 3
        long = 4
        float = 5
        double = 6
        byte_array = 7
        string = 8
        list = 9
        compound = 10
        int_array = 11
        long_array = 12
    SEQ_FIELDS = ["root_check", "root"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        if  ((self.root_type == MinecraftNbt.Tag.end) and (False)) :
            self._debug['root_check']['start'] = self._io.pos()
            self.root_check = self._io.read_bytes(0)
            self._debug['root_check']['end'] = self._io.pos()

        self._debug['root']['start'] = self._io.pos()
        self.root = MinecraftNbt.NamedTag(self._io, self, self._root)
        self.root._read()
        self._debug['root']['end'] = self._io.pos()

    class TagLongArray(KaitaiStruct):
        SEQ_FIELDS = ["num_tags", "tags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_tags']['start'] = self._io.pos()
            self.num_tags = self._io.read_s4be()
            self._debug['num_tags']['end'] = self._io.pos()
            self._debug['tags']['start'] = self._io.pos()
            self.tags = []
            for i in range(self.num_tags):
                if not 'arr' in self._debug['tags']:
                    self._debug['tags']['arr'] = []
                self._debug['tags']['arr'].append({'start': self._io.pos()})
                self.tags.append(self._io.read_s8be())
                self._debug['tags']['arr'][i]['end'] = self._io.pos()

            self._debug['tags']['end'] = self._io.pos()

        @property
        def tags_type(self):
            if hasattr(self, '_m_tags_type'):
                return self._m_tags_type

            self._m_tags_type = MinecraftNbt.Tag.long
            return getattr(self, '_m_tags_type', None)


    class TagByteArray(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_s4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


    class TagIntArray(KaitaiStruct):
        SEQ_FIELDS = ["num_tags", "tags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_tags']['start'] = self._io.pos()
            self.num_tags = self._io.read_s4be()
            self._debug['num_tags']['end'] = self._io.pos()
            self._debug['tags']['start'] = self._io.pos()
            self.tags = []
            for i in range(self.num_tags):
                if not 'arr' in self._debug['tags']:
                    self._debug['tags']['arr'] = []
                self._debug['tags']['arr'].append({'start': self._io.pos()})
                self.tags.append(self._io.read_s4be())
                self._debug['tags']['arr'][i]['end'] = self._io.pos()

            self._debug['tags']['end'] = self._io.pos()

        @property
        def tags_type(self):
            if hasattr(self, '_m_tags_type'):
                return self._m_tags_type

            self._m_tags_type = MinecraftNbt.Tag.int
            return getattr(self, '_m_tags_type', None)


    class TagList(KaitaiStruct):
        SEQ_FIELDS = ["tags_type", "num_tags", "tags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['tags_type']['start'] = self._io.pos()
            self.tags_type = KaitaiStream.resolve_enum(MinecraftNbt.Tag, self._io.read_u1())
            self._debug['tags_type']['end'] = self._io.pos()
            self._debug['num_tags']['start'] = self._io.pos()
            self.num_tags = self._io.read_s4be()
            self._debug['num_tags']['end'] = self._io.pos()
            self._debug['tags']['start'] = self._io.pos()
            self.tags = []
            for i in range(self.num_tags):
                if not 'arr' in self._debug['tags']:
                    self._debug['tags']['arr'] = []
                self._debug['tags']['arr'].append({'start': self._io.pos()})
                _on = self.tags_type
                if _on == MinecraftNbt.Tag.long_array:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    _t_tags = MinecraftNbt.TagLongArray(self._io, self, self._root)
                    _t_tags._read()
                    self.tags.append(_t_tags)
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.compound:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    _t_tags = MinecraftNbt.TagCompound(self._io, self, self._root)
                    _t_tags._read()
                    self.tags.append(_t_tags)
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.double:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    self.tags.append(self._io.read_f8be())
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.list:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    _t_tags = MinecraftNbt.TagList(self._io, self, self._root)
                    _t_tags._read()
                    self.tags.append(_t_tags)
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.float:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    self.tags.append(self._io.read_f4be())
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.short:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    self.tags.append(self._io.read_s2be())
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.int:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    self.tags.append(self._io.read_s4be())
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.byte_array:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    _t_tags = MinecraftNbt.TagByteArray(self._io, self, self._root)
                    _t_tags._read()
                    self.tags.append(_t_tags)
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.byte:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    self.tags.append(self._io.read_s1())
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.int_array:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    _t_tags = MinecraftNbt.TagIntArray(self._io, self, self._root)
                    _t_tags._read()
                    self.tags.append(_t_tags)
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.string:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    _t_tags = MinecraftNbt.TagString(self._io, self, self._root)
                    _t_tags._read()
                    self.tags.append(_t_tags)
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                elif _on == MinecraftNbt.Tag.long:
                    if not 'arr' in self._debug['tags']:
                        self._debug['tags']['arr'] = []
                    self._debug['tags']['arr'].append({'start': self._io.pos()})
                    self.tags.append(self._io.read_s8be())
                    self._debug['tags']['arr'][i]['end'] = self._io.pos()
                self._debug['tags']['arr'][i]['end'] = self._io.pos()

            self._debug['tags']['end'] = self._io.pos()


    class TagString(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u2be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = (self._io.read_bytes(self.len_data)).decode(u"utf-8")
            self._debug['data']['end'] = self._io.pos()


    class TagCompound(KaitaiStruct):
        SEQ_FIELDS = ["tags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['tags']['start'] = self._io.pos()
            self.tags = []
            i = 0
            while True:
                if not 'arr' in self._debug['tags']:
                    self._debug['tags']['arr'] = []
                self._debug['tags']['arr'].append({'start': self._io.pos()})
                _t_tags = MinecraftNbt.NamedTag(self._io, self, self._root)
                _t_tags._read()
                _ = _t_tags
                self.tags.append(_)
                self._debug['tags']['arr'][len(self.tags) - 1]['end'] = self._io.pos()
                if _.is_tag_end:
                    break
                i += 1
            self._debug['tags']['end'] = self._io.pos()

        @property
        def dump_num_tags(self):
            if hasattr(self, '_m_dump_num_tags'):
                return self._m_dump_num_tags

            self._m_dump_num_tags = (len(self.tags) - (1 if  ((len(self.tags) >= 1) and (self.tags[-1].is_tag_end))  else 0))
            return getattr(self, '_m_dump_num_tags', None)


    class NamedTag(KaitaiStruct):
        SEQ_FIELDS = ["type", "name", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(MinecraftNbt.Tag, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            if not (self.is_tag_end):
                self._debug['name']['start'] = self._io.pos()
                self.name = MinecraftNbt.TagString(self._io, self, self._root)
                self.name._read()
                self._debug['name']['end'] = self._io.pos()

            if not (self.is_tag_end):
                self._debug['payload']['start'] = self._io.pos()
                _on = self.type
                if _on == MinecraftNbt.Tag.long_array:
                    self.payload = MinecraftNbt.TagLongArray(self._io, self, self._root)
                    self.payload._read()
                elif _on == MinecraftNbt.Tag.compound:
                    self.payload = MinecraftNbt.TagCompound(self._io, self, self._root)
                    self.payload._read()
                elif _on == MinecraftNbt.Tag.double:
                    self.payload = self._io.read_f8be()
                elif _on == MinecraftNbt.Tag.list:
                    self.payload = MinecraftNbt.TagList(self._io, self, self._root)
                    self.payload._read()
                elif _on == MinecraftNbt.Tag.float:
                    self.payload = self._io.read_f4be()
                elif _on == MinecraftNbt.Tag.short:
                    self.payload = self._io.read_s2be()
                elif _on == MinecraftNbt.Tag.int:
                    self.payload = self._io.read_s4be()
                elif _on == MinecraftNbt.Tag.byte_array:
                    self.payload = MinecraftNbt.TagByteArray(self._io, self, self._root)
                    self.payload._read()
                elif _on == MinecraftNbt.Tag.byte:
                    self.payload = self._io.read_s1()
                elif _on == MinecraftNbt.Tag.int_array:
                    self.payload = MinecraftNbt.TagIntArray(self._io, self, self._root)
                    self.payload._read()
                elif _on == MinecraftNbt.Tag.string:
                    self.payload = MinecraftNbt.TagString(self._io, self, self._root)
                    self.payload._read()
                elif _on == MinecraftNbt.Tag.long:
                    self.payload = self._io.read_s8be()
                self._debug['payload']['end'] = self._io.pos()


        @property
        def is_tag_end(self):
            if hasattr(self, '_m_is_tag_end'):
                return self._m_is_tag_end

            self._m_is_tag_end = self.type == MinecraftNbt.Tag.end
            return getattr(self, '_m_is_tag_end', None)


    @property
    def root_type(self):
        if hasattr(self, '_m_root_type'):
            return self._m_root_type

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_root_type']['start'] = self._io.pos()
        self._m_root_type = KaitaiStream.resolve_enum(MinecraftNbt.Tag, self._io.read_u1())
        self._debug['_m_root_type']['end'] = self._io.pos()
        self._io.seek(_pos)
        if not self.root_type == MinecraftNbt.Tag.compound:
            raise kaitaistruct.ValidationNotEqualError(MinecraftNbt.Tag.compound, self.root_type, self._io, u"/instances/root_type")
        return getattr(self, '_m_root_type', None)


