#!/bin/bash

kaitai_struct_formats_path=./tmp2/kaitai_struct_formats
output_path=../kaitai/formats/

rm -rf $kaitai_struct_formats_path
mkdir -p $kaitai_struct_formats_path
git clone https://github.com/kaitai-io/kaitai_struct_formats $kaitai_struct_formats_path

#mkdir -p $output_path

for file in $kaitai_struct_formats_path/**/*.ksy; do
    [ -f "$file" ] || continue
    echo $file
    ksc --target python --debug --outdir $output_path --import-path $kaitai_struct_formats_path "$file"
done

