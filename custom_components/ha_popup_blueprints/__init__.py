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
    """Set up integration from a config entry (UI)."""
    try:
        changed = await sync_blueprints(hass)
        if changed:
            _LOGGER.info("Blueprint synced/updated to /config/blueprints/automation/%s", DOMAIN)
        else:
            _LOGGER.debug("Blueprint already up to date")
    except Exception as err:
        _LOGGER.exception("Blueprint sync failed: %s", err)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload the config entry."""
    return True
