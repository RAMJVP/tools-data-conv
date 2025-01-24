import re
input_tex_file = 'manuscript.tex'
output_xml_file = 'step1.xml'
label_pattern = re.compile(r'\\label\{.*?\}')
section_pattern = re.compile(r'\\section\{(.+?)\}')
subsection_pattern = re.compile(r'\\subsection\{(.+?)\}')
table_pattern = re.compile(r'\\begin{table}.*?\\end{table}', re.DOTALL)

with open(input_tex_file, 'r') as file:
    lines = file.readlines()
section_count = 0
subsection_count = 0
final_modified_lines = ''
for line in lines:
    if line.strip().startswith('%'):
    #   if '%' in line.strip():
        continue
# for line in lines:
#     if '%' in line:
#         line = line.split('%')[0]
#         continue

    modified_line = label_pattern.sub('', line)
    match_subsection = subsection_pattern.search(modified_line)
    if match_subsection:
        subsection_count += 1
        subsection_title = match_subsection.group(1)
        final_modified_lines += f'<sec id="sc{section_count}.{subsection_count}"><label>{section_count}.{subsection_count}</label><title>{subsection_title}</title>\n'
    else:
        match_section = section_pattern.search(modified_line)
        if match_section:
            section_count += 1
            subsection_count = 0
            section_title = match_section.group(1)
            final_modified_lines += f'<sec id="sc{section_count}"><label>{section_count}</label><title>{section_title}</title>\n'
        else:
            if modified_line.strip():
                final_modified_lines += f'<p>{modified_line.strip()}</p>\n'



with open(output_xml_file, 'w') as outfile:
    outfile.write(final_modified_lines)
