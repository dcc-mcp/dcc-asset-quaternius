from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _quaternius import inspect


@skill_entry
def main(pack_url_or_slug: str, **_: Any) -> dict[str, Any]:
    try:
        return skill_success("Quaternius pack inspected", pack=inspect(pack_url_or_slug))
    except Exception as exc:
        return skill_exception(exc, message="Failed to inspect Quaternius pack")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

