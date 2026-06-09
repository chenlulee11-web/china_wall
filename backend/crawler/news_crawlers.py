"""
News website crawlers for PRC/CCP history event perspectives.

Supported sources:
  - BBC News (en) — UK perspective
  - Reuters (en) — International wire service
  - NHK News (ja) — Japanese perspective
  - Kyodo News (ja) — Japanese perspective
  - Yonhap News (ko) — Korean perspective
  - 中央社 CNA (zh_tw) — Taiwanese perspective
"""

import asyncio
import re
from datetime import date, datetime
from typing import Optional

import httpx
from bs4 import BeautifulSoup

USER_AGENT = "ChinaWall/1.0 (educational project; contact@chinawall.dev)"


async def _fetch_soup(client: httpx.AsyncClient, url: str) -> Optional[BeautifulSoup]:
    """Fetch a URL and return parsed BeautifulSoup, or None on failure."""
    try:
        resp = await client.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
        resp.raise_for_status()
        return BeautifulSoup(resp.text, "lxml")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None


async def crawl_bbc_search(query: str, max_results: int = 20) -> list[dict]:
    """Search BBC News for articles about a given topic."""
    url = "https://www.bbc.com/search"
    params = {"q": query, "page": 1}
    results = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, f"{url}?q={query}")
        if not soup:
            return results
        articles = soup.select("a[href*='/news/']") or soup.select('[data-testid="internal-link"]')
        seen_urls = set()
        for a in articles:
            href = a.get("href", "")
            if not href.startswith("http"):
                href = "https://www.bbc.com" + href
            if href in seen_urls:
                continue
            seen_urls.add(href)
            title = a.get_text(strip=True)
            if title and len(title) > 20:
                results.append({
                    "title": title[:200],
                    "url": href,
                    "source": "BBC News",
                    "lang": "en",
                    "country": "GB",
                })
                if len(results) >= max_results:
                    break
    return results


async def crawl_bbc_article(url: str) -> Optional[dict]:
    """Parse a single BBC News article for perspective content."""
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, url)
        if not soup:
            return None
        paragraphs = soup.select("article p, [data-component='text-block'] p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        headline = soup.find("h1")
        title = headline.get_text(strip=True) if headline else ""
        time_tag = soup.find("time")
        pub_date = None
        if time_tag and time_tag.get("datetime"):
            try:
                pub_date = datetime.fromisoformat(time_tag["datetime"].replace("Z", "+00:00")).date()
            except ValueError:
                pass
        return {
            "title": title[:200] if title else "",
            "content": content[:2000] if content else "",
            "url": url,
            "date": pub_date or date.today(),
            "source": "BBC News",
            "lang": "en",
            "country_code": "GB",
        }


async def crawl_reuters_search(query: str, max_results: int = 20) -> list[dict]:
    """Search Reuters for articles about a given topic."""
    url = "https://www.reuters.com/search"
    params = {"q": query, "page": 1, "blob": query}
    results = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, f"https://www.reuters.com/search/news?blob={query}")
        if not soup:
            return results
        articles = soup.select("a[href*='/article/']")
        seen_urls = set()
        for a in articles:
            href = a.get("href", "")
            if not href.startswith("http"):
                href = "https://www.reuters.com" + href
            if href in seen_urls:
                continue
            seen_urls.add(href)
            title = a.get_text(strip=True)
            if title and len(title) > 20:
                results.append({
                    "title": title[:200],
                    "url": href,
                    "source": "Reuters",
                    "lang": "en",
                    "country": "GB",
                })
                if len(results) >= max_results:
                    break
    return results


async def crawl_nhk_search(query: str, max_results: int = 20) -> list[dict]:
    """Search NHK News (Japan) for articles."""
    url = "https://www3.nhk.or.jp/news/search"
    results = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, f"{url}?q={query}")
        if not soup:
            return results
        articles = soup.select("a[href*='/news/html/']")
        seen_urls = set()
        for a in articles:
            href = a.get("href", "")
            if href.startswith("/"):
                href = "https://www3.nhk.or.jp" + href
            if href in seen_urls:
                continue
            seen_urls.add(href)
            title = a.get_text(strip=True)
            if title and len(title) > 10:
                results.append({
                    "title": title[:200],
                    "url": href,
                    "source": "NHK News",
                    "lang": "ja",
                    "country": "JP",
                })
                if len(results) >= max_results:
                    break
    return results


async def crawl_kyodo_search(query: str, max_results: int = 20) -> list[dict]:
    """Search Kyodo News (Japan) for articles."""
    url = "https://english.kyodonews.net/search"
    results = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, f"{url}?q={query}")
        if not soup:
            return results
        articles = soup.select("a[href*='/news/']")
        seen_urls = set()
        for a in articles:
            href = a.get("href", "")
            if not href.startswith("http"):
                href = "https://english.kyodonews.net" + href
            if href in seen_urls:
                continue
            seen_urls.add(href)
            title = a.get_text(strip=True)
            if title and len(title) > 15:
                results.append({
                    "title": title[:200],
                    "url": href,
                    "source": "Kyodo News",
                    "lang": "en",
                    "country": "JP",
                })
                if len(results) >= max_results:
                    break
    return results


async def crawl_yonhap_search(query: str, max_results: int = 20) -> list[dict]:
    """Search Yonhap News (Korea) for articles."""
    url = "https://en.yna.co.kr/search"
    results = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, f"{url}?q={query}")
        if not soup:
            return results
        articles = soup.select("a[href*='/news/']")
        seen_urls = set()
        for a in articles:
            href = a.get("href", "")
            if not href.startswith("http"):
                href = "https://en.yna.co.kr" + href
            if href in seen_urls:
                continue
            seen_urls.add(href)
            title = a.get_text(strip=True)
            if title and len(title) > 15:
                results.append({
                    "title": title[:200],
                    "url": href,
                    "source": "Yonhap News",
                    "lang": "en",
                    "country": "KR",
                })
                if len(results) >= max_results:
                    break
    return results


async def crawl_cna_search(query: str, max_results: int = 20) -> list[dict]:
    """Search Central News Agency (CNA, Taiwan) for articles."""
    url = "https://www.cna.com.tw/search"
    results = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, f"{url}?q={query}")
        if not soup:
            return results
        articles = soup.select("a[href*='/news/']")
        seen_urls = set()
        for a in articles:
            href = a.get("href", "")
            if href.startswith("/"):
                href = "https://www.cna.com.tw" + href
            if href in seen_urls:
                continue
            seen_urls.add(href)
            title = a.get_text(strip=True)
            if title and len(title) > 10:
                results.append({
                    "title": title[:200],
                    "url": href,
                    "source": "中央社 CNA",
                    "lang": "zh_tw",
                    "country": "TW",
                })
                if len(results) >= max_results:
                    break
    return results


async def crawl_all_news_sources(query: str, max_per_source: int = 10) -> list[dict]:
    """Crawl all supported news sources for a given topic query."""
    tasks = [
        crawl_bbc_search(query, max_per_source),
        crawl_reuters_search(query, max_per_source),
        crawl_nhk_search(query, max_per_source),
        crawl_kyodo_search(query, max_per_source),
        crawl_yonhap_search(query, max_per_source),
        crawl_cna_search(query, max_per_source),
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    all_articles = []
    for result in results:
        if isinstance(result, list):
            all_articles.extend(result)
    return all_articles


async def fetch_article_perspective(url: str, source: str) -> Optional[dict]:
    """Fetch and parse a news article, returning perspective data."""
    if "bbc.com" in url:
        return await crawl_bbc_article(url)
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        soup = await _fetch_soup(client, url)
        if not soup:
            return None
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))[:2000]
        headline = soup.find("h1")
        title = headline.get_text(strip=True) if headline else ""
        return {
            "title": title[:200],
            "content": content,
            "url": url,
            "source": source,
        }
