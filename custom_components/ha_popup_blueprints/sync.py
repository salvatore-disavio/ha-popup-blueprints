from __future__ import annotations

import hashlib
from pathlib import Path

from homeassistant.core import HomeAssistant

from .const import DOMAIN, BLUEPRINT_FILENAME


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


async def sync_blueprints(hass: HomeAssistant) -> bool:
    """Copy/update blueprint from the integration folder to HA config blueprint folder.

    Returns True if something changed.
    """
    config_dir = Path(hass.config.config_dir)

    # Destination (where HA UI reads blueprints from)
    dest_dir = config_dir / "blueprints" / "automation" / DOMAIN
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / BLUEPRINT_FILENAME

    # Source (inside the custom component folder)
    integration_dir = config_dir / "custom_components" / DOMAIN
    source_path = integration_dir / "blueprints" / "automation" / BLUEPRINT_FILENAME

    if not source_path.exists():
        return False

    if dest_path.exists() and _sha256(dest_path) == _sha256(source_path):
        return False

    tmp_path = dest_path.with_suffix(".yaml.tmp")
    tmp_path.write_bytes(source_path.read_bytes())
    tmp_path.replace(dest_path)

    return True
