import os
import re

nav_template = """    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="{prefix}index.html" class="nav-logo">
                <img src="{prefix}logo-futuristic.png" alt="4 Mevsim Branda Logo" class="logo-img">
                <div class="logo-text">
                    <span class="logo-title">4 Mevsim Branda</span>
                    <span class="logo-tagline">Fethiye'nin Brandacısı</span>
                </div>
            </a>

            <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
                ☰
            </button>

            <ul class="nav-links" id="navLinks">
                <li><a href="{prefix}index.html">Ana Sayfa</a></li>
                <li class="dropdown">
                    <a href="{prefix}sayfa/hakkimizda/index.html" class="dropbtn">Kurumsal ▾</a>
                    <div class="dropdown-content">
                        <a href="{prefix}sayfa/hakkimizda/index.html">Hakkımızda</a>
                        <a href="{prefix}sayfa/vizyonumuz/index.html">Vizyonumuz</a>
                        <a href="{prefix}sayfa/misyonumuz/index.html">Misyonumuz</a>
                    </div>
                </li>
                <li class="dropdown">
                    <a href="{prefix}hizmetdetay/index.html" class="dropbtn">Hizmetlerimiz ▾</a>
                    <div class="dropdown-content">
                        <a href="{prefix}hizmetdetay/pergole-sistemleri.html">Pergole Sistemleri</a>
                        <a href="{prefix}hizmetdetay/golgelendirme-sistemleri.html">Gölgelendirme Sistemleri</a>
                        <a href="{prefix}hizmetdetay/tente-sistemleri.html">Tente Sistemleri</a>
                        <a href="{prefix}hizmetdetay/semsiye-sistemleri.html">Şemsiye Sistemleri</a>
                        <a href="{prefix}hizmetdetay/balkon-stor-perde.html">Balkon Stor Perde</a>
                        <a href="{prefix}hizmetdetay/mafsalli-tente.html">Mafsallı Tente</a>
                        <a href="{prefix}hizmetdetay/zip-perde-sistemleri.html">Zip Perde Sistemleri</a>
                        <a href="{prefix}hizmetdetay/giyotin-cam-sistemleri.html">Giyotin Cam Sistemleri</a>
                        <a href="{prefix}hizmetdetay/wint-tente.html">Wint Tente</a>
                        <a href="{prefix}hizmetdetay/arac-kaplama.html">Araç Kaplama</a>
                    </div>
                </li>
                <li><a href="{prefix}albumler/galeri/index.html">Galeri</a></li>
                <li><a href="{prefix}blog/index.html">Blog</a></li>
                <li><a href="{prefix}iletisim/index.html">İletişim Bilgileri</a></li>
                <li>
                    <a href="tel:05514218705" class="btn btn-primary" style="padding: 0.5rem 1rem;">
                        0 551 421 87 05
                    </a>
                </li>
            </ul>
        </div>
    </nav>"""

footer_template = """    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3 class="text-gradient">4 Mevsim Branda</h3>
                    <p>
                        Yaşam alanlarını her mevsim konforlu, estetik ve kullanışlı hale getiren yenilikçi çözümler sunarak,
                        tente ve gölgelendirme sistemleri sektöründe öncü ve güvenilir bir marka olmak. Kalite, estetik ve
                        müşteri memnuniyetini ön planda tutarak, hem bireysel hem de kurumsal müşterilerimizin ilk tercihi olmak.
                    </p>
                </div>

                <div class="footer-section">
                    <h3>Hızlı Bağlantılar</h3>
                    <ul class="footer-links">
                        <li><a href="{prefix}index.html">Ana Sayfa</a></li>
                        <li><a href="{prefix}sayfa/hakkimizda/index.html">Kurumsal</a></li>
                        <li><a href="{prefix}hizmetdetay/index.html">Hizmetlerimiz</a></li>
                        <li><a href="{prefix}albumler/galeri/index.html">Galeri</a></li>
                        <li><a href="{prefix}blog/index.html">Blog</a></li>
                        <li><a href="{prefix}iletisim/index.html">İletişim</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Müşteri Hizmetleri</h3>
                    <ul class="footer-links">
                        <li><a href="{prefix}sayfa/montaj-hizmeti/index.html">Montaj Hizmeti</a></li>
                        <li><a href="{prefix}sayfa/garanti-politikasi/index.html">Garanti Politikası</a></li>
                        <li><a href="{prefix}sayfa/bakim-onarim/index.html">Bakım & Onarım</a></li>
                        <li><a href="{prefix}sayfa/referanslarimiz/index.html">Referanslarımız</a></li>
                        <li><a href="{prefix}sayfa/sss/index.html">SSS</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Kurumsal</h3>
                    <ul class="footer-links">
                        <li><a href="{prefix}sayfa/hikayemiz/index.html">Hikayemiz</a></li>
                        <li><a href="{prefix}sayfa/kariyer/index.html">Kariyer</a></li>
                        <li><a href="{prefix}sayfa/ticari-hesaplar/index.html">Ticari Hesaplar</a></li>
                        <li><a href="{prefix}sayfa/gizlilik-politikasi/index.html">Gizlilik Politikası</a></li>
                        <li><a href="{prefix}sayfa/sartlar-kosullar/index.html">Şartlar & Koşullar</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2026 4 Mevsim Branda. Tüm hakları saklıdır. Fethiye/Muğla.</p>
            </div>
        </div>
    </footer>"""

root_dir = "/Users/atamantra/Desktop/branda"

html_files = []
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    # Determine depth
    rel_path = os.path.relpath(file_path, root_dir)
    dir_name = os.path.dirname(rel_path)
    if dir_name == "":
        depth = 0
    else:
        depth = len(dir_name.split(os.sep))
    
    prefix = "../" * depth
    
    # Format templates
    nav_to_insert = nav_template.replace("{prefix}", prefix)
    footer_to_insert = footer_template.replace("{prefix}", prefix)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace nav
    # The navbar usually starts with <nav class="navbar"...> and ends with </nav>
    # We will use regex to find this block and replace it.
    new_content = re.sub(r'<nav\s+class="navbar"[^>]*>.*?</nav>', nav_to_insert, content, flags=re.DOTALL)
    
    # Replace footer
    # Usually starts with <footer class="footer"...> and ends with </footer>
    new_content = re.sub(r'<footer\s+class="footer".*?</footer>', footer_to_insert, new_content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Standardized {len(html_files)} HTML files.")
