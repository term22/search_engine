# David Burg
# 1/26/23
# Drive Storage Program

# Imports
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess
import os

# Important Variables
ourFiles = []

# Obtains the current background color
def getBackgroundColor():
    file = open("csc116/color.txt", "r")
    color = file.read()
    file.close()
    return color

# Obtains all of the documents the user contains
def loadDocs():
    clearFiles()
    files = os.listdir("csc116/search_engine/files/docs")
    x_coord = 100
    y_coord = 100
    for file in files:
        myFile = tk.Label(text=(file + "\n"))
        ourFiles.append(myFile)
        myFile.place(x=x_coord, y=y_coord)
        y_coord += 50

# Obtains all of the pics the user contains
def loadImages():
    clearFiles()
    files = os.listdir("csc116/search_engine/files/pics")
    x_coord = 100
    y_coord = 100
    for file in files:
        myFile = tk.Label(text=(file + "\n"))
        ourFiles.append(myFile)
        myFile.place(x=x_coord, y=y_coord)
        y_coord += 50

# Clears all of the results from the screen
def clearFiles():
    for label in ourFiles:
        label.destroy()
    ourFiles.clear()

# Goto Search Engine
def gotoSearchEngine():
    window.destroy()
    subprocess.call(['python', 'csc116/search_engine/search-engine.py'])

# Goto text Editor
def gotoTextEditor():
    subprocess.call(['python', 'csc116/search_engine/editor.py'])

# Refresh drive
def refreshDrive():
    window.destroy()
    subprocess.call(['python', 'csc116/search_engine/drive.py'])

# Contains file
def containsFile(file):
    files = os.listdir("csc116/search_engine/files/docs")
    for i in files:
        if file + ".txt" == i:
            return True
    return False

# Goto Notepad
def gotoNotepad():
    myFile = filename.get()
    if myFile == "" or ".txt" in myFile:
        messagebox.showerror("Error", "Please Enter a valid filename")
    else:
        if containsFile(myFile):
            ourFile = "notepad.exe csc116/search_engine/files/docs/" + myFile + ".txt"
            os.system(ourFile)
        else:
            messagebox.showerror("Error", "Given file does not exist")

# Main GUI Code

# Setup Window
window = tk.Tk()
window.title("Drive")
window.geometry("500x500")
window.configure(bg=getBackgroundColor())

# Important Buttons
Button(window, text="Docs", command=gotoTextEditor).place(x=50, y=10)
Button(window, text="Load Docs", command=loadDocs).place(x=50, y=50)
Button(window, text="Load Images", command=loadImages).place(x=150, y=50)
Button(window, text="Exit Drive", command=gotoSearchEngine).place(x=100, y=10)
Button(window, text="Refresh Drive", command=refreshDrive).place(x=200, y=10)

# Filename field to open docs
filename = Entry(window)
filename.place(x=300, y=10)
Button(window, text="Goto Notepad", command=gotoNotepad).place(x=300, y=40)

# Letting the program run
window.mainloop()