import re
input_file_path = 'step1.xml'
output_file_path = 'step2.xml'
with open(input_file_path, 'r') as file:
    input_text = file.read()
table_pattern = re.compile(r'\\begin{table}.*?\\end{table}', re.DOTALL)
figure_pattern = re.compile(r'\\begin{figure}.*?\\end{figure}', re.DOTALL)
abstract_pattern =  re.compile(r'\\begin{abstract}.*?\\end{abstract}', re.DOTALL)
proposition_pattern =  re.compile(r'\\begin{proposition}.*?\\end{proposition}', re.DOTALL)
equation_pattern = re.compile(r'\\begin{equation}.*?\\end{equation}', re.DOTALL)
split_pattern = re.compile(r'\\begin{split}.*?\\end{split}', re.DOTALL)
remark_pattern = re.compile(r'\\begin{remark}.*?\\end{remark}', re.DOTALL)
definition_pattern = re.compile(r'\\begin{definition}.*?\\end{definition}',re.DOTALL)
theorem_pattern = re.compile(r'\\begin{theorem}.*?\\end{theorem}',re.DOTALL)
align_pattern = re.compile(r'\\begin{align}.*?\\end{align}',re.DOTALL)
align_pattern_star = re.compile(r'\\begin{align\*}.*?\\end{align\*}',re.DOTALL)

multline_pattern = re.compile(r'\\begin{multline}.*?\\end{multline}',re.DOTALL)
multline_star_pattern = re.compile(r'\\begin{multline\*}.*?\\end{multline\*}',re.DOTALL)


def remove_p_tags(match):
    return match.group().replace('<p>', '').replace('</p>', '')

output_text = re.sub(table_pattern, remove_p_tags, input_text)
output_text = re.sub(figure_pattern, remove_p_tags, output_text)
output_text = re.sub(abstract_pattern,remove_p_tags,output_text)
output_text = re.sub(proposition_pattern,remove_p_tags,output_text)
output_text = re.sub(equation_pattern,remove_p_tags,output_text)
output_text = re.sub(split_pattern,remove_p_tags,output_text)
output_text = re.sub(remark_pattern,remove_p_tags,output_text)
output_text = re.sub(definition_pattern,remove_p_tags,output_text)
output_text = re.sub(theorem_pattern,remove_p_tags,output_text)
output_text = re.sub(align_pattern,remove_p_tags,output_text)
output_text = re.sub(multline_pattern,remove_p_tags,output_text)
output_text = re.sub(align_pattern_star,remove_p_tags,output_text)
output_text = re.sub(multline_star_pattern,remove_p_tags,output_text)





# print(figure_pattern)

with open(output_file_path, 'w') as file:
    file.write(output_text)