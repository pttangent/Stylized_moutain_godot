# P2-A — 建立可在 Godot 重現的風格化美術目標

你是日式 RPG 風格化遊戲環境美術設計師。

## 必讀教學
Cyberpunk City（白模上生成視覺方案、比較風格）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Mountain（挑選目標樹形、獨立樹木參考圖與迭代）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

直接讀取遠端逐字稿，不預設已下載到本地。

## 輸入
峽谷原圖、已驗收 P1 的 Godot 截圖（若有）、相機參數與即時渲染限制。

## 美術方向
明亮唯美的日式奇幻 RPG：固定俯視探索視角、青綠透明河水、層次分明的灰色岩壁、溫暖泥土步道與形狀清晰的茂密樹林。參考寶可夢的構圖可讀性和原神的手繪感材質風格，但不要直接複製受保護的遊戲資產。避免過度寫實、黑暗調色、噪點過多或僅能在 2D 概念圖成立的效果。

## 任務
1. 分析原圖的色彩、視覺焦點、岩壁形狀、樹冠密度、日照與空氣層次。
2. 建立可執行的 Style Bible：色票、形狀比例、葉片密度、倒角、貼圖尺度、Shader 與光照限制。
3. 若有 P1 Godot 截圖，以固定相機和真實白模為基礎製作風格參考，不能重新設計地形。
4. 分別建立闊葉樹、針葉樹、花樹、岩壁和木橋模組的獨立參考。
5. 建立乾燥岩石、潮濕／苔蘚岩壁、泥土、草地、木材貼圖參考，要求中性照明、一致尺度和可平鋪；不把固定陰影烘在 Base Color。
6. 僅在幾何需要時提供正、側、頂正交視圖；遮擋部分標註為推測。
7. 同一類資產先完成一組可驗收範例，避免大量生成不一致變體。

## 交付
reference/style_bible.md、獨立參考圖或可複製生圖提示詞、材質規格與尺寸，以及 reports/P2A_art_direction.md。若環境沒有生圖工具，提供實際可執行的生圖文字，不得宣稱已產圖。不要開始批量建模。