from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    print("[*] Word Counter")
    print("[*] Choose your file.")
    filename = choosefile()
    count = word_count(filename)
    print("[*] There are", count, "words in", filename, ".")

def choosefile():
    Tk().withdraw()
    filename = askopenfilename()
    return filename

def word_count(filename):
    # open the file
    file = open(filename, "r")
    # read the file
    text = file.read()
    # split the text into a list of words
    words = text.split()
    # count the amount of words
    count = len(words)
    # close the file
    file.close()
    # return the count
    return count



