from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .sync import sync_blueprints

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up integration from YAML (not used, but required by HA)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    try:
        changed = await sync_blueprints(hass)
        if changed:
            _LOGGER.info("Blueprint synced/updated into %s", hass.config.path("blueprints", "automation", DOMAIN))
        else:
            _LOGGER.warning(
                "No blueprint changes applied. If the blueprint does not appear, check that the source file exists in the integration folder."
            )
    except Exception as err:
        _LOGGER.exception("Blueprint sync failed: %s", err)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload the config entry."""
    return True
