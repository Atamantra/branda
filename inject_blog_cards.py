import re

posts_data = [
    {
        "slug": "fethiye-kafe-restoran-tente-cozumleri",
        "title": "Fethiye Kafe ve Restoranları İçin En İyi Tente Çözümleri",
        "date": "10 Mart 2026",
        "category": "trendler",
        "category_label": "Trendler",
        "img": "../isikli-tente.jpg",
        "excerpt": "Sezonu uzatmak ve müşteri konforunu artırmak isteyen Fethiye işletmecileri için en trend ışıklı pergola ve tente modelleri."
    },
    {
        "slug": "gocek-villalari-icin-biyoklimatik-pergola",
        "title": "Göcek Villaları İçin Biyoklimatik Pergola Sistemleri",
        "date": "05 Mart 2026",
        "category": "urunler",
        "category_label": "Ürün İncelemeleri",
        "img": "../hero.png",
        "excerpt": "Lüks ve estetiğin buluştuğu Göcek villalarının dış mekan tasarımlarında neden biyoklimatik pergola tercih edilmeli?"
    },
    {
        "slug": "oludeniz-otellerinde-havuz-kenari-golgelendirme",
        "title": "Ölüdeniz Otellerinde Havuz Kenarı Gölgelendirme İpuçları",
        "date": "28 Şubat 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../hero4.png",
        "excerpt": "Ölüdeniz bölgesindeki otel ve tatil köyleri için misafir memnuniyetini artıracak havuz başı şemsiye ve tente seçimi."
    },
    {
        "slug": "kavacik-rüzgarlarina-karsi-zip-perde",
        "title": "Kayaköy ve Seydikemer Rüzgarlarına Karşı Zip Perde",
        "date": "22 Şubat 2026",
        "category": "urunler",
        "category_label": "Ürün İncelemeleri",
        "img": "../zip_perde.jpg",
        "excerpt": "Fethiye'nin rüzgarlı kesimlerindeki evler için tasarlanmış, fırtınaya dayanıklı motorlu zip perde sistemleri."
    },
    {
        "slug": "fethiye-cam-balkon-kapatma-fiyatlari-2026",
        "title": "Fethiye Cam Balkon Kapatma Fiyatları 2026",
        "date": "18 Şubat 2026",
        "category": "trendler",
        "category_label": "Trendler",
        "img": "../giyotin.jpg",
        "excerpt": "2026 yılında Fethiye'de balkon veya teras kapatmak isteyenler için katlanır ve giyotin cam balkon maliyet analizi."
    },
    {
        "slug": "calis-plaji-isletmeleri-icin-mafsalli-tenteler",
        "title": "Çalış Plajı İşletmeleri İçin Mafsallı Tentelerin Önemi",
        "date": "12 Şubat 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../hero3.png",
        "excerpt": "Güneşin en güzel battığı yer olan Çalış Plajı'ndaki kafe ve bar işletmecilerine tente seçimi tüyoları."
    },
    {
        "slug": "mugla-kavurucu-sicaklarinda-serin-teraslar",
        "title": "Muğla Sıcaklarında Serin Teraslar Yaratmanın Sırrı",
        "date": "02 Şubat 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../tente_sistemleri.jpg",
        "excerpt": "Temmuz ve Ağustos aylarında 40 dereceyi bulan Muğla sıcağına karşı terasını korumanın ve serin tutmanın yolları."
    },
    {
        "slug": "fethiye-marina-tekne-golgelendirme-sistemleri",
        "title": "Göcek ve Fethiye Marinalarında Tekne Gölgelendirme Sistemleri",
        "date": "20 Ocak 2026",
        "category": "trendler",
        "category_label": "Trendler",
        "img": "../hero2.png",
        "excerpt": "Lüks yatlar ve guletler için tuzlu suya dayanıklı, paslanmaz gölgelendirme ve branda tasarımları."
    },
    {
        "slug": "hisaronu-villalarinda-kis-bahcesi-keyfi",
        "title": "Ovacık ve Hisarönü Villalarında Kış Bahçesi Keyfi",
        "date": "10 Ocak 2026",
        "category": "urunler",
        "category_label": "Ürün İncelemeleri",
        "img": "../giyotin.jpg",
        "excerpt": "Havası her zaman serin olan Ovacık ve Hisarönü mevkilerindeki evler için ideal kış bahçesi dekorasyonu."
    },
    {
        "slug": "fethiye-branda-semsiye-secim-rehberi",
        "title": "Fethiye'de İşletmeler İçin Şemsiye ve Branda Seçim Rehberi",
        "date": "05 Ocak 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../arackaplama.jpg",
        "excerpt": "Çay bahçelerinden butik otellere; mekanınız için hangi şemsiye veya tente modelinin uygun olduğuna nasıl karar verirsiniz?"
    }
]

html_cards = ""
for post in posts_data:
    html_cards += f"""
                <a href="{post['slug']}.html" class="blog-card" data-category="{post['category']}">
                    <span class="blog-category-badge">{post['category_label']}</span>
                    <div class="blog-img-wrapper">
                        <img src="{post['img']}" alt="{post['title']}" loading="lazy" onerror="this.src='../logo-futuristic.png'">
                    </div>
                    <div class="blog-content">
                        <span class="blog-date">{post['date']}</span>
                        <h3 class="blog-title">{post['title']}</h3>
                        <p class="blog-excerpt">
                            {post['excerpt']}
                        </p>
                        <span class="blog-read-more">Devamını Oku</span>
                    </div>
                </a>
"""

file_path = "/Users/atamantra/Desktop/branda/blog/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# find the closing </div> of the <div class="blog-grid" id="blogGrid">
pattern = r'(<div class="blog-grid" id="blogGrid">.*?)(\s*</div>\s*</div>\s*</section>)'
match = re.search(pattern, content, flags=re.DOTALL)

if match:
    new_content = match.group(1) + html_cards + match.group(2)
    # replace the entire matched block
    content = content.replace(match.group(0), new_content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected 10 blog cards.")
else:
    print("Could not find insertion point.")
