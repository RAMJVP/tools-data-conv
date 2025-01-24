import section
import removeptag
import last
files_to_run = ['section.py', 'removeptag.py', 'last.py']
for file_name in files_to_run:
    with open(file_name, 'r') as file:
        code = file.read()
        exec(code)
