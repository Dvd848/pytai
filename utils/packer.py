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
import os

def filter_func(path: Path) -> bool:
    for part in path.parts:
        if part.startswith(".") or part in ["__pycache__", "tmp", "tests", "docs"]:
            return False

    for pattern in ["*.pyc", "*.ini", "*.pyz"]:
        if path.match(pattern):
            return False

    return True


def main(source, target, version) -> None:
    version_file_path = str(Path(source) / "pytai" / "version.py")
    with open(version_file_path, "w") as version_file:
        version_file.write(f"__version__ = '{version}'")
        
    zipapp.create_archive(source, target, filter = filter_func)
    os.remove(version_file_path) 
    print(f"File created: {target}, version: {version}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pack pytai to a *.pyz file.')
    args = parser.parse_args()

    try:
        import setuptools_scm
        
        source = ".."
        version = setuptools_scm.get_version(root=source, relative_to=__file__)
        
        main(source, "pytai.pyz", version)
    except Exception as e:
        print(f"Error: {e}")
    
    input("Press Enter to continue...")
