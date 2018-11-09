# Smart Home - Home Assistant

You will probably think, what is Home Assistant!? Well Home Assistant is a home automation platform running on Python 3. It is able to track and control all devices at home and offer a platform for automating control.

To inspire others I have set up this github and update it regularly with new code. Be free to use code from this repo for your own Home Assistant environment, keep in mind that you can not always copy everything line by line. If you can not get out, you can always contact me.

## Information

| [![Travis CI][travis-shield]][travis] [![Gitlab CI][gitlabci-shield]][gitlabci] | [![GitHub Last Commit][last-commit-shield]][commits]|
|:---:|:---:|
| This shows whether the configuration in this repo is valid | This shows how up to date this repo is |
| [![GitHub issues][issues-shield]][issues] | [![HA Version][ha-version-shield]][home-assistant] |
| I now use the issues as a TODO list | This is the version that I am currently running with Home Assistant |
| [![Uptime Robot status][uptime-shield]][uptime-robot] | [![GitHub Activity][commits-shield]][commits] |
| I use Uptime Robot to monitor my instance from outside in case of crashes | Shows how active I am with this repo annually |
| [![GitHub Stars][stars-shield]][stars] | [![Buy Me A Fanta][paypal-shield]][paypal] |
| Please :star: this repo if you find it useful, like these people have | If this config was very helpfull, you could buy a fanta :tropical_drink: for me :smile: |

## Current Configuration

I use a raspberry pi 3rd generation to run home assistant. In addition, I use a Z-wave stick to control devices that use the z-wave protocol and an RFX module for controlling devices that work on the 433mhz frequency band. Because the raspberry pi is hanging in the meter closet, the smart meter is also read via a P1 cable.

- RaspberryPi 3B+ using the [Hassbian installation](<https://home-assistant.io/docs/installation/hassbian/>).
- [Aeotec USB Z-Stick](<https://aeotec.com/z-wave-usb-stick>) - Z-Wave Plus
- [RFXCOM RFXtrx433E](<http://www.rfxcom.com/store/Transceivers/14103>)
- [P1 cable](<https://www.sossolutions.nl/slimme-meter-kabel>)
- Using also the [Lovelace UI](<https://www.home-assistant.io/lovelace/>) (still in a beta).

## My House

Curious about what kind of integrations I have in my Home Assistant system? I made a very usefull list: [Check it out][components] (Last update: 9 November 2018).

## Apps to control

Nothing is better than being able to control your own smart home from your phone or tablet.

- [HomeAssist](<https://play.google.com/store/apps/details?id=com.axzae.homeassistant&hl=nl>) (for android)
- [Home Assistant](<https://www.home-assistant.io/docs/ecosystem/ios/>) (for iOS)
- [Home Assistant](<https://www.home-assistant.io/docs/frontend/mobile/>) (As web app)

## Needing Help?

- [Home Assistant Homepage](<https://home-assistant.io/>)
- [Home Assistant Forums](<https://community.home-assistant.io/>)
- [Home Assistant Discord Chat](<https://discord.gg/c5DvZ4e>)
- [Other Featured Home Assistant Configurations](https://home-assistant.io/cookbook/>)
- [Home Assistant GitHub Source Repository](<https://github.com/home-assistant/home-assistant>)
- [Official Home Assistant Demo](<https://home-assistant.io/demo/>)

## Useful Links:

- This will be updated soon.

[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/smarthome-homeassistant-config.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/Smarthome-homeassistant-config.svg?color=blue&style=plasticr
[travis-shield]: https://travis-ci.org/klaasnicolaas/Smarthome-homeassistant-config.svg?branch=master
[stars-shield]: https://img.shields.io/github/stars/klaasnicolaas/Smarthome-homeassistant-config.svg
[ha-version-shield]: https://img.shields.io/badge/Home%20Assistant-0.81.6-blue.svg
[uptime-shield]: https://img.shields.io/uptimerobot/status/m781145866-63b6526d17827ec6eebe586f.svg
[gitlabci-shield]: https://gitlab.com/klaasnicolaas/Smarthome-homeassistant-config/badges/master/pipeline.svg
[paypal-shield]: https://img.shields.io/badge/BuyMeAFanta-Paypal-orange.svg
[issues-shield]: https://img.shields.io/github/issues/klaasnicolaas/Smarthome-homeassistant-config.svg

[commits]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/commits/master
[travis]: https://travis-ci.org/klaasnicolaas/Smarthome-homeassistant-config
[stars]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/stargazers
[home-assistant]: https://home-assistant.io
[uptime-robot]: https://uptimerobot.com
[gitlabci]: https://gitlab.com/klaasnicolaas/Smarthome-homeassistant-config/pipelines
[paypal]: https://www.paypal.me/dexterfpv
[issues]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/issues
[components]: https://github.com/klaasnicolaas/Smarthome-homeassistant-config/tree/master/extras/github_resources/components.md