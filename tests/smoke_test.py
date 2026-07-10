from __future__ import annotations

import importlib.util
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "quaternius-assets"
SCRIPTS = SKILL / "scripts"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def validate_skill() -> None:
    from dcc_mcp_core import validate_skill

    report = validate_skill(str(SKILL))
    assert not report.has_errors, report


def descriptor_smoke() -> None:
    result = load("describe_quaternius_asset").asset_descriptor(
        {
            "title": "Ultimate Platformer Pack",
            "url": "https://quaternius.com/packs/ultimateplatformer.html",
            "official_download_url": "https://quaternius.com/packs/ultimateplatformer.html",
            "usage_notice": "Quaternius pages mark these packs as CC0.",
            "license_name": "CC0 1.0 Universal",
        },
        "C:/tmp/ultimateplatformer.zip",
    )
    assert result["variants"][0]["local_path"] == "C:/tmp/ultimateplatformer.zip"
    assert result["attribution"]["source_url"].endswith("ultimateplatformer.html")
    assert result["attribution"]["license_text"].startswith("Quaternius pages")


def live_smoke() -> None:
    if os.environ.get("RUN_LIVE_API_SMOKE") != "true":
        print("skip live Quaternius smoke")
        return
    result = load("inspect_quaternius_asset").main(pack_url_or_slug="ultimateplatformer")
    assert result["success"], result
    assert result["context"]["pack"]["license_detected"], result


def main() -> None:
    validate_skill()
    descriptor_smoke()
    live_smoke()


if __name__ == "__main__":
    main()

