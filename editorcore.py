#Harmony editor CORE version 1.0
#Copyright EyeScary Development
#Uses some code from Stronge by EyeScary Development
#Modified? []
import extensions
import os

#put your imports here


#variables
lines=[]
filename=...
extension=...

#functions

#opens the file
def openfile(filename):
    with open(filename, "r") as file:
        return file.readlines()

#write to the file
def write(filename, extension):
    global lines
    with open(filename, "w") as file:
        for item in lines:
            file.write(item)

#core print file functionality (no syntax highlighting, build your own and replace all references to printfilecore with extensions.customprintfile)            
def printfilecore():
   linenum = 1
   global lines
   for item in lines:
            print(str(linenum)+"|"+item, end="")
            linenum+=1

#editor function
def editor():
    global lines
    global filename
    global extension
    os.system("cls" if os.name == "nt" else "clear")
    printfilecore()
    userInput=input("|")
    if userInput.startswith(":"):
        lines = extensions.commands(userInput.strip(), lines, filename, extension)
    else:
        lines.append(userInput+'\n')
    write(filename, extension)

#main function
def main():
    global filename, extension, lines
    name=input("what is the name of the file you wish to edit?: ")
    if "." in name:
        extension = "." + name.split(".")[1]
        filename = name
    else:
        extension = input("what is the extension of the file?: ")
        if not extension.startswith("."):
            extension = "." + extension
        filename = name + extension
    print(filename, extension)
    try:
        lines = openfile(filename)
    except FileNotFoundError:
        lines=[]
    while True:
        editor()

if __name__ == "__main__":
    main()
