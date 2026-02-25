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

        dropdown = f"""<li class="dropdown">
                    <a href="{prefix}sayfa/hakkimizda/index.html" class="dropbtn">Kurumsal ▾</a>
                    <div class="dropdown-content">
                        <a href="{prefix}sayfa/hakkimizda/index.html">Hakkımızda</a>
                        <a href="{prefix}sayfa/vizyonumuz/index.html">Vizyonumuz</a>
                        <a href="{prefix}sayfa/misyonumuz/index.html">Misyonumuz</a>
                    </div>
                </li>"""

        # Replace single links
        targets = [
            '<li><a href="../index.html#about">Hakkımızda</a></li>',
            '<li><a href="../../index.html#about">Hakkımızda</a></li>'
        ]
        
        for t in targets:
            if t in content:
                content = content.replace(t, dropdown)
                modified = True

        # Footer edits
        footer_targets = [
            '<li><a href="../index.html#about">Hakkımızda</a></li>',
            '<li><a href="../../index.html#about">Hakkımızda</a></li>',
            '<li><a href="#about">Hakkımızda</a></li>'
        ]
        footer_replace = f'<li><a href="{prefix}sayfa/hakkimizda/index.html">Hakkımızda</a></li>'
        
        # We need to only do footer edits if they are in the footer to avoid double replacing the nav
        # But wait, nav is already replaced by dropdown!
        for t in footer_targets:
            if t in content:
                content = content.replace(t, footer_replace)
                modified = True
                
        # Also need to fix the sayfa/ pages which have incorrect dropdowns pointing to "index.html"
        bad_dropdown_1 = f"""<li class="dropdown">
                    <a href="index.html" class="dropbtn">Kurumsal ▾</a>
                    <div class="dropdown-content">
                        <a href="index.html">Hakkımızda</a>
                        <a href="index.html">Vizyonumuz</a>
                        <a href="index.html">Misyonumuz</a>
                    </div>
                </li>"""
                
        bad_dropdown_2 = f"""<li class="dropdown">
                    <a href="../hakkimizda/index.html" class="dropbtn">Kurumsal ▾</a>
                    <div class="dropdown-content">
                        <a href="../hakkimizda/index.html">Hakkımızda</a>
                        <a href="index.html">Vizyonumuz</a>
                        <a href="../misyonumuz/index.html">Misyonumuz</a>
                    </div>
                </li>"""

        bad_dropdown_3 = f"""<li class="dropdown">
                    <a href="../hakkimizda/index.html" class="dropbtn">Kurumsal ▾</a>
                    <div class="dropdown-content">
                        <a href="../hakkimizda/index.html">Hakkımızda</a>
                        <a href="../vizyonumuz/index.html">Vizyonumuz</a>
                        <a href="index.html">Misyonumuz</a>
                    </div>
                </li>"""

        bad_dropdown_4 = f"""<li class="dropdown">
                    <a href="../../sayfa/hakkimizda/index.html" class="dropbtn">Kurumsal ▾</a>
                    <div class="dropdown-content">
                        <a href="../../sayfa/hakkimizda/index.html">Hakkımızda</a>
                        <a href="index.html">Vizyonumuz</a>
                        <a href="../../sayfa/misyonumuz/index.html">Misyonumuz</a>
                    </div>
                </li>"""

        for b in [bad_dropdown_1, bad_dropdown_2, bad_dropdown_3, bad_dropdown_4]:
            if b in content:
                content = content.replace(b, dropdown)
                modified = True

        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")

if __name__ == "__main__":
    update_files()
