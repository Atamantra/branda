import re

updates = {
    "fethiye-kafe-restoran-tente-cozumleri": "isikli-tente.jpg",  # Already fine, but let's change gocek to new one
    "gocek-villalari-icin-biyoklimatik-pergola": "motorlu_pergola_gocek.png",
    "oludeniz-otellerinde-havuz-kenari-golgelendirme": "oludeniz_havuz_semsiye.png",
    "kavacik-rüzgarlarina-karsi-zip-perde": "zip_perde_kayakoy.png",
    "fethiye-cam-balkon-kapatma-fiyatlari-2026": "giyotin.jpg", # Fine
    "calis-plaji-isletmeleri-icin-mafsalli-tenteler": "mafsalli_tente_calis.png",
    "mugla-kavurucu-sicaklarinda-serin-teraslar": "tente_sistemleri.jpg", # Fine
    "fethiye-marina-tekne-golgelendirme-sistemleri": "hero2.png", # Fine
    "hisaronu-villalarinda-kis-bahcesi-keyfi": "kis_bahcesi_hisaronu.png",
    "fethiye-branda-semsiye-secim-rehberi": "branda_semsiye_fethiye.png"
}

# Update main index feed
index_path = "/Users/atamantra/Desktop/branda/blog/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

for slug, new_img in updates.items():
    # Update individual post files
    post_path = f"/Users/atamantra/Desktop/branda/blog/{slug}.html"
    try:
        with open(post_path, "r", encoding="utf-8") as pf:
            p_content = pf.read()
        p_content = re.sub(r'<img src="\.\./[^"]+" alt="[^"]+" class="article-hero-img"', f'<img src="../{new_img}" alt="{{title}}" class="article-hero-img"', p_content)
        # Note: we lost {title}, let's precise the regex
        
        # Better replace method, find the <img src="../xxxxx.png"
        p_content = re.sub(r'(class="article-hero-img" loading="lazy" onerror="this\.src=\'\.\./logo-futuristic\.png\'"\n\s*)*<img src="\.\./[^"]+"', f'<img src="../{new_img}"', p_content)

        with open(post_path, "w", encoding="utf-8") as pf:
            pf.write(p_content)
    except Exception as e:
        print(f"Skipping {slug}: {e}")

    # Update index feed
    # in index feed, the block looks like:
    # <a href="{slug}.html" ...
    #    ...
    #    <img src="../{old_img}"
    
    pattern = rf'(<a href="{slug}\.html".*?<div class="blog-img-wrapper">\s*<img src="\.\./)[^"]+(")'
    content = re.sub(pattern, rf'\g<1>{new_img}\g<2>', content, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated image references.")
