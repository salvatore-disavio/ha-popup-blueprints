from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .sync import sync_blueprint

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    changed = await sync_blueprint(hass)
    if changed:
        _LOGGER.info("Blueprint installed/updated")
    else:
        _LOGGER.info("Blueprint already up to date (or source missing)")
    return True
