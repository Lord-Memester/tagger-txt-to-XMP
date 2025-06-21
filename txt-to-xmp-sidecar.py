# THIS CODE IS A PLACEHOLDER, WRITTEN ENTIRELY BY CHATGPT. DO NOT ATTEMPT TO USE AT ALL, LET ALONE ON ANYTHING YOU CARE ABOUT.

import os
import glob
import xml.etree.ElementTree as ET
import argparse

XMP_NS = 'adobe:ns:meta/'
RDF_NS = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
DC_NS = 'http://purl.org/dc/elements/1.1/'

def create_xmp(tags):
    xmp_template = ET.Element('x:xmpmeta', {
        'xmlns:x': XMP_NS
    })

    rdf = ET.SubElement(xmp_template, 'rdf:RDF', {
        'xmlns:rdf': RDF_NS
    })

    desc = ET.SubElement(rdf, 'rdf:Description', {
        'xmlns:dc': DC_NS
    })

    subject = ET.SubElement(desc, 'dc:subject')
    bag = ET.SubElement(subject, 'rdf:Bag')

    for tag in tags:
        li = ET.SubElement(bag, 'rdf:li')
        li.text = tag

    return '<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d" padding="256"?>\n' + \
        ET.tostring(xmp_template, encoding='unicode') + \
        '\n<?xpacket end="w"?>'

def normalize_tags(text):
    # Split by comma or newline, strip whitespace
    raw_tags = [t.strip() for t in text.replace('\n', ',').split(',')]
    return [tag for tag in raw_tags if tag]

def process_directory(directory):
    for txt_file in glob.glob(os.path.join(directory, '*.txt')):
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()

            tags = normalize_tags(content)

            if not tags:
                continue

            xmp_data = create_xmp(tags)
            base_name = os.path.splitext(txt_file)[0]
            xmp_file = base_name + '.xmp'

            image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            image_exists = False
            for ext in image_extensions:
                if os.path.exists(base_name + ext):
                    image_exists = True
                    break

            if not image_exists:
                print(f"No corresponding image found for {txt_file}, skipping XMP creation.")
                continue

            with open(xmp_file, 'w', encoding='utf-8') as f:
                f.write(xmp_data)
            print(f"Created: {xmp_file}")
        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process txt files to create XMP sidecar files.')
    parser.add_argument('-i', '--input', default='in', help='Input directory containing txt files.')
    args = parser.parse_args()

    process_directory(args.input)
