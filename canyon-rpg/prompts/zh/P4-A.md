# P4-A — 以離線流場驅動 Godot 河流和瀑布

你是數值環境模擬與 Godot 水體 Shader 工程師。

## 必讀 Mountain 教學
離線河床方格、水深與流向、Cache、Godot 渲染、瀑布獨立處理：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

請直接存取遠端完整相關段落，不預設本地已有逐字稿。

## 輸入
已核准的 Water Flow Graph、河床幾何、高程、河道寬度、瀑布落差、既有 Godot 場景與目標圖片；不得破壞先前驗收的地形與通行。

## 實作
1. 以可重建的格網或等效資料表示河流、深潭與障礙，存河床高度、水位／深度、流向向量、相對流速、邊界／障礙及有效格。
2. 實作穩定、適當簡化的**離線**流動計算，從已知上游輸入，符合高低差、深潭、匯流與出口。
3. 以乾河床開始或同等方法測試重複性，證明上游到下游連通、流向合理、繞開障礙、計算結果穩定。無法證明完整物理正確時，明確說明只是近似。
4. 將水深、流向資料保存為 Godot 可載入的 Flow Atlas／Cache，不在每幀重新計算整條河流。
5. Godot Shader 根據 Cache 控制水面 UV、細浪、深淺顏色、透明度、岸邊泡沫與相對流速。
6. **瀑布單獨建構**流水片 Mesh、落下軌跡、UV 動畫、衝擊泡沫與需要的水霧粒子；上下游相接自然。
7. 在 Godot 上游、急流、深潭、下游各點實際截圖與核對流向，遵守原圖美術風格。
8. 記錄指定硬體／渲染模式下的記憶體及 Shader 效能。

## 交付
可重複執行的 Python 離線水流工具、資料格式與 Cache、Godot Shader、瀑布場景、測試樣例、真正引擎截圖、reports/P4A_water_system.md。附實測和 PASS / FAIL / ASSUMED / NOT RUN，不製作無關環境物件。