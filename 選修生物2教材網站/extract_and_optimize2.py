# -*- coding: utf-8 -*-
"""
抽取選修生物2教材網站 20 個單元 HTML 中的 base64 圖片至獨立 WebP 靜態檔案，
將原本 5~36 MB 的單檔 HTML 瘦身為 50~150 KB 的極速秒開網頁。
"""
import os, sys, re, json, base64, glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def sanitize_filename(name):
    return re.sub(r'[^\w\.\-]', '_', name)

def get_ext_from_header(header):
    if "png" in header: return ".png"
    if "jpeg" in header or "jpg" in header: return ".jpg"
    if "gif" in header: return ".gif"
    if "svg" in header: return ".svg"
    return ".webp"

def process_folder(folder_name):
    folder_path = os.path.join(BASE_DIR, folder_name)
    filepath = os.path.join(folder_path, "index.html")
    if not os.path.exists(filepath):
        return

    orig_size = os.path.getsize(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m_img = re.search(r"const\s+IMG\s*=\s*(\{.*?\});", content, re.DOTALL)
    if not m_img:
        print(f"[WARN] No const IMG found in {folder_name}/index.html")
        return

    assets_dir = os.path.join(folder_path, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    raw_img = json.loads(m_img.group(1))
    new_img = {}
    saved_count = 0

    for k, v in raw_img.items():
        if isinstance(v, str) and v.startswith("data:image/"):
            header, b64 = v.split(",", 1)
            ext = get_ext_from_header(header)
            lower_k = k.lower()
            if lower_k.endswith((".webp", ".png", ".jpg", ".jpeg", ".gif", ".svg")):
                img_name = sanitize_filename(k)
            else:
                img_name = f"{sanitize_filename(k)}{ext}"
            
            target_path = os.path.join(assets_dir, img_name)
            with open(target_path, "wb") as img_f:
                img_f.write(base64.b64decode(b64))
            
            new_img[k] = f"assets/{img_name}"
            saved_count += 1
        else:
            new_img[k] = v

    new_img_str = f"const IMG = {json.dumps(new_img, ensure_ascii=False, indent=2)};"
    new_content = content[:m_img.start()] + new_img_str + content[m_img.end():]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    new_size = os.path.getsize(filepath)
    reduction = (1 - new_size / orig_size) * 100
    print(f"[{folder_name:8s}] {orig_size/1024/1024:6.2f} MB -> {new_size/1024:6.1f} KB (節省 {reduction:5.1f}%) | 圖片抽出: {saved_count:3d} 張")

def main():
    print("=== 開始選修生物2 單元網頁瘦身優化 ===")
    folders = sorted([
        d for d in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, d)) and os.path.exists(os.path.join(BASE_DIR, d, "index.html"))
    ])
    total_orig = 0
    total_new = 0
    for f in folders:
        fp = os.path.join(BASE_DIR, f, "index.html")
        total_orig += os.path.getsize(fp)
        process_folder(f)
        total_new += os.path.getsize(fp)

    total_red = (1 - total_new / total_orig) * 100 if total_orig else 0
    print("=" * 60)
    print(f"總計 HTML 體積: {total_orig/1024/1024:.2f} MB -> {total_new/1024/1024:.2f} MB (總共節省 {total_red:.1f}%)")
    print("=== 全部優化完成 ===")

if __name__ == "__main__":
    main()
