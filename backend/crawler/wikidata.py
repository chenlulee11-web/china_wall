"""
WikiData API client for cross-lingual event alignment.

Resolves Wikipedia page titles to WikiData Q-ids and fetches
cross-language title mappings for automatic event correlation.
"""

import asyncio
from typing import Optional

import httpx

USER_AGENT = "ChinaWall/1.0 (educational project; contact@chinawall.dev)"
WIKIDATA_API = "https://www.wikidata.org/w/api.php"
WIKIPEDIA_API_TEMPLATE = "https://{lang}.wikipedia.org/w/api.php"

LANG_TO_WIKI_CODE = {
    "zh_tw": "zh",
    "en": "en",
    "ja": "ja",
    "ko": "ko",
}


async def find_qid_by_title(title: str, lang: str = "en") -> Optional[str]:
    """Resolve a Wikipedia page title to its WikiData Q-id."""
    wiki_code = LANG_TO_WIKI_CODE.get(lang, lang)
    params = {
        "action": "query",
        "prop": "pageprops",
        "titles": title,
        "format": "json",
        "redirects": 1,
    }
    url = WIKIPEDIA_API_TEMPLATE.format(lang=wiki_code)
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(url, params=params, headers={"User-Agent": USER_AGENT})
            resp.raise_for_status()
            data = resp.json()
            pages = data.get("query", {}).get("pages", {})
            for page_id, page_data in pages.items():
                if page_id != "-1":
                    return page_data.get("pageprops", {}).get("wikibase_item")
        except Exception as e:
            print(f"WikiData Q-id lookup error for {title} ({lang}): {e}")
    return None


async def get_qid_batch(titles: list[str], lang: str = "en") -> dict[str, Optional[str]]:
    """Batch resolve Wikipedia page titles to WikiData Q-ids."""
    wiki_code = LANG_TO_WIKI_CODE.get(lang, lang)
    params = {
        "action": "query",
        "prop": "pageprops",
        "titles": "|".join(titles),
        "format": "json",
        "redirects": 1,
    }
    url = WIKIPEDIA_API_TEMPLATE.format(lang=wiki_code)
    result = {}
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(url, params=params, headers={"User-Agent": USER_AGENT})
            resp.raise_for_status()
            data = resp.json()
            pages = data.get("query", {}).get("pages", {})
            title_to_normalized = {}
            normalized = data.get("query", {}).get("normalized", [])
            for n in normalized:
                title_to_normalized[n.get("from", "")] = n.get("to", "")
            for page_id, page_data in pages.items():
                if page_id != "-1":
                    title = page_data.get("title", "")
                    qid = page_data.get("pageprops", {}).get("wikibase_item")
                    result[title] = qid
            for orig_title in titles:
                normalized_title = title_to_normalized.get(orig_title, orig_title)
                if normalized_title not in result:
                    result[orig_title] = None
                else:
                    result[orig_title] = result[normalized_title]
        except Exception as e:
            print(f"Batch Q-id lookup error: {e}")
            for t in titles:
                result[t] = None
    return result


async def get_multilingual_titles(qid: str) -> dict[str, str]:
    """Fetch multilingual page titles for a given WikiData Q-id."""
    params = {
        "action": "wbgetentities",
        "ids": qid,
        "props": "sitelinks",
        "sitefilter": "zhwiki|enwiki|jawiki|kowiki",
        "format": "json",
    }
    lang_map = {"zhwiki": "zh_tw", "enwiki": "en", "jawiki": "ja", "kowiki": "ko"}
    result = {}
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(WIKIDATA_API, params=params, headers={"User-Agent": USER_AGENT})
            resp.raise_for_status()
            data = resp.json()
            entities = data.get("entities", {})
            entity = entities.get(qid, {})
            sitelinks = entity.get("sitelinks", {})
            for site_key, site_data in sitelinks.items():
                mapped_lang = lang_map.get(site_key)
                if mapped_lang:
                    result[mapped_lang] = site_data.get("title", "")
        except Exception as e:
            print(f"Multilingual title fetch error for {qid}: {e}")
    return result


async def batch_get_multilingual_titles(qids: list[str]) -> dict[str, dict[str, str]]:
    """Batch fetch multilingual titles for multiple Q-ids."""
    params = {
        "action": "wbgetentities",
        "ids": "|".join(qids),
        "props": "sitelinks",
        "sitefilter": "zhwiki|enwiki|jawiki|kowiki",
        "format": "json",
    }
    lang_map = {"zhwiki": "zh_tw", "enwiki": "en", "jawiki": "ja", "kowiki": "ko"}
    result = {}
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(WIKIDATA_API, params=params, headers={"User-Agent": USER_AGENT})
            resp.raise_for_status()
            data = resp.json()
            entities = data.get("entities", {})
            for qid, entity in entities.items():
                titles = {}
                sitelinks = entity.get("sitelinks", {})
                for site_key, site_data in sitelinks.items():
                    mapped_lang = lang_map.get(site_key)
                    if mapped_lang:
                        titles[mapped_lang] = site_data.get("title", "")
                result[qid] = titles
        except Exception as e:
            print(f"Batch multilingual title fetch error: {e}")
    return result


async def get_event_description(qid: str, lang: str = "en") -> Optional[str]:
    """Fetch the description/label for a WikiData entity in a given language."""
    wiki_code = LANG_TO_WIKI_CODE.get(lang, lang)
    params = {
        "action": "wbgetentities",
        "ids": qid,
        "props": "descriptions|labels",
        "languages": wiki_code,
        "format": "json",
    }
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(WIKIDATA_API, params=params, headers={"User-Agent": USER_AGENT})
            resp.raise_for_status()
            data = resp.json()
            entity = data.get("entities", {}).get(qid, {})
            desc = entity.get("descriptions", {}).get(wiki_code, {}).get("value")
            if not desc:
                desc = entity.get("labels", {}).get(wiki_code, {}).get("value")
            return desc
        except Exception as e:
            print(f"WikiData description fetch error for {qid}: {e}")
    return None
