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


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GenmidiOp2(KaitaiStruct):
    """GENMIDI.OP2 is a sound bank file used by players based on DMX sound
    library to play MIDI files with General MIDI instruments using OPL2
    sound chip (which was commonly installed on popular AdLib and Sound
    Blaster sound cards).
    
    Major users of DMX sound library include:
    
    * Original Doom game engine (and games based on it: Heretic, Hexen, Strife, Chex Quest)
    * Raptor: Call of the Shadows
    
    .. seealso::
       Source - http://www.fit.vutbr.cz/~arnost/muslib/op2_form.zip
    
    
    .. seealso::
       Source - https://doom.fandom.com/wiki/GENMIDI
    
    
    .. seealso::
       Source - https://moddingwiki.shikadi.net/wiki/OP2_Bank_Format
    """
    SEQ_FIELDS = ["magic", "instruments", "instrument_names"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x23\x4F\x50\x4C\x5F\x49\x49\x23":
            raise kaitaistruct.ValidationNotEqualError(b"\x23\x4F\x50\x4C\x5F\x49\x49\x23", self.magic, self._io, u"/seq/0")
        self._debug['instruments']['start'] = self._io.pos()
        self.instruments = []
        for i in range(175):
            if not 'arr' in self._debug['instruments']:
                self._debug['instruments']['arr'] = []
            self._debug['instruments']['arr'].append({'start': self._io.pos()})
            _t_instruments = GenmidiOp2.InstrumentEntry(self._io, self, self._root)
            _t_instruments._read()
            self.instruments.append(_t_instruments)
            self._debug['instruments']['arr'][i]['end'] = self._io.pos()

        self._debug['instruments']['end'] = self._io.pos()
        self._debug['instrument_names']['start'] = self._io.pos()
        self.instrument_names = []
        for i in range(175):
            if not 'arr' in self._debug['instrument_names']:
                self._debug['instrument_names']['arr'] = []
            self._debug['instrument_names']['arr'].append({'start': self._io.pos()})
            self.instrument_names.append((KaitaiStream.bytes_terminate(KaitaiStream.bytes_strip_right(self._io.read_bytes(32), 0), 0, False)).decode(u"ASCII"))
            self._debug['instrument_names']['arr'][i]['end'] = self._io.pos()

        self._debug['instrument_names']['end'] = self._io.pos()

    class InstrumentEntry(KaitaiStruct):
        SEQ_FIELDS = ["flags", "finetune", "note", "instruments"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['finetune']['start'] = self._io.pos()
            self.finetune = self._io.read_u1()
            self._debug['finetune']['end'] = self._io.pos()
            self._debug['note']['start'] = self._io.pos()
            self.note = self._io.read_u1()
            self._debug['note']['end'] = self._io.pos()
            self._debug['instruments']['start'] = self._io.pos()
            self.instruments = []
            for i in range(2):
                if not 'arr' in self._debug['instruments']:
                    self._debug['instruments']['arr'] = []
                self._debug['instruments']['arr'].append({'start': self._io.pos()})
                _t_instruments = GenmidiOp2.Instrument(self._io, self, self._root)
                _t_instruments._read()
                self.instruments.append(_t_instruments)
                self._debug['instruments']['arr'][i]['end'] = self._io.pos()

            self._debug['instruments']['end'] = self._io.pos()


    class Instrument(KaitaiStruct):
        SEQ_FIELDS = ["op1", "feedback", "op2", "unused", "base_note"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['op1']['start'] = self._io.pos()
            self.op1 = GenmidiOp2.OpSettings(self._io, self, self._root)
            self.op1._read()
            self._debug['op1']['end'] = self._io.pos()
            self._debug['feedback']['start'] = self._io.pos()
            self.feedback = self._io.read_u1()
            self._debug['feedback']['end'] = self._io.pos()
            self._debug['op2']['start'] = self._io.pos()
            self.op2 = GenmidiOp2.OpSettings(self._io, self, self._root)
            self.op2._read()
            self._debug['op2']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u1()
            self._debug['unused']['end'] = self._io.pos()
            self._debug['base_note']['start'] = self._io.pos()
            self.base_note = self._io.read_s2le()
            self._debug['base_note']['end'] = self._io.pos()


    class OpSettings(KaitaiStruct):
        """OPL2 settings for one operator (carrier or modulator)
        """
        SEQ_FIELDS = ["trem_vibr", "att_dec", "sust_rel", "wave", "scale", "level"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['trem_vibr']['start'] = self._io.pos()
            self.trem_vibr = self._io.read_u1()
            self._debug['trem_vibr']['end'] = self._io.pos()
            self._debug['att_dec']['start'] = self._io.pos()
            self.att_dec = self._io.read_u1()
            self._debug['att_dec']['end'] = self._io.pos()
            self._debug['sust_rel']['start'] = self._io.pos()
            self.sust_rel = self._io.read_u1()
            self._debug['sust_rel']['end'] = self._io.pos()
            self._debug['wave']['start'] = self._io.pos()
            self.wave = self._io.read_u1()
            self._debug['wave']['end'] = self._io.pos()
            self._debug['scale']['start'] = self._io.pos()
            self.scale = self._io.read_u1()
            self._debug['scale']['end'] = self._io.pos()
            self._debug['level']['start'] = self._io.pos()
            self.level = self._io.read_u1()
            self._debug['level']['end'] = self._io.pos()



