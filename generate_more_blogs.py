import os

posts = {
    "fethiye-kafe-restoran-tente-cozumleri": {
        "title": "Fethiye Kafe ve Restoranları İçin En İyi Tente Çözümleri",
        "date": "10 Mart 2026",
        "category": "trendler",
        "category_label": "Trendler",
        "img": "../isikli-tente.jpg",
        "excerpt": "Sezonu uzatmak ve müşteri konforunu artırmak isteyen Fethiye işletmecileri için en trend ışıklı pergola ve tente modelleri.",
        "content": """
            <p>Fethiye'nin kalbinde, Paspatur'da veya kordon boyunda bir kafe işletiyorsanız, mekanınızın dış alanını verimli kullanmak ticari başarınızın anahtarıdır. Akdeniz'in yakıcı güneşi ve aniden bastıran yağmurları, doğru gölgelendirme sistemini seçmeyi zorunlu kılıyor.</p>
            <h2>Işıklı Katlanır Pergola Sistemleri</h2>
            <p>Müşterilerinizin akşamları loş bir ortamda keyifle oturabilmesi için entegre LED aydınlatmalı pergola sistemleri tercih edebilirsiniz. 4 Mevsim Branda olarak sunduğumuz motorlu sistemler, tek bir kumanda ile tüm açık alanı 1 dakika içerisinde kapalı bir kış bahçesine dönüştürebilir.</p>
            <h2>Giyotin Cam Entegrasyonu</h2>
            <p>Sadece üstünü kapatmak yetmez; kış aylarında rüzgarı kesmek için tentenizi <b>giyotin cam sistemleri</b> ile destekleyerek mekanınızı 12 ay boyunca hizmet verebilir hale getirebilirsiniz. Fethiye kordon boyundaki referans projelerimizi inceleyerek işletmeniz için en uygun modele karar verebilirsiniz.</p>
        """
    },
    "gocek-villalari-icin-biyoklimatik-pergola": {
        "title": "Göcek Villaları İçin Biyoklimatik Pergola Sistemleri",
        "date": "05 Mart 2026",
        "category": "urunler",
        "category_label": "Ürün İncelemeleri",
        "img": "../hero.png",
        "excerpt": "Lüks ve estetiğin buluştuğu Göcek villalarının dış mekan tasarımlarında neden biyoklimatik pergola tercih edilmeli?",
        "content": """
            <p>Göcek, eşsiz koyları ve lüks villa yaşamıyla bilinen, elit bir yaşam merkezidir. Buradaki müstakil evlerin bahçe ve teras dekorasyonları, hem şıklığı hem de fonksiyonelliği bir arada sunmalıdır. İşte tam bu noktada <b>Biyoklimatik (Akıllı) Pergola</b> sistemleri devreye giriyor.</p>
            <h2>Doğal Havalandırma ve İklimlendirme</h2>
            <p>Klasik brandaların aksine, biyoklimatik pergolaların tavanı kendi ekseni etrafında dönebilen alüminyum panellerden oluşur. Göcek'in sıcak yaz akşamlarında, panelleri hafifçe aralayarak içerideki sıcak havanın tahliye edilmesini (baca etkisi) sağlayabilir, aynı zamanda güneşi tamamen kesebilirsiniz.</p>
            <h2>Modern Mimari ile Kusursuz Uyum</h2>
            <p>Antrasit gri, siyah veya ahşap görünümlü fırın boyalı alüminyum paneller, Göcek'in modern villa mimarisiyle kusursuz bir uyum sağlar. 4 Mevsim Branda kalitesiyle uyguladığımız bu sistemler, evinize değer katan en önemli yatırım olacaktır.</p>
        """
    },
    "oludeniz-otellerinde-havuz-kenari-golgelendirme": {
        "title": "Ölüdeniz Otellerinde Havuz Kenarı Gölgelendirme İpuçları",
        "date": "28 Şubat 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../hero4.png",
        "excerpt": "Ölüdeniz bölgesindeki otel ve tatil köyleri için misafir memnuniyetini artıracak havuz başı şemsiye ve tente seçimi.",
        "content": """
            <p>Dünyaca ünlü Ölüdeniz plajına ev sahipliği yapan otelinizde, misafirlerinizin havuz başında konforlu vakit geçirmesi için doğru gölgelendirme sistemini seçmek büyük önem taşır. Turizm sezonunda UV ışınlarından korunmak, müşteri memnuniyetinin ilk kurallarındandır.</p>
            <h2>Mega Şemsiye Sistemleri</h2>
            <p>Geniş havuz başı alanları için 4x4 veya 5x5 metre ebatlarındaki teleskopik <b>Mega Şemsiye Sistemleri</b> idealdir. Tek bir şemsiye çatısı altında dört şezlongu gölgeleyebilir, alan tasarrufu sağlayabilirsiniz. Üstelik akrilik kumaş seçenekleriyle otelinizin kurumsal renklerini şemsiyelerinize yansıtabilirsiniz.</p>
            <h2>Wint Tente ve Çift Açılır Sistemler</h2>
            <p>Bar ve snack alanları için çift tarafa açılabilen "T Tente" (Çift Açılır Tente) modelleri, geniş gölge alanı yaratırken direk sayısını minimize ederek mekan kullanımını rahatlatır. 4 Mevsim Branda olarak Ölüdeniz bölgesindeki birçok seçkin otelin havuz başı projesine imza atmaktayız.</p>
        """
    },
    "kavacik-rüzgarlarina-karsi-zip-perde": {
        "title": "Kayaköy ve Seydikemer Rüzgarlarına Karşı Zip Perde",
        "date": "22 Şubat 2026",
        "category": "urunler",
        "category_label": "Ürün İncelemeleri",
        "img": "../zip_perde.jpg",
        "excerpt": "Fethiye'nin rüzgarlı kesimlerindeki evler için tasarlanmış, fırtınaya dayanıklı motorlu zip perde sistemleri.",
        "content": """
            <p>Fethiye'nin yüksek kesimleri olan Seydikemer, Kayaköy ve Ovacık bölgeleri yaz kış sürekli bir esintiye maruz kalır. Bu bölgelerde standart stor perdeler rüzgardan dolayı uçuşur ve raydan çıkar. Çözüm: <b>Zip Perde (Fermuarlı Perde) Sistemleri</b>.</p>
            <h2>Fermuar Teknolojisi ile Maksimum Dayanıklılık</h2>
            <p>Zip perde sistemlerinde kumaşın her iki kenarında özel bir fermuar bulunur ve bu fermuar, yan dikey rayların içine kenetlenir. Bu sayede perde ne kadar rüzgar alırsa alsın yerinden çıkmaz, şişme yapmaz.</p>
            <h2>Güneşi Kırarken Manzarayı Korumak</h2>
            <p>Kullandığımız mikro delikli Ferrari veya Screen kumaşlar sayesinde, perde inikken bile Kayaköy'ün o güzel orman ve dağ manzarasını izlemeye devam edebilirsiniz. Dışarıdan bakıldığında ise içerisi görünmez, bu da size mükemmel bir mahremiyet sağlar.</p>
        """
    },
    "fethiye-cam-balkon-kapatma-fiyatlari-2026": {
        "title": "Fethiye Cam Balkon Kapatma Fiyatları 2026",
        "date": "18 Şubat 2026",
        "category": "trendler",
        "category_label": "Trendler",
        "img": "../giyotin.jpg",
        "excerpt": "2026 yılında Fethiye'de balkon veya teras kapatmak isteyenler için katlanır ve giyotin cam balkon maliyet analizi.",
        "content": """
            <p>Evinize ekstra bir yaşam alanı eklemek veya kış aylarında balkonunuzu kullanabilmek için en etkili yol onu cam ile kapatmaktır. Peki, 2026 sezonunda Fethiye'de cam balkon yaptırmanın ortalama maliyetleri ve seçenekleri nelerdir?</p>
            <h2>Katlanır Cam Balkon vs. Giyotin Cam</h2>
            <p>Standart <b>katlanır cam balkonlar</b> (8mm veya Isıcamlı), metrekare bazında en ekonomik çözümdür. Ancak daha lüks ve kullanımı kolay bir sistem arıyorsanız, motorlu <b>giyotin cam sistemleri</b> öne çıkmaktadır.</p>
            <h2>Fiyatları Belirleyen Unsurlar</h2>
            <ul>
                <li><strong>Camın Niteliği:</strong> Isıcam (çift cam) kullanılması maliyeti artırsa da uzun vadede yakıt ve elektrik tasarrufu sağlar.</li>
                <li><strong>Profil Kalitesi:</strong> Alüminyum et kalınlığı, sistemin sağlamlığını ve rüzgar direncini doğrudan etkiler. Fethiye 4 Mevsim Branda olarak sadece yüksek kaliteli ve garantili alüminyum profiller kullanıyoruz.</li>
                <li><strong>Motor Markası:</strong> Giyotin ve pergola sistemlerinde Somfy, Becker veya yerli Mosel gibi motor tercihleri toplam bütçeyi değiştirir.</li>
            </ul>
            <p>Size en uygun teklifi almak için Fethiye'deki uzman ekibimizden ücretsiz keşif randevusu oluşturabilirsiniz.</p>
        """
    },
    "calis-plaji-isletmeleri-icin-mafsalli-tenteler": {
        "title": "Çalış Plajı İşletmeleri İçin Mafsallı Tentelerin Önemi",
        "date": "12 Şubat 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../hero3.png",
        "excerpt": "Güneşin en güzel battığı yer olan Çalış Plajı'ndaki kafe ve bar işletmecilerine tente seçimi tüyoları.",
        "content": """
            <p>Fethiye'nin en popüler turizm noktalarından biri olan Çalış Plajı, özellikle gün batımı manzarasıyla meşhurdur. Kordon boyuna dizilmiş restoran ve kafelerin, misafirlerini güneşin dik açılarla geldiği öğle ve ikindi saatlerinde koruması hayati önem taşır.</p>
            <h2>Ekonomik ve Pratik Çözüm: Mafsallı Tente</h2>
            <p>Dükkan önlerini gölgelendirmek için en çok tercih edilen sistem <b>Mafsallı Tentelerdir</b>. İsteğe bağlı olarak motorlu veya manuel (çevirme kollu) yapılabilen bu sistemler, kasetli modelleriyle kapandığında kumaşı kışın yağmurdan ve tozdan korur.</p>
            <h2>Kumaş Değişimi ve Bakım</h2>
            <p>Deniz tuzu ve güneş sebebiyle yıllar içinde tentenizin mekanizması sağlam kalsa da kumaşı solabilir. 4 Mevsim Branda olarak, Çalış plajındaki işletmelere hızlı <b>tente kumaşı değişimi</b> hizmeti sunarak, mekanınızı yeni bir tenteye ihtiyaç duymadan sezona hazırlıyoruz.</p>
        """
    },
    "mugla-kavurucu-sicaklarinda-serin-teraslar": {
        "title": "Muğla Sıcaklarında Serin Teraslar Yaratmanın Sırrı",
        "date": "02 Şubat 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../tente_sistemleri.jpg",
        "excerpt": "Temmuz ve Ağustos aylarında 40 dereceyi bulan Muğla sıcağına karşı terasını korumanın ve serin tutmanın yolları.",
        "content": """
            <p>Muğla ve Fethiye bölgesinin yazı harikadır, ancak kavurucu Ağustos sıcakları balkon ve terasları gündüzleri kullanılamaz hale getirebilir. İklimlendirmenin yetmediği açık alanları doğal yollarla serinletmek için gölge elzemdir.</p>
            <h2>Akrilik Kumaşın Gücü</h2>
            <p>Piyasada bulunan ucuz polyester brandalar güneşi tutar ancak altını sera gibi ısıtır. Bizim kullandığımız ithal <b>akrilik tente kumaşları</b> nefes alan yapısı ve UV filtreli özelliği sayesinde güneş ışınlarını geçirmez ve altındaki havanın boğucu olmasını engeller.</p>
            <h2>Gölgelendirme Açıları</h2>
            <p>Terasınızın baktığı cepheye (Güney, Batı vs.) göre tentenin eğim açısı uzmanlarımız tarafından ayarlanır. Mafsallı tentelerdeki "eğim ayar mekanizması" sayesinde güneşin batış saatinde düşen dik ışınları engellemek için tentenizi aşağı doğru eğebilirsiniz.</p>
        """
    },
    "fethiye-marina-tekne-golgelendirme-sistemleri": {
        "title": "Göcek ve Fethiye Marinalarında Tekne Gölgelendirme Sistemleri",
        "date": "20 Ocak 2026",
        "category": "trendler",
        "category_label": "Trendler",
        "img": "../hero2.png",
        "excerpt": "Lüks yatlar ve guletler için tuzlu suya dayanıklı, paslanmaz gölgelendirme ve branda tasarımları.",
        "content": """
            <p>Türkiye'nin en önemli deniz turizmi merkezleri olan Fethiye, Göcek ve Marmaris marinalarında demirli binlerce tekne ve yat için, güvertede geçirilen zamanın kalitesini artıracak gölgelendirme sistemleri üretiyoruz.</p>
            <h2>Marine Kalite Su Geçirmez Kumaşlar</h2>
            <p>Deniz üzerinde kullanılan brandaların yapısı karadaki tentelerden farklıdır. Tuzlu suya, rüzgara, martı pisliklerine ve yoğun UV ışınlarına ekstra dayanıklı, su ve yağ itici <b>Marine grubu kumaşlar</b> (Sunbrella Marine gibi) tercih edilmelidir.</p>
            <h2>Paslanmaz Çelik Aksam</h2>
            <p>Teknelerdeki tüm bağlantı ekipmanları ve mafsallar, denizin korozyon etkisine direnebilmesi için 316 kalite paslanmaz çelik kullanılarak üretilir. Kışlama (kışlık kapama) brandaları veya yazlık bimini tente çözümleri için Fethiye 4 Mevsim Branda yanınızda.</p>
        """
    },
    "hisaronu-villalarinda-kis-bahcesi-keyfi": {
        "title": "Ovacık ve Hisarönü Villalarında Kış Bahçesi Keyfi",
        "date": "10 Ocak 2026",
        "category": "urunler",
        "category_label": "Ürün İncelemeleri",
        "img": "../giyotin.jpg",
        "excerpt": "Havası her zaman serin olan Ovacık ve Hisarönü mevkilerindeki evler için ideal kış bahçesi dekorasyonu.",
        "content": """
            <p>Fethiye merkeze göre havası 5-6 derece daha serin ve nemsiz olan Ovacık ve Hisarönü bölgeleri, İngiliz turistlerin ve yerli halkın en sevdiği yerleşim yerleridir. Ancak kışları ve serin bahar akşamlarında verandayı kullanabilmek için izole bir kış bahçesi şarttır.</p>
            <h2>Tavan: Işıklı Otomatik Pergola</h2>
            <p>Kış bahçesinin çatınızı oluşturan açılır kapanır tavanı sayesinde yıldızlı geceyi izleyebilir veya yağmur başladığında tek tuşla tamamen kapanarak koruma altına alabilirsiniz.</p>
            <h2>Etrafı Camla Çevirme</h2>
            <p>Pergolanın etrafını <b>sürme cam sistemleri</b> veya <b>giyotin camlar</b> ile kapatarak mekanı rüzgara karşı yalıtabilirsiniz. İçeriye kuracağınız şık bir şömine sobası veya infrared ısıtıcı sayesinde, Hisarönü'nün serin kış akşamlarında kahvenizi yudumlayacağınız harika bir odanız olacaktır.</p>
        """
    },
    "fethiye-branda-semsiye-secim-rehberi": {
        "title": "Fethiye'de İşletmeler İçin Şemsiye ve Branda Seçim Rehberi",
        "date": "05 Ocak 2026",
        "category": "ipuclari",
        "category_label": "İpuçları",
        "img": "../arackaplama.jpg",
        "excerpt": "Çay bahçelerinden butik otellere; mekanınız için hangi şemsiye veya tente modelinin uygun olduğuna nasıl karar verirsiniz?",
        "content": """
            <p>Bir işletme sahibi olarak dış mekanı değerlendirmek istiyorsanız, önünüzde birçok seçenek mevcut. Yatırım maliyetlerini doğru yönetmek ve uzun ömürlü bir ürün almak için nelere dikkat etmelisiniz?</p>
            <ul>
                <li><strong>Alan Büyüklüğü:</strong> 15-20 metrekare arasına kadar olan alanlarda mafsallı tente veya 4x4 teleskopik şemsiyeler fiyat/performans ürünüdür.</li>
                <li><strong>Sabit mi, Yarı Açık mı?:</strong> Alanınız belediye yönetmeliğine göre sabit yapılaşmaya izin vermiyorsa, tekerlekli ağırlık bidonlarına sahip büyük şemsiyeler veya kolay sökülebilir mafsallı çadır sistemlerini tercih etmelisiniz (T Tente).</li>
                <li><strong>Kışın Kullanılacak mı?:</strong> Sadece yazlık faaliyet gösteren bir dondurmacıysanız pergola maliyetli olabilir; renkli bir körüklü tente (karpuz tente) hem retro bir hava katar hem de ekonomiktir. Ancak kışın da faal olan bir kafeyseniz, Pergola + Giyotin cam yatırımı kendisini tek kış sezonunda amorti edecektir.</li>
            </ul>
            <p>Doğru yatırımı yapmak için Fethiye 4 Mevsim Branda teknik ekibiyle irtibata geçin.</p>
        """
    }
}

template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 4 Mevsim Branda Blog</title>
    
    <link rel="icon" type="image/png" href="../logo-futuristic.png">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="../styles.css?v=6">
</head>
<body>
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="../index.html" class="nav-logo">
                <img src="../logo-futuristic.png" alt="4 Mevsim Branda Logo" class="logo-img">
                <div class="logo-text">
                    <span class="logo-title">4 Mevsim Branda</span>
                    <span class="logo-tagline">Fethiye'nin Brandacısı</span>
                </div>
            </a>
            <ul class="nav-links" id="navLinks">
                <li><a href="../index.html">Ana Sayfa</a></li>
                <li><a href="index.html" class="active" style="color: var(--color-primary)">Blog</a></li>
            </ul>
        </div>
    </nav>

    <article>
        <div class="article-header">
            <div class="container">
                <div class="article-meta">
                    <span>{date}</span>
                    <span style="color: var(--color-primary); font-weight: 600;">{category_label}</span>
                </div>
                <h1 style="font-family: 'Playfair Display', serif; font-size: 3rem; color: var(--color-text-main); margin-bottom: 2rem;">{title}</h1>
            </div>
        </div>
        
        <div class="container">
            <img src="{img}" alt="{title}" class="article-hero-img" loading="lazy" onerror="this.src='../logo-futuristic.png'">
            
            <div class="article-content">
                {content}
            </div>
        </div>
    </article>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom" style="text-align: center; border-top: none;">
                <p>&copy; 2026 4 Mevsim Branda. Tüm hakları saklıdır. Fethiye/Muğla.</p>
            </div>
        </div>
    </footer>
    <script src="../script.js"></script>
</body>
</html>
"""

for slug, data in posts.items():
    file_path = f"/Users/atamantra/Desktop/branda/blog/{slug}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template.format(
            title=data["title"],
            date=data["date"],
            category_label=data["category_label"],
            img=data["img"],
            content=data["content"]
        ))
        
print("Successfully generated 10 Fethiye blog posts.")
