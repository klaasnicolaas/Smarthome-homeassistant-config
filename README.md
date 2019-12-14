# Smart Home = Home Assistant

![header](/extras/img/header.png "header")

You will probably think, what is Home Assistant!? Well Home Assistant is a home automation platform running on Python 3. It is able to track and control all devices at home and offer a platform for automating control.

To inspire others I have set up this github and update it regularly with new code. Be free to use code from this repo for your own Home Assistant environment, keep in mind that you can not always copy everything line by line. If you can not get out, you can always contact me.

This is by the way not my first [Home Assistant][home-assistant] configuration that you can find on Github. Since this year I have a second Home Assistant installation, you can read all about it on the website [www.student-techlife.com](https://student-techlife.com) and you can find the [configuration/repository][student-techlife] here on Github.

## Status Information

| [![Gitlab CI][gitlabci-shield]][gitlabci] | [![GitHub Last Commit][last-commit-shield]][commits]|
|:---:|:---:|
| This shows whether the configuration in this repo is valid | This shows how up to date this repo is |
| [![GitHub issues][issues-shield]][issues] | [![HA Version][ha-version-shield]][home-assistant] |
| I now use the issues as a TODO list | This is the version that I am currently running with Home Assistant |
| [![Uptime Robot status][uptime-shield]][uptime-robot] | [![GitHub Activity][commits-shield]][commits] |
| I use Uptime Robot to monitor my instance from outside in case of crashes | Shows how active I am with this repo annually |
| [![GitHub Stars][stars-shield]][stars] | [![Buy Me A Fanta][paypal-shield]][paypal] |
| Please :star: this repo if you find it useful, like these people have | If this config was very helpfull, you could buy a fanta :tropical_drink: for me :smile: |

## Current Configuration

Recently I switched from a raspberry pi 3B+ to an Intel NUC. I noticed that the Pi for my house was no longer powerful enough to run all processes. That is why I invested in an Intel NUC at Christmas 2018, which is now smoothly running after a long transition in the 2018-2019 Christmas holiday. I also switched from hassbian to [hass.io][hassio] in docker.

So now I use an Intel NUC to run home assistant. In addition, I use a Z-wave stick to control devices that use the z-wave protocol and an RFX module for controlling devices that work on the 433mhz frequency band. Because the Intel NUC is hanging in the meter closet, the smart meter is also read via a P1 cable.

- [Intel Baby Canyon NUC7i5BNH][intel-nuc] - Inside it 16GB Ram, 500GB SSD and running [Ubuntu Server LTS][ubuntu-server].
- Using the [Hass.io installation][hassio-install].
- [Aeotec USB Z-Stick](<https://aeotec.com/z-wave-usb-stick>) - Z-Wave Plus
- [RFXCOM RFXtrx433E](<http://www.rfxcom.com/store/Transceivers/14103>)
- [P1 cable](<https://www.sossolutions.nl/slimme-meter-kabel>)
- Using also the [Lovelace UI](<https://www.home-assistant.io/lovelace/>)

## My House

Curious about what kind of integrations I have in my Home Assistant system? I made a very usefull list for others: [Check it out][components] (Last update: 6 Januari 2019).

## Grafana gas/energy consumption dashboard

I have built my own dashboard in grafana for my gas and energy consumption, which I can call through an iframe panel in Home Assistant. If you want to know more about this, [take a look here][useage-dashboard].

## Back-ups

Every Sunday at 3:00 am an [automation makes a snapshot][backup-github] of my installation. In the past it happened that the sd card of my Pi became corrupt and I lost everything. That's why this backup is also made locally on my Synology NAS automatically and this is fully automated. (Inspired by: [@adonno][adonno-github])

## Apps to control

Nothing is better than being able to control your own smart home from your phone or tablet.

- [HomeAssist](<https://play.google.com/store/apps/details?id=com.axzae.homeassistant&hl=nl>) (for android)
- [Home Assistant](<https://www.home-assistant.io/docs/ecosystem/ios/>) (for iOS)
- [Home Assistant](<https://www.home-assistant.io/docs/frontend/mobile/>) (As web app)

---

## Needing Help?

- [Home Assistant Homepage](<https://home-assistant.io/>)
- [Home Assistant Forums](<https://community.home-assistant.io/>)
- [Home Assistant Discord Chat](<https://discord.gg/c5DvZ4e>)
- [Other Featured Home Assistant Configurations](<https://home-assistant.io/cookbook/>)
- [Home Assistant GitHub Source Repository](<https://github.com/home-assistant/home-assistant>)
- [Official Home Assistant Demo](<https://home-assistant.io/demo/>)

## License

MIT License

Copyright (c) 2019 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/smarthome-homeassistant-config.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/Smarthome-homeassistant-config.svg?color=blue&style=plasticr
[stars-shield]: https://img.shields.io/github/stars/klaasnicolaas/Smarthome-homeassistant-config.svg
[ha-version-shield]: https://img.shields.io/badge/Home%20Assistant-0.103.0-blue.svg
[uptime-shield]: https://img.shields.io/uptimerobot/status/m781145866-63b6526d17827ec6eebe586f.svg
[gitlabci-shield]: https://gitlab.com/klaasnicolaas/Smarthome-homeassistant-config/badges/master/pipeline.svg
[paypal-shield]: https://img.shields.io/badge/BuyMeAFanta-Paypal-orange.svg
[issues-shield]: https://img.shields.io/github/issues/klaasnicolaas/Smarthome-homeassistant-config.svg

[commits]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/commits/master
[stars]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/stargazers
[home-assistant]: https://home-assistant.io
[uptime-robot]: https://uptimerobot.com
[gitlabci]: https://gitlab.com/klaasnicolaas/Smarthome-homeassistant-config/pipelines
[paypal]: https://www.paypal.me/dexterfpv
[issues]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/issues
[components]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/tree/master/extras/github_resources/components.md

[intel-nuc]: https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc7i5bnh.html
[ubuntu-server]: https://www.ubuntu.com/download/server
[hassio-install]: https://www.home-assistant.io/hassio/installation/#alternative-install-on-generic-linux-server
[hassio]: https://www.home-assistant.io/hassio/
[adonno-github]: https://github.com/adonno/Home-AssistantConfig
[backup-github]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/blob/master/automations/system/auto_backup.yaml
[useage-dashboard]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/tree/master/panels/iframes/consumption
[student-techlife]: https://github.com/klaasnicolaas/Student-homeassistant-config
