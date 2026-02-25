import re

directories = [
    "montaj-hizmeti", "garanti-politikasi", "bakim-onarim", "referanslarimiz", "sss",
    "hikayemiz", "kariyer", "ticari-hesaplar", "gizlilik-politikasi", "sartlar-kosullar"
]

for d in directories:
    file_path = f"/Users/atamantra/Desktop/branda/sayfa/{d}/index.html"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        pattern = r'<div class="container"\s*style="max-width: 800px; margin: 0 auto; color: var\(--color-text\); line-height: 1\.8; font-size: 1\.1rem;">\s*(.*?)\s*</div>\s*</section>'
        
        match = re.search(pattern, content, flags=re.DOTALL)
        if match:
            inner_html = match.group(1)
            # Remove inline styles from inner HTML elements to let CSS take over
            inner_html = re.sub(r'\sstyle="[^"]*"', '', inner_html)
            
            replacement = f'''<section class="text-page-wrapper">
        <div class="container" style="max-width: 900px;">
            <div class="text-page-card">
                <div class="text-page-content">
                    {inner_html}
                </div>
            </div>
        </div>
    </section>'''
            
            # Replace the old section entirely
            pattern_full = r'<section class="section" style="padding-top: 0;">\s*<div class="container"\s*style="max-width: 800px; margin: 0 auto; color: var\(--color-text\); line-height: 1\.8; font-size: 1\.1rem;">\s*.*?\s*</div>\s*</section>'
            new_content = re.sub(pattern_full, replacement, content, flags=re.DOTALL)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {d}")
        else:
            print(f"Pattern not found in {d}")
    except Exception as e:
        print(f"Error processing {d}: {e}")
