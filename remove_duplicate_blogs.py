import os
import re

html_files = []
for root, dirs, files in os.walk('/Users/atamantra/Desktop/branda'):
    for file in files:
        if file.endswith('.html') and 'blog' not in file:
            html_files.append(os.path.join(root, file))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nav and Footer basically got duplicated. What's actually there right now?
    # Let's clean it up:
    
    # regex to match: 
    # <li><a href="../../blog/index.html">Blog</a></li> followed by whitespace, followed by 
    # <li><a href="../../blog/index.html">Blog</a></li> ... and similarly.
    
    # An easier way is just to reduce any consecutive identical lines
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        if len(new_lines) > 0 and line.strip() != "" and line.strip() == new_lines[-1].strip():
            # If the current line is identical to the last line (ignoring indentation)
            # and it contains "Blog", skip it.
            if ">Blog<" in line:
                continue
        new_lines.append(line)

    with open(file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

print("Removed consecutive duplicate Blog links.")
