import os
import re

html_files = []
for root, dirs, files in os.walk('/Users/atamantra/Desktop/branda'):
    for file in files:
        if file.endswith('.html') and 'blog' not in file: # skip styling main blog pages for now
            html_files.append(os.path.join(root, file))

def get_relative_path(from_path, to_dir):
    rel = os.path.relpath('/Users/atamantra/Desktop/branda' + to_dir, os.path.dirname(from_path))
    return rel + '/' if rel != '.' else ''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Blog to Nav
    blog_nav_link = f'<li><a href="{get_relative_path(file, "/blog")}index.html">Blog</a></li>'
    if '<li><a href="index.html">Blog</a></li>' not in content and 'Blog' not in re.findall(r'<li><a href=".*?">Blog</a></li>', content):
        content = re.sub(
            r'(<li><a href="[^"]*">Galeri</a></li>)',
            r'\1\n                ' + blog_nav_link,
            content
        )

    # Add Blog to Footer
    blog_footer_link = f'<li><a href="{get_relative_path(file, "/blog")}index.html">Blog</a></li>'
    if '<li><a href="index.html">Blog</a></li>' not in content and 'Blog' not in re.findall(r'<li><a href=".*?">Blog</a></li>', content):
        content = re.sub(
            r'(<li><a href="[^"]*">Galeri</a></li>)',
            r'\1\n                        ' + blog_footer_link,
            content
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Linked Blog in nav and footer across site.")
