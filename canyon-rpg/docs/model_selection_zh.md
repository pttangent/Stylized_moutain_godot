# Canyon RPG｜提示詞外的模型與工具分工

這份文件是**執行建議**，不是提示詞正文。提示詞內不指定其他開發助手名稱，不預設資料包已 Clone 到本地。模型是否可用、推理檔位名稱與訂閱限制，請依當前應用介面確認。

| 工作 | 首選執行環境／模型 | 推理 | 建議工具 | 成本控制 |
|---|---|---|---|---|
| 00 專案初始化 | Codex / GPT-6 Luna | Low | Git、Terminal | 基本檢查，不用強模型 |
| P0-A 空間分析 | Gemini 4 Argon | High | 圖片理解、資料推理 | 確實需要全局空間理解 |
| P0-B 藍圖產生 | Codex / GPT-6 Sol | Medium | Python、NumPy、Pillow | 先驗證 schema，難題再升 High |
| P1 3D 白模 | Claude Code / Opus 5.5 | Medium → High | Blender Python、Godot | 先以可走白模為目標 |
| P2-A 美術設計 | GPT-6 Astra | Medium | 圖片生成 | 確立單一可執行的視覺風格 |
| P2-B Godot 樣板 | Claude Code / Opus 5.5 | Medium | Blender、Godot Shader | 只精修中央瀑布與三棵樹 |
| P3-A 資產三視圖 | GPT-6 Luna | Low | 生圖工具 | 每類先一套合格視圖 |
| P3-B 模組建模 | Codex / GPT-6 Sol | Medium | Blender Python、可選 Tripo3D | 精確幾何優先 Blender |
| P4-A 水流計算 | Claude Code / Opus 5.5 | High | Python、Godot Shader | 多次卡關才提高至 Max |
| P4-B 世界組裝 | Codex / GPT-6 Sol | Medium → High | Godot Curve3D、MultiMesh | 以程序化批次替代手動擺放 |
| P5-A 視覺評估 | Gemini 4 Argon | High | 原圖與實際 Godot 截圖 | 只回報可定位、可修復的問題 |
| P5-B 效能驗收 | Codex / GPT-6 Sol | Medium | Godot Profiler、測試工具 | 以實測資料為準 |

## 教學取捨
- [Cyberpunk City](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/XqtnBlPJ6KE_is-this-really-ai-insane-opus-5-5-gamedev-workflow.md)：俯視布局 → 幾何白模 → Blender 精確幾何＋AI 表面材質；Tripo 用於少量裝飾。
- [Mountain](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md)：Blender Python 背景執行、Spline 道路、小測試場景、離線水深／流向與瀑布獨立處理。
- [Modular Village](https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/57QEdTgUC3c_stop-asking-ai-for-whole-houses-opus-5-5-tripo.md)：嚴格正交參考、模組尺寸、角色通行、Texture Atlas。
- 參考中文 Codex＋Blender 教學的節費方式：簡單正交圖用 Low、規格建模用 Medium、只有空間和演算法難題才 High／Max；面數依畫面重要性與效能決定。

## 注意
Studio credits 不能預設可用於 Tripo CLI/API。花費前先確認點數種類、估算單件成本並取得明確許可。模型命名及訂閱權限可能變動，因此以上只是路由推薦，非目前帳號權限證明。