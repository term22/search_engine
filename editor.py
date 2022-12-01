# David Burg
# 12/1/22
# Document Editor Program

# Imports
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import tkinter as tk
import subprocess
import os

# Obtains the current background color
def getBackgroundColor():
    file = open("csc116/color.txt", "r")
    color = file.read()
    file.close()
    return color

# Function that saves a file
def saveFile():
    myFilename = filename.get()
    file = open("csc116/files/" + myFilename + ".txt", "w")
    myText = text.get('1.0','end')
    for i in range(0, len(myText), 1):
        file.write(myText[i]) 
        if (i + 1) % 90 == 0:
            file.write('\n')
    file.close()
    messagebox.showinfo("Saved", "File succesfully saved")

# Function to load a currently existing file
def loadFile():
    myFilename = filename.get()
    if os.path.exists("csc116/files/" + myFilename + ".txt") == False:
        messagebox.showerror("Error", "File with the given filename does not exist")
    else:
        file = open("csc116/files/" + myFilename + ".txt", "r")
        content = file.read()
        text.insert(tk.END, content)
        file.close()

# Function to exit text editor
def exitTextEditor():
    exit = askyesno("Exit", message="Would you like to exit the text editor? (Anything not saved will be lost)")
    if exit:
        window.destroy()
        subprocess.call(['python', 'csc116/search-engine.py'])    

# Setup GUI Frame
window = tk.Tk()
window.title("Results:")
window.geometry("1000x1000")
window.configure(bg=getBackgroundColor())

# Create Text Widget
text = Text(window, height = 50, width = 90)
text.place(x=100, y=100)

# Buttons to save and load files
Button(window, text="Save File", command=saveFile).place(x=200, y=50)
Button(window, text="Load File", command=loadFile).place(x=300, y=50)

# Button to exit text editor
Button(window, text="Exit Text Editor", command=exitTextEditor).place(x=400, y=50)

# Filename
filename = Entry(window)
filename.place(x=400, y=10)

# Execute GUI
window.mainloop()