# Components Index List

A house with Home Assistant can not work without a lot of components, below a brief summary of some of these. In the future I still have plans to expand it.

On this page you will find in addition to all the components that I use a reference to:

- The Home Assistant documentation (**HA Documentation**)
- The code that is used in my configuration (**On My Github**)
- References to stores (**Where to Buy**) where you can buy it yourself, if it is a physical product.

References to stores will mainly be Dutch webshops, because I live in this wonderful little country with its famous cheese, weed :no_smoking:, clogs :shoe:, windmills and tulips :tulip:.

If one of the links no longer works, let me know!

## Sensors

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|FIBARO Smoke sensors|
|FIBARO Door sensors|
|FIBARO Motion sensors|
|FIBARO Wall plug|
|DSMR (Smart meter)|[DSMR Docs][dsmr-docs]|[DSMR YAML][dsmr-github]|
|Aftership||[Aftership YAML][aftership-yaml] - [Aftership Python File][aftership-python]|
|Buienradar|[Buienradar Docs][buienradar-docs]|
|Cert_Expiry|
|Command_Line|
|DNS ip|
|Filesize|[Filesize Docs][filesize-docs]|
|Nederlandse Spoorwegen|[Nederlandse Spoorwegen Docs][ns-docs]|
|PostNL|[PostNL Docs][postnl-docs]|[PostNL YAML][postnl-github]|
|Speedtest|[Speedtest Docs][speedtest-docs]|
|Versions|
|Template|
|Travis Ci|[Travis Ci Docs][travis-ci-docs]|
|Gitlab Ci|[Github Ci Docs][github-ci-docs]|

There are many more sensors that I use, but I have not had the time to put them here.

## Switches

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|KlikAanKlikUit devices (CoCo)|[RFXtrx Switch][rfxtrx-switch-docs]|[RFXtrx Switch YAML][rfxtrx-switch-github]|
|Doorbel|[RFXtrx Switch][rfxtrx-switch-docs] (use fire-event)|[RFXtrx Switch YAML][rfxtrx-switch-github]|

## Lights

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Yeelights|[YeeLight Docs][yeelight-wifi-bulb-docs]|[YeeLight YAML][yeelight-github]|

## Media

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Google Chromecast|[Cast Docs][cast-docs]|
|Philips TV|[Cast Docs][cast-docs]|

## Interfaces

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Google home (mini)|[Google Assistant Docs][google-assistant-docs]|
|Teclast P80 Pro (wall tablet)|
|Lovelace UI|[Lovelace UI Docs][lovelace-ui-docs]|[Lovelace UI YAML][lovelace-ui-github]|
|Home Assistant Cloud|[Nabu Casa Docs][nabu-casa-docs]||[Nabu Casa][nabu-casa-buy] (price: $5 per month)

## Other Hardware

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Water fountain in the garden|

[rfxtrx-switch-docs]: https://www.home-assistant.io/components/switch.rfxtrx/
[yeelight-wifi-bulb-docs]: https://www.home-assistant.io/components/light.yeelight/
[cast-docs]: https://www.home-assistant.io/components/cast/
[dsmr-docs]: https://www.home-assistant.io/components/sensor.dsmr/
[google-assistant-docs]: https://www.home-assistant.io/components/google_assistant/
[lovelace-ui-docs]: https://www.home-assistant.io/lovelace/
[nabu-casa-docs]: https://www.home-assistant.io/components/cloud/
[buienradar-docs]: https://www.home-assistant.io/components/sensor.buienradar/
[filesize-docs]: https://www.home-assistant.io/components/sensor.filesize/
[ns-docs]: https://www.home-assistant.io/components/sensor.nederlandse_spoorwegen/
[postnl-docs]: https://www.home-assistant.io/components/sensor.postnl/
[speedtest-docs]: https://www.home-assistant.io/components/sensor.speedtest/
[travis-ci-docs]: https://www.home-assistant.io/components/sensor.travisci/
[github-ci-docs]: https://www.home-assistant.io/components/sensor.gitlab_ci/

[lovelace-ui-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/ui-lovelace.yaml
[postnl-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/postnl.yaml
[dsmr-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/smart_meter.yaml
[aftership-yaml]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/aftership.yaml
[aftership-python]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/custom_components/sensor/aftership.py
[rfxtrx-switch-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/switches/rfxtrx_switch.yaml
[yeelight-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/lights/yeelight.yaml

[nabu-casa-buy]: https://www.nabucasa.com/
