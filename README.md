# Popup Blueprints (Browser Mod)
Blueprint riutilizzabile per Home Assistant che consente di mostrare **popup moderni in stile app** direttamente nelle dashboard tramite **Browser Mod**.
Progettato principalmente per **tablet, wall panel e dashboard touch**, ma utilizzabile anche su desktop.
Ideale per notifiche visive, conferme di azione e messaggi contestuali legati allo stato delle entità.

<p align="center">
  <img src="https://raw.githubusercontent.com/salvatore-disavio/ha-popup-blueprints/main/images/custom_card.png" width="300">
</p>
---

## ✨ Features

- Popup in stile **app**, puliti e leggibili
- Ottimizzato per **tablet e wall panel**
- Visualizzazione su uno specifico dispositivo tramite `browser_id`
- Trigger flessibili:
  - quando un’entità passa a uno stato specifico
  - quando un’entità passa da uno stato a un altro
  - quando un’entità passa a **uno dei due stati** configurati
- Preset grafici pronti all’uso:
  **success / warning / alert / personalizzato**
- Personalizzazione completa di:
  - titolo e testo
  - icona
  - colori
  - animazioni
- Possibilità di rendere il popup **chiudibile cliccando all’esterno** (opzionale)

<details>
  <summary><strong>English version</strong></summary>

  ## ✨ Features (EN)

  - App-style popup UI
  - Optimized for **tablet and wall panel dashboards**
  - Target a specific device using `browser_id`
  - Flexible trigger logic:
    - when an entity changes to a specific state
    - when an entity changes from one state to another
    - when an entity changes to **one of two configured states**
  - Visual presets:
    **success / warning / alert / custom**
  - Fully customizable:
    - title and text
    - icon
    - colors
    - animations
  - Optional close-on-click-outside behavior

</details>

---

## 🚀 Installazione

### Installazione tramite HACS (consigliata)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=salvatore-disavio&repository=ha-popup-blueprints&category=integration)

Il progetto viene distribuito come **custom integration HACS**.
L’integrazione si occupa automaticamente di installare e aggiornare il blueprint.

1. Apri **HACS**
2. Vai su **Integrations**
3. Menu ⋮ → **Custom repositories**
4. Inserisci la repository: https://github.com/salvatore-disavio/ha-popup-blueprints
5. Categoria: **Integration**
6. Installa e **riavvia Home Assistant**

Dopo il riavvio, il blueprint sarà disponibile in:
**Impostazioni → Automazioni e scene → Blueprint**

<details>
<summary><strong>English version</strong></summary>

### Installation via HACS (recommended)

This project is distributed as a **HACS custom integration**.
The integration automatically installs and updates the blueprint.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=salvatore-disavio&repository=ha-popup-blueprints&category=integration)

1. Open **HACS**
2. Go to **Integrations**
3. Menu ⋮ → **Custom repositories**
4. Add the repository:
  ```
  https://github.com/salvatore-disavio/ha-popup-blueprints
  ```
5. Category: **Integration**
6. Install and **restart Home Assistant**

After the restart, the blueprint will be available in:
**Settings → Automations & Scenes → Blueprints**

</details>

---

## 🖥️ Guida rapida

1. Crea una nuova automazione partendo dal blueprint  
**“Popup Blueprints (Browser Mod)”**
2. Inserisci il **Browser ID** del dispositivo su cui visualizzare il popup
3. Seleziona l’**entità trigger**
4. Scegli la **modalità di attivazione**:
- **to** → popup quando l’entità passa a uno stato specifico  
- **from_to** → popup solo nel passaggio da uno stato a un altro  
- **to_or_to** → popup quando l’entità passa a uno dei due stati indicati  
5. Compila i campi richiesti in base alla modalità scelta
6. Personalizza il popup (testi, icona, colori, preset grafico)
7. Decidi se il popup può essere chiuso cliccando all’esterno
8. Salva l’automazione e verifica il funzionamento

<details>
<summary><strong>English version</strong></summary>

## 🖥️ Quick guide (EN)

1. Create a new automation using the  
  **“Popup Blueprints (Browser Mod)”** blueprint
2. Enter the **Browser ID** of the target device
3. Select the **trigger entity**
4. Choose the **trigger mode**:
  - **to** → popup when the entity changes to a specific state  
  - **from_to** → popup only when changing from one state to another  
  - **to_or_to** → popup when the entity changes to one of the two configured states  
5. Fill in the required state fields
6. Customize the popup appearance (text, icon, colors, preset)
7. Choose whether the popup can be closed by clicking outside
8. Save the automation and test the behavior

</details>

---

## 🎨 Preset grafici disponibili

### Alert - Warning - Success - Custom

<p align="center">
  <img src="https://raw.githubusercontent.com/salvatore-disavio/ha-popup-blueprints/main/images/success_card.png" width="300">
  <img src="https://raw.githubusercontent.com/salvatore-disavio/ha-popup-blueprints/main/images/warning_card.png" width="300">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/salvatore-disavio/ha-popup-blueprints/main/images/custom_card.png" width="300">
  <img src="https://raw.githubusercontent.com/salvatore-disavio/ha-popup-blueprints/main/images/alert_card.png" width="300">
</p>

---
## 📦 Requisiti

- Home Assistant
- [Browser Mod](https://github.com/thomasloven/hass-browser_mod)
- [Button Card](https://github.com/custom-cards/button-card)

---

## ☕ Supporta il progetto (opzionale)

Questo progetto è **open source e liberamente utilizzabile**.  
Se lo trovi utile, puoi supportarne lo sviluppo con un contributo volontario:

👉 https://buymeacoffee.com/salvatore.disavio

---

## 🧑‍💻 Autore

Creato da **Salvatore Di Savio**

---

## 📄 Licenza

MIT License

