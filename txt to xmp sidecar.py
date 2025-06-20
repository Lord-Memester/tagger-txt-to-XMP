# THIS CODE IS A PLACEHOLDER, WRITTEN ENTIRELY BY CHATGPT. DO NOT ATTEMPT TO USE AT ALL, LET ALONE ON ANYTHING YOU CARE ABOUT.

import os
import glob
import xml.etree.ElementTree as ET

def create_xmp(tags):
    xmp_template = ET.Element('x:xmpmeta', {
        'xmlns:x': 'adobe:ns:meta/'
    })

    rdf = ET.SubElement(xmp_template, 'rdf:RDF', {
        'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
    })

    desc = ET.SubElement(rdf, 'rdf:Description', {
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/'
    })

    subject = ET.SubElement(desc, 'dc:subject')
    bag = ET.SubElement(subject, 'rdf:Bag')

    for tag in tags:
        li = ET.SubElement(bag, 'rdf:li')
        li.text = tag

    return '<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n' + \
        ET.tostring(xmp_template, encoding='unicode') + \
        '\n<?xpacket end="w"?>'

def normalize_tags(text):
    # Split by comma or newline, strip whitespace
    raw_tags = [t.strip() for t in text.replace('\n', ',').split(',')]
    return [tag for tag in raw_tags if tag]

def process_directory(directory):
    for txt_file in glob.glob(os.path.join(directory, '*.txt')):
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()

        tags = normalize_tags(content)

        if not tags:
            continue

        xmp_data = create_xmp(tags)
        base_name = os.path.splitext(txt_file)[0]
        xmp_file = base_name + '.xmp'

        with open(xmp_file, 'w', encoding='utf-8') as f:
            f.write(xmp_data)
        print(f"Created: {xmp_file}")

# Example usage
# Replace '.' with your directory path if needed
process_directory('.')
