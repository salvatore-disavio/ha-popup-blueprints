from __future__ import annotations

import hashlib
from pathlib import Path

from homeassistant.core import HomeAssistant

NAMESPACE = "popup_blueprint_homeassistant"
BLUEPRINT_FILENAME = "popup_homeassistant.yaml"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


async def sync_blueprints(hass: HomeAssistant) -> bool:
    """Copy/update blueprint from integration folder to HA blueprints folder.
    Returns True if updated.
    """
    config_dir = Path(hass.config.config_dir)

    # Source: inside the integration folder (ensured by HACS download)
    integration_dir = config_dir / "custom_components" / "popup_blueprint_sync"
    source_path = integration_dir / "blueprints" / "automation" / BLUEPRINT_FILENAME

    if not source_path.exists():
        # Nothing to sync (repo installed incorrectly or missing files)
        return False

    # Destination: official HA blueprint folder
    dest_dir = config_dir / "blueprints" / "automation" / NAMESPACE
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_path = dest_dir / BLUEPRINT_FILENAME

    source_hash = _sha256(source_path)
    if dest_path.exists():
        dest_hash = _sha256(dest_path)
        if dest_hash == source_hash:
            return False

        # Backup existing file before overwriting
        backup_path = dest_path.with_suffix(".yaml.bak")
        backup_path.write_bytes(dest_path.read_bytes())

    # Atomic write
    tmp_path = dest_path.with_suffix(".yaml.tmp")
    tmp_path.write_bytes(source_path.read_bytes())
    tmp_path.replace(dest_path)

    return True
