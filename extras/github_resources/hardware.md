# Hardware Index List

On this page you will find in addition to all the components that I use a reference to:

- The Home Assistant documentation (**HA Documentation**)
- The code that is used in my configuration (**On My Github**)
- References to stores (**Where to Buy**) where you can buy it yourself, if it is a physical product.

References to stores will mainly be Dutch webshops, because I live in this wonderful little country with its famous cheese, weed :no_smoking:, clogs :shoe:, windmills and tulips :tulip:.

If one of the links no longer works, let me know!

## Sensors

|Nr.|Device|Where to Buy|
|:---:|:---|:---:|
|1.|FIBARO Smoke sensors||
|2.|FIBARO Door sensors||
|3.|FIBARO Motion sensors||
|4.|FIBARO Wall plug||
|5.|Xiaomi Window Door Sensors|
|6.|Xiaomi Temperature & Humidity Sensors|

---

## Switches

|Nr.|Device|HA Documentation|On My Github|Where to Buy|
|:---:|:---|:---:|:---:|:---:|
|1.|Wall Plug (ACD3-1000R) - CoCo |[RFXtrx Switch][rfxtrx-switch-docs]|[RFXtrx Switch YAML][rfxtrx-switch-github]|
|2.|Mini Built-in Switch (AWMR-230) - CoCo |[RFXtrx Switch][rfxtrx-switch-docs]|[RFXtrx Switch YAML][rfxtrx-switch-github]|

---

## Lights

|Nr.|Device|HA Documentation|On My Github|Where to Buy|
|:---:|:---|:---:|:---:|:---:|
|1.|Yeelights|[YeeLight Docs][yeelight-wifi-bulb-docs]|[YeeLight YAML][yeelight-github]|[Banggood][yeelight-banggood]

---

## Media

|Nr.|Device|HA Documentation|On My Github|
|:---:|:---|:---:|:---:|:---:|
|1.|Google Chromecast|[Cast Docs][cast-docs]|[Cast YAML][cast-github]|
|2.|Philips TV|[Cast Docs][cast-docs]|[Cast YAML][cast-github]|

---

## Interfaces

|Nr.|Device|HA Documentation|On My Github|Where to Buy|
|:---:|:---|:---:|:---:|:---:|
|1.| Google home (mini) |[Google Assistant Docs][google-assistant-docs]|
|2.| Lovelace UI |[Lovelace UI Docs][lovelace-ui-docs]|[Lovelace UI YAML][lovelace-ui-github]|
|3.| Home Assistant Cloud |[Nabu Casa Docs][nabu-casa-docs]||[Nabu Casa][nabu-casa-buy] (price: $5 per month)

---

## Other Hardware

|Nr.|Device|HA Documentation|On My Github|
|:---:|:---|:---:|:---:|:---:|
|1.| Water fountain in the garden |
|2.| Doorbel (ACDB-7000AC) - CoCo |[RFXtrx Switch][rfxtrx-switch-docs] (use fire-event)|[RFXtrx Switch YAML][rfxtrx-switch-github]|

---

## Terms

Here I will name some terms / abbreviations.

- Coco = Click on Click off (in dutch: KlikaanKlikuit).

[rfxtrx-switch-docs]: https://www.home-assistant.io/components/switch.rfxtrx/
[yeelight-wifi-bulb-docs]: https://www.home-assistant.io/components/light.yeelight/
[cast-docs]: https://www.home-assistant.io/components/cast/
[google-assistant-docs]: https://www.home-assistant.io/components/google_assistant/
[lovelace-ui-docs]: https://www.home-assistant.io/lovelace/
[nabu-casa-docs]: https://www.home-assistant.io/components/cloud/

[grafana-github]: https://github.com/hassio-addons/addon-grafana
[ide-github]: https://github.com/hassio-addons/addon-ide
[influxdb-github]: https://github.com/hassio-addons/addon-influxdb
[ssh-web-terminal-github]: https://github.com/hassio-addons/addon-ssh
[motioneye-github]: https://github.com/hassio-addons/addon-motioneye

[lovelace-ui-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/ui-lovelace.yaml
[rfxtrx-switch-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/switches/rfxtrx_switch.yaml
[yeelight-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/lights/yeelight.yaml
[cast-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/cast.yaml

[nabu-casa-buy]: https://www.nabucasa.com/
[hassio]: https://www.home-assistant.io/hassio/
[yeelight-banggood]:https://www.banggood.com/search/yeelight.html
