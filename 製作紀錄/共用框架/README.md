# 優化版共用框架（CH1-3 起）

- `base.html`：單檔網頁模板（首頁四入口、圖解、練習、簡報、影片、診斷）。單元差異只在 `{{...}}` 文字欄位與 `content.js`。
- `gen_lib.py`：從課本 PDF 以 288dpi 裁圖（`crop`，可 `wipe` 塗掉圖外課文）、長框切半並排（`pair`）、以 PDF 文字層自動定位遮罩做貼標籤圖（`label`，並檢查槽位重疊）。
- `build_lib.py`：讀原網頁內嵌的 PPT 逐步畫面（統一改名 `sNN_MM`）、組裝單檔並 `node --check`。
- `t_layout.cjs`：七種視窗逐頁、逐張圖解、逐關版面稽核。`t_func.cjs`：真實 UI 作答與功能測試。
- 各單元資料夾：`unit.py`（裁圖設定與頁面文字）、`content.js`（圖解與題目）。重建：`python3 unit.py build`（需該單元課本 PDF 存為 `book.pdf`）。
