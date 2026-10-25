# P3-B — Blender 程序化模組庫與選擇性 Tripo 建模

你是 Blender 程序化遊戲資產與輸出管線工程師。

## 必讀教學
Modular Village（真實尺寸、網格接合、人體通行、Smart UV、Texture Atlas）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md

Cyberpunk City（Blender 精確幾何＋AI 材質、貼圖邊緣處理、模組拼接破壞測試）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

請閱讀遠端逐字稿與上下文，不預設已 Clone 教學專案。

## 輸入
P3-A 已核准資產清單與三視圖、P2 樣板和 Style Bible，以及既有 Blend／GLB。先盤點，再製作可重複生成的版本。

## 建模／匯出
1. Blender Python 產生直線／轉角／崖頂岩壁、河岸、橋板／橋墩、石階、欄杆、樹幹與指定擺件等參數化模組。
2. 轉出 Godot Y-up 時統一公尺尺度，清楚記錄 Pivot、Socket、朝向和接合面。
3. 尺寸、倒角、變體、材質應可修改；保留原始腳本與 Blend，每件模組獨立匯出 GLB。
4. 面數依螢幕佔比、使用頻率設定起始預算，記錄實際輸出三角形數，不把 Blender Face 數混同 Tris。
5. 建立正確 Normal、UV、共享材質／Texture Atlas 和簡單碰撞網格，不在 Base Color 內固定光照陰影。
6. 葉片需依 P2 已通過的風格選擇 Alpha Clip、葉片卡片、Atlas 或其他方式，並為 LOD／Instancing 做準備。

## 選擇性 Tripo
只在小型獨特擺件比程序化模型更有效率時才考慮圖生 3D。先確認 Studio/API 點數類型與當下價格，Studio 點數不等於 CLI 可用點數。**沒有明確批准不能花點數**。先做一個版本測試，不一次產生四款。匯入後檢查朝向、比例、拓撲、UV、碰撞、貼圖清晰度與面數；修復步驟要可重現。

## 故意破壞的測試
建立 Godot Asset Gallery，單獨與組裝展示。以程式檢查接合點、間隙、橋階淨空、UV 接縫、材質數量及碰撞；刻意把某模組錯位／轉向，證明驗證器能抓到錯誤。多角度檢查並讓 CharacterBody3D 實測通行。

## 交付
docs/asset_manifest.csv、Blender Python、Blend、獨立 GLB、Atlas、資產預覽、Godot 測試場景、模組驗證與 reports/P3B_asset_kit.md。報告 PASS / FAIL / ASSUMED / NOT RUN 及成本。模組尚未驗收前不做全地圖散布。