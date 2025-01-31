import re
from lxml import etree

# Input and output file paths
input_tex_file = 'step2.xml'
output_xml_file = 'mera_mehnat.xml'
dtd_file = 'JATS-journalpublishing-oasis-article1-mathml3.ucp.dtd'

# Read input file
with open(input_tex_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Define XML namespaces
nsmap = {
    "mml": "http://www.w3.org/1998/Math/MathML",
    "xlink": "http://www.w3.org/1999/xlink",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    None: "http://jats.nlm.nih.gov"
}

# Create root element with namespace
root = etree.Element("article",
                     attrib={
                         "article-type": "research-article",
                         "dtd-version": "1.2"
                     },
                     nsmap=nsmap)
root.set("{http://www.w3.org/XML/1998/namespace}lang", "en")

# Add DOCTYPE declaration
doctype = f'<!DOCTYPE article PUBLIC "-//NLM//DTD UCP JATS (Z39.96) Journal Publishing DTD with OASIS Tables with MathML3 v1.2 20190208//EN" "{dtd_file}">' 

# Create front section
front = etree.SubElement(root, "front")
journal_meta = etree.SubElement(front, "journal-meta")
journal_id = etree.SubElement(journal_meta, "journal-id", attrib={"journal-id-type": "publisher-id"})
journal_id.text = "JPE"

# Article metadata
article_meta = etree.SubElement(front, "article-meta")
title_group = etree.SubElement(article_meta, "title-group")
article_title = etree.SubElement(title_group, "article-title")
article_title.text = "Generated Article Title"

# Abstract
abstract = etree.SubElement(article_meta, "abstract")
abstract_p = etree.SubElement(abstract, "p")
abstract_p.text = "This is a generated abstract."

# Create body
body = etree.SubElement(root, "body")
for line in lines:
    p = etree.SubElement(body, "p")
    p.text = line.strip()

# Additional processing for equations, tables, figures, references
xref_patterns = [
    (re.compile(r'\\cite\{(.*?)\}'), "bibr"),
    (re.compile(r'\\ref\{sec:(.*?)\}'), "sec"),
    (re.compile(r'\\ref\{fig:(.*?)\}'), "fig"),
    (re.compile(r'\\ref\{tab:(.*?)\}'), "table")
]

for para in body.iter("p"):
    text = para.text
    if text:
        for pattern, ref_type in xref_patterns:
            matches = pattern.findall(text)
            for match in matches:
                xref = etree.Element("xref", attrib={"ref-type": ref_type, "rid": match})
                xref.text = match
                para.append(xref)

# Create back section
back = etree.SubElement(root, "back")
ref_list = etree.SubElement(back, "ref-list")
label = etree.SubElement(ref_list, "label")
label.text = "References"

# Convert to string and write to file
xml_string = etree.tostring(root, pretty_print=True, encoding='utf-8').decode('utf-8')
xml_string = f'<?xml version="1.0" encoding="UTF-8"?>\n{doctype}\n{xml_string}'

with open(output_xml_file, 'w', encoding='utf-8') as output_file:
    output_file.write(xml_string)

print(f"XML generated successfully: {output_xml_file}")
