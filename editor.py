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
import re

# Important Variables
current_font = "Times New Roman (Times)"
current_font_size = 11

# Configure the font
def configureFont(current_font, current_font_size):
    text.configure(font = (current_font, current_font_size))

# Change Font Size
def changeFontSize():
    mySize = size.get()
    current_font_size = mySize
    configureFont(current_font, current_font_size)

# Get word count
def getWordCount():
    return len(re.findall(r'\w+', text.get('1.0', 'end')))

# Display word and char count
def displayWordCount():
    display = "Word count: " + str(getWordCount())
    messagebox.showinfo("Word Count", display)

# Change the font
def changeFont():
    if font == "Helvetica":
        current_font = "Helvetica"
    elif font == "Courier New (Courier)":
        current_font = "Courier New (Courier)"
    elif font == "Comic Sans MS":
        current_font = "Comic Sans MS"
    elif font == "Fixedsys":
        current_font = "Fixedsys"
    elif font == "MS Sans Serif":
        current_font = "MS Sans Serif"
    elif font == "MS Serif":
        current_font = "MS Serif"
    elif font == "Symbol":
        current_font = "Symbol"
    elif font == "System":
        current_font = "System"
    elif font == "Times New Roman (Times)":
        current_font = "Times New Roman (Times)"
    else:
        current_font = "Verdana"
    configureFont(current_font, current_font_size)

# Function that saves a file
def saveFile():
    myFilename = filename.get()
    if myFilename == "":
        myFilename = "doc-1"
    file = open("csc116/search_engine/files/docs/" + myFilename + ".txt", "w")
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
    if os.path.exists("csc116/search_engine/files/docs/" + myFilename + ".txt") == False:
        messagebox.showerror("Error", "File with the given filename does not exist")
    else:
        file = open("csc116/search_engine/files/docs/" + myFilename + ".txt", "r")
        content = file.read()
        text.insert(tk.END, content)
        file.close()

# Obtains the current background color
def getBackgroundColor():
    file = open("csc116/color.txt", "r")
    color = file.read()
    file.close()
    return color

# Function to exit text editor
def exitTextEditor():
    exit = askyesno("Exit", message="Would you like to exit the text editor? (Anything not saved will be lost)")
    if exit:
        window.destroy()
        subprocess.call(['python', 'csc116/search_engine/search-engine.py'])    

# Setup GUI Frame
window = tk.Tk()
window.title("Results:")
window.geometry("1000x1000")
window.configure(bg=getBackgroundColor())

# Create Text Widget
text = Text(window, height = 50, width = 90)
text.place(x=100, y=100)
configureFont(current_font, current_font_size)

# Buttons to save and load files
Button(window, text="Save File", command=saveFile).place(x=200, y=50)
Button(window, text="Load File", command=loadFile).place(x=300, y=50)

# Button to exit text editor
Button(window, text="Exit Text Editor", command=exitTextEditor).place(x=400, y=50)

# Button to get word and char counts
Button(window, text="Word Count", command=displayWordCount).place(x=825, y=50)

# Filename
filename = Entry(window)
filename.place(x=400, y=10)

# Font size field
size = Entry(window, width=3)
size.place(x=500, y=50)
Button(window, text="Font Size", command=changeFontSize).place(x=500, y=75)

# List of fonts
font = StringVar()
font.set("Change font")
fonts = OptionMenu(window, font, "Helvetica", "Courier New (Courier)", "Comic Sans MS", "Fixedsys", "MS Sans Serif", "MS Serif", "Symbol",
"System", "Times New Roman (Times)", "Verdana")
fonts.place(x=600, y=50)
Button(window, text="Change Font", command=changeFont).place(x=725, y=50)

# Execute GUI
window.mainloop()