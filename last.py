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

equation_pattern_end =[
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


proposition_pattern_start = [
    re.compile(r'<p>\\begin{proposition}')
]
proposition_pattern_end = [
    re.compile(r'\\end{proposition}</p>')
]
split_pattern_start = [
    re.compile(r'<p>\\begin{split}')
]
split_pattern_end = [
    re.compile(r'\\end{split}</p>')
]

remark_pattern_start = [
    re.compile(r'<p>\\begin{remark}')
]
remark_pattern_end = [
    re.compile(r'\\end{remark}</p>')
]


definition_pattern_start = [
    re.compile(r'<p>\\begin{definition}')
]
definition_pattern_end = [
    re.compile(r'\\end{definition}</p>')
]

theorem_pattern_start = [
    re.compile(r'<p>\\begin{theorem}')
]
theorem_pattern_end = [
    re.compile(r'\\end{theorem}</p>')
]

align_pattern_start = [
    re.compile(r'<p>\\begin{align}')
]
align_pattern_end = [
    re.compile(r'\\end{align}</p>')
]
align_pattern_star_start = [
    re.compile(r'<p>\\begin{align\*}')
]
align_pattern_star_end = [
    re.compile(r'\\end{align\*}</p>')
]

multline_pattern_start = [
    re.compile(r'<p>\\begin{multline}')
]
multline_pattern_end = [
    re.compile(r'\\end{multline}</p>')
]

multline_pattern_star_start = [
    re.compile(r'<p>\\begin{multline\*}')
]
multline_pattern_star_end = [
    re.compile(r'\\end{multline\*}</p>')
]

footnote_pattern  = [
    # re.compile(r'\\footnote{(.*)}')
        re.compile(r'\\footnote{(?:\\label{foot:gap}\s*)?(.*?)\.}')

]

# footnote_pattern_bootom = [
#     </sup></xref> my mname is manish</p>
# ]

caption_in_figure_pattern = [
          re.compile(r'\\caption{(.*)\}')
          
]



IT_pattern = [
          re.compile(r'\\it\s*([^}]+)')
          
]

ref_tab_number = [    
              re.compile(r'\\ref\{tab:(\d+)\}')  
                             
]

ref_tab_number_alpha = [    
              re.compile(r'\\ref\{tab:([a-zA-Z]+)\}')                 

]
equation_pattern_dig = [    
              re.compile(r'\\eqref\{eq:(\d+)\}')                 
]

fig_reference_pattern = [
     re.compile(r'\\ref\{fig:(\d+)\}')   
]


# Corrected: Use re.DOTALL flag in re.compile
#figure_pattern = re.compile(r'\\begin{figure}(.*?)\\end{figure}', re.DOTALL)

figure_pattern = re.compile(r'\\begin{figure}(.*?)\\end{figure}', re.DOTALL)


#figure_pattern = re.compile(r'\\begin{figure}(.*?)(?s)\\end{figure}', re.DOTALL)

footnote_textbf = re.compile (r'\\textbf\{.*:\}')


footnotesize_pattern = [
# re.compile (r'\\textbf{Notes:}(.*?)$'),
# re.compile(r'\\footnotesize\s*{(.*?)}'),
# re.compile(r'\\footnotesize\s*(.*?)$'),
# re.compile(r'\\footnotesize{(.*?)}')
    # r'\\footnotesize{(.*?)}', re.DOTALL
re.compile(r'\\footnotesize(.*)', re.DOTALL)
# re.compile(r'\\footnotesize{(.*?)}'),
# re.compile(r'\\footnotesize{([^}]*)}')
# re.compile(r'\\footnotesize\{(.+?)\}', re.DOTALL)
]


with open(input_tex_file, 'r') as file:
    lines = file.readlines()
with open(output_xml_file, 'w') as output_file:
    footnote_rid = 0
    for line in lines:
        processed_line = line
         
        for pattern in xref_patterns:
            match = pattern.search(processed_line)
            if match:
                target = f'<xref ref-type="bibr" rid="">{match.group()}</xref>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
                 
        for pattern in figure_patterns:
            match = pattern.search(processed_line)
            if match:
                target = f'<xref ref-type="fig" rid="">{match.group()}</xref>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)

        for pattern in section_patterns:
            match = pattern.search(processed_line)
            if match:
                target = f'<xref ref-type="sec" rid="">{match.group()}</xref>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
        
        for pattern in paragraph_patterns:
            match = pattern.search(processed_line)
            if match:
                target = f'<bold>{match.group(1)}</bold>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for pattern in textit_patterns:
            match = pattern.search(processed_line)
            if match:
                target = f'<italic toggle="yes">{match.group(1)}</italic>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)

        for pattern in equation_pattern_begin:
            match = pattern.search(processed_line)
            if match:
                target = f'\nEQUATION BEGIN\n {match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for pattern in equation_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target = f'{match.group()} \nEQUATION END \n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)

        for  pattern in table_pattern_begin:
            match = pattern.search(processed_line)
            if match:
                target= f'\nTABLE START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)

        for  pattern in table_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\nTABLE END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)

        for  pattern in figure_pattern_begin:
            match = pattern.search(processed_line)
            if match:
                target= f'\nFIGURE START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in figure_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\nFIGURE END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)

        for pattern in footnote_pattern:
            match = pattern.search(processed_line)            
            if match:
                # print(match)
                footnote_rid += 1
                target = f'<xref ref-type="fn" rid="fn{footnote_rid}"><sup>{footnote_rid}</sup></xref>{match.group(1)}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
        
        for  pattern in proposition_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n PROPOSITION START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)


        
        for  pattern in proposition_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n PROPOSITION END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in split_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n SPLIT START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in split_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n SPLIT END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)

        for  pattern in remark_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n REMARK START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in remark_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n REMARK END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in definition_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n DEFINITION START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in definition_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n  DEFINITION END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in theorem_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n theorem START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in theorem_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n  theorem END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in align_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n align START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in align_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n  align END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
                
        for  pattern in align_pattern_star_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n align* START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in align_pattern_star_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n  align* END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in multline_pattern_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n MULTILINE START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in multline_pattern_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n  MULTILINE END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
                
        for  pattern in multline_pattern_star_start:
            match = pattern.search(processed_line)
            if match:
                target= f'\n MULTILINE* START\n{match.group()}'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        
        for  pattern in multline_pattern_star_end:
            match = pattern.search(processed_line)
            if match:
                target= f'{match.group()}\n  MULTILINE* END\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target,processed_line)
        for pattern in IT_pattern:
            match = pattern.search(processed_line)            
            if match:
                target = f'<italic toggle="yes">{match.group(1)}</italic>'
                # print(target)
                target = target.replace("\\", "\\\\").replace("{<italic>","<italic>").replace("</italic>}","</italic>")
                processed_line = pattern.sub(target, processed_line)
        
        
        for pattern in ref_tab_number:
            match = pattern.search(processed_line)     
            # print(match)       
            if match:
                target = f'<xref place="yes" ref-type="table" rid="tb{match.group(1)}">Table {match.group(1)}</xref>'
                # print(target)
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
                processed_line = processed_line.replace("Table <xref place", "<xref place")
        
        
        for pattern in ref_tab_number_alpha:
            match = pattern.search(processed_line)     
            # print(match)       
            if match:
                print(match)
                target = f'<xref place="no" ref-type="table" rid="">Table</xref>'
                # print(target)
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
        
        for pattern in fig_reference_pattern:
            match = pattern.search(processed_line)     
            # print(match)       
            if match:
                print(match)
                target = f'figure {match.group(1)}'
                # print(target)
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
                
        for pattern in equation_pattern_dig:
            match = pattern.search(processed_line)     
            # print(match)       
            if match:
                target = f'<xref ref-type="disp-formula" rid="df{match.group(1)}">{match.group(1)}</xref>'
                # print(target)
                target = target.replace("\\", "\\\\").replace("{<italic>","<italic>").replace("</italic>}","</italic>")
                processed_line = pattern.sub(target, processed_line)


        output_file.write(processed_line)


footnote_rid = 0

# with open('footnote.xml', 'w') as output_file:
#     output_file.write('<fn-group>\n')  

#     for processed_line in lines:  
#         for pattern in footnote_pattern:
#             match = pattern.search(processed_line)
#             if match:
#                 footnote_rid += 1
#                 target = f'<fn id="fn{footnote_rid}"><label><sup>{footnote_rid}</sup></label>{match.group(1)}<p>'
#                 output_file.write(target + '\n')                
#     output_file.write('</fn-group>\n')
with open('footnote.xml', 'w') as output_file:
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
    
with open('footnote.xml', 'r') as file:
    lines = file.readlines()

with open('footnote.xml', 'w') as output_file:
    for line in lines:
        processed_line = line
        for pattern in xref_patterns:
            match = pattern.search(processed_line)
            if match:
                target = f'<xref ref-type="bibr" rid="">{match.group()}</xref>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
        output_file.write(processed_line +'\n')


# with open(input_tex_file, 'r') as file:
#     lines = file.readlines()

# footnote_rid =0
# with open(output_xml_file, 'w') as output_file:
#         for line in lines:
           
#             processed_line = line
#             for pattern in footnote_pattern:
#                 match = pattern.search(processed_line)            
#                 if match:
#                         footnote_rid += 1
#                         target = f'<xref ref-type="fn" rid="fn{footnote_rid}"><sup>{footnote_rid}</sup></xref>'
#                         target = target.replace("\\", "\\\\")
#                         processed_line = pattern.sub(target, processed_line)
#                         print(target)
#             output_file.write(processed_line)
            
           
            

                
                

 
with open(input_tex_file, 'r') as file:
    content = file.read()
    matches = figure_pattern.findall(content)

with open('figure.xml', 'w') as output_files:
    for match in matches:
        target = f'{match}\n'
        output_files.write(target)


filtered_lines = []


keep_line = False

with open('figure.xml', 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        if r"\caption" in line or r"\\footnotesize" in line:

       # if "\caption" in line or "\\footnotesize" in line:
   
            filtered_lines.append(line)

with open('figure.xml', 'w') as output_file:
    output_file.writelines(filtered_lines)

# third_line = '<graphic position="float" orientation="portrait" xlink:type="simple" xlink:href="fg4.tiff" specific-use="all"/>'

with open('figure.xml', 'r') as file:
    lines = file.readlines()

with open('figure.xml', 'w') as output_file:
    output_file.write('<floats-group>\n')  
    fig_id = 0
    for line in lines:
        processed_line = line
        for pattern in caption_in_figure_pattern:
            match = pattern.search(processed_line)
            if match:
                fig_id+=1
                target = f'<fig id="fg{fig_id}" position="float" orientation="portrait" fig-type="figure" specific-use="all"><label>Fig. {fig_id}</label><caption><p>{match.group(1)}</p>'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
                
        for pattern in footnotesize_pattern:
            # print(pattern)
            match = pattern.search(processed_line)
            if match:
                # print(match)
                target = f'\n\n<p><bold>Notes:</bold>{match.group(1)} </p></caption> \n<graphic position="float" orientation="portrait" xlink:type="simple" xlink:href="fg{fig_id}.tiff" specific-use="all"/></fig>\n'
                target = target.replace("\\", "\\\\")
                processed_line = pattern.sub(target, processed_line)
                # processed_line = pattern.sub(footnote_textbf)
                processed_line = footnote_textbf.sub('', processed_line)

        
        
        # for pattern in footnote_textbf:
        #     # print(pattern)
        #     match = pattern.search(processed_line)
        #     if match:
        #         # print(match)
                
        #         # target = target.replace("\\", "\\\\").repalace()
        #         processed_line = pattern.sub(match, processed_line)
                # processed_line = pattern.sub(footnote_textbf)       
        output_file.write(processed_line)



file_paths = ['step3.xml','footnote.xml','figure.xml']
contents = []

for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        contents.append(content)

output_file_path = "mera_mehnat.xml"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for content in contents:
        output_file.write(content + "\n")

