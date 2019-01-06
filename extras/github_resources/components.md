# Components Index List

A house with Home Assistant can not work without a lot of components, below a brief summary of some of these. In the future I still have plans to expand it.

On this page you will find in addition to all the components that I use a reference to:

- The Home Assistant documentation (**HA Documentation**)
- The code that is used in my configuration (**On My Github**)
- References to stores (**Where to Buy**) where you can buy it yourself, if it is a physical product.

References to stores will mainly be Dutch webshops, because I live in this wonderful little country with its famous cheese, weed :no_smoking:, clogs :shoe:, windmills and tulips :tulip:.

If one of the links no longer works, let me know!

## Sensors

|Nr.|Device|HA Documentation|On My Github|
|:---:|:---|:---:|:---:|
|1.|FIBARO Smoke sensors|
|2.|FIBARO Door sensors|
|3.|FIBARO Motion sensors|
|4.|FIBARO Wall plug|
|5.|DSMR (Smart meter)|[DSMR Docs][dsmr-docs]|[DSMR YAML][dsmr-github]|
|6.|Aftership||[Aftership YAML][aftership-yaml] - [Aftership Python File][aftership-python]|
|7.|Buienradar|[Buienradar Docs][buienradar-docs]|[Buienradar YAML][buienradar-github]|
|8.|Cert Expiry|[Cert Expiry Docs][cert-expiry-docs]|[Cert Expiry YAML][cert-expiry-github]|
|9.|Command Line|
|10.|DNS ip|[DNS IP Docs][dns-ip-docs]|[DNS IP YAML][dnsip-github]|
|11.|Filesize|[Filesize Docs][filesize-docs]|[Filesize YAML][filesize-github]|
|12.|Nederlandse Spoorwegen|[Nederlandse Spoorwegen Docs][ns-docs]|[NS YAML][ns-github]|
|13.|PostNL|[PostNL Docs][postnl-docs]|[PostNL YAML][postnl-github]|
|14.|Speedtest|[Speedtest Docs][speedtest-docs]|[Speedtest YAML][speedtest-github]|
|15.|Versions|[Versions Docs][versions-docs]|[Versions YAML][versions-github]|
|16.|Template|
|17.|Travis Ci|[Travis Ci Docs][travis-ci-docs]|[Travis Ci YAML][travis-github]|
|18.|Gitlab Ci|[Github Ci Docs][github-ci-docs]|[Gitlab Ci YAML][gitlab-github]|

There are many more sensors that I use, but I have not had the time to put them here.

---

## Add-on Integrations

The nice thing about using [hass.io][hassio] are the add-ons, which allows you to easily add extra functionalities to your Home Assistant environment, in addition to all the other components that are already available for Home Assistant.

- **Documentation** column leads to the page on the community forum.
- **Github** column to the repository of the add-on.

|Nr.|Device|Documentation|Github Page|
|:---:|:---|:---:|:---:|
|1.|Grafana|[Community Page][grafana-community]|[Github][grafana-github]
|2.|IDE|[Community Page][ide-community]|[Github][ide-github]
|3.|InfluxDB|[Community Page][influxdb-community]|[Github][influxdb-github]
|4.|SSH & Web Terminal|[Community Page][ssh-web-terminal-community]|[Github][ssh-web-terminal-github]
|5.|Samba Share|[Add-on Page][samba-share-homeassistant]
|6.|Traccar|[Community Page][traccar-community]|[Github][traccar-github]
|7.|MotionEye|[Community Page][motioneye-community]|[Github][motioneye-github]

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
|1.|Yeelights|[YeeLight Docs][yeelight-wifi-bulb-docs]|[YeeLight YAML][yeelight-github]|[Banggood][yeelight-banggood]|

---

## Media

|Nr.|Device|HA Documentation|On My Github|Where to Buy|
|:---:|:---|:---:|:---:|:---:|
|1.|Google Chromecast|[Cast Docs][cast-docs]|[Cast YAML][cast-github]|
|2.|Philips TV|[Cast Docs][cast-docs]|[Cast YAML][cast-github]|

---

## Interfaces

|Nr.|Device|HA Documentation|On My Github|Where to Buy|
|:---:|:---|:---:|:---:|:---:|
|1.|Google home (mini)|[Google Assistant Docs][google-assistant-docs]|
|2.|Teclast P80 Pro (wall tablet)|
|3.|Lovelace UI|[Lovelace UI Docs][lovelace-ui-docs]|[Lovelace UI YAML][lovelace-ui-github]|
|4.|Home Assistant Cloud|[Nabu Casa Docs][nabu-casa-docs]||[Nabu Casa][nabu-casa-buy] (price: $5 per month)

---

## Other Hardware

|Nr.|Device|HA Documentation|On My Github|Where to Buy|
|:---:|:---|:---:|:---:|:---:|
|1.|Water fountain in the garden|
|2.| Doorbel (ACDB-7000AC) - CoCo |[RFXtrx Switch][rfxtrx-switch-docs] (use fire-event)|[RFXtrx Switch YAML][rfxtrx-switch-github]|

---

## Host Hardware

|Nr.|Device|Where to Buy|
|:---:|:---|:---:|
|1.|Intel Baby Canyon NUC7i5BNH|
|2.|16GB Ram (2x 8GB)|
|3.|Samsung 840 evo 500GB|

---

## Terms

Here I will name some terms / abbreviations.

- Coco = Click on Click off (in dutch: KlikaanKlikuit).

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
[versions-docs]:https://www.home-assistant.io/components/sensor.version/
[cert-expiry-docs]:https://www.home-assistant.io/components/sensor.cert_expiry/
[dns-ip-docs]:https://www.home-assistant.io/components/sensor.dnsip/

[grafana-community]: https://community.home-assistant.io/t/community-hass-io-add-on-grafana/54674
[ide-community]: https://community.home-assistant.io/t/community-hass-io-add-on-ide-based-on-cloud9/33810
[influxdb-community]: https://community.home-assistant.io/t/community-hass-io-add-on-influxdb/54491
[ssh-web-terminal-community]: https://community.home-assistant.io/t/community-hass-io-add-on-ssh-web-terminal/33820
[samba-share-homeassistant]: https://www.home-assistant.io/addons/samba/
[traccar-community]: https://community.home-assistant.io/t/community-hass-io-add-on-traccar/81407
[motioneye-community]: https://community.home-assistant.io/t/community-hass-io-add-on-motioneye/71826

[grafana-github]: https://github.com/hassio-addons/addon-grafana
[ide-github]: https://github.com/hassio-addons/addon-ide
[influxdb-github]: https://github.com/hassio-addons/addon-influxdb
[ssh-web-terminal-github]: https://github.com/hassio-addons/addon-ssh
[traccar-github]: https://github.com/hassio-addons/addon-traccar
[motioneye-github]: https://github.com/hassio-addons/addon-motioneye

[lovelace-ui-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/ui-lovelace.yaml
[postnl-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/postnl.yaml
[dsmr-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/smart_meter.yaml
[aftership-yaml]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/aftership.yaml
[aftership-python]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/custom_components/sensor/aftership.py
[rfxtrx-switch-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/switches/rfxtrx_switch.yaml
[yeelight-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/lights/yeelight.yaml
[versions-github]:https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/versions.yaml
[speedtest-github]:https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/speedtest.yaml
[buienradar-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/buienradar.yaml
[cast-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/cast.yaml
[filesize-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/system.yaml#L239
[dnsip-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/system.yaml#L245
[cert-expiry-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/system.yaml#L247
[ns-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/ns.yaml
[travis-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/packages/system.yaml#L269
[gitlab-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/components/sensors/gitlab_ci.yaml

[nabu-casa-buy]: https://www.nabucasa.com/
[hassio]: https://www.home-assistant.io/hassio/
[yeelight-banggood]:https://www.banggood.com/search/yeelight.html
