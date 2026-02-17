from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


NAMESPACE = "popup_blueprints_salvatoredisavio"
BLUEPRINT_FILENAME = "popup_homeassistant.yaml"


def _sha256(path: Path) -> str:
    """
    Calculate SHA256 hash of a file.
    """
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


async def sync_blueprints(hass: HomeAssistant) -> bool:
    """
    Copy or update the popup blueprint into Home Assistant blueprint folder.

    Returns True if the blueprint was updated.
    """
    config_dir = Path(hass.config.config_dir)

    # Source file inside the integration folder (downloaded by HACS)
    integration_dir = config_dir / "custom_components" / "popup_blueprint_sync"
    source_path = (
        integration_dir
        / "blueprints"
        / "automation"
        / BLUEPRINT_FILENAME
    )

    if not source_path.exists():
        _LOGGER.warning("Blueprint sorgente non trovato: %s", source_path)
        return False

    # Destination path where HA reads blueprints
    dest_dir = (
        config_dir
        / "blueprints"
        / "automation"
        / NAMESPACE
    )
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_path = dest_dir / BLUEPRINT_FILENAME

    source_hash = _sha256(source_path)

    if dest_path.exists():
        dest_hash = _sha256(dest_path)

        if dest_hash == source_hash:
            return False

        # Backup existing blueprint
        backup_path = dest_path.with_suffix(".yaml.bak")
        backup_path.write_bytes(dest_path.read_bytes())

    # Atomic write
    tmp_path = dest_path.with_suffix(".yaml.tmp")
    tmp_path.write_bytes(source_path.read_bytes())
    tmp_path.replace(dest_path)

    return True

