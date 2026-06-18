---
name: quaternius-assets
description: Search and inspect Quaternius CC0 game asset packs.
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    display_name: Quaternius Assets
    group: asset.download.cc0
    default_icon: package
    affinity: any
    marketplace: dcc-asset-quaternius
    tools: tools.yaml
    execution: sync
    permissions:
      - network
    examples:
      - "Search Quaternius for platformer packs"
      - "Inspect a Quaternius pack license and official download page"
    contact:
      name: dcc-mcp team
      url: https://github.com/dcc-mcp/dcc-asset-quaternius
    install:
      add_source: "dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-quaternius"
      then_install: "dcc-mcp-cli marketplace install dcc-asset-quaternius"
---

# Quaternius Assets

Use this skill to discover Quaternius CC0 packs and return their official
download pages. It deliberately does not automate Google Drive or itch.io
downloads.

