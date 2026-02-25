import os

pages = {
    "montaj-hizmeti": "Montaj Hizmeti",
    "garanti-politikasi": "Garanti Politikası",
    "bakim-onarim": "Bakım & Onarım",
    "referanslarimiz": "Referanslarımız",
    "sss": "SSS",
    "hikayemiz": "Hikayemiz",
    "kariyer": "Kariyer",
    "ticari-hesaplar": "Ticari Hesaplar",
    "gizlilik-politikasi": "Gizlilik Politikası",
    "sartlar-kosullar": "Şartlar & Koşullar"
}

template_path = "/Users/atamantra/Desktop/branda/sayfa/hakkimizda/index.html"
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

for folder, title in pages.items():
    file_path = f"/Users/atamantra/Desktop/branda/sayfa/{folder}/index.html"
    
    # Simple replacement of Hakkımızda titles with the specific title
    new_content = template.replace("<title>Hakkımızda - 4 Mevsim Branda", f"<title>{title} - 4 Mevsim Branda")
    new_content = new_content.replace('<h1 class="text-gradient" style="font-size: 3rem; margin-bottom: 1rem;">Hakkımızda</h1>', f'<h1 class="text-gradient" style="font-size: 3rem; margin-bottom: 1rem;">{title}</h1>')
    
    # Replace the main text area entirely
    import re
    new_content = re.sub(
        r'<div class="container"\s+style="max-width: 800px; margin: 0 auto; color: var\(--color-text\); line-height: 1\.8; font-size: 1\.1rem;">.*?</div>',
        f'<div class="container" style="max-width: 800px; margin: 0 auto; color: var(--color-text); line-height: 1.8; font-size: 1.1rem;">\n            <p style="margin-bottom: 1.5rem;">\n                {title} sayfası yapım aşamasındadır. En kısa sürede güncellenecektir.\n            </p>\n        </div>',
        new_content,
        flags=re.DOTALL
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Created {file_path}")

