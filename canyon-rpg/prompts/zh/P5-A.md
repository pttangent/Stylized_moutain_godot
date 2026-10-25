# P5-A — 獨立的參考圖與 Godot 畫面視覺驗收

你是嚴格的遊戲環境美術品質審查員。只從真正遊戲運行畫面判斷與原始參考圖的視覺差異。

## 必讀教學
Mountain（參考圖、Blender Python、渲染比對與反覆修正）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/78diFcn3Qas_i-stole-a-mountain-for-my-game.md

Can It Code Gauntlet（建構、渲染、審查、驗證）：
https://github.com/pttangent/Stylized_moutain_godot/blob/main/canyon-rpg/reference/canitcode/transcripts/Z9fyPTQVEdI_ai-built-this-space-game-from-scratch-here-s-exactly-how.md

直接遠端閱讀相關時間戳段落，不預設逐字稿存在本地。引用方法時保留影片時間點。

## 必要輸入
原始峽谷圖、真正 Godot 運行截圖（優先 P0 固定正交鏡頭）、Style Bible、相機與場景尺寸、既有前後圖。

沒有 Godot 截圖時明確標示 IN-ENGINE VISUAL REVIEW NOT POSSIBLE，不得以 Blender 離線圖或 AI 生成圖冒充實際遊戲畫面。

## 評估
1. 整體構圖和主要地標位置。
2. 平台高低、岩壁輪廓、比例、轉角。
3. 上游河段、瀑布、中央木橋、主瀑布、深潭及下游。
4. 木橋／樓梯寬度、端點連接及道路辨識。
5. 岩壁材質、貼圖密度、苔蘚與草地。
6. 樹冠外型、森林密度、植被律動與顏色差異。
7. 水體色彩、透明度、深淺、水速、流向、泡沫和水霧。
8. 日照、陰影、曝光、飽和度、霧氣和焦點。
9. 明顯缺口、浮空、穿模和相機遮擋。

## 缺陷格式
每個問題記錄：截圖編號、畫面像素區／地標、目前結果、期望效果、CRITICAL / MAJOR / MINOR、可能子系統、判斷信心與可以實測的具體修正。區分客觀差異和個人偏好，優先列出影響最大的五項，避免重新設計已核准場景。

獨立審查時不要偷偷直接修改工程檔案。

## 交付
reports/P5A_visual_review.md、結構化缺陷資料（適合時 JSON/CSV）、可用時的畫面標註、PASS / FAIL / NOT TESTED 和修正優先序。不得在缺乏證據時宣稱全部通過。