from os import name

if name != "nt":
    print("Only Windows OS is supported!")
    exit()
    
from json import dump, load
from os import getenv, makedirs, system, startfile
from os.path import exists, join
from sys import exit
from time import sleep
from colorama import init, Fore, Style
init()

class EnableChromeDevTools():

    APPDATA = getenv("APPDATA")
    LOCALAPPDATA = getenv("LOCALAPPDATA")
    JSON_KEY = "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"
    SETTINGS_FILE = "settings.json"
    PROCESS_NAME = "Discord.exe"
    DISCORD_DIR = "discord"
    DISCORD_EXE = join(LOCALAPPDATA, "Discord", "app-1.0.9005", PROCESS_NAME)
    APP_DIR = "DCDTE"
    APP_PATH = join(APPDATA, APP_DIR)
    CONFIG_FILE = "config.json"
    CONFIG_PATH = join(APPDATA, APP_DIR, CONFIG_FILE)
    CONFIG_DATA = {
        "relaunch": False,
    }

    # colors
    RESET = Style.RESET_ALL
    CYAN = Fore.LIGHTCYAN_EX
    RED = Fore.LIGHTRED_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    BRIGHT = Style.BRIGHT
    GREEN = Fore.LIGHTGREEN_EX

    def mainMenu(self):
        self.clearScreen()
        choice = input(rf"""{self.RESET}{self.CYAN}
    ___  ___   ___  _____  __ 
   /   \/ __\ /   \/__   \/__\
  / /\ / /   / /\ /  / /\/_\  
 / /_// /___/ /_//  / / //__  
/___,'\____/___,'   \/  \__/
{self.RESET}

  {self.YELLOW}1.{self.RESET} {self.BRIGHT}Enable DevTools{self.RESET}
  {self.YELLOW}2.{self.RESET} {self.BRIGHT}Disable DevTools{self.RESET}
  {self.YELLOW}3.{self.RESET} {self.BRIGHT}Configure Settings{self.RESET}
  {self.YELLOW}4.{self.RESET} {self.BRIGHT}Exit{self.RESET}

  {self.RED}Input:{self.GREEN} """)
        self.clearScreen()

        match choice:
            case "1":
                self.enableDevTools()
            case "2":
                self.disableDevTools()
            case "3":
                self.changeSettings()
            case "4":
                exit()
            case other:
                print(f"{self.RESET}{self.RED}{self.BRIGHT}Invalid option!{self.RESET}")
                self.back(1)


    def back(self, time: int):
        sleep(time)
        self.clearScreen()
        self.mainMenu()


    def clearScreen(self):
        system("cls")


    def readConfig(self):
        if not exists(self.CONFIG_PATH):
            self.createConfig()
        
        with open(self.CONFIG_PATH, "r") as f:
            return load(f)


    def changeConfig(self, json_key):
        dict = self.readConfig()
        if dict[json_key]:
            dict[json_key] = False
        else:
            dict[json_key] = True
        self.writeToConfig(dict)

    def changeSettings(self):
        dict = self.readConfig()
        relaunch = Fore.GREEN if (dict.get("relaunch")) is True else Fore.RED
        self.clearScreen()
        choice = input(rf"""{self.RESET}{self.CYAN}
 __      _   _   _                 
/ _\ ___| |_| |_(_)_ __   __ _ ___ 
\ \ / _ \ __| __| | '_ \ / _` / __|
_\ \  __/ |_| |_| | | | | (_| \__ \
\__/\___|\__|\__|_|_| |_|\__, |___/
                         |___/
{self.RESET}

    {self.YELLOW}1.{self.RESET} {relaunch}{self.BRIGHT}Automatically relaunch Discord{self.RESET}
    {self.YELLOW}2.{self.RESET} {self.BRIGHT}Back{self.RESET}

    {self.RED}Input:{self.RESET} """)
        self.clearScreen()

        match choice:
            case "1":
                self.changeConfig("relaunch")
                self.changeSettings()
            case "2":
                self.back(0)
            case other:
                print(f"{self.RESET}{self.RED}{self.BRIGHT}Invalid option!{self.RESET}")
                self.back(1)

    def createConfig(self):
        makedirs(self.APP_PATH)
        with open(self.CONFIG_PATH, "w") as f:
                dump(self.CONFIG_DATA, f, indent=4)


    def writeToConfig(self, data: dict):
        with open(self.CONFIG_PATH, "w") as f:
            dump(data, f, indent=4)


    def getSettings(self):
        with open(join(self.APPDATA, self.DISCORD_DIR, self.SETTINGS_FILE), "r") as f:
            return load(f)


    def disableDevTools(self):
        config = self.readConfig()
        dict = self.getSettings()
        if (dict.get(self.JSON_KEY) is False):
            print(f"{self.RESET}{self.YELLOW}{self.BRIGHT}Already disabled!{self.RESET}")
            self.back(1)
        else:
            try:
                dict[self.JSON_KEY] = False
                with open(join(self.APPDATA, self.DISCORD_DIR, self.SETTINGS_FILE), "w") as f:
                    dump(dict, f, indent=2)
                
                if (config.get("relaunch")) is True:
                    try:
                        system(f"taskkill /im {self.PROCESS_NAME} /F")
                    except:
                        pass
                    system("start " + self.DISCORD_EXE)

                print(f"{self.RESET}{self.GREEN}{self.BRIGHT}Disabled Chrome DevTools!{self.RESET}")
                self.back(2)
            except Exception as e:
                print(self.RESET + e)


    def enableDevTools(self):
        config = self.readConfig()
        dict = self.getSettings()
        if (dict.get(self.JSON_KEY) is True):
            print(f"{self.RESET}{self.YELLOW}{self.BRIGHT}Already enabled!{self.RESET}")
            self.back(1)
        else:
            try:
                dict[self.JSON_KEY] = True
                with open(join(self.APPDATA, self.DISCORD_DIR, self.SETTINGS_FILE), "w") as f:
                    dump(dict, f, indent=2)

                if (config.get("relaunch")) is True:
                    try:
                        system(f"taskkill /im {self.PROCESS_NAME} /F")
                    except:
                        pass
                    system("start " + self.DISCORD_EXE)

                print(f"{self.RESET}{self.GREEN}{self.BRIGHT}Enabled Chrome DevTools!\n{self.RESET}{self.CYAN}{self.BRIGHT}CTRL + SHIFT + I{self.RESET}")
                self.back(2)
            except Exception as e:
                print(self.RESET + e)


    def main(self):
        self.mainMenu()
        

if __name__ == "__main__":
    EnableChromeDevTools().main()