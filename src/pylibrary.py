import os
import sys

def get_file_names():
    file_names = []
    for file_name in os.listdir():
        if file_name.endswith(".py"):
            file_name = file_name[:-3]
            file_names.append(file_name)
    return file_names

# function to import every file in a list
def import_files(file_names):
    modules = list(map(__import__, (file_names)))
    return modules

class Library:
    def __init__(self, modules):
        self.modules = modules
        self.file_names = get_file_names()
    def area3dcalc(self):
        area3dcalc = self.modules[self.file_names.index("area3dcalc")]
        return area3dcalc
    def areacalculator(self):
        areacalculator = self.modules[self.file_names.index("areacalculator")]
        return areacalculator
    def birthday_calculator(self):
        birthday_calculator = self.modules[self.file_names.index("birthday_calculator")]
        return birthday_calculator
    def clock(self):
        clock = self.modules[self.file_names.index("clock")]
        return clock
    def countdown(self):
        countdown = self.modules[self.file_names.index("countdown")]
        return countdown
    def dad_joke(self):
        dad_joke = self.modules[self.file_names.index("dad_joke")]
        return dad_joke
    def diceroller(self):
        diceroller = self.modules[self.file_names.index("diceroller")]
        return diceroller
    def dictionary(self):
        dictionary = self.modules[self.file_names.index("dictionary")]
        return dictionary
    def DVDCorner(self):
        dvdcorner = self.modules[self.file_names.index("DVDCorner")]
        return dvdcorner
    def emails(self):
        emails = self.modules[self.file_names.index("emails")]
        return emails
    def filesystem(self):
        filesystem = self.modules[self.file_names.index("filesystem")]
        return filesystem
    def githubuser(self):
        githubuser = self.modules[self.file_names.index("githubuser")]
        return githubuser
    def guessthenumber(self):
        guessthenumber = self.modules[self.file_names.index("guessthenumber")]
        return guessthenumber
    def interest(self):
        interest = self.modules[self.file_names.index("interest")]
        return interest
    def musicplayer(self):
        musicplayer = self.modules[self.file_names.index("musicplayer")]
        return musicplayer
    def passwordgen(self):
        passwordgen = self.modules[self.file_names.index("passwordgen")]
        return passwordgen
    def quadratics(self):
        quadratics = self.modules[self.file_names.index("quadratics")]
        return quadratics
    def steganography(self):
        steganography = self.modules[self.file_names.index("steganography")]
        return steganography
    def strings(self):
        strings = self.modules[self.file_names.index("strings")]
        return strings
    def urlchecker(self):
        urlchecker = self.modules[self.file_names.index("urlchecker")]
        return urlchecker
    def wordcounter(self):
        wordcounter = self.modules[self.file_names.index("wordcounter")]
        return wordcounter
    def colourconverter(self):
        colourconverter = self.modules[self.file_names.index("colourconverter")]
        return colourconverter 

def main():
    moduleList = get_file_names()
    lib = Library(import_files(moduleList))
    pickmodule(moduleList, lib)
    pass

def pickmodule(moduleList, lib):
    print("[*] Pick a module to use:\n")
    for i in range(len(moduleList)):
        print(str(i+1) + ": " + moduleList[i])
    module = int(input("\nEnter a number:\n"))
    for i in range(len(moduleList)):
        if module == i+1:
            print("\n" + moduleList[i] + " selected\n")
            # print("\n" + moduleList[i].__doc__ + "\n")
            module = lib.__getattribute__(moduleList[i])
            module().main()
            break

if __name__ == "__main__":
    main()
    sys.exit(0)