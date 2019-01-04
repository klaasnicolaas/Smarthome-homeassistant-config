# Components Index List

A house with Home Assistant can not work without a lot of components, below a brief summary of some of these. In the future I still have plans to expand it.

On this page you will find in addition to all the components that I use a reference to:

- The Home Assistant documentation (**HA Documentation**)
- The code that is used in my configuration (**On My Github**)
- References to stores (**Where to Buy**) where you can buy it yourself, if it is a physical product.

References to stores will mainly be Dutch webshops, because I live in this wonderful little country with its famous cheese, weed :no_smoking:, clogs :shoe:, windmills and tulips :tulip:.

If one of the links no longer works, let me know!

## Sensors

|Device|HA Documentation|On My Github|
|:---|:---:|:---:|
|FIBARO Smoke sensors|
|FIBARO Door sensors|
|FIBARO Motion sensors|
|FIBARO Wall plug|
|DSMR (Smart meter)|[DSMR Docs][dsmr-docs]|[DSMR YAML][dsmr-github]|
|Aftership||[Aftership YAML][aftership-yaml] - [Aftership Python File][aftership-python]|
|Buienradar|[Buienradar Docs][buienradar-docs]|[Buienradar YAML][buienradar-github]|
|Cert Expiry|[Cert Expiry Docs][cert-expiry-docs]|[Cert Expiry YAML][cert-expiry-github]|
|Command Line|
|DNS ip|[DNS IP Docs][dns-ip-docs]|[DNS IP YAML][dnsip-github]|
|Filesize|[Filesize Docs][filesize-docs]|[Filesize YAML][filesize-github]|
|Nederlandse Spoorwegen|[Nederlandse Spoorwegen Docs][ns-docs]|[NS YAML][ns-github]|
|PostNL|[PostNL Docs][postnl-docs]|[PostNL YAML][postnl-github]|
|Speedtest|[Speedtest Docs][speedtest-docs]|[Speedtest YAML][speedtest-github]|
|Versions|[Versions Docs][versions-docs]|[Versions YAML][versions-github]|
|Template|
|Travis Ci|[Travis Ci Docs][travis-ci-docs]|[Travis Ci YAML][travis-github]|
|Gitlab Ci|[Github Ci Docs][github-ci-docs]|[Gitlab Ci YAML][gitlab-github]|

There are many more sensors that I use, but I have not had the time to put them here.

---

## Add-on Integrations

The nice thing about using [hass.io][hassio] are the add-ons, which allows you to easily add extra functionalities to your Home Assistant environment, in addition to all the other components that are already available for Home Assistant.

- **Documentation** column leads to the page on the community forum.
- **Github** column to the repository of the add-on.

|Device|Documentation|Github Page|
|:---|:---:|:---:|
|Grafana|[Community Page][grafana-community]|[Github][grafana-github]
|IDE|[Community Page][ide-community]|[Github][ide-github]
|InfluxDB|[Community Page][influxdb-community]|[Github][influxdb-github]
|SSH & Web Terminal|[Community Page][ssh-web-terminal-community]|[Github][ssh-web-terminal-github]
|Samba Share|[Add-on Page][samba-share-homeassistant]
|Traccar|[Community Page][traccar-community]|[Github][traccar-github]
|MotionEye|[Community Page][motioneye-community]|[Github][motioneye-github]

---

## Switches

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|KlikAanKlikUit devices (CoCo)|[RFXtrx Switch][rfxtrx-switch-docs]|[RFXtrx Switch YAML][rfxtrx-switch-github]|
|Doorbel|[RFXtrx Switch][rfxtrx-switch-docs] (use fire-event)|[RFXtrx Switch YAML][rfxtrx-switch-github]|

---

## Lights

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Yeelights|[YeeLight Docs][yeelight-wifi-bulb-docs]|[YeeLight YAML][yeelight-github]|[Banggood][yeelight-banggood]|

---

## Media

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Google Chromecast|[Cast Docs][cast-docs]|[Cast YAML][cast-github]|
|Philips TV|[Cast Docs][cast-docs]|[Cast YAML][cast-github]|

---

## Interfaces

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Google home (mini)|[Google Assistant Docs][google-assistant-docs]|
|Teclast P80 Pro (wall tablet)|
|Lovelace UI|[Lovelace UI Docs][lovelace-ui-docs]|[Lovelace UI YAML][lovelace-ui-github]|
|Home Assistant Cloud|[Nabu Casa Docs][nabu-casa-docs]||[Nabu Casa][nabu-casa-buy] (price: $5 per month)

---

## Other Hardware

|Device|HA Documentation|On My Github|Where to Buy|
|:---|:---:|:---:|:---:|
|Water fountain in the garden|

---

## Host Hardware

|Device|Where to Buy|
|:---|:---:|
|Intel Baby Canyon NUC7i5BNH|
|16GB Ram (2x 8GB)|
|Samsung 840 evo 500GB|

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
