# TXT to XMP Sidecar Script

## Description

This script takes a plaintext list of comma-separated tags relevant to an image and turns it into an XMP sidecar file by creating an XML file with the reformatted contents.

## Installation

1. Install Python 3.x.
2. Install the required packages:

    ```bash
    pip install xml.etree.ElementTree argparse
    ```

## Usage

```bash
python "txt to xmp sidecar.py" -i <input_directory>
```

* `-i`: Optional. The input directory containing the `.txt` files. Defaults to an "in" directory within the same directory as the python script.

## Example

To process all `.txt` files in the "test" directory:

```bash
python "txt to xmp sidecar.py" -i test
```
