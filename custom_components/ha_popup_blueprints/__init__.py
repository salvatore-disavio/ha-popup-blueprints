from __future__ import annotations

import logging
from pathlib import Path
import shutil

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "ha_popup_blueprints"

_BP_RELATIVE_PATH = Path("blueprints") / "automation" / "popup_homeassistant.yaml"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the wrapper integration and ensure the blueprint is available under /config/blueprints."""
    src = Path(__file__).parent / _BP_RELATIVE_PATH
    dst_dir = Path(hass.config.path("blueprints", "automation", DOMAIN))
    dst = dst_dir / "popup_homeassistant.yaml"

    try:
        dst_dir.mkdir(parents=True, exist_ok=True)

        # Copia/overwrite: così ad ogni update HACS ti aggiorna anche il blueprint visibile in UI
        shutil.copyfile(src, dst)
        _LOGGER.info("Installed/updated blueprint to %s", dst)

    except Exception as err:
        _LOGGER.error("Failed to install blueprint: %s", err)
        # Non blocchiamo l'integrazione: è solo un wrapper
        return True

    return True
