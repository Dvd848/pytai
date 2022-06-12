# pytai

`pytai` is a Python-based [Kaitai Struct](https://kaitai.io/) visualizer and Hex viewer. 

> Kaitai Struct is a declarative language used for describing various binary data structures laid out in files or in memory: i.e. binary file formats, network stream packet formats, etc.

Given a binary file with a supported format, `pytai` can be used to browse the structure of the file and locate its members in the Hex view.

## Install

```console
$ pip install pytai-hex
```

Alternatively, the latest stable version of `pytai.pyz` can be downloaded from the [Releases](https://github.com/Dvd848/pytai/releases) page.

## Usage

```console
$ pytai -h                 
usage: pytai [-h] [-kf FORMAT] [file]

pytai: A Python-based Kaitai Struct Visualizer and HEX Viewer

positional arguments:
  file                  Path to binary file

optional arguments:
  -h, --help            show this help message and exit
  -kf FORMAT, --kaitai-format FORMAT
                        Kaitai Format to use when parsing the file. Current formats found under "kaitai/formats" are:
                        aix_utmp, allegro_dat, andes_firmware, android_asus_bootldr, android_dto, android_img,
                        android_opengl_shaders_cache, android_super, apm_partition_table, apple_single_double, au,
                        avi, bcd, bitcoin_transaction, blender_blend, bmp, broadcom_trx, bson, btrfs_stream,
                        bytes_with_io, code_6502, compressed_resource, cpio_old_le, cramfs, creative_voice_file, dbf,
                        dex, dicom, dime_message, dns_packet, doom_wad, dos_datetime, dos_mz, ds_store, dune_2_pak,
                        edid, efivar_signature_list, elf, ethernet_frame, exif, ext2, fallout2_dat, fallout_dat,
                        ftl_dat, genmidi_op2, gettext_mo, gif, gimp_brush, glibc_utmp, gltf_binary, google_protobuf,
                        gpt_partition_table, gran_turismo_vol, gzip, hashcat_restore, hccap, hccapx, heaps_pak,
                        heroes_of_might_and_magic_agg, heroes_of_might_and_magic_bmp, icmp_packet, ico, id3v1_1,
                        id3v2_3, id3v2_4, ines, ipv4_packet, ipv6_packet, iso9660, java_class, jpeg, luks, lvm2, lzh,
                        mach_o, mac_os_resource_snd, magicavoxel_vox, mbr_partition_table, microsoft_cfb,
                        microsoft_network_monitor_v2, microsoft_pe, minecraft_nbt, monomakh_sapr_chg, mozilla_mar,
                        msgpack, nitf, ogg, openpgp_message, packet_ppi, pcap, pcf_font, pcx, pcx_dcx,
                        phar_without_stub, php_serialized_value, png, protocol_body, psx_tim, python_pickle,
                        python_pyc_27, quake_mdl, quake_pak, quicktime_mov, rar, regf, renderware_binary_stream,
                        resource_fork, riff, rtcp_payload, rtpdump, rtp_packet, ruby_marshal, saints_row_2_vpp_pc,
                        shapefile_index, shapefile_main, sqlite3, ssh_public_key, standard_midi_file, stl, sudoers_ts,
                        swf, systemd_journal, tcp_segment, tga, tls_client_hello, tr_dos_image, tsm, ttf,
                        udp_datagram, uefi_te, uimage, utf8_string, vdi, vfat, vlq_base128_be, vlq_base128_le,
                        vmware_vmdk, vp8_ivf, warcraft_2_pud, wav, websocket, windows_evt_log, windows_lnk_file,
                        windows_minidump, windows_resource_file, windows_shell_items, windows_systemtime, wmf, xwd,
                        zip, zx_spectrum_tap
```

Examples:

```console
$ pytai
$ pytai ../../image.png
$ pytai ../../image.png -kf png
$ python3 ./pytai.pyz ../../archive.zip -kf zip
$ python3 __main__.py ../../program.exe -kf dos_mz
```

## Screenshots

### Main Window

![Main Window](https://github.com/Dvd848/pytai/raw/main/docs/images/pytai.png)

### Marking Elements

![Mark Elements 1](https://github.com/Dvd848/pytai/raw/main/docs/images/mark1.png)

![Mark Elements 2](https://github.com/Dvd848/pytai/raw/main/docs/images/mark2.png)

### Metadata Members

These are members that are inferred from the binary contents (usually a user-friendly display for explicit data).

![Mark Elements 2](https://github.com/Dvd848/pytai/raw/main/docs/images/meta.png)

### Cross References

It's possible to right-click an area in the Hex output and locate its logical structure in the structure tree.

![Cross Reference](https://github.com/Dvd848/pytai/raw/main/docs/images/xref.gif)

## Similar Tools

* [Kaitai Struct: Visualizer](https://github.com/kaitai-io/kaitai_struct_visualizer): Text-based visualizer written in Ruby
* [Kaitai Web IDE](https://ide.kaitai.io/): A browser-based visualizer
* [Kaitai Struct: Visualization GUI Tool](https://github.com/kaitai-io/kaitai_struct_gui): GUI visualizer written in Java
* [Binary Ninja UI Plugin](https://github.com/Vector35/kaitai): A GUI plugin for Binary Ninja
* [Kaitai Struct VSCode](https://marketplace.visualstudio.com/items?itemName=fudgepops.kaitai-struct-vscode): Extension for [VS Code](https://code.visualstudio.com/)
* [Hobbits](https://github.com/Mahlet-Inc/hobbits): Multi-platform GUI for bit-based analysis, processing, and visualization
* [PolyFile](https://github.com/trailofbits/polyfile): A utility to identify and map the semantic structure of files

Find more tools under [Awesome Kaitai](https://github.com/kaitai-io/awesome-kaitai) or angea's '[Hex Viewers and Editors](https://twitter.com/i/events/841916822014332930)' list.

## Requirements

 * Python3.8+ with tkinter

## Formats

The supported formats were taken from the [Kaitai Struct format gallery repo](https://github.com/kaitai-io/kaitai_struct_formats) and compiled to Python using the [Kaitai Struct Compiler](http://kaitai.io/#download).

### Adding Support for New Formats

1. Create or download a format definition (`*.ksy` file) using the Kaitai Struct language
2. Install the Kaitai Struct Compiler 
3. Compile the format definition file:

    `ksc --target python --debug --import-path /path/to/imports/if/needed /path/to/format.ksy`

4. Copy the output file (`*.py`) to the `pytai/kaitai/formats` subfolder.


## Known Limitations

 * No ability to interactively edit files (not a Hex editor, just a viewer).
 * Currently no special optimizations implemented in order to handle very large files.
 * Structure offsets are based on output from Kaitai. Kaitai doesn't fully support bit-field offsets, and therefore the GUI cannot accurately mark bit-field members.

## Contributions

Contributions in the form of pull requests, comments, suggestions and issue reports are welcome! 

As a general guideline, this project attempts to minimize the amount of external dependencies which it relies on. The preference of the project is to avoid adding external dependencies except for cases which involve complex logic that can be significantly simplified using a popular package.