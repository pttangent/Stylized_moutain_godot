# P0-A — 將風格化峽谷參考圖轉換成可探索的三維空間藍圖

你是專業 3D RPG 關卡設計師與環境空間規劃師。

## 必讀教學
閱讀 Can It Code 的 Cyberpunk City 完整時間戳逐字稿：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

特別研究俯視關卡規劃、簡單方塊建立空間與玩家尺度驗證。請直接開啟遠端連結，不預設逐字稿存在本地。

## 目標
把使用者提供的場景圖片轉換成真實可建立、可探索且具有統一坐標的三維世界規劃。圖片是視覺目標，不是精確施工圖，也不能直接得知遮擋區域的幾何。

## 執行
1. 盤點所有主要地形平台、懸崖、河道、瀑布、深潭、橋梁、樓梯、步道與地標，分配穩定 ID 與圖片相對坐標。
2. 區分畫面直接可見、合理推測和完全未知的部分，記錄信心與假設。
3. 建立真正的俯視布局，不是透視拉伸原圖。
4. 採用 Godot Y-up，X/Z 為水平、Y 為高度，1 unit = 1m。可暫以 96×64m、1.6m 測試角色估算尺度，但必須能根據證據修正。
5. 規劃平台範圍、相對高程、岩壁邊界與高度轉換；懸挑岩壁不應完全依賴 Heightmap。
6. 建立有方向的 Water Flow Graph，包含水源、河段、匯流、瀑布落差、深潭與下游出口。
7. 建立 Navigation Graph，標註可走平台、階梯、木橋、封閉邊界、主線與支線，檢查橋梁端點及路線連通。
8. 設定約 45° 俯視的固定 RPG 相機，優先正交、16:9、不見地平線；列出坐標、朝向、Ortho Size、裁切距離與地標對齊。
9. 遮擋區不能為了輸出漂亮數值就宣稱已精確還原。

## 交付
- blueprint/scene_blueprint_draft.json
- 帶比例尺與座標的真正俯視規劃圖；若無法產圖則給完整向量與坐標規格
- 平台高度表、岩壁邊界
- 水流與通行拓撲
- 相機規格
- reports/P0A_spatial_analysis.md，區分 OBSERVED / INFERRED / UNKNOWN 並記錄信心

工具允許時直接產生檔案，否則如實標記未建立的檔案並提供可讓程式執行的規格。不要開始建模。