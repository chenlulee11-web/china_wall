"""
Wikipedia multilingual crawler for PRC/CCP history events.

Supported languages: zh_tw (Traditional Chinese), en (English),
                     ja (Japanese), ko (Korean)

Excludes: zh_cn, zh_hans (Simplified Chinese)

Uses the Wikimedia REST API and WikiData for cross-lingual event linking.
"""

import asyncio
import re
from datetime import date, datetime
from typing import Optional

import httpx
from bs4 import BeautifulSoup

USER_AGENT = "ChinaWall/1.0 (educational project; contact@chinawall.dev)"

WIKI_LANG_MAP = {
    "zh_tw": "zh.wikipedia.org",
    "en": "en.wikipedia.org",
    "ja": "ja.wikipedia.org",
    "ko": "ko.wikipedia.org",
}

WIKI_API_BASE = "https://{lang}.wikipedia.org/w/api.php"
WIKI_REST_BASE = "https://{lang}.wikipedia.org/api/rest_v1"

# Key historical topics to crawl across languages
TOPICS = {
    "zh_tw": [
        "中國共產黨歷史",
        "中華人民共和國歷史",
        "中華人民共和國年表",
        "中華人民共和國政治",
        "改革開放",
        "天安門事件",
        "中國人權",
        "中國經濟",
        "文化大革命",
        "大躍進",
    ],
    "en": [
        "History of the Communist Party of China",
        "History of the People's Republic of China",
        "Timeline of the People's Republic of China",
        "Chinese economic reform",
        "Tiananmen Square protests and massacre",
        "Cultural Revolution",
        "Great Leap Forward",
        "Human rights in China",
        "Political status of Taiwan",
        "Xinjiang conflict",
        "Tibet since 1950",
        "Foreign relations of China",
    ],
    "ja": [
        "中国共産党の歴史",
        "中華人民共和国の歴史",
        "改革開放",
        "天安門事件",
        "文化大革命",
        "大躍進",
        "中国の人権問題",
        "日中関係史",
        "新疆問題",
        "チベット問題",
    ],
    "ko": [
        "중국공산당의 역사",
        "중화인민공화국의 역사",
        "개혁개방",
        "톈안먼 사건",
        "문화대혁명",
        "대약진 운동",
        "중국의 인권",
        "한중 관계",
        "신장 문제",
        "티베트 문제",
    ],
}


async def _fetch_json(client: httpx.AsyncClient, url: str) -> dict:
    resp = await client.get(url, headers={"User-Agent": USER_AGENT})
    resp.raise_for_status()
    return resp.json()


async def _fetch_html_summary(lang: str, title: str) -> Optional[str]:
    """Fetch the summary/extract for a Wikipedia page via REST API."""
    host = WIKI_LANG_MAP.get(lang, f"{lang}.wikipedia.org")
    url = f"https://{host}/api/rest_v1/page/summary/{title}"
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            data = await _fetch_json(client, url)
            return data.get("extract")
        except Exception:
            return None


def _parse_date_from_wikitext(text: str) -> Optional[date]:
    """Try to extract a date from Wikipedia infobox text."""
    patterns = [
        r"(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日",
        r"(\d{4})\s*-\s*(\d{1,2})\s*-\s*(\d{1,2})",
        r"(\d{4})\s*年\s*(\d{1,2})月",
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})",
        r"(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})",
        r"^(\d{4})$",
    ]
    months_en = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
    }

    for pattern in patterns:
        m = re.search(pattern, text)
        if m:
            try:
                if len(m.groups()) == 3:
                    if m.group(2).isdigit():
                        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                    elif m.group(1).isdigit() and m.group(3).isdigit():
                        if m.group(2) in months_en:
                            return date(int(m.group(3)), months_en[m.group(2)], int(m.group(1)))
                        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                elif len(m.groups()) == 2:
                    return date(int(m.group(1)), int(m.group(2)), 1)
                elif len(m.groups()) == 1:
                    return date(int(m.group(1)), 1, 1)
            except (ValueError, IndexError):
                continue
    return None


def _parse_year_range(text: str) -> tuple:
    """Parse year ranges like '1966-1976' or '1958-1961'."""
    m = re.search(r"(\d{4})\s*[–\-—~to]\s*(\d{4})", text)
    if m:
        return date(int(m.group(1)), 1, 1), date(int(m.group(2)), 1, 1)
    return None, None


async def crawl_wikipedia_topic(
    topic: str,
    lang: str = "en",
    max_events: int = 50,
) -> list[dict]:
    """
    Crawl a Wikipedia topic page for lists/sections containing historical events.
    Returns a list of event dicts.
    """
    host = WIKI_LANG_MAP.get(lang, f"{lang}.wikipedia.org")
    api_url = WIKI_API_BASE.format(lang=lang.split("_")[0])
    rest_url = WIKI_REST_BASE.format(lang=lang.split("_")[0])

    params = {
        "action": "parse",
        "page": topic,
        "prop": "text|links|sections|categories",
        "format": "json",
        "redirects": 1,
    }

    events = []

    async with httpx.AsyncClient(timeout=60) as client:
        try:
            resp = await client.get(
                api_url,
                params=params,
                headers={"User-Agent": USER_AGENT},
            )
            resp.raise_for_status()
            data = resp.json()

            if "error" in data:
                print(f"Wikipedia API error for {topic} ({lang}): {data['error']}")
                return events

            parse_result = data.get("parse", {})
            html_text = parse_result.get("text", {}).get("*", "")

            # Parse sections to find timelines and lists
            soup = BeautifulSoup(html_text, "lxml")

            # Find all list items and table rows which often contain date entries
            for tag in soup.find_all(["li", "tr"]):
                text = tag.get_text(strip=True)

                # Try to extract a date from the beginning of list items
                ev_date = _parse_date_from_wikitext(text[:100])
                if ev_date:
                    # Get the full event text (remove the date prefix)
                    event_text = re.sub(
                        r"^\d{4}年\d{1,2}月\d{1,2}日[：:－\s]*|"
                        r"^\d{4}年\d{1,2}月[：:－\s]*|"
                        r"^\d{4}[年\s:：\-]\s*|"
                        r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\s*[–\-—]?\s*|"
                        r"^\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\s*[–\-—]?\s*",
                        "", text, count=1,
                    ).strip()

                    # Determine category
                    category = None
                    for cat_name, keywords in _CATEGORY_KEYWORDS.items():
                        if any(kw in text.lower() for kw in keywords):
                            category = cat_name
                            break

                    events.append({
                        "title": event_text[:200] if event_text else text[:200],
                        "date": ev_date,
                        "date_precision": "day",
                        "summary": text[:500],
                        "category": category,
                        "tags": [topic],
                        "importance": 0,
                        "source_url": f"https://{host}/wiki/{topic.replace(' ', '_')}",
                    })

                    if len(events) >= max_events:
                        break

            # Also try to get the summary for main topic
            try:
                summary_data = await _fetch_json(
                    client, f"{rest_url}/page/summary/{topic.replace(' ', '_')}"
                )
                summary_text = summary_data.get("extract", "")
                if summary_text and not events:
                    events.append({
                        "title": topic,
                        "date": date(1949, 10, 1),  # default to PRC founding
                        "date_precision": "year",
                        "summary": summary_text[:1000],
                        "category": "general",
                        "tags": [topic],
                        "importance": 50,
                        "source_url": f"https://{host}/wiki/{topic.replace(' ', '_')}",
                    })
            except Exception:
                pass

        except httpx.HTTPError as e:
            print(f"HTTP error crawling {topic} ({lang}): {e}")
        except Exception as e:
            print(f"Unexpected error crawling {topic} ({lang}): {e}")

    return events


async def crawl_all_languages(topics_override: dict = None) -> dict:
    """Crawl events across all supported languages."""
    all_results = {}
    langs = topics_override or TOPICS

    for lang, topics in langs.items():
        lang_events = []
        for topic in topics:
            print(f"Crawling [{lang}]: {topic}")
            events = await crawl_wikipedia_topic(topic, lang=lang, max_events=30)
            lang_events.extend(events)
        all_results[lang] = lang_events
        print(f"[{lang}] collected {len(lang_events)} events")

    return all_results


_CATEGORY_KEYWORDS = {
    "politics": [
        "party", "congress", "election", "politburo", "plenum", "ccp",
        "共产党", "黨", "政治", "人民代表大会", "政協",
        "共産党", "党大会", "政治局",
        "공산당", "당대회", "정치",
    ],
    "economy": [
        "economic", "reform", "gdp", "trade", "market", "financial",
        "经济", "改革开放", "贸易", "gdp",
        "経済", "改革開放", "貿易",
        "경제", "개혁개방", "무역",
    ],
    "military": [
        "military", "army", "war", "conflict", "defense", "nuclear",
        "军事", "军队", "战争", "解放军",
        "軍事", "軍隊", "戦争", "人民解放軍",
        "군사", "군대", "전쟁",
    ],
    "foreign_relations": [
        "foreign", "diplomatic", "embassy", "treaty", "relations",
        "外交", "国际", "条约", "关系",
        "外交", "国際", "条約", "関係",
        "외교", "국제", "조약", "관계",
    ],
    "human_rights": [
        "human rights", "protest", "democracy", "crackdown", "dissident",
        "人权", "抗议", "民主", "镇压",
        "人権", "抗議", "民主化", "弾圧",
        "인권", "항의", "민주화", "탄압",
    ],
    "society": [
        "social", "population", "education", "health", "migration",
        "社会", "人口", "教育", "医疗",
        "社会", "人口", "教育", "医療",
        "사회", "인구", "교육", "의료",
    ],
    "science_tech": [
        "science", "technology", "space", "satellite", "nuclear",
        "科学", "技术", "科技", "航天",
        "科学", "技術", "宇宙", "衛星",
        "과학", "기술", "우주", "위성",
    ],
    "environment": [
        "environment", "pollution", "climate", "emission",
        "环境", "污染", "气候",
        "環境", "汚染", "気候",
        "환경", "오염", "기후",
    ],
}


if __name__ == "__main__":
    asyncio.run(crawl_all_languages())
