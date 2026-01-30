from __future__ import annotations

from homeassistant import config_entries

DOMAIN = "popup_blueprint_sync"


class PopupBlueprintSyncConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        # Evita doppia installazione
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        return self.async_create_entry(title="Popup Blueprint Sync", data={})
