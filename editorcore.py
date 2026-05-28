#Harmony NEW code editor core version 1.0.1
#Copyright Eyescary development 2026
#Modified? []

import extensions
import os

class editor:
    def openfile(filename):
        try:
            with open(filename, "r") as file:
                return file.readlines()
        except:
            return []
        
    def write(self, filename):
        with open(filename, "w") as file:
            for item in self.lines:
                file.write(item)

    def printfilecore(self):
        os.system("cls" if os.name == "nt" else "clear")
        linenum = 1
        for item in self.lines:
            print(str(linenum)+"|"+item, end="")
            linenum+=1

    def main(self):
        editor.printfilecore(self)
        userInput=input("|")
        if userInput.startswith(":"):
            self.lines = extensions.commands(userInput.strip(), self.lines, self.filename, self.extension)
        else:
            self.lines.append(userInput+'\n')
        editor.write(self, self.filename)

    def __init__(self):
        name=input("what is the name of the file you wish to edit?: ")
        if "." in name:
            self.extension = "." + name.split(".")[1]
            self.filename = name
        else:
            self.extension = input("what is the extension of the file?: ")
            if not self.extension.startswith("."):
                self.extension = "." + self.extension
            self.filename = name + self.extension
        print(self.filename, self.extension)
        self.lines = editor.openfile(self.filename)


instance = editor()
while True:
    instance.main()