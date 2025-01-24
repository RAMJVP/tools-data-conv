import re

input_tex_file = 'manuscript.tex'
output_xml_file = 'footnote.xml'

footnote_pattern = [
    # re.compile(r'\\footnote{(.*?)}')
    re.compile(r'\\footnote{(?:\\label{foot:gap}\s*)?(.*?)\.}')

]

footnote_rid = 0
with open(input_tex_file, 'r') as file:
    lines = file.readlines()

with open(output_xml_file, 'w') as output_file:
    output_file.write('<fn-group>\n')

    for processed_line in lines:
        for pattern in footnote_pattern:
            matches = pattern.finditer(processed_line)
            for match in matches:
                footnote_rid += 1
                target = f'<fn id="fn{footnote_rid}"><label><sup>{footnote_rid}</sup></label>{match.group(1)}<p>'
                target = target.replace("\\", "\\\\")

                output_file.write(target + '\n')

    output_file.write('</fn-group>\n')
