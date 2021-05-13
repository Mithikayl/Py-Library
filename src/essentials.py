import os, sys
# this file is ONLY to be imported into others for repetetive functions that shouldn't be written again and again
def clear():
    if sys.platform == "win32": # check if win
        os.system('cls') # windows syntax
    else: 
        os.system('clear') # mac & linux syntax

guessnumguessed = False

