"""A basic Visualizer and HEX Viewer GUI in Python, based on Kaitai Struct parsing.

This program offers a basic user interface to analyze the internal structure of 
binary files for a number of predefined formats. 
It utilizes the Kaitai Struct project to allow the user to navigate through 
a given binary file and match its logical contents to the matching binary
representation as displayed in the HEX view.

Source:
    https://github.com/Dvd848/pytai

License:
    MIT License

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
import argparse

from pytai.application import Application
from pytai.common import *


def getFormat(fn):
    with open(fn, "rb") as f:
        data = f.read(0x8010)
    
    sigs0 = {
        b"BM":"bmp",
        b"dex\x0A":"dex",
        b"IWAD":"doom_wad",
        b"PWAD":"doom_wad",
        b"\x7fELF":"elf",
        b"GIF87a":"gif",
        b"GIF89a":"gif",
        b"\x1f\x8b":"gzip",
        b"ID3\3":"id3v2_3",
        b"ID3\4":"id3v2_4",
        b"NES":"ines",
        b"\xCA\xFE\xBA\xBE":"java_class",
        b"\xFF\xD8":"jpeg",
        b"\xCE\xFA\xED\xFE":"mach_o",
        b"\xCF\xFA\xED\xFE":"mach_o",
        b"\xD0\xCF\x11\xE0":"microsoft_cfb",
        # b"\x0A":"pcx", # way too unreliable
        b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A":"png",
        b"OggS":"ogg",
        b"\0\0\0\x14ftypqt  ":"quicktime_mov",
        b"Rar!\x1a\x07\0":"rar",
        b"Rar!\x1a\x07\1\0":"rar",
        b"SQLite format 3\0":"sqlite3",
        b"FWS":"swf",
        b"VZ":"uefi_te",
        # b"II*\0":"tiff", # not in kaitai?
        # b"MM\0*":"tiff", # not in kaitai?
        b"PK\3\4":"zip",
    }

    for sig in sorted(sigs0, key=lambda x:len(x)):
        if data[:len(sig)] == sig:
            return sigs0[sig]

    if data.startswith(b"RIFF"):
        sub = data[8:8+4]
        riff_sigs = {b"AVI ":"avi", b"WAVE":"wav"}
        for sig in riff_sigs:
            if sub == sig:
                return riff_sigs[sub]
        return "riff"

    if data.startswith(b"MZ"):
        lfanew = int.from_bytes(data[60:64], "little")
        if lfanew <= 0x400:
            if data[lfanew:lfanew+4] == b"PE\0\0":
                return "microsoft_pe"
        return "dos_mz"

    if data[0x80:0x80+4] == b"DICM":
        return "dicom"

    if data[0x8001:0x8001+5] == b"CD001":
        return "iso9660"

    if data[-128:-128+5] == b"TAGv1":
        return "id3v1_1"

    if data[-18:] == b"TRUEVISION-XFILE.\0":
        return "tga"

    return None


def main() -> None:
    allowed_formats = kaitai_formats()
    parser = argparse.ArgumentParser(description='pytai: A Python-based Kaitai Struct Visualizer and HEX Viewer')
    parser.add_argument('file', action="store", help='Path to binary file')
    parser.add_argument('-kf', '--kaitai-format', action="store", 
                        choices = allowed_formats, metavar="FORMAT", 
                        help='Kaitai Format to use when parsing the file. '
                             f'Current formats found under "{SUBFOLDER_KAITAI}/{SUBFOLDER_FORMATS}" are: {", ".join(allowed_formats)}')
    args = parser.parse_args()

    if args.kaitai_format and (args.file is None):
        parser.error("--kaitai-format requires --file")

    if args.kaitai_format is None:
        args.kaitai_format = getFormat(args.file)
        if args.kaitai_format is not None:
            print(f"Format detection: {args.kaitai_format}")

    if args.kaitai_format is None:
        parser.error("Format unknown. Requires --kaitai-format")

    format = {"kaitai_format": args.kaitai_format}

    app = Application(args.file, format)
    
    app.run()


if __name__ == "__main__":
    main()