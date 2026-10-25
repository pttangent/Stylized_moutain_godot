# P0-B 空間設計藍圖 — Marble 1.1 瀑布峽谷

日期：2026-10-26。狀態：**設計數值 Gate PASS；Godot 角色碰撞／實際畫面 Gate PENDING P1**。本階段只交付空間藍圖，未進入詳細 3D 建模。

## 交付

| 內容 | 檔案 | 用途 |
|---|---|---|
| 註冊、尺度、範圍與地標 | [`blueprint/scene_blueprint.json`](../blueprint/scene_blueprint.json) | Godot Y-up，1 unit = 1 m，保留每個原始 GLB 點和設計座標 |
| 俯視布局 | [`blueprint/layout_topdown.png`](../blueprint/layout_topdown.png) | 水流藍線、主路橙線、階地與分離懸崖 |
| 16-bit 高度資料 | [`blueprint/heightmap_16bit.png`](../blueprint/heightmap_16bit.png) | 768×960，0.125 m/pixel，bulk terrain；數值解碼範圍 -8 至 30 m |
| 設計語義遮罩 | [`blueprint/semantic_mask_design.png`](../blueprint/semantic_mask_design.png) | 地形、水床、路、橋、階梯、懸崖、植被保留區；**設計分區，非 GLB 語義真值** |
| 水流與路線 | [`blueprint/water_graph.json`](../blueprint/water_graph.json)、[`blueprint/navigation_graph.json`](../blueprint/navigation_graph.json) | 定向高差、路徑尺寸、階梯段數 |
| 懸崖與遊戲相機 | [`blueprint/cliff_edges.json`](../blueprint/cliff_edges.json)、[`blueprint/camera.json`](../blueprint/camera.json) | 懸崖需獨立碰撞；遊戲相機與原圖 PnP 相機分開 |
| 重建與驗證腳本 | [`blueprint/build_p0_design.py`](../blueprint/build_p0_design.py)、[`blueprint/validate_p0_design.py`](../blueprint/validate_p0_design.py) | 從保留的標註及 Marble 證據再生數值藍圖 |

## 採用尺寸

世界範圍 **96 × 120 m**；橋中點為 (0,0,0)。GLB 原始 −Y 為向上，GLB/SPZ 同用繞 X 180° 的翻轉。選擇橋左右落腳點水平跨度 **6.0 m**，原始量測為 0.2165015 Marble 單位，因此設計比例為 **27.71343 m／Marble 單位**。這是我根據構圖和角色通行需求選定的**遊戲尺度**，不是宣稱 Marble 具備真實公尺標定。Godot 座標轉換是 `27.71343 × (rawX−x0, −(rawY−y0), −(rawZ−z0))`。

尺寸決定：橋淨寬 **1.6 m**、主路 **1.8 m**、樓梯 **1.6 m**、欄杆 **1.1 m**；角色設計身高 **1.75 m**、碰撞半徑 **0.35 m**；階梯踏面 **0.32 m**、單級最大約 **0.175 m**。6 m 橋跨與 1.6 m 橋面形成 3.75:1 的細橋比例，接近原圖的長窄構圖；3 m 方案會使橋與瀑布落差過小。這是設計推論，不是從照片量出的實際物理尺寸。

參考尺寸來自 [U.S. Access Board 戶外步道指南](https://www.access-board.gov/aba/guides/chapter-10-outdoor/)（最低 0.915 m 通行淨寬，對架高木棧道建議約 1.525 m）、[U.S. Access Board 樓梯指南](https://www.access-board.gov/ada/guides/chapter-5-stairways/)（約 0.102–0.178 m 級高、踏面至少約 0.279 m）及 [FHWA 行人橋指南](https://www.fhwa.dot.gov/publications/research/safety/pedbike/05085/chapt9.cfm)（防墜欄杆約 1.1 m）。這些是尺度參考；本奇幻關卡沒有聲稱符合現實無障礙或工程法規。

## 高度與拓樸

Marble 用作可量測的**候選空間關係**。來源相機 25 點配準的 RANSAC 內點為 23，誤差中位數 19.3 px；使用者核對了 25 組點，但 `stream_lower` 與 `stair_left_upper` 的重投影偏差較大。原圖相機資料仍在 [`analysis/p0_marble_2026-10-26/registration`](../analysis/p0_marble_2026-10-26/registration/camera_registration_candidate.json)。遊戲相機另設約 45° 俯角、約 8.84° 偏航，正交高度 128 m；數值視框包含所有 25 個已核對點。

水流圖 8 條設計邊全朝下游降低，從遠端上游通到左下出口。中央主瀑布以兩個已標河沿的中點建立落水唇；唇到主池約 5.42 m 高差（分為兩段節點）。橋面至橋下水面相差約 1.22 m，尚未扣除橋板厚度。`exit_lower_left` 的設計點取原圖相機射線命中並微調，**未經使用者直接點選**，在 JSON 中標為假設。瀑布需獨立落水面與懸崖構件；高度圖不能表現垂直面或遮擋後的洞穴。

主路圖從右下起點經橋到左上階地連通，右支線從橋到右上階地連通。12 條路線邊都有設計寬度、端點高度與坡度；普通路段最大端點坡角 11.75°，低於本遊戲設定的 18° 普通路上限。三段指定階梯為左路 17 級、右下 16 級、右上 65 級（三段 22／22／21 級及平台）。右上這一段在原 GLB 的路線取樣曾有缺口，故 P0 設計明確要求**新建樓梯面及碰撞**，不能沿用 Marble collider 作玩家碰撞。

語義遮罩是設計者畫出的用途分區，**不是**將所有 GLB 三角面判為地面。樹冠、背景殼體、岩壁和水的原始幾何仍須在 P1 白模中分開處理。[Godot 導航文件](https://docs.godotengine.org/en/4.5/tutorials/navigation/navigation_using_navigationmeshes.html)也明確區分渲染、碰撞與 NavMesh，agent 半徑、最大攀爬和坡度需在烘焙時設定。這份導航圖驗證的是設計連通與尺寸，不是已烘焙、已通行的 NavMesh。

## 獨立檢查與未完成的實機驗收

執行 `python blueprint/build_p0_design.py` 後，執行 `python blueprint/validate_p0_design.py`：**17 PASS／0 FAIL**。檢查涵蓋位深和解析度、尺度／邊界、節點引用、水流正向與無環、兩條路線連通、普通路坡度、樓梯踏面／級高與路段長度、通行淨寬、橋水高差、25 個地標在圖幅內、相機數值視框及獨立懸崖資料。原標註後結構檢查 11 PASS／0 FAIL；原工作包單元與故障注入測試 16/16 通過。見 [`reports/P0_design_validation.json`](P0_design_validation.json) 和[前輪的審核紀錄](../analysis/p0_marble_2026-10-26/P0_SPATIAL_REVIEW.md)。

本機有 Godot 4.7.2；`Godot --headless --editor --path canyon-rpg --quit` 與 `Godot --headless --path canyon-rpg --quit-after 2` 均以 exit code 0 完成。這只驗證專案匯入與既有空場景啟動，**沒有 P0 Godot 截圖、CharacterBody3D 行走、NavMesh 烘焙、橋面碰撞或 GPU 性能數據**。`scene_blueprint.json` 是可實作的 P0-B 設計藍圖，`P0_B_DESIGN_COMPLETE_P1_PHYSICS_PENDING` 不是場景可玩性 PASS。P1 應依這些尺寸做白模，實際檢查三段階梯、橋面、斷崖邊及整條主路；在使用者批准 P0 前不推進 P1。

## 來源與改作界線

本次只使用既有 World Labs Marble 1.1 的 GLB/SPZ 與原始圖片，沒有重新生成世界，也沒有 Hunyuan。Can It Code 的 [模組尺寸一致與角色通行實測](https://www.youtube.com/watch?v=57QEdTgUC3c&t=149s)（影片 02:29–03:10、04:05–05:12）和 [路線曲線／地形分層](https://www.youtube.com/watch?v=78diFcn3Qas&t=235s)（03:55–04:25）提供工作流程參考；本藍圖的 6 m 橋跨、96×120 m 範圍、階高及所有節點座標均為本專案的工程設計，並非影片提供的數值。原始逐字稿可能有轉錄錯誤。
