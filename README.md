# TXT to XMP Sidecar Script

## Description

This script takes a plaintext list of comma-separated tags relevant to an image and turns it into an XMP sidecar file by reformatting the contents and changing it into an XML file.

## Installation

1.  Install Python 3.x.
2.  Install the required packages:

    ```bash
    pip install xml.etree.ElementTree argparse
    ```

## Usage

```bash
python txt to xmp sidecar.py -i <input_directory>
```

*   `-i` or `--input`: Optional. The input directory containing the `.txt` files. Defaults to the "in" directory within the project directory.

## Example

To process all `.txt` files in the "test" directory:

```bash
python txt to xmp sidecar.py -i test
```

## License

MIT License

Copyright (c) 2025

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

## Contributing

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, concise messages.
4.  Submit a pull request.
