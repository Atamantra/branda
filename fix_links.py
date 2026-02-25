import os
import re

html_files = []
for root, dirs, files in os.walk('/Users/atamantra/Desktop/branda'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

def get_relative_path(from_path, to_dir):
    rel = os.path.relpath('/Users/atamantra/Desktop/branda' + to_dir, os.path.dirname(from_path))
    return rel + '/' if rel != '.' else ''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Müşteri Hizmetleri
    content = re.sub(r'<a href="[^"]*">Montaj Hizmeti</a>', f'<a href="{get_relative_path(file, "/sayfa/montaj-hizmeti")}index.html">Montaj Hizmeti</a>', content)
    content = re.sub(r'<a href="[^"]*">Garanti Politikası</a>', f'<a href="{get_relative_path(file, "/sayfa/garanti-politikasi")}index.html">Garanti Politikası</a>', content)
    content = re.sub(r'<a href="[^"]*">Bakım &amp; Onarım</a>|<a href="[^"]*">Bakım & Onarım</a>', f'<a href="{get_relative_path(file, "/sayfa/bakim-onarim")}index.html">Bakım & Onarım</a>', content)
    content = re.sub(r'<a href="[^"]*">Referanslarımız</a>', f'<a href="{get_relative_path(file, "/sayfa/referanslarimiz")}index.html">Referanslarımız</a>', content)
    content = re.sub(r'<a href="[^"]*">SSS</a>', f'<a href="{get_relative_path(file, "/sayfa/sss")}index.html">SSS</a>', content)

    # Kurumsal
    content = re.sub(r'<a href="[^"]*">Hikayemiz</a>', f'<a href="{get_relative_path(file, "/sayfa/hikayemiz")}index.html">Hikayemiz</a>', content)
    content = re.sub(r'<a href="[^"]*">Kariyer</a>', f'<a href="{get_relative_path(file, "/sayfa/kariyer")}index.html">Kariyer</a>', content)
    content = re.sub(r'<a href="[^"]*">Ticari Hesaplar</a>', f'<a href="{get_relative_path(file, "/sayfa/ticari-hesaplar")}index.html">Ticari Hesaplar</a>', content)
    content = re.sub(r'<a href="[^"]*">Gizlilik Politikası</a>', f'<a href="{get_relative_path(file, "/sayfa/gizlilik-politikasi")}index.html">Gizlilik Politikası</a>', content)
    content = re.sub(r'<a href="[^"]*">Şartlar &amp; Koşullar</a>|<a href="[^"]*">Şartlar & Koşullar</a>', f'<a href="{get_relative_path(file, "/sayfa/sartlar-kosullar")}index.html">Şartlar & Koşullar</a>', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Linked all new pages in footers.")
