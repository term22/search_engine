# David Burg
# 5/12/23
# Photo Viewer Program

# Imports
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess
import os

# Obtains the current background color
def getBackgroundColor():
    file = open("csc116/color.txt", "r")
    color = file.read()
    file.close()
    return color

# Finds the photo based on the filename
def getPhoto():
    myPhoto = photo.get()
    photos = os.listdir("csc116/search_engine/files/pics")
    for ourPhoto in photos:
        p = ourPhoto[0:ourPhoto.index(".png")]
        if p == myPhoto:
            return "csc116/search_engine/files/pics/" + p + ".png"
    return None

def loadPhoto():
    photoName = getPhoto()
    if photoName != None:
        pic = tk.PhotoImage(photoName)
        canvas = tk.Canvas(width=300, height=300)
        canvas.create_image(300, 300, image = pic)
        canvas.place(x=300, y=300)
        canvas.update()
        #ourPhoto = tk.Label(window, image = pic)
        #ourPhoto.place(x=200, y=300)
    else:
        messagebox.showerror("Error", "Photo Does not exist")

# GUI Code

# Setup window
window = tk.Tk()
window.title("Photo Viewer")
window.geometry("1000x1000")
window.configure(bg=getBackgroundColor())

# Loads Photos
Button(window, text="Search", command=loadPhoto).place(x=700, y=10)

# Photo Label
pLabel = tk.Label(text="Enter photo name")
pLabel.place(x=375, y=10)

# Photo Name
photo = Entry(window)
photo.place(x=500, y=10)

# Letting the program run
window.mainloop()