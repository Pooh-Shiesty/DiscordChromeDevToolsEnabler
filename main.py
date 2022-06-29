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
    def __init__(self):
        self.appdata = getenv("APPDATA")
        self.localappdata = getenv("LOCALAPPDATA")
        self.json_key = "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"
        self.settings_file = "settings.json"
        self.process_name = "Discord.exe"
        self.discord_dir = "discord"
        self.discord_exe = join(self.localappdata, "Discord", "app-1.0.9005", self.process_name)
        self.app_dir = "DCDTE"
        self.app_path = join(self.appdata, self.app_dir)
        self.config_file = "config.json"
        self.config_path = join(self.appdata, self.app_dir, self.config_file)
        self.data = {
            "relaunch": False,
            "terminate": False,
        }
        self.r = Style.RESET_ALL
        self.cyan = Fore.LIGHTCYAN_EX
        self.red = Fore.LIGHTRED_EX
        self.yellow = Fore.LIGHTYELLOW_EX
        self.bright = Style.BRIGHT
        self.green = Fore.LIGHTGREEN_EX

    def mainMenu(self):
        self.clearScreen()
        choice = input(rf"""{self.r}{self.cyan}
    ___  ___   ___  _____  __ 
   /   \/ __\ /   \/__   \/__\
  / /\ / /   / /\ /  / /\/_\  
 / /_// /___/ /_//  / / //__  
/___,'\____/___,'   \/  \__/
{self.r}

  {self.yellow}1.{self.r} {self.bright}Enable DevTools{self.r}
  {self.yellow}2.{self.r} {self.bright}Disable DevTools{self.r}
  {self.yellow}3.{self.r} {self.bright}Configure Settings{self.r}
  {self.yellow}4.{self.r} {self.bright}Exit{self.r}

  {self.red}Input:{self.r} """)
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
                print(f"{self.r}{self.red}{self.bright}Invalid option!{self.r}")
                self.back(1)


    def back(self, time: int):
        sleep(time)
        self.clearScreen()
        self.mainMenu()


    def clearScreen(self):
        system("cls")


    def readConfig(self):
        if not exists(self.config_path):
            self.createConfig()
        
        with open(self.config_path, "r") as f:
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
        terminate = Fore.GREEN if (dict.get("terminate")) is True else Fore.RED
        self.clearScreen()
        choice = input(rf"""{self.r}{self.cyan}
 __      _   _   _                 
/ _\ ___| |_| |_(_)_ __   __ _ ___ 
\ \ / _ \ __| __| | '_ \ / _` / __|
_\ \  __/ |_| |_| | | | | (_| \__ \
\__/\___|\__|\__|_|_| |_|\__, |___/
                         |___/
{self.r}

    {self.yellow}1.{self.r} {relaunch}{self.bright}Automatically relaunch Discord{self.r}
    {self.yellow}2.{self.r} {terminate}{self.bright}Automatically terminate Discord{self.r}
    {self.yellow}3.{self.r} {self.bright}Back{self.r}

    {self.red}Input:{self.r} """)
        self.clearScreen()

        match choice:
            case "1":
                self.changeConfig("relaunch")
                self.changeSettings()
            case "2":
                self.changeConfig("terminate")
                self.changeSettings()
            case "3":
                self.back(0)

    def createConfig(self):
        makedirs(self.app_path)
        with open(self.config_path, "w") as f:
                dump(self.data, f, indent=4)


    def writeToConfig(self, data: dict):
        with open(self.config_path, "w") as f:
            dump(data, f, indent=4)


    def getSettings(self):
        with open(join(self.appdata, self.discord_dir, self.settings_file), "r") as f:
            return load(f)


    def disableDevTools(self):
        config = self.readConfig()
        dict = self.getSettings()
        if (dict.get(self.json_key) is False):
            print(f"{self.r}{self.yellow}{self.bright}Already disabled!{self.r}")
            self.back(1)
        else:
            try:
                dict[self.json_key] = False
                with open(join(self.appdata, self.discord_dir, self.settings_file), "w") as f:
                    dump(dict, f, indent=2)
                
                if (config.get("terminate")) is True:
                    system(f"taskkill /im {self.process_name} /F")
                if (config.get("relaunch")) is True:
                    try:
                        system(f"taskkill /im {self.process_name} /F")
                    except:
                        pass
                    system("start " + self.discord_exe)
                print(f"{self.r}{self.green}{self.bright}Disabled Chrome DevTools!{self.r}")
                self.back(2)
            except Exception as e:
                print(self.r + e)


    def enableDevTools(self):
        config = self.readConfig()
        dict = self.getSettings()
        if (dict.get(self.json_key) is True):
            print(f"{self.r}{self.yellow}{self.bright}Already enabled!{self.r}")
            self.back(1)
        else:
            try:
                dict[self.json_key] = True
                with open(join(self.appdata, self.discord_dir, self.settings_file), "w") as f:
                    dump(dict, f, indent=2)

                if (config.get("terminate")) is True:
                    system(f"taskkill /im {self.process_name} /F")
                if (config.get("relaunch")) is True:
                    try:
                        system(f"taskkill /im {self.process_name} /F")
                    except:
                        pass
                    system("start " + self.discord_exe)
                print(f"{self.r}{self.green}{self.bright}Enabled Chrome DevTools!\n{self.r}{self.cyan}{self.bright}CTRL + SHIFT + I{self.r}")
                self.back(2)
            except Exception as e:
                print(self.r + e)


    def main(self):
        self.mainMenu()
        

if __name__ == "__main__":
    EnableChromeDevTools().main()