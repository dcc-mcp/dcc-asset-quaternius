from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from dcc_mcp_core.asset_import import AssetAttribution, AssetDescriptor, AssetFileVariant
from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _quaternius import inspect


def asset_descriptor(pack: dict[str, Any], local_path: str) -> dict[str, Any]:
    descriptor = AssetDescriptor(
        asset_id=f"quaternius:{pack['url']}",
        variants=[
            AssetFileVariant(
                local_path=local_path,
                format=Path(local_path).suffix.lstrip(".").lower() or "unknown",
                preferred=True,
            )
        ],
        attribution=AssetAttribution(
            source_url=pack["url"],
            license_text=pack["usage_notice"],
            attribution_text=f"{pack['title']} — {pack['license_name']}.",
        ),
        extra={"official_download_url": pack["official_download_url"]},
    )
    descriptor.validate()
    return descriptor.to_dict()


@skill_entry
def main(pack_url_or_slug: str, local_path: str, **_: Any) -> dict[str, Any]:
    try:
        pack = inspect(pack_url_or_slug)
        return skill_success(
            "Quaternius asset described",
            pack=pack,
            asset_descriptor=asset_descriptor(pack, local_path),
        )
    except Exception as exc:
        return skill_exception(exc, message="Failed to describe Quaternius asset")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
