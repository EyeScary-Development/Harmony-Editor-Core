#Harmony NEW code editor core version 1.1
#Copyright Eyescary development 2026
#Modified? []

#imports
import extensions
import os

#put your imports here

class editor:
    def openfile(self): #copies the file contents to self.lines
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except:
            return []
        
    def write(self): #writes self.lines to the file
        with open(self.filename, "w") as file:
            file.write(''.join(self.lines))

    def printfilecore(self): #basic print file function
        os.system("cls" if os.name == "nt" else "clear")
        linenum = 1
        for item in self.lines:
            print(str(linenum)+"|"+item, end="")
            linenum+=1

    def main(self): #main editor function
        editor.printfilecore(self)
        userInput=input("|")
        if userInput.startswith(":"):
            self.lines = extensions.commands(userInput.strip(), self.lines, self.filename, self.extension)
        else:
            self.lines.append(userInput+'\n')
        editor.write(self)

    def __init__(self): #init menu
        name=input("what is the name of the file you wish to edit?: ")
        if "." in name:
            self.extension = "." + name.split(".")[1]
            self.filename = name
        else:
            self.extension = input("what is the extension of the file?: ")
            if not self.extension.startswith("."):
                self.extension = "." + self.extension
            self.filename = name + self.extension
        self.lines = editor.openfile(self)

def main():
    instance = editor()
    while True:
        instance.main()

if __name__ == "__main__":
    main()