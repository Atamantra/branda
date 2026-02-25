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

        # 1. Update Navigation Galeri Link (if missing or #gallery)
        nav_targets = [
            '<li><a href="#gallery">Galeri</a></li>',
            '<li><a href="index.html#gallery">Galeri</a></li>',
            '<li><a href="../../index.html#gallery">Galeri</a></li>'
        ]
        new_nav_link = f'<li><a href="{prefix}albumler/galeri/index.html">Galeri</a></li>'
        for target in nav_targets:
            if target in content:
                content = content.replace(target, new_nav_link)
                modified = True

        # 2. Add to Footer Hızlı Bağlantılar
        footer_link_str = f'<li><a href="{prefix}albumler/galeri/index.html">Galeri</a></li>'
        
        # We need to insert it into the footer-links ul under Hızlı Bağlantılar.
        # A good anchor is the 'İletişim' link or 'Bizi Arayın' link in the footer.
        iletisim_anchor = '<li><a href="' + prefix + 'iletisim/index.html">İletişim</a></li>'
        if iletisim_anchor in content and footer_link_str not in content:
            content = content.replace(
                iletisim_anchor,
                f'{footer_link_str}\n                            {iletisim_anchor}'
            )
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    update_files()
    print("Done updating files")
