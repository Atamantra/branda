import os
import re

content_map = {
    "montaj-hizmeti": """
            <h2 style="margin-bottom: 1.5rem;">Profesyonel Montaj Hizmeti</h2>
            <p style="margin-bottom: 1.5rem;">
                4 Mevsim Branda olarak, ürünlerimizin yalnızca üretiminde değil, kurulum aşamasında da en yüksek kalite standartlarını sunmayı hedefliyoruz. Satın aldığınız tente, pergole, giyotin cam ve diğer tüm gölgelendirme sistemlerinin montajı, alanında uzman ve deneyimli saha ekiplerimiz tarafından titizlikle gerçekleştirilir.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Montaj Süreci Nasıl İşler?</h3>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;"><strong>Keşif ve Planlama:</strong> Uzman ekibimiz, kurulum yapılacak alanı önceden inceler ve projenize en uygun montaj planını çıkarır.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Güvenli Taşıma:</strong> Ürünleriniz, taşıma sırasında zarar görmeyecek şekilde özenle paketlenir ve montaj alanına ulaştırılır.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Profesyonel Kurulum:</strong> Gelişmiş ekipmanlarımız ve iş güvenliği kurallarına uygun olarak çalışan ekibimiz, sistemi sorunsuz bir şekilde yerine monte eder.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Test ve Teslimat:</strong> Montaj tamamlandıktan sonra, sistemin motorlu, manuel mekanizmaları, aydınlatma ve otomasyon özellikleri test edilir ve sistem kullanımınıza hazır bir şekilde teslim edilir.</li>
            </ul>
            <p style="margin-bottom: 3rem;">
                Hızlı, temiz ve güvenli montaj hizmetimizle yaşam alanlarınızda kesintisiz konfor sağlamak için buradayız.
            </p>
""",
    "garanti-politikasi": """
            <h2 style="margin-bottom: 1.5rem;">Kapsamlı Garanti Politikası</h2>
            <p style="margin-bottom: 1.5rem;">
                4 Mevsim Branda olarak, üretimini ve montajını üstlendiğimiz tüm tente, pergola, şemsiye ve gölgelendirme sistemlerinin arkasında duruyoruz. Müşteri memnuniyetini en üst düzeye çıkarmak için ürünlerimizi uzun yıllar sorunsuz kullanabilmenizi sağlayan kapsamlı garanti seçenekleri sunuyoruz.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Garanti Kapsamı ve Süreleri</h3>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;"><strong>Kumaş Garantisi:</strong> Kullandığımız Avrupa standartlarındaki akrilik ve ithal kumaşlar, solmaya, çürümeye ve su geçirmeye karşı üretici standartlarına bağlı olarak genellikle <strong>5 Yıl</strong> garantilidir.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Motor ve Otomasyon:</strong> Sistemlerimizde tercih ettiğimiz dünya markası motorlar (Somfy, Becker, vb.), fabrikasyon hatalara karşı en az <strong>5 Yıl</strong> garantilidir.</li>
                <li style="margin-bottom: 0.5rem;"><strong>İskelet ve Alüminyum Aksam:</strong> Paslanmaz, elektrostatik fırın boyalı alüminyum ve çelik aksamlarımız, yapısal bütünlük açısından <strong>2 Yıl</strong> garantimiz altındadır.</li>
                <li style="margin-bottom: 0.5rem;"><strong>İşçilik ve Montaj:</strong> 4 Mevsim Branda ekipleri tarafından gerçekleştirilen tüm montaj işlemleri <strong>2 Yıl</strong> boyunca teknik servis garantimiz altındadır.</li>
            </ul>
            <p style="margin-bottom: 3rem;">
                Garanti koşulları, ürünlerin kullanım kılavuzunda belirtilen standartlara uygun şekilde ve amacı doğrultusunda kullanılması şartıyla geçerlidir. Doğal afetler (fırtına, dolu vb.), kullanıcı kaynaklı hatalar ve dışarıdan yapılan izinsiz müdahaleler garanti kapsamı dışındadır.
            </p>
""",
    "bakim-onarim": """
            <h2 style="margin-bottom: 1.5rem;">Bakım ve Onarım Hizmetleri</h2>
            <p style="margin-bottom: 1.5rem;">
                Tente, pergole ve gölgelendirme sistemlerinizin ilk günkü performansını ve şıklığını koruması için düzenli bakım son derece önemlidir. Sistemlerinizin ömrünü uzatmak, mekanik ve motor arızalarının önüne geçmek için profesyonel bakım ve onarım desteği sunuyoruz.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Hizmet Kapsamımız</h3>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;"><strong>Periyodik Bakım:</strong> Özellikle kış ve yaz ayları öncesinde yapılan hareketli parçaların yağlanması, kayış / ray sistemlerinin kontrolü ve kumaş temizliği.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Kumaş Yenileme (Kılıf Değişimi):</strong> Zamanla yıpranan, solan veya dekorasyonunuza artık uymayan tente/şemsiye kumaşlarınızı, iskelet sisteminizi değiştirmeden yeniliyoruz.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Motor ve Sensör Onarımı:</strong> Çalışmayan veya arıza veren motor, kumanda, güneş, rüzgar sensörleri yetkili ekiplerimizce hızla onarılır veya yenisiyle değiştirilir.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Mekanik Aksam Onarımı:</strong> Kırılmış veya yamulmuş mafsallar, bağlantı aparatları ve fitillerin orijinal yedek parçalar ile değişim hizmeti.</li>
            </ul>
            <p style="margin-bottom: 3rem;">
                İster bizim ürünümüz olsun, ister farklı bir markanın ürünü; bakım ve onarım ihtiyaçlarınız için Fethiye ve çevresinde güvenilir çözüm ortağınız 4 Mevsim Branda'dır.
            </p>
""",
    "referanslarimiz": """
            <h2 style="margin-bottom: 1.5rem;">Referanslarımız</h2>
            <p style="margin-bottom: 1.5rem;">
                Fethiye, Göcek, Ölüdeniz ve Muğla çevresinde 10 yılı aşkın sürede tamamladığımız binlerce başarılı proje, kalitemizin ve güvenilirliğimizin en büyük göstergesidir. Evlerin balkonlarından yatların brandalarına, kafelerden büyük turistik tesislere kadar geniş yelpazede hizmet sunmaktan gurur duyuyoruz.
            </p>
            <p style="margin-bottom: 1.5rem;">
                Hizmet Verdiğimiz Başlıca Sektörler:
            </p>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;"><strong>Oteller ve Tatil Köyleri:</strong> Havuz başı pergole sistemleri, plaj şemsiyeleri ve restoran gölgelendirmeleri.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Kafe ve Restoranlar:</strong> Giyotin cam sistemleri ve kış bahçesi çözümleri ile işletmelerin 4 mevsim hizmet verebilmesini sağlayan tasarımlar.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Özel Konutlar & Villalar:</strong> Balkon stor perdeleri, veranda kapatmaları ve hareketli tente uygulamaları.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Tekne ve Yat Sahipleri:</strong> Deniz şartlarına dayanıklı ithal kumaşlarla tekne brandaları ve özel minder dikimleri.</li>
            </ul>
            <p style="margin-bottom: 3rem;">
                Projelerimize dair detaylı fotoğrafları ve öncesi/sonrası görüntüleri görmek için lütfen <strong>Galeri</strong> sayfamızı ziyaret edin.
            </p>
""",
    "sss": """
            <h2 style="margin-bottom: 1.5rem;">Sıkça Sorulan Sorular (SSS)</h2>
            <p style="margin-bottom: 1.5rem;">
                Firmamız ve hizmetlerimizle ilgili en çok merak edilen soruları ve cevaplarını aşağıda bulabilirsiniz.
            </p>
            
            <h4 style="margin-bottom: 0.5rem; margin-top: 1.5rem;">1. Ücretsiz keşif hizmetiniz var mı?</h4>
            <p style="margin-bottom: 1.5rem;">Evet, Fethiye içi ve yakın çevre projelerinizde alanında uzman ekibimiz yerinizi ziyaret ederek ücretsiz ölçü alır ve projenize en uygun çözüm önerileri ile birlikte fiyat teklifi sunar.</p>

            <h4 style="margin-bottom: 0.5rem;">2. Üretim ve montaj süresi ortalama kaç gündür?</h4>
            <p style="margin-bottom: 1.5rem;">Standart tente ve stor perde siparişleriniz genellikle 3-7 iş günü içerisinde teslim edilir. Motorlu pergole ve giyotin cam gibi özel üretim gerektiren büyük projelerde ise bu süre 15-20 iş gününü bulabilmektedir.</p>

            <h4 style="margin-bottom: 0.5rem;">3. Tente kumaşları suyu geçirir mi, güneşte solar mı?</h4>
            <p style="margin-bottom: 1.5rem;">Kullandığımız ithal akrilik kumaşlar su itici özelliğe (teflon kaplama) sahiptir ve hafif/orta şiddetli yağmurlarda su geçirmez. Ayrıca UV korumalı yapısı sayesinde güneşte solmaya karşı 5 yıl üretici garantilidir.</p>

            <h4 style="margin-bottom: 0.5rem;">4. Şehir dışına (veya Fethiye dışındaki ilçelere) hizmet veriyor musunuz?</h4>
            <p style="margin-bottom: 1.5rem;">Öncelikli hizmet alanımız Fethiye, Göcek, Dalaman, Seydikemer, Kalkan ve Kaş bölgeleridir. Ancak proje büyüklüğüne göre Muğla geneli ve civar illere de montaj hizmeti sağlamaktayız. Şehir dışından gelen sadece mekanizma/kumaş siparişlerini ise kargo ile gönderebiliyoruz.</p>

            <h4 style="margin-bottom: 0.5rem;">5. Rüzgarlı havalarda tente kullanabilir miyim?</h4>
            <p style="margin-bottom: 3rem;">Mafsallı ve kasetli tentelerin aşırı rüzgarlı ve fırtınalı havalarda kapalı tutulması mekanizmanın sağlığı açısından şarttır. Bu durumlar için sistemlerimize <strong>Rüzgar Sensörü</strong> ekliyoruz; böylece tente rüzgar şiddetlendiğinde otomatik olarak kendini kapatır. Pergola ve Zip Perde sistemlerimiz ise yüksek rüzgar hızlarına dayanıklı şekilde tasarlanmıştır.</p>
""",
    "hikayemiz": """
            <h2 style="margin-bottom: 1.5rem;">Hikayemiz</h2>
            <p style="margin-bottom: 1.5rem;">
                Yıllar önce küçük bir atölyede, zanaatkârlık ruhuyla başlayan serüvenimiz, bugün Fethiye ve Muğla bölgesinin en çok tercih edilen; yenilikçi gölgelendirme ve tente sistemleri üreten öncü markası <strong>4 Mevsim Branda</strong>'ya dönüştü.
            </p>
            <p style="margin-bottom: 1.5rem;">
                Kurulduğumuz ilk günden bu yana inandığımız tek bir ilke var: <i>"Mekanları sadece güneşten veya yağmurdan korumak değil, o mekanlara ruh katan, insanların içinde 4 mevsim konforla yaşayabileceği estetik yaşam alanları yaratmak."</i> 
            </p>
            <p style="margin-bottom: 1.5rem;">
                Geçmişten gelen terzilik ve branda dikim tecrübemizi, bugün modern dünyanın gereksinimleri olan motorlu pergola, akıllı ev otomasyonuna entegre tente sistemleri ve mimari giyotin cam projeleriyle harmanladık. Aile şirketi sıcaklığını profesyonel mühendislik yaklaşımıyla birleştirerek her müşterimizi "birinci müşteri" heyecanıyla karşıladık.
            </p>
            <p style="margin-bottom: 3rem;">
                Bugün teknolojiyi yakından takip eden üretim parkurumuz, alanında uzman montaj ekiplerimiz ve "satış sonrası" sağladığımız sonsuz güvenle; bölgedeki kafelerin, lüks villaların, otellerin ve her bir sıcak evin değişmez çözüm ortağı olmaktan büyük bir gurur duyuyoruz. Dışarıda mevsim ne olursa olsun, içerde hep konforu yaşatmak için çalışmaya devam edeceğiz.
            </p>
""",
    "kariyer": """
            <h2 style="margin-bottom: 1.5rem;">Kariyer Olanakları</h2>
            <p style="margin-bottom: 1.5rem;">
                4 Mevsim Branda olarak başarımızın temelinde, işini tutkuyla yapan, yenilikçi ve sürekli gelişime açık çalışma arkadaşlarımız yatıyor. Büyüyen şirket yapımızda, hem üretim/atölye tarafında hem de montaj ve satış ağımızda bizimle birlikte büyüyecek ekip arkadaşları arıyoruz.
            </p>
            <p style="margin-bottom: 1.5rem;">
                Çalışma prensibimiz "biz" olabilmektir. Çalışanlarımıza güvenli ve huzurlu bir çalışma ortamı sağlamak, iş sağlığı ve güvenliği kurallarına titizlikle uymak birinci önceliğimizdir. Zanaatkâr ruhu modern sanayi teknikleriyle birleştirmek isteyen herkesi bu ailenin bir parçası olmaya davet ediyoruz.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Açık Pozisyonlar (Genel Başvuru)</h3>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;">Usta ve Kalfa (Tente, Demir-Doğrama ve Alüminyum Kesim)</li>
                <li style="margin-bottom: 0.5rem;">Sahada Görev Alacak Montaj Elemanları</li>
                <li style="margin-bottom: 0.5rem;">Makine Dikiş ve Branda Dikim Ustası</li>
                <li style="margin-bottom: 0.5rem;">Satış ve Müşteri Temsilcisi</li>
            </ul>
            <p style="margin-bottom: 3rem;">
                Eğer siz de bu büyüyen ailenin bir parçası olmak istiyorsanız, CV'nizi ve iletişim bilgilerinizi <strong>info@4mevsimbranda.com</strong> adresine iletebilir ya da iletişim numaralarımızdan bize ulaşabilirsiniz.
            </p>
""",
    "ticari-hesaplar": """
            <h2 style="margin-bottom: 1.5rem;">Ticari Hesaplar ve B2B Çözümler</h2>
            <p style="margin-bottom: 1.5rem;">
                4 Mevsim Branda olarak oteller, restoranlar, mimarlık ofisleri, inşaat firmaları ve peyzaj mimarları için özel <strong>B2B (İşletmeden İşletmeye) Kurumsal Çözüm Ortaklığı</strong> sunuyoruz. İşletmenizin dış alanlarını verimli ve şık bir şekilde kullanıma açarak müşteri kapasitenizi kışın ve yazın maksimize ediyoruz.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Ticari Hesap Olmanın Avantajları</h3>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;"><strong>Proje Bazlı Fiyatlandırma:</strong> Kurumsal iş ortaklarımıza, toplu veya büyük ölçekli alımlarda özel iskonto oranları ve toptan fiyatlandırma avantajı sağlanır.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Öncelikli Hizmet ve Montaj:</strong> İşletmelerin zaman kaybını önlemek için kurumsal projelerde özel planlama yapılarak "hızlı üretim ve gece montajı" gibi esnek çalışma saatleri sunulur.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Mimari Destek:</strong> 3D tasarımlar ve mimari projelerinize tam uyum sağlayan özel renklendirme (RAL kodlarına göre elektrostatik boya uygulamaları) ve kumaş seçimleri.</li>
                <li style="margin-bottom: 0.5rem;"><strong>Logo ve Markalama:</strong> İşletmenizin kurumsal kimliğine uygun olarak üretilen tentelerin üzerine profesyonel logo baskı uygulaması.</li>
            </ul>
            <p style="margin-bottom: 3rem;">
                Mekanınıza değer katan dev projelerde güvenilir iş ortağınız olmak için satış temsilcilerimizle randevu oluşturabilir ve işletmenize özel çözümleri keşfedebilirsiniz.
            </p>
""",
    "gizlilik-politikasi": """
            <h2 style="margin-bottom: 1.5rem;">Gizlilik Politikası</h2>
            <p style="margin-bottom: 1.5rem;">
                4 Mevsim Branda ("Şirketimiz"), müşterilerinin ve web sitemizi (www.4mevsimbranda.com) ziyaret eden kullanıcıların (“Kullanıcı”) kişisel verilerinin korunmasına büyük önem vermektedir. Bu gizlilik politikası, hangi verilerin toplandığını, nasıl kullanıldığını ve güvenliğinin nasıl sağlandığını açıklamaktadır.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Toplanan Veriler ve Kullanımı</h3>
            <p style="margin-bottom: 1.5rem;">
                Web sitemiz üzerinden doldurduğunuz iletişim formları aracılığıyla adınız, soyadınız, telefon numaranız, e-posta adresiniz ve projenizle ilgili detaylar talep edilebilir. Bu veriler yalnızca şu amaçlarla kullanılır:
            </p>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;">Sizlere ücretsiz keşif fırsatı sunmak ve teklif hazırlamak</li>
                <li style="margin-bottom: 0.5rem;">Müşteri destek ve satış sonrası onarım hizmetlerini yürütebilmek</li>
                <li style="margin-bottom: 0.5rem;">Kampanya, yenilik ve bakım hatırlatmaları hakkında sizleri bilgilendirmek</li>
            </ul>
            <p style="margin-bottom: 1.5rem;">
                <strong>Veri Paylaşımı:</strong> 4 Mevsim Branda, kişisel verilerinizi yasal zorunluluklar haricinde hiçbir 3. şahıs, kurum veya kuruluşla paylaşmaz, satmaz veya kiralamaz. 
            </p>
            <p style="margin-bottom: 3rem;">
                Web sitemizde standart web analiz araçları (Örn: Google Analytics) aracılığıyla, site trafiğini ölçmek adına tamamen anonim olarak çerezler (cookies) kullanılabilir. Siteyi kullanarak bu politikanın şartlarını kabul etmiş sayılırsınız. Kişisel verilerinizin silinmesi talebi için dilediğiniz zaman bizimle info@4mevsimbranda.com üzerinden iletişime geçebilirsiniz.
            </p>
""",
    "sartlar-kosullar": """
            <h2 style="margin-bottom: 1.5rem;">Şartlar & Koşullar</h2>
            <p style="margin-bottom: 1.5rem;">
                Bu web sitesini (www.4mevsimbranda.com) ziyaret eden veya hizmetlerimizden yararlanan tüm kişiler, aşağıdaki şartlar ve koşulları okumuş ve kabul etmiş sayılır.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Sözleşme ve Sipariş Süreçleri</h3>
            <p style="margin-bottom: 1.5rem;">
                Web sitesi üzerinden veya telefonla alınan bir fiyat teklifi, sadece bilgilendirme amaçlıdır ve bağlayıcı bir sözleşme niteliği taşımaz. Kesin sipariş, sahada alınan net ölçüler sonucunda, tarafların imzaladığı pro-forma fatura (veya sipariş fişi) ile geçerlilik kazanır. Ürünler müşterinin mekanlarına özel üretildiğinden (kişiye/alana özel üretim), cayma hakkı kapsamı dışındadır ve üretime başlandıktan sonra siparişin iptali gerçekleştirilemez.
            </p>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Ödeme ve Teslimat</h3>
            <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.5rem;">Aksi belirtilmedikçe, siparişin üretime alınması için mutabık kalınan ön peşinatın (kapora) yapılması gerekmektedir; kalan bakiye ise montaj/teslimat gününde tahsil edilir.</li>
                <li style="margin-bottom: 0.5rem;">Tarafımızca belirtilen teslimat/montaj süreleri (örneğin 10-15 iş günü), olağan şartlar için verilmiş olup, resmi tatiller, mücbir sebepler (doğal afetler, malzeme tedarik ağlarındaki küresel gecikmeler, vb.) hariç tutulur.</li>
            </ul>
            <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Telif Hakları</h3>
            <p style="margin-bottom: 3rem;">
                Bu web sitesinde yer alan 4 Mevsim Branda logoları, tasarım, metinler, grafikler ve projelere (referanslara) ait tüm fotoğraf ile görsellerin telif hakları 4 Mevsim Branda'ya aittir. Yazılı iznimiz olmadan kopyalanamaz, çoğaltılamaz ve izinsiz ticari mecralarda kullanılamaz.
            </p>
"""
}

for folder, html_content in content_map.items():
    file_path = f"/Users/atamantra/Desktop/branda/sayfa/{folder}/index.html"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the placeholder content
    new_content = re.sub(
        r'<div class="container"\s+style="max-width: 800px; margin: 0 auto; color: var\(--color-text\); line-height: 1\.8; font-size: 1\.1rem;">.*?</div>',
        f'<div class="container" style="max-width: 800px; margin: 0 auto; color: var(--color-text); line-height: 1.8; font-size: 1.1rem;">\n{html_content}        </div>',
        content,
        flags=re.DOTALL
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
print("Successfully generated detailed text for all 10 pages.")

