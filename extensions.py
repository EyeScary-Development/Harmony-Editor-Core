#Harmony code editor EXTENDED FUNCTIONS version 0.next developer build
#Copyright EyeScary Development 2026
#Uses some code from Stronge by EyeScary Development
#How did you get this?

#Imports
import os
from typing import (List, Any)
import tkinter # tkinter is used here to make editing a line compatible everywhere (clunkier but readline is only nix)
from pathlib import Path

#variables


#functions

#handles commands
def commands(userInput: str, lines: List[Any], filename, extension):
    command = userInput.split()[0]
    match command:
        case ":q" | ":x" | ":exit":
            os.system("cls" if os.name == "nt" else "clear")
            exit(0)
        case _:
            print("invalid command")
            input("press enter to continue: ")
    return lines


def clearfile():
    return []