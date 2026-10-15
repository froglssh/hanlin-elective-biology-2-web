# -*- coding: utf-8 -*-
"""
選生二網頁＿new 單元圖片分離與 HTML 瘦身優化腳本
將 20 個單元 HTML 中的 base64 圖片抽出至 assets/<unit_code>/ 靜態檔案，
將原本 217 MB 的單檔 HTML 集合瘦身至 2~3 MB，達成秒開效能。
各單元原檔備份於各章節資料夾中，絕不異動各章節內部檔案。
"""
import os, sys, re, json, base64, glob

TARGET_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_ROOT = os.path.join(TARGET_DIR, "assets")

def sanitize_filename(name):
    return re.sub(r'[^\w\.\-]', '_', name)

def get_ext(header):
    if "webp" in header: return ".webp"
    if "png" in header: return ".png"
    if "jpeg" in header or "jpg" in header: return ".jpg"
    if "svg" in header: return ".svg"
    if "gif" in header: return ".gif"
    return ".webp"

def extract_unit_code(filename):
    # 例如: 1-1_生源論戰法庭_質感新版_優化版.html -> 1-1
    # 活動2-1_植物組織觀察站_質感新版_優化版.html -> lab2-1
    m = re.match(r"^(活動)?(\d+-\d+)_", filename)
    if m:
        is_lab, code = m.group(1), m.group(2)
        return f"lab{code}" if is_lab else code
    return filename.split("_")[0]

def process_file(fpath):
    fname = os.path.basename(fpath)
    unit_code = extract_unit_code(fname)
    unit_assets_dir = os.path.join(ASSETS_ROOT, unit_code)
    os.makedirs(unit_assets_dir, exist_ok=True)

    orig_size = os.path.getsize(fpath)
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()

    decoder = json.JSONDecoder()

    # 1. 處理 ASSETS
    idx_assets = c.find("const ASSETS")
    if idx_assets == -1:
        print(f"[SKIP] No const ASSETS found in {fname}")
        return
    brace_assets = c.find("{", idx_assets)
    assets_obj, end_assets = decoder.raw_decode(c[brace_assets:])
    abs_end_assets = brace_assets + end_assets

    # 2. 處理 SLIDES
    idx_slides = c.find("const SLIDES", abs_end_assets)
    if idx_slides == -1:
        print(f"[SKIP] No const SLIDES found in {fname}")
        return
    brace_slides = c.find("{", idx_slides)
    slides_obj, end_slides = decoder.raw_decode(c[brace_slides:])
    abs_end_slides = brace_slides + end_slides

    # 抽取 ASSETS 圖片
    new_assets = {}
    saved_assets = 0
    for k, v in assets_obj.items():
        if isinstance(v, str) and v.startswith("data:image/"):
            hdr, b64 = v.split(",", 1)
            ext = get_ext(hdr)
            img_fname = f"{sanitize_filename(k)}{ext}"
            tpath = os.path.join(unit_assets_dir, img_fname)
            with open(tpath, "wb") as of:
                of.write(base64.b64decode(b64))
            new_assets[k] = f"assets/{unit_code}/{img_fname}"
            saved_assets += 1
        else:
            new_assets[k] = v

    # 抽取 SLIDES 圖片
    new_slides = {}
    saved_slides = 0
    for k, v in slides_obj.items():
        if isinstance(v, str) and v.startswith("data:image/"):
            hdr, b64 = v.split(",", 1)
            ext = get_ext(hdr)
            img_fname = f"{sanitize_filename(k)}{ext}"
            tpath = os.path.join(unit_assets_dir, img_fname)
            with open(tpath, "wb") as of:
                of.write(base64.b64decode(b64))
            new_slides[k] = f"assets/{unit_code}/{img_fname}"
            saved_slides += 1
        else:
            new_slides[k] = v

    new_assets_str = json.dumps(new_assets, ensure_ascii=False)
    new_slides_str = json.dumps(new_slides, ensure_ascii=False)

    # 由後往前替換避免 offset 偏移
    c_new = c[:brace_slides] + new_slides_str + c[abs_end_slides:]
    c_new = c_new[:brace_assets] + new_assets_str + c_new[abs_end_assets:]

    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(c_new)

    new_size = len(c_new)
    red = (1 - new_size / orig_size) * 100
    print(f"[{unit_code:6s}] {orig_size/1024/1024:5.2f} MB -> {new_size/1024:5.1f} KB (節省 {red:4.1f}%) | 圖片: {saved_assets + saved_slides:3d} 張")
    return orig_size, new_size, saved_assets + saved_slides

def main():
    print("=== 開始選修生物2【選生二網頁＿new】圖片抽離與秒開優化 ===")
    pattern = os.path.join(TARGET_DIR, "*_優化版.html")
    files = sorted(glob.glob(pattern))
    print(f"找到 {len(files)} 個單元檔案需處理。\n")

    total_orig = 0
    total_new = 0
    total_imgs = 0

    for f in files:
        res = process_file(f)
        if res:
            orig, new, imgs = res
            total_orig += orig
            total_new += new
            total_imgs += imgs

    print("\n" + "=" * 60)
    print(f"總計 HTML 體積: {total_orig/1024/1024:.2f} MB -> {total_new/1024/1024:.2f} MB (總共節省 {(1-total_new/total_orig)*100:.1f}%)")
    print(f"總計抽出圖片檔: {total_imgs} 張 WebP 靜態圖片")
    print("=== 全部優化完成 ===")

if __name__ == "__main__":
    main()
