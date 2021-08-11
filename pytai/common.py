from pathlib import Path

SUBFOLDER_KAITAI = "kaitai"
SUBFOLDER_FORMATS = "formats"

KAITAI_DIR = Path(__file__).resolve().parent / SUBFOLDER_KAITAI
KAITAI_FORMAT_DIR = KAITAI_DIR / SUBFOLDER_FORMATS

class PyTaiException(Exception):
    pass