from __future__ import annotations

import asyncio
import logging

from homeassistant.core import HomeAssistant

from .sync import sync_blueprints

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    hass.async_create_task(_delayed_sync(hass))
    return True

async def _delayed_sync(hass: HomeAssistant) -> None:
    await asyncio.sleep(5)
    try:
        updated = await sync_blueprints(hass)
        if updated:
            _LOGGER.info("Popup Blueprints: blueprint aggiornato con successo.")
        else:
            _LOGGER.info("Popup Blueprints: nessun aggiornamento necessario.")
    except Exception as err:
        _LOGGER.exception("Popup Blueprints: errore durante la sincronizzazione: %s", err)
