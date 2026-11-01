# P0-B — 將通用場景設計實體化為可驗證藍圖

根據 P0-A 真正的參考資料、場景 Profile 與核准的特徵設計，產生後續 Blender 可用的空間／視覺藍圖。不得自行添加場景物件。

1. 建立版本化 `scene_profile.json`、`blueprint/scene_blueprint.json` 或等效 Manifest；連結來源 ID、特徵 ID、幾何表示、單位、軸向、變換、約束及不確定性。
2. 依 `docs/REFERENCE_GEOMETRY_CONTRACT.md` 建立 `blueprint/reference_geometry_contract.json` v2。參考來源不一定是圖片；非圖片不要求像素座標，也不必虛構相機。
3. 只製作需要的空間資料：俯視圖、剖面圖、體積結構圖、關係圖、曲線、遮罩、網格、數值場等依實際需求取捨。沒有任何一種格式是所有場景都必備。
4. 若使用高度圖或其他採樣場，必須符合該幾何的維度與表示限制，紀錄單位、精度、映射及未知區。不得將無法單值表示的幾何強行壓入單張高度圖。
5. 針對場景真的包含的功能系統檢查拓撲、連接、比例、風格及物理約束；其他測試標記 NOT_APPLICABLE，不能以不相關測試阻擋美術。
6. 根據批准的構圖／交付需求建立真正需要的視圖，區分來源影像相機推測與製作相機。相機角度、投影與數量不能硬編碼。
7. 已提供的生成模型只當可檢查候選資料，保留原始座標、來源及可能錯誤，不預設服務商、精度或通行面。
8. 保留來源與核准版，變更另建版本、差異紀錄及可重跑生成腳本。

建立合同後，可執行 `python blueprint/validate_reference_geometry_contract.py blueprint/reference_geometry_contract.json --report reports/P0B_geometry_contract_validation.json`。它只驗證格式、ID 與依賴，不代表美術、幾何或可玩性通過。

交付藍圖、真正需要的視圖／資料、鏡頭規格、來源連結與真實驗證報告。完成後預設進 P1-concept。
