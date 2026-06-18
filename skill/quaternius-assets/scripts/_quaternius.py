from __future__ import annotations

import html
import re
import urllib.parse
import urllib.request
from typing import Any


BASE = "https://quaternius.com"
LICENSE = {
    "license_name": "CC0 1.0 Universal",
    "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    "usage_notice": "Quaternius pages mark these packs as CC0; use the official download page for files.",
}


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "dcc-mcp-quaternius/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "ignore")


def pack_url(slug_or_url: str) -> str:
    if slug_or_url.startswith("http"):
        return slug_or_url
    slug = slug_or_url.strip("/")
    if not slug.endswith(".html"):
        slug += ".html"
    return f"{BASE}/packs/{slug}"


def search() -> list[dict[str, Any]]:
    text = get(BASE + "/")
    packs = []
    pattern = re.compile(r'<a href="(/packs/[^"]+\.html)"[^>]*>.*?<div class="PackText">(.*?)<!--TITLE -->(.*?)</div>', re.S)
    for match in pattern.finditer(text):
        title = html.unescape(re.sub(r"<.*?>", "", match.group(2)).strip())
        tags = [html.unescape(t.strip()) for t in re.findall(r'<div class="(?:viewtag )?tags">(.*?)</div>', match.group(3), re.S)]
        packs.append({"title": title, "url": BASE + match.group(1), "tags": tags, **LICENSE})
    return packs


def inspect(slug_or_url: str) -> dict[str, Any]:
    url = pack_url(slug_or_url)
    text = get(url)
    title_match = re.search(r"<title>(.*?)</title>", text, re.S)
    drive_match = re.search(r"window\.open\('([^']+)'", text)
    formats = sorted(set(re.findall(r'<div class="text-right tags">([^<]+)</div>', text)))
    license_detected = "creativecommons.org/publicdomain/zero/1.0" in text or "CC0" in text
    return {
        "title": html.unescape(re.sub(r"\s+", " ", title_match.group(1)).strip()) if title_match else url,
        "url": url,
        "official_download_url": drive_match.group(1) if drive_match else url,
        "formats": formats,
        "license_detected": license_detected,
        **LICENSE,
    }

