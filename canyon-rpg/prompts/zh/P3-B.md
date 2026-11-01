# P3-B — 可編輯資產製作與局部修改

身份：Blender 資產建模工程師。使用已核准的 P3-A 清單與 P2 風格規格，**只製作真正需要的物件**。

1. 依形體選擇建模技術，使用穩定 asset_id／art_id／art_owner／art_revision，保留原始可編輯模型與版本化匯出。
2. 先單獨建立代表性資產並置入實際使用情境比對，驗證主要輪廓與連接後再建立變體。
3. 需要大量重複時，可用 Shared Mesh、Collection Instances 或 Geometry Nodes 等程序化方法，保留種子與位置清單；預設不把所有實例 Realize，也不假設實例化沒有渲染成本。
4. 分開統計來源網格、求值後實例和實際可見幾何；效能與 LOD 以目標平台和核准鏡頭評估，不能套用固定通用數值。
5. 依實際輸出要求檢查軸向、尺寸、Pivot、法線、UV、材質、接縫及匯入格式；無需要的規格標 NOT_APPLICABLE。
6. 既有生成模型僅在來源／授權／尺度與形體檢查後使用；沒有明確許可不得使用付費服務。
7. 使用 `blender/scripts/art_idempotent_geometry.py` 進行受控局部 Mesh 替換，記錄變更原因與受影響視圖，不重建其他核准內容。
8. 只有選取 P1-playable 才進行資產碰撞與互動測試。

交付來源模型、需要的生成腳本、資產 Manifest、真實樣板渲染、實例量測與 `reports/P3B_asset_kit.md`。
