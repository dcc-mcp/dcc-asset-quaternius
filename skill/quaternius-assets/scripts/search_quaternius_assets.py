from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _quaternius import search


@skill_entry
def main(query: str | None = None, limit: int = 12, **_: Any) -> dict[str, Any]:
    try:
        needle = (query or "").lower()
        items = [
            p
            for p in search()
            if not needle or needle in p["title"].lower() or needle in " ".join(p["tags"]).lower()
        ]
        return skill_success("Quaternius packs found", packs=items[:limit], count=min(len(items), limit))
    except Exception as exc:
        return skill_exception(exc, message="Failed to search Quaternius packs")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

