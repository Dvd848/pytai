"""Packer utility to pack the application to a pyz file.

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
import zipapp
import argparse
from pathlib import Path

def filter(path: Path) -> bool:
    for part in path.parts:
        if part.startswith(".") or part in ["__pycache__", "tmp", "tests", "docs"]:
            return False

    for pattern in ["*.pyc", "*.ini", "*.pyz"]:
        if path.match(pattern):
            return False

    return True


def main(source, target) -> None:
    zipapp.create_archive(source, target, filter = filter)
    print(f"File created: {target}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pack pytai to a *.pyz file.')
    args = parser.parse_args()

    main("..", "pytai.pyz")
