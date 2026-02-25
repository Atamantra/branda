import os
from datetime import datetime

base_url = "https://4mevsimbranda.com/"
root_dir = "/Users/atamantra/Desktop/branda"

# Find all HTML files
html_files = []
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# Start XML
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

today = datetime.now().strftime('%Y-%m-%d')

for file_path in html_files:
    # Get relative path from root
    rel_path = os.path.relpath(file_path, root_dir)
    
    # Skip template or duplicate files if necessary (none known right now)
    
    # Format URL
    url_path = rel_path.replace(os.sep, '/')
    
    # priority logic
    priority = "0.8"
    if url_path == "index.html":
        priority = "1.0"
        url_path = "" # base URL usually just points to /
    elif url_path.startswith("blog/index.html") or url_path.startswith("hizmetdetay/index.html"):
        priority = "0.9"
    elif url_path.startswith("blog/"):
        priority = "0.7"
    
    full_url = f"{base_url}{url_path}"
    
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{full_url}</loc>\n'
    xml_content += f'    <lastmod>{today}</lastmod>\n'
    xml_content += '    <changefreq>weekly</changefreq>\n'
    xml_content += f'    <priority>{priority}</priority>\n'
    xml_content += '  </url>\n'

xml_content += '</urlset>\n'

sitemap_path = os.path.join(root_dir, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

print(f"Generated sitemap.xml with {len(html_files)} URLs.")
