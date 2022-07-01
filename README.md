# Discord Chrome DevTools Enabler [![GitHub license](https://img.shields.io/github/license/Pooh-Shiesty/DiscordChromeDevToolsEnabler?style=flat-square)](https://github.com/Pooh-Shiesty/DiscordChromeDevToolsEnabler/blob/main/LICENSE)

> Tool to enable Chrome DevTools on the Discord Client

This tool takes use of `settings.json` and adds a JSON key to allow Chrome DevTools to be used. It's very lightweight since it only uses colorama for visual appearance.

## Installing

If you are on Windows you can get the latest version of DCDTE [here](https://github.com/Pooh-Shiesty/DiscordChromeDevToolsEnabler/releases/latest). If you are on a Linux or Unix-based system you can check out [Building](#building)

## Building

Prerequisites
* [Python](https://python.org/) (built with 3.10)

- Clone or download the repo

- It's highly recommended to create a virtual environment.  
    
    `Windows`
    ```shell
    python -m venv env
    .\env\Scripts\activate
    ```

    `Linux`
    ```shell
    python3 -m venv env
    source /env/Scripts/activate
    ```

- `pip install -r requirements.txt`
- `python -m nuitka --standalone main.py`
- Once the command has finished `main.dist` will contain a file named `main.exe`


## Licensing

This project is licensed under the MIT license, more information can be found [here](https://github.com/Pooh-Shiesty/DiscordChromeDevToolsEnabler/blob/main/LICENSE)
