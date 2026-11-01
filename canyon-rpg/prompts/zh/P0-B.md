# P0-B — Blender 美術白模的空間藍圖

以已核准 P0-A 與原圖為準，建立可重現的結構化藍圖。舊版數值檢查通過不代表場景自然、漂亮或可行走。

1. blueprint/scene_blueprint.json：唯一地標 ID、來源像素、世界尺度和座標、Y-up 協定、修訂與信心標記。
2. blueprint/layout_topdown.png：有公尺比例尺、地形高差、主／次瀑布、河岸、深潭、岩壁輪廓與可選的美術路徑。
3. blueprint/heightmap_16bit.png：真正單通道 uint16，高度映射及採樣規格。**只表示大地形**，垂直岩壁、懸挑、瀑布面與橋樑另建 3D 幾何。
4. landform_zones.json、cliff_edges.json：緩坡／丘坡／陡坡／斷崖／河岸／瀑布唇口／水池等類別；檢查曲折、岩層與侵蝕形態，避免規則重複。
5. water_graph.json：明確的上游→瀑布→下方水池→出口及各段下降高差。
6. 依 atan(sqrt((dY/dX)^2+(dY/dZ)^2))（輸出度數），在約 0.5m、2m、5m 平滑尺度計算坡度分佈；有 blueprint/landform_slope_audit.py 時執行並保存影像和 JSON。**不能以 18° 全域限制直接判定地形 FAIL。** 只有明確指定的普通步道可參考坡度上限。
7. 分離來源相機、45° 主構圖相機及兩側檢查鏡頭，留下鏡頭變換、投影範圍與地標畫面座標。
8. 新 Tripo 小模型若確實存在，必須保留 raw 座標、尺度與不確定性；找不到就採圖片導向，不得擅自替換來源。歷史資料只能在新修訂中附差異。
9. navigation_graph.json 可以選擇保留為 ART_ROUTE_INTENT_ONLY；無需 Godot、碰撞、NavMesh 或 CharacterBody3D 便可完成 P0。

交付可重跑生成器、藍圖、視角與剖面圖、坡度稽核及 reports/P0B_art_validation.md。記錄 PASS／FAIL／ASSUMED／NOT RUN。完成後預設進 P1-concept。
