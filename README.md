# Discord Chrome DevTools Enabler [![GitHub license](https://img.shields.io/github/license/Pooh-Shiesty/DiscordChromeDevToolsEnabler?style=flat-square)](https://github.com/Pooh-Shiesty/DiscordChromeDevToolsEnabler/blob/main/LICENSE)

> Tool to enable Chrome DevTools on Discord's Desktop app

This tool takes use of `settings.json` and adds a JSON key to allow Chrome DevTools to be used. It's also extremely lightweight as it doesn't use any pip packages, it only takes use of default Python libraries.

## Installing / Getting started

Prerequisites
* [Python](https://python.org/) (tested on 3.10)
* [Git](https://git-scm.com/)

`Windows`
```shell
python main.py
```

`Linux`
```shell
python3 main.py
```

When you execute the code it will automatically terminate all Discord processes and add a JSON key to your `settings.json` file which allows Chrome DevTools to be used. It will print out that Chrome DevTools has been enabled, how to use it in Discord, and to re-launch Discord. And if you launch it again it will print out that you already have Chrome DevTools enabled.

## Developing

### Built with
It has been purely built with Python itself, no extra libraries has been used.

## Licensing

This project is licensed under the MIT license, more information can be found [here](https://github.com/Pooh-Shiesty/DiscordChromeDevToolsEnabler/blob/main/LICENSE)
