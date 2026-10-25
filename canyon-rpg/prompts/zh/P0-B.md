# P0-B — 建立並驗證可直接交給 Blender / Godot 的藍圖資料

你是程序化關卡工具與資料驗證工程師。

## 必讀來源
Cyberpunk City 的俯視規劃與尺寸白模：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md

需要時直接閱讀遠端逐字稿，不假設已經 Clone 倉庫。

## 輸入
使用者提供的參考圖、已驗收 P0-A 空間規劃（檔案或文字），以及目前工作目錄。若沒有 P0-A 規劃，應明確列為缺失，不得自行冒充已核准內容。

## 實作
利用 Python、NumPy、Pillow、SVG、JSON 或同等工具建立：
1. blueprint/scene_blueprint.json：唯一 ID、世界範圍、座標轉換、單位、平台高程與不確定性。
2. blueprint/layout_topdown.png：有公尺比例尺、網格軸、平台、懸崖、河流、橋梁、階梯與標註的真正俯視圖。
3. blueprint/heightmap_16bit.png：**真正單通道 16-bit** 高度圖，附最小／最大 Y 的映射說明，不是 8-bit RGB 假圖。
4. blueprint/cliff_edges.json：陡峭、垂直、懸挑岩壁的獨立邊界及高度資料。
5. blueprint/water_graph.json：流向、節點坐標、瀑布、落差與匯流關係。
6. blueprint/navigation_graph.json：可走平台、移動方式、橋梁／樓梯端點、可達性、封閉邊界。
7. blueprint/camera.json：Godot 可用的相機變換、正交尺寸、裁切與構圖地標。

所有輸出必須共用相同坐標、單位與 ID，不得默默改寫已確認的規劃。

## 自動驗證
製作可重複使用的 Python 測試，檢查：檔案存在、JSON 正確、單位一致、ID 不重複、Graph 引用有效、高度圖位深確實為 16-bit、高度映射、瀑布向下、橋梁接合、道路可達、坐標範圍、相機合理，以及地標是否完整。能產圖時提供預覽與疊合比對。

## 交付與驗收
輸出所有真實檔案、生成和測試腳本、預覽，以及 reports/P0B_validation.md。標記 PASS / FAIL / ASSUMED / NOT RUN，附實際命令和錯誤。P0 驗收前不得開始 P1。