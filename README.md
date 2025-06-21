# TXT to XMP Sidecar Script

This script takes a plaintext list of comma-separated tags relevant to an image and turns it into an XMP sidecar file by creating an XML file with the reformatted contents. Its intended use is for Immich, but it may be useful in other programs as well.

## Usage

```bash
python txt-to-xmp-sidecar.py -i <input_directory>
```

* `-i`: Optional. Used to specify the input directory containing the `.txt` files. If unspecified, uses an "in" folder if found in the same directory as the python script. Otherwise yells at you. I hope.
