import re

posts = {
    "mugla-kavurucu-sicaklarinda-serin-teraslar": "mugla_serin_teras.png",
    "fethiye-marina-tekne-golgelendirme-sistemleri": "marina_tekne_branda.png"
}

index_path = "/Users/atamantra/Desktop/branda/blog/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

for slug, new_img in posts.items():
    post_path = f"/Users/atamantra/Desktop/branda/blog/{slug}.html"
    try:
        with open(post_path, "r", encoding="utf-8") as pf:
            p_content = pf.read()
        
        # Replace hero image src in the post
        p_content = re.sub(r'<img src="\.\./[^"]+" (alt="[^"]*" class="article-hero-img")', rf'<img src="../{new_img}" \g<1>', p_content)
        
        with open(post_path, "w", encoding="utf-8") as pf:
            pf.write(p_content)
    except Exception as e:
        print(f"Skipping {slug}: {e}")

    # Replace image src in the index loop
    pattern = rf'(<a href="{slug}\.html".*? <div class="blog-img-wrapper">\s*<img src="\.\./)[^"]+(" alt="[^"]*" loading="lazy")'
    content = re.sub(pattern, rf'\g<1>{new_img}\g<2>', content, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated duplicated post image references.")
