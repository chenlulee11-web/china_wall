# China Wall - 中華人民共和國歷史地圖與編年史

> 從中國共產黨建立 (1921) 至今，多國語言、多國視角的客觀歷史紀錄平台。
> 前後端分離架構 (Python FastAPI + 前端 SPA)

---

## 技術棧

| 層級 | 技術 | 狀態 |
|------|------|------|
| **後端框架** | Python FastAPI 0.115 | ✅ 完成 |
| **資料庫** | SQLite (SQLAlchemy 2.0 ORM) | ✅ 完成 |
| **爬蟲** | httpx + BeautifulSoup4 (Wikipedia API) | ✅ 完成 |
| **API 風格** | RESTful JSON | ✅ 完成 |
| **前端** | 靜態 SPA (待選框架) | ❌ 未開始 |
| **地圖** | 待整合 (Leaflet / Mapbox / Maplibre) | ❌ 未開始 |
| **時間軸** | 待開發 (vis-timeline / 自製) | ❌ 未開始 |
| **多國語系** | 繁中/英/日/韓 (排除簡中) | ✅ 部分完成 |

---

## 資料庫結構 (已完成)

### Event (主表)
| 欄位 | 型態 | 說明 |
|------|------|------|
| id | UUID | 主鍵 |
| date | Date | 事件日期 |
| date_end | Date | 結束日期 (區間事件) |
| date_precision | String | day / month / year |
| category | String | 分類 |
| tags | JSON | 標籤陣列 |
| importance | Integer | 0-100 重要程度 |

### 多語系關聯表 (已完成)
- **event_titles** — 多語言標題 (zh_tw/en/ja/ko)
- **event_descriptions** — 多語言描述
- **event_locations** — 地理座標 + 多語言地名
- **event_sources** — 參考來源 (含語言、可靠性評分)
- **event_perspectives** — 各國觀點 (country_code: TW/JP/KR/US/GB)
- **event_media** — 多媒體附件

---

## 爬蟲系統 (已完成)

### Wikipedia 多語言爬蟲 (`backend/crawler/wikipedia.py`)
- 支援語言：`zh_tw` (繁中)、`en` (英文)、`ja` (日文)、`ko` (韓文)
- **排除** `zh_cn` / `zh_hans` (簡體中文)
- 透過 Wikimedia REST API 獲取頁面摘要
- 透過 Wikimedia Action API 解析時間軸列表
- 內建日期解析器 (支援多語言日期格式)
- 分類關鍵字對照表：politics / economy / military / foreign_relations / human_rights / society / science_tech / environment

### 關鍵主題清單 (各語言 10-12 個主題)
- 涵蓋：中共黨史、文革、大躍進、天安門、改革開放、人權、新疆、西藏、香港、外交關係等

---

## Seed 資料 (已完成)

目前內建 **50 個重大歷史事件**（15 原始 + 35 擴充），每筆含四國語言完整內容：

| # | 事件 | 日期 | 類別 | 重要性 |
|---|------|------|------|--------|
| 1 | 中共一大 (建黨) | 1921-07-23 | politics | 100 |
| 2 | 長征 | 1934-10-16 ~ 1935-10-20 | military | 95 |
| 3 | 中華人民共和國成立 | 1949-10-01 | politics | 100 |
| 4 | 韓戰 (中國介入) | 1950-10-19 ~ 1953-07-27 | military | 90 |
| 5 | 大躍進 | 1958 ~ 1962 | economy | 95 |
| 6 | 文化大革命 | 1966-05-16 ~ 1976-10-06 | politics | 100 |
| 7 | 十一屆三中全會 (改革開放) | 1978-12-18 ~ 1978-12-22 | economy | 100 |
| 8 | 六四天安門事件 | 1989-04-15 ~ 1989-06-04 | human_rights | 100 |
| 9 | 香港主權移交 | 1997-07-01 | politics | 90 |
| 10 | 中國加入 WTO | 2001-12-11 | economy | 85 |
| 11 | 北京奧運 | 2008-08-08 ~ 2008-08-24 | society | 80 |
| 12 | 一帶一路倡議 | 2013-09 | foreign_relations | 85 |
| 13 | 香港反送中運動 | 2019 | human_rights | 90 |
| 14 | 新冠疫情與武漢封城 | 2020-01-23 ~ 2020-04-08 | society | 90 |
| 15 | 中共二十大 (習近平第三任期) | 2022-10-16 | politics | 85 |

### 擴充 35 事件一覽

**1925-1949（5 筆）**: 五卅運動、南昌起義、遵義會議、七七事變、重慶談判

**1950s-1970s（9 筆）**: 西藏和平解放、百花齊放/反右、中蘇分裂、中印邊境戰爭、原子彈爆炸、林彪事件、聯合國2758號決議、尼克森訪華、毛澤東逝世/四人幫垮台

**1980s-1990s（7 筆）**: 一胎化政策、中越邊境戰爭、經濟特區、鄧小平南巡、台海飛彈危機、五八事件、習近平出任總書記

**2000s（6 筆）**: 神舟五號、反日示威、西藏騷亂、新疆騷亂、中國GDP超日本、薄熙來事件

**2010s（4 筆）**: 香港雨傘運動、南海仲裁案、修憲取消任期制、中美貿易戰

**2020s（4 筆）**: 香港國安法、恒大債務危機、中共百年黨慶、上海封城與白紙運動

**分布**: politics 16 / economy 8 / foreign_relations 7 / military 7 / society 5 / human_rights 5 / science_tech 2

天安門事件包含 TW/JP/KR/US 四國觀點。

> ✅ 資料庫已成功 seed 50 筆事件（2025-06-09）

---

## API 端點 (已完成)

| 方法 | 路徑 | 功能 |
|------|------|------|
| GET | `/api/health` | 健康檢查 |
| GET | `/api/events` | 列表 (支援 lang/category/q/date/importance 篩選) |
| GET | `/api/events/geo` | GeoJSON 地圖資料 |
| GET | `/api/events/categories` | 分類列表 |
| GET | `/api/events/languages` | 語言列表 |
| GET | `/api/events/{id}` | 事件詳情 (含 perspectives/media) |
| POST | `/api/events` | 新增事件 |
| PUT | `/api/events/{id}` | 更新事件 |
| DELETE | `/api/events/{id}` | 刪除事件 |
| POST | `/api/crawl/start` | 啟動爬蟲 |
| POST | `/api/seed` | 匯入 seed 資料 |

---

## 待開發項目

### Phase 1 — 基礎建設 (已完成 ✅)
- [x] 前端框架選擇：**Vue 3 + Vite + TypeScript**
- [x] 前端多國語系架構 (vue-i18n v11，繁中/英/日/韓)
- [x] 基本 API 串接層 (utils/api.ts，axios)
- [x] Vite proxy 設定 (開發模式 /api → backend :8000)
- [x] `.env` 設定檔 (backend)
- [x] TypeScript `@` alias 路徑正確設定 (tsconfig paths + vite alias)
- [x] 修正 crawl API 非同步 bug (`await crawl_wikipedia_topic`)
- [x] 修正 EventDetailPage 地點區塊顯示錯誤 i18n key
- [x] Docker Compose 開發環境 (backend + frontend dev mode)

### Phase 2 — 核心功能 (已完成雛形 ✅)
- [x] **時間軸頁面** — 依年份分組、category/importance 篩選、搜尋
- [x] **地圖頁面** — Maplibre GL JS 整合，GeoJSON 事件標記含 popup
- [x] **事件詳情頁** — 多語言切換、多國觀點並列比較、來源列表
- [x] **語系切換** — Header 下拉即時切換繁中/英/日/韓

### Phase 3 — 資料擴充
- [x] 擴充 seed 事件至 50+ 筆（50 筆，1921-2022，7 類別）
- [ ] 改善 Wikipedia 爬蟲精度 (支援 infobox 解析、跨語言事件關聯)
- [ ] 增加新聞網站爬蟲來源 (BBC/Reuters/NHK/Kyodo/Yonhap/中央社)
- [ ] 自動化多語言事件對齊 (WikiData Q-id 關聯)
- [ ] 各國觀點爬取與整理

### Phase 4 — 進階功能
- [ ] 進階搜尋 (全文檢索、標籤過濾)
- [ ] 時間軸 + 地圖連動 (點時間軸事件 ➔ 地圖定位)
- [ ] 統計儀表板 (事件類別分布、年分布)
- [ ] 主題遊覽路線 (預設歷史路徑)
- [ ] 事件比較模式 (並排比較不同國家敘述)

### Phase 5 — 維運
- [ ] 單元測試 (pytest backend, vitest frontend)
- [ ] PostgreSQL 遷移 (正式部署)
- [ ] CI/CD pipeline
- [ ] 靜態匯出功能 (PDF/CSV)
- [ ] API 文件自動生成 (Swagger 已內建)

---

## 目錄結構

```
china_wall/
├── PROGRESS.md              # 本檔案 (開發進度)
├── backend/
│   ├── requirements.txt
│   ├── .env
│   ├── data/
│   │   └── china_wall.db    # SQLite 資料庫
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI 入口
│   │   ├── config.py        # 設定檔
│   │   ├── database.py      # SQLAlchemy 連線
│   │   ├── models.py        # ORM 模型
│   │   ├── schemas.py       # Pydantic schemas
│   │   └── routers/
│   │       ├── __init__.py
│   │       ├── events.py    # CRUD API
│   │       ├── crawl.py     # 爬蟲 API
│   │       └── seed_api.py  # Seed 匯入 API
│   └── crawler/
│       ├── __init__.py
│       ├── wikipedia.py     # Wikipedia 多語言爬蟲
│       └── seed.py          # 初始事件資料
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.ts       # Proxy /api → :8000, @ alias
    ├── tsconfig.json
    ├── public/
    └── src/
        ├── main.ts          # Entry: router + i18n + maplibre CSS
        ├── App.vue          # Layout: header + lang switch + router-view
        ├── style.css        # Global styles
        ├── types/
        │   └── event.ts     # TypeScript interfaces + constants
        ├── utils/
        │   └── api.ts       # Axios instance + API functions
        ├── router/
        │   └── index.ts     # Routes: timeline / map / event/:id
        ├── i18n/
        │   ├── index.ts     # vue-i18n setup
        │   └── locales/
        │       ├── zh_tw.ts
        │       ├── en.ts
        │       ├── ja.ts
        │       └── ko.ts
        ├── components/      # (尚無共用元件)
        └── pages/
            ├── TimelinePage.vue    # ✅ 時間軸 + 篩選側欄
            ├── MapPage.vue         # ✅ Maplibre 地圖 + 事件標記
            └── EventDetailPage.vue # ✅ 事件詳情 + 觀點 + 來源
```

---

## 如何執行

```bash
# 後端
cd backend
pip install -r requirements.txt
python -m app.main
# ➔ http://localhost:8000
# ➔ Swagger UI: http://localhost:8000/docs

# Seed 資料庫
python -m crawler.seed

# 啟動爬蟲 (from FastAPI)
curl -X POST http://localhost:8000/api/seed
```

---

## 設計原則

1. **多國視角** — 每件大事呈現 TW/JP/KR/US 等國觀點，不做單一敘述
2. **可靠來源** — 以 Wikipedia 為起點，後續擴充新聞通訊社、學術論文
3. **排除簡中** — 不使用 `zh_cn`/`zh_hans` 來源，避免內容審查偏誤
4. **地理脈絡** — 所有事件盡可能標註地點，支援地圖視覺化
5. **開放定義** — 任何人都可透過 API 新增事件與觀點
