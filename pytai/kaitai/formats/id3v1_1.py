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

class Id3v11(KaitaiStruct):
    """ID3v1.1 tag is a method to store simple metadata in .mp3 files. The
    tag is appended to the end of file and spans exactly 128 bytes.
    
    This type is supposed to be used on full .mp3 files, seeking to
    proper position automatically. If you're interesting in parsing only
    the tag itself, please use `id3v1_1::id3_v1_1_tag` subtype.
    
    .. seealso::
       Source - https://id3.org/ID3v1
    """
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        pass

    class Id3V11Tag(KaitaiStruct):
        """ID3v1.1 tag itself, a fixed size 128 byte structure. Contains
        several metadata fields as fixed-size strings.
        
        Note that string encoding is not specified by standard, so real
        encoding used would vary a lot from one implementation to
        another. Most Windows-based applications tend to use "ANSI"
        (i.e. locale-dependent encoding, usually one byte per
        character). Some embedded applications allow selection of
        charset.
        """

        class GenreEnum(Enum):
            blues = 0
            classic_rock = 1
            country = 2
            dance = 3
            disco = 4
            funk = 5
            grunge = 6
            hip_hop = 7
            jazz = 8
            metal = 9
            new_age = 10
            oldies = 11
            other = 12
            pop = 13
            rnb = 14
            rap = 15
            reggae = 16
            rock = 17
            techno = 18
            industrial = 19
            alternative = 20
            ska = 21
            death_metal = 22
            pranks = 23
            soundtrack = 24
            euro_techno = 25
            ambient = 26
            trip_hop = 27
            vocal = 28
            jazz_funk = 29
            fusion = 30
            trance = 31
            classical = 32
            instrumental = 33
            acid = 34
            house = 35
            game = 36
            sound_clip = 37
            gospel = 38
            noise = 39
            alternrock = 40
            bass = 41
            soul = 42
            punk = 43
            space = 44
            meditative = 45
            instrumental_pop = 46
            instrumental_rock = 47
            ethnic = 48
            gothic = 49
            darkwave = 50
            techno_industrial = 51
            electronic = 52
            pop_folk = 53
            eurodance = 54
            dream = 55
            southern_rock = 56
            comedy = 57
            cult = 58
            gangsta = 59
            top_40 = 60
            christian_rap = 61
            pop_funk = 62
            jungle = 63
            native_american = 64
            cabaret = 65
            new_wave = 66
            psychadelic = 67
            rave = 68
            showtunes = 69
            trailer = 70
            lo_fi = 71
            tribal = 72
            acid_punk = 73
            acid_jazz = 74
            polka = 75
            retro = 76
            musical = 77
            rock_n_roll = 78
            hard_rock = 79
            folk = 80
            folk_rock = 81
            national_folk = 82
            swing = 83
            fast_fusion = 84
            bebob = 85
            latin = 86
            revival = 87
            celtic = 88
            bluegrass = 89
            avantgarde = 90
            gothic_rock = 91
            progressive_rock = 92
            psychedelic_rock = 93
            symphonic_rock = 94
            slow_rock = 95
            big_band = 96
            chorus = 97
            easy_listening = 98
            acoustic = 99
            humour = 100
            speech = 101
            chanson = 102
            opera = 103
            chamber_music = 104
            sonata = 105
            symphony = 106
            booty_bass = 107
            primus = 108
            porn_groove = 109
            satire = 110
            slow_jam = 111
            club = 112
            tango = 113
            samba = 114
            folklore = 115
            ballad = 116
            power_ballad = 117
            rhythmic_soul = 118
            freestyle = 119
            duet = 120
            punk_rock = 121
            drum_solo = 122
            a_capella = 123
            euro_house = 124
            dance_hall = 125
        SEQ_FIELDS = ["magic", "title", "artist", "album", "year", "comment", "genre"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(3)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x54\x41\x47":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x41\x47", self.magic, self._io, u"/types/id3_v1_1_tag/seq/0")
            self._debug['title']['start'] = self._io.pos()
            self.title = self._io.read_bytes(30)
            self._debug['title']['end'] = self._io.pos()
            self._debug['artist']['start'] = self._io.pos()
            self.artist = self._io.read_bytes(30)
            self._debug['artist']['end'] = self._io.pos()
            self._debug['album']['start'] = self._io.pos()
            self.album = self._io.read_bytes(30)
            self._debug['album']['end'] = self._io.pos()
            self._debug['year']['start'] = self._io.pos()
            self.year = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['year']['end'] = self._io.pos()
            self._debug['comment']['start'] = self._io.pos()
            self.comment = self._io.read_bytes(30)
            self._debug['comment']['end'] = self._io.pos()
            self._debug['genre']['start'] = self._io.pos()
            self.genre = KaitaiStream.resolve_enum(Id3v11.Id3V11Tag.GenreEnum, self._io.read_u1())
            self._debug['genre']['end'] = self._io.pos()


    @property
    def id3v1_tag(self):
        if hasattr(self, '_m_id3v1_tag'):
            return self._m_id3v1_tag

        _pos = self._io.pos()
        self._io.seek((self._io.size() - 128))
        self._debug['_m_id3v1_tag']['start'] = self._io.pos()
        self._m_id3v1_tag = Id3v11.Id3V11Tag(self._io, self, self._root)
        self._m_id3v1_tag._read()
        self._debug['_m_id3v1_tag']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_id3v1_tag', None)


