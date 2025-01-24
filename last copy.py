import re

input_tex_file = 'step2.xml'
output_xml_file = 'step3.xml'

xref_patterns = [
    re.compile(r'\\citealp\{.*?\}'),
    re.compile(r'\\citep\{.*?\}'),
    re.compile(r'\\citet\{.*?\}'),
    re.compile(r'\\cite\{.*?\}'),
]

figure_patterns = [
    re.compile(r'\\ref\{fig:([^{}]+)\}')
]

section_patterns = [
    re.compile(r'\\ref\{sec:([^{}]+)\}')
]

paragraph_patterns = [
    re.compile(r'\\paragraph\{(.*?)\}')
]

textit_patterns = [
    re.compile(r'\\textit\{(.*?)\}')
]

equation_pattern_begin = [
    re.compile(r'<p>\\begin\{(equation)\}')
]

equation_pattern_end = [
    re.compile(r'\\end\{(equation)\}</p>')
]

table_pattern_begin = [
    re.compile(r'<p>\\begin\{(table)\}')
]

table_pattern_end = [
    re.compile(r'\\end\{(table)\}</p>')
]

figure_pattern_begin = [
    re.compile(r'<p>\\begin\{(figure)\}')
]

figure_pattern_end = [
    re.compile(r'\\end\{(figure)\}</p>')
]

# Corrected: Use re.DOTALL flag in re.compile
figure_pattern = re.compile(r'\\begin{figure}(.*?)\\end{figure}', re.DOTALL)

footnotesize_pattern = [
    re.compile(r'\\footnotesize(.*)', re.DOTALL)
]

caption_in_figure_pattern = [
    re.compile(r'\\caption{(.*)\}')
]

# Corrected: Use raw string for "\caption" and "\\footnotesize"
with open('figure.xml', 'r') as input_file:
    lines = input_file.readlines()

filtered_lines = []

for line in lines:
    if r"\caption" in line or r"\\footnotesize" in line:
        filtered_lines.append(line)

with open('figure.xml', 'w') as output_file:
    output_file.writelines(filtered_lines)

# The rest of the script remains unchanged
