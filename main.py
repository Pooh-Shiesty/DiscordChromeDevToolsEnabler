from json import dump, load
from os import getenv, system
from os.path import join
from sys import exit
from time import sleep

class EnableChromeDevTools():
    def __init__(self):
        self.appdata = getenv("APPDATA")
        self.key = "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"
        self.config = "settings.json"
        self.name = "Discord.exe"
        self.dir = "discord"

    def readSettings(self):
        with open(join(self.appdata, self.dir, self.config), "r") as f:
            return load(f)

    def enableDevTools(self):
        if self.key in self.readSettings():
            print("Chrome DevTools already enabled!")
            sleep(2)
            exit()
        else:
            dict = self.readSettings()
            dict[self.key] = True

            try:
                with open(join(self.appdata, self.dir, self.config), "w") as f:
                    dump(dict, f, indent=2)

                system("taskkill /im Discord.exe /F")
                print("Chrome DevTools enabled!\nPlease re-launch Discord!\nCTRL + SHIFT + I to enable Chrome DevTools :)\n")
                sleep(5)
                exit()
            except Exception as e:
                print(e)

    def main(self):
        self.enableDevTools()

if __name__ == "__main__":
    EnableChromeDevTools().main()
else:
    print("Error!")
