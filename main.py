from os import name

if name != "nt":
    exit()
    
from json import dump, load
from os import getenv, makedirs, system
from os.path import exists, join
from sys import exit
from time import sleep


class EnableChromeDevTools():
    def __init__(self):
        self.appdata = getenv("APPDATA")
        self.key = "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"
        self.settings_file = "settings.json"
        self.name = "Discord.exe"
        self.dir = "discord"
        self.app_dir = "CDTenabler"
        self.app_path = join(self.appdata, self.app_dir)
        self.config_file = "config.json"
        self.config_path = join(self.appdata, self.app_dir, self.config_file)
        self.data = {
            "autoUpdate": None,
        }


    def mainMenu(self):
        choice = input("1. Enable DevTools\n2. Disable DevTools\n3. Exit\n\nInput: ")
        self.clearScreen()

        if choice == "1":
            self.enableDevTools()
        elif choice == "2":
            self.disableDevTools()
        elif choice == "3":
            exit()
        else:
            print("Invalid option!\nPlease try again!")
            self.back(2)


    def back(self, time: int):
        sleep(time)
        self.clearScreen()
        self.mainMenu()


    def clearScreen(self):
        system("cls")


    def readConfig(self):
        if not exists(self.config_path):
            self.createConfig()
        else:
            with open(self.config_path, "r") as f:
                return load(f)


    def createConfig(self):
        makedirs(self.app_dir)
        with open(self.config_path, "w") as f:
                dump(self.data, f, indent=4)


    def writeToConfig(self, data: dict):
        with open(self.config_path, "w") as f:
            dump(data, f, indent=4)


    def getSettings(self):
        with open(join(self.appdata, self.dir, self.settings_file), "r") as f:
            return load(f)


    def disableDevTools(self):
        if self.key is False in self.getSettings():
            print("Chrome DevTools already disabled!")
            self.back(2)
        else:
            dict = self.getSettings()
            dict[self.key] = False

            try:
                with open(join(self.appdata, self.dir, self.settings_file), "w") as f:
                    dump(dict, f, indent=2)
                
                system("taskkill /im Discord.exe /F")
                print("Chrome DevTools disabled!\nPlease re-launch Discord!\n")
                self.back(3)
            except Exception as e:
                print(e)


    def enableDevTools(self):
        if self.key is True in self.getSettings():
            print("Chrome DevTools already enabled!")
            self.back(2)
        else:
            dict = self.getSettings()
            dict[self.key] = True

            try:
                with open(join(self.appdata, self.dir, self.settings_file), "w") as f:
                    dump(dict, f, indent=2)

                system("taskkill /im Discord.exe /F")
                print("Chrome DevTools enabled!\nPlease re-launch Discord!\nCTRL + SHIFT + I to use Chrome DevTools\n")
                self.back(5)
            except Exception as e:
                print(e)


    def main(self):
        self.mainMenu()
        

if __name__ == "__main__":
    EnableChromeDevTools().main()
else:
    print("Error!")
