import sys, playsound
from tkinter import Tk, Button   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def main():
    # create a GUI window
    root = Tk()
    root.title("[*] Music Player")
    root.geometry("300x300")
    root.resizable(False, False)
    # create a button
    button = Button(root, text="Select a file", command=select_file)
    button.pack()
    # run the main loop
    root.mainloop()

def select_file():
    # ask for a file
    filename = askopenfilename()
    # play the file
    playsound(filename)

