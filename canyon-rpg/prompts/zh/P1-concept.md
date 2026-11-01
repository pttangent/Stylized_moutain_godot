# P1-concept — Blender 優先的自然場景美術白模（預設）

身份：風格化 RPG 自然環境美術總監、Blender 程序化地形與雕塑工程師。任務是**真正製作可編輯 Blender 3D 白模**，不是只畫 2D 概念圖，也不是做可行走關卡。

## 輸入
讀取原始參考圖、最新 P0-A/B 或修訂、既有高度圖、水流／岩壁／地貌類別、相機參數與坡度分析；不可把 P0 數值檢查通過解釋成完成 3D 場景驗收。保留人為核對的地標 ID 和原始標註，所有更動建立獨立 P1 修訂。新提供 Tripo 小型模型只可當可選形體候選參考，不能直接變成準確地面；若缺少就用原圖與 P0 美術假設製作。

規定：儲存的設計座標採 Godot Y-up（X/Z 水平），Blender 本機建模 Z-up；確保右手座標轉換 Blender(X,Y,Z)=(Godot X,-Godot Z,Godot Y)，匯出 glTF 時檢查地標位置，不可重複變換。編寫可重跑 Blender Python，保留 .blend；MCP 不是必要條件。

## C1 宏觀地貌與構圖
1. 先建大型階地、河谷切面、左右高低不齊的岩壁、瀑布落差、深潭及下游河床。高度圖只是粗略地形起點，**不要直接照搬舊版長斜坡、細窄水溝與直線岩壁**。
2. 明確建立上游→各層瀑布唇口→落水面→接水池→下游河道的三維空間關係。垂直岩壁與懸挑另外建 Mesh，不用 Heightmap 偽裝。
3. 先安排主瀑布和水池為視覺焦點，木橋、上方瀑布與前景轉彎為次焦點。重視前中後景、輪廓、深度、留白和遮擋。
4. 暫時只用材質 ID 的 clay 白模，不加樹、草、噪聲微細節、正式 Shader。立刻從固定 45° 鏡頭真實渲染，再依照原圖修改宏觀形體。

## C2 中觀地貌
5. 雕刻有地貌原因的不規則河岸、岩層平台、崖腳、岩石塊和水池深度。避免高度相同、垂直切面等距、河流寬度一致、兩岸鏡像與隨機噪聲堆砌。
6. 水面和瀑布獨立成物件，水位必須按地勢下降，每段有唇口和承接盆地。
7. 原圖步道／階梯／橋可作美術示意，**不用通行寬度、18° 限制或 NavMesh**；不得為了連通而把自然岩壁削平。
8. 參考 P0 地形分區，在約 0.5／2／5 公尺尺度查看坡度分佈與形體轉折；陡坡、岩壁超過 18° 並不是錯誤。
9. 逐階段產出實際 Blender 截圖並修正。每個改動的高信心地標要寫明原因、舊值／新值。

## C3 相機、QA 和交付
10. 建立 CAM_HERO_45（16:9、約45°、近正交）、CAM_ALT_LEFT、CAM_ALT_RIGHT、CAM_TOP_ENGINEERING，以及可選來源比對相機。來源相機與正式遊戲相機分開。
11. **真實渲染至少三張固定鏡頭**，補上頂／前／側三視圖。每張保留相機參數、畫面尺寸與地標標註；只有同一套三維幾何，不能每張重建不同場景。
12. 檢查岩壁與地形接縫、懸挑底面、瀑布斷口、漂浮幾何、水面穿插、河岸自然度和多鏡頭一致性。
13. 地形、岩壁、水體、步道示意、道具白模、相機分組保存，不可合併為一個不可編輯的巨大模型。保留固定種子與生成腳本。
14. 報告所有可見失敗的鏡頭 ID、畫面區域、原因、修正方案與 before/after；確實執行過才能標 PASS。

交付 blender/scripts/build_p1_concept.py、blender/source/p1_concept.blend、blender/renders/p1_concept/ 的主鏡頭／左右鏡頭及三視圖、blueprint/p1_art_revision.json、reports/P1_concept.md（PASS／FAIL／ASSUMED／NOT RUN）。

**P1_CONCEPT_ART_APPROVED** 僅表示地貌、構圖和形體已通過美術驗收，不表示可行走。不開始碰撞、Godot NavMesh、正式材質、植被或付費生成；P2 可以直接接續。

## L1／L2／L3 分層建模及局部修正（新增）
L1 對應 C1：先完成宏觀山體、峽谷、瀑布階地、主水池及真正的 45° 白模渲染。L2 對應 C2：再建立獨立岩層、懸挑、崖腳、河岸侵蝕與地形接縫，重渲主鏡頭、左右鏡頭。L1／L2 的錯誤不能靠樹木草叢遮擋。L3 植被與小石頭延後 P3／P4，不是 P1-concept 必做項目。

讀取真正的 blueprint/reference_geometry_contract.json；缺少時提出版本化草案並標示 P0 交接未完成，不能把 example 當成已核准文件。地貌 Mesh 標記 obj["art_id"]、obj["art_owner"]、obj["art_revision"]，地標以獨立 Empty 的 art_id 對應 anchor_art_id，放在真實要核對的表面位置，而非隨便取物件中心。

**禁止局部修正時重建整個場景。** 修改前記錄 change_scope、受影響 art_id、版本、seed、地標／鏡頭依賴。使用 blender/scripts/art_idempotent_geometry.py 僅替換目標 Mesh data，保留 Transform、Parent、Collection 與其他已核准物件，保留舊 Mesh 作為可回復版本，不做全場 purge 或不受控 .001 重複物件。將改動記錄到 blueprint/p1_art_revision.json 並保存 before/after；未改鏡頭可沿用有來源的舊證據，不能偽稱新測量。

建立相機和 Anchor 後執行 blender -b blender/source/p1_concept.blend --python blender/scripts/p1_visual_layout_validator.py -- --contract blueprint/reference_geometry_contract.json --out reports/P1_layout_validation.json；可用 --features、--shots 聚焦變更範圍。它只檢查 world_to_camera_view 投影與初步 raycast 遮擋候選，不是正式渲染、美術輪廓驗收或角色碰撞。SCREEN_POSITION_UNSPECIFIED／NOT_RUN／OCCLUSION_CANDIDATE 都不算 PASS。最終仍須主／左右三鏡頭真實 Blender 白模對照圖。
