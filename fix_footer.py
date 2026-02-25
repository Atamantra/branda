import os
import glob

def get_relative_prefix(filepath):
    depth = filepath.count('/') - 1
    if depth <= 0:
        return ""
    return "../" * depth

def update_files():
    html_files = glob.glob('./**/*.html', recursive=True)
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        prefix = get_relative_prefix(file)
        modified = False

        # Footer targets - inject after Hakkimizda
        # The user has various forms of Hakkimizda in the footer:
        # Example 1: <li><a href="index.html">Hakkımızda</a></li>
        # Example 2: <li><a href="../sayfa/hakkimizda/index.html">Hakkımızda</a></li>
        # Wait, the string to match should just be >Hakkımızda</a></li>
        # We find the line containing >Hakkımızda</a></li> and we add Vizyonumuz and Misyonumuz after it.
        
        lines = content.split('\n')
        new_lines = []
        in_footer = False
        
        for line in lines:
            if 'class="footer"' in line:
                in_footer = True
            if '</footer>' in line:
                in_footer = False
                
            new_lines.append(line)
            
            if in_footer and '>Hakkımızda</a></li>' in line:
                # Add Vizyonumuz and Misyonumuz right after if they aren't already there in the next few lines
                if not 'Vizyonumuz' in content: 
                    # Wait, Vizyonumuz might be in the file but in the top nav! We just check if they are in the footer
                    pass
                # We can just blindly add them if we don't see Vizyonumuz in the footer?
                # Actually, let's just make sure we only add it once per footer.
                # A safer way: Check if the file's footer already contains Vizyonumuz.
                footer_str = content[content.find('class="footer"'):content.find('</footer>')]
                if 'Vizyonumuz</a>' not in footer_str:
                    # Find out indentation
                    indent = line[:len(line) - len(line.lstrip())]
                    new_lines.append(indent + f'<li><a href="{prefix}sayfa/vizyonumuz/index.html">Vizyonumuz</a></li>')
                    new_lines.append(indent + f'<li><a href="{prefix}sayfa/misyonumuz/index.html">Misyonumuz</a></li>')
                    modified = True
        
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f"Updated footer in {file}")

if __name__ == "__main__":
    update_files()
