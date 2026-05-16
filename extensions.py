#Harmony code editor EXTENDED FUNCTIONS version 1.0
#Copyright EyeScary Development 2026
#Uses some code from Stronge by EyeScary Development

#Imports
import os
from typing import (List, Any)
from pathlib import Path

#Add your imports here

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
