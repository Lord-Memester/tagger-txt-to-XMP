# TXT to XMP Sidecar Script

This script takes a plaintext list of comma-separated tags relevant to an image and turns it into an XMP sidecar file by creating an XML file with the reformatted contents.

## Usage

```bash
python "txt-to-xmp-sidecar.py" -i <input_directory>
```

* `-i`: Optional. The input directory containing the `.txt` files. If not specified, uses an "in" folder found in the same directory as the python script.
