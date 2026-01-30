from __future__ import annotations

import asyncio
import logging

from homeassistant.core import HomeAssistant

from .sync import sync_blueprints

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the integration and sync the blueprint on startup."""
    hass.async_create_task(_delayed_sync(hass))
    return True


async def _delayed_sync(hass: HomeAssistant) -> None:
    """Wait HA startup, then copy/update blueprint(s)."""
    await asyncio.sleep(5)
    try:
        updated = await sync_blueprints(hass)
        if updated:
            _LOGGER.info("Popup Blueprint Sync: blueprint aggiornato.")
        else:
            _LOGGER.info("Popup Blueprint Sync: blueprint già aggiornato (nessuna modifica).")
    except Exception as err:
        _LOGGER.exception("Popup Blueprint Sync: errore durante la sync: %s", err)
