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

class Code6502(KaitaiStruct):
    """This spec can be used to disassemble raw stream of 6502 CPU machine
    code into individual operations. Each operation includes an opcode
    and, optionally, an argument. Register arguments are part of the
    `opcode` enum.
    """

    class Opcode(Enum):
        brk_impl = 0
        ora_x_ind = 1
        ora_zpg = 5
        asl_zpg = 6
        php_impl = 8
        ora_imm = 9
        asl_a = 10
        ora_abs = 13
        asl_abs = 14
        bpl_rel = 16
        ora_ind_y = 17
        ora_zpg_x = 21
        asl_zpg_x = 22
        clc_impl = 24
        ora_abs_y = 25
        ora_abs_x = 29
        asl_abs_x = 30
        jsr_abs = 32
        and_x_ind = 33
        bit_zpg = 36
        and_zpg = 37
        rol_zpg = 38
        plp_impl = 40
        and_imm = 41
        rol_a = 42
        bit_abs = 44
        and_abs = 45
        rol_abs = 46
        bmi_rel = 48
        and_ind_y = 49
        and_zpg_x = 53
        rol_zpg_x = 54
        sec_impl = 56
        and_abs_y = 57
        and_abs_x = 61
        rol_abs_x = 62
        rti_impl = 64
        eor_x_ind = 65
        eor_zpg = 69
        lsr_zpg = 70
        pha_impl = 72
        eor_imm = 73
        lsr_a = 74
        jmp_abs = 76
        eor_abs = 77
        lsr_abs = 78
        bvc_rel = 80
        eor_ind_y = 81
        eor_zpg_x = 85
        lsr_zpg_x = 86
        cli_impl = 88
        eor_abs_y = 89
        eor_abs_x = 93
        lsr_abs_x = 94
        rts_impl = 96
        adc_x_ind = 97
        adc_zpg = 101
        ror_zpg = 102
        pla_impl = 104
        adc_imm = 105
        ror_a = 106
        jmp_ind = 108
        adc_abs = 109
        ror_abs = 110
        bvs_rel = 112
        adc_ind_y = 113
        adc_zpg_x = 117
        ror_zpg_x = 118
        sei_impl = 120
        adc_abs_y = 121
        adc_abs_x = 125
        ror_abs_x = 126
        sta_x_ind = 129
        sty_zpg = 132
        sta_zpg = 133
        stx_zpg = 134
        dey_impl = 136
        txa_impl = 138
        sty_abs = 140
        sta_abs = 141
        stx_abs = 142
        bcc_rel = 144
        sta_ind_y = 145
        sty_zpg_x = 148
        sta_zpg_x = 149
        stx_zpg_y = 150
        tya_impl = 152
        sta_abs_y = 153
        txs_impl = 154
        sta_abs_x = 157
        ldy_imm = 160
        lda_x_ind = 161
        ldx_imm = 162
        ldy_zpg = 164
        lda_zpg = 165
        ldx_zpg = 166
        tay_impl = 168
        lda_imm = 169
        tax_impl = 170
        ldy_abs = 172
        lda_abs = 173
        ldx_abs = 174
        bcs_rel = 176
        lda_ind_y = 177
        ldy_zpg_x = 180
        lda_zpg_x = 181
        ldx_zpg_y = 182
        clv_impl = 184
        lda_abs_y = 185
        tsx_impl = 186
        ldy_abs_x = 188
        lda_abs_x = 189
        ldx_abs_y = 190
        cpy_imm = 192
        cmp_x_ind = 193
        cpy_zpg = 196
        cmp_zpg = 197
        dec_zpg = 198
        iny_impl = 200
        cmp_imm = 201
        dex_impl = 202
        cpy_abs = 204
        cmp_abs = 205
        dec_abs = 206
        bne_rel = 208
        cmp_ind_y = 209
        cmp_zpg_x = 213
        dec_zpg_x = 214
        cld_impl = 216
        cmp_abs_y = 217
        cmp_abs_x = 221
        dec_abs_x = 222
        cpx_imm = 224
        sbc_x_ind = 225
        cpx_zpg = 228
        sbc_zpg = 229
        inc_zpg = 230
        inx_impl = 232
        sbc_imm = 233
        nop_impl = 234
        cpx_abs = 236
        sbc_abs = 237
        inc_abs = 238
        beq_rel = 240
        sbc_ind_y = 241
        sbc_zpg_x = 245
        inc_zpg_x = 246
        sed_impl = 248
        sbc_abs_y = 249
        sbc_abs_x = 253
        inc_abs_x = 254
    SEQ_FIELDS = ["operations"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['operations']['start'] = self._io.pos()
        self.operations = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['operations']:
                self._debug['operations']['arr'] = []
            self._debug['operations']['arr'].append({'start': self._io.pos()})
            _t_operations = Code6502.Operation(self._io, self, self._root)
            _t_operations._read()
            self.operations.append(_t_operations)
            self._debug['operations']['arr'][len(self.operations) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['operations']['end'] = self._io.pos()

    class Operation(KaitaiStruct):
        SEQ_FIELDS = ["code", "args"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = KaitaiStream.resolve_enum(Code6502.Opcode, self._io.read_u1())
            self._debug['code']['end'] = self._io.pos()
            self._debug['args']['start'] = self._io.pos()
            _on = self.code
            if _on == Code6502.Opcode.bcc_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.ora_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.lda_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cpx_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sta_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sta_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.bcs_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.ldy_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.lsr_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.and_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.adc_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sta_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.bne_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.lda_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.adc_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.lsr_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.adc_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sta_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.cpx_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.jmp_ind:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.adc_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.eor_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.eor_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sta_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sbc_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cpy_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ldx_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.adc_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.bpl_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.ora_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ror_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.adc_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.eor_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.lda_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.bit_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.rol_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sty_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.jsr_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.eor_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.eor_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.lda_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.lda_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.bmi_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.sty_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.adc_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.rol_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.stx_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.asl_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.lsr_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ora_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.adc_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ldy_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.cmp_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.lda_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.bvs_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.lda_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cmp_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.inc_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.asl_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.and_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ldx_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.and_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cpx_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.dec_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ror_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ldx_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.dec_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sbc_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cmp_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ror_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.inc_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.and_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sbc_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.asl_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.eor_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ora_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ldy_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sbc_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.asl_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sbc_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.rol_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.lsr_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.stx_zpg_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ora_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.eor_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.bit_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ldx_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ldy_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.jmp_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.beq_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.dec_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.and_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.and_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cmp_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.eor_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sbc_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.cmp_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sbc_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cmp_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.stx_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sty_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.cpy_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.dec_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.ror_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sta_abs_y:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.inc_abs_x:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.lda_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cmp_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cpy_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ldx_zpg_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.sbc_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ora_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.rol_zpg_x:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ora_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.sta_ind_y:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.and_abs:
                self.args = self._io.read_u2le()
            elif _on == Code6502.Opcode.and_imm:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.cmp_x_ind:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.ldy_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.inc_zpg:
                self.args = self._io.read_u1()
            elif _on == Code6502.Opcode.bvc_rel:
                self.args = self._io.read_s1()
            elif _on == Code6502.Opcode.ora_zpg:
                self.args = self._io.read_u1()
            self._debug['args']['end'] = self._io.pos()



