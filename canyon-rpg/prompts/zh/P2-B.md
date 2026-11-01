**美術優先相容規則（2026-11）：** 預設 P1-concept Blender 美術白模；P1-playable 為可選，不能阻擋 P2–P5 美術。舊文中要求 P1 可走、角色、NavMesh、通路淨空的句子，僅在使用者明確選擇 playable 才適用；純美術模式標記 NOT APPLICABLE。應保留 P1-concept 的地形與固定 45°／左右三鏡頭，P2 Godot 視覺與材質測試仍應按要求實測。

# P2-B — 在 Godot 完成中央瀑布的高品質視覺樣板

你是 Blender 程序化環境美術與 Godot 即時渲染技術美術師。

## 必讀教學
Cyberpunk City（比較建模途徑、Blender 精準幾何搭配生成材質）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

Mountain（Blender Python 樹木建模、小場景測試、渲染審查迴圈）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

需要時直接遠端閱讀，不預設已 Clone 教學倉庫。

## 工作範圍
僅中央大瀑布、上方木橋、左右岩壁、小段河流／深潭、**三棵**樹木原型及少量草石，不裝飾整張地圖。

## 實作
1. 保留 P1 已確認的地形、通行與相機，只精修可單獨測試的中央場景。
2. 比較 A 已有且經授權的生成式 3D 道具（若有）、B Blender 精確幾何＋程序化材質、C Blender 幾何＋生成圖片貼圖。在相同 Godot 光照和鏡頭下比對造型、材質、可編輯性、面數及成本。未核准點數不得使用付費生成。
3. 以版本化 Blender Python 製作精準橋梁與岩石；製作可平鋪、沒有固定陰影的岩石、苔蘚、泥土、草地、木紋 Base Color，並適當產生 Normal/Roughness 和濕潤污漬遮罩。
4. 先製作恰好三棵不同形狀的樹，測試樹幹／主要枝條、樹冠、烘焙葉片平面或低面數葉片、Texture Atlas 與自然微幅風動；同時觀察單棵及小組合效果。
5. 使用 Godot Shader 製作河面方向動畫，瀑布獨立用流水 Mesh、UV 動畫、衝擊泡沫和少量水霧。加入自然陽光、柔和陰影、適度空氣感。
6. 持續進行建構 → 真正 Godot 渲染 → 固定鏡頭截圖 → 比對參考圖和 Style Bible → 定位失敗處 → 僅修正失敗項，保留前後圖。
7. 從多視角檢查背面破洞、穿模、UV 接縫、透明排序與碰撞。

## 交付與驗收
可運行 Godot 視覺樣板、Blender 原始腳本／Blend／GLB、貼圖、Shader、三棵樹比較、A/B/C 比較（能測時）、真正 Godot 截圖，以及 reports/P2B_vertical_slice.md。以 Godot 即時效果為準，單靠 Blender 離線渲染不算通過。此階段不大量建模。