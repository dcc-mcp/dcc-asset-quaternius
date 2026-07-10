---
name: quaternius-assets
description: Search and inspect Quaternius CC0 game asset packs, then describe official downloads as AssetDescriptors.
license: MIT
compatibility: "dcc-mcp-core 0.19+, Python 3.7+"
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    layer: domain
    tags:
      - asset
      - quaternius
      - cc0
      - game-assets
      - 3d-models
    search-hint: "quaternius, cc0 game assets, game asset pack, platformer kit, low poly models, official download page"
    produces: [asset_descriptor]
    tools: tools.yaml
---

# Quaternius Assets

Use this skill to discover Quaternius CC0 packs and return their official
download pages. It deliberately does not automate Google Drive or itch.io
downloads. After downloading from the official page, use
`describe_quaternius_asset` with the local file to obtain an `asset_descriptor`
for a host-specific DCC import skill.

