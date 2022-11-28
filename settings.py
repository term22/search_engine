# David Burg
# 11/15/22
# Settings for Search Engine

# Imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import subprocess

# Setup window
root = tk.Tk()
root.title("Settings")
root.geometry("500x600")

# Important variables
location = StringVar(root)
location.set("Select a Location")

# Change password
def changePassword():
    file = open("csc116/password.txt", "w")
    pw = askstring("Input", "Enter a Password:", show='*')
    if pw == None:
        root.destroy()
        subprocess.call(['python', 'csc116/settings.py'])
        return
    file.write(pw)
    file.close()

# Obtains the current background color
def getBackgroundColor():
    file = open("csc116/color.txt", "r")
    color = file.read()
    file.close()
    return color

# Changes the background color
def changeBackgroundColor():
    entry = colorEntry.get()
    if entry.lower() == "red":
        file = open("csc116/color.txt", "w")
        file.write("red")
        file.close()
        root.configure(bg=getBackgroundColor())        
    elif entry.lower() == "green":
        file = open("csc116/color.txt", "w")
        file.write("green")
        file.close()
        root.configure(bg=getBackgroundColor())
    elif entry.lower() == "blue":
        file = open("csc116/color.txt", "w")
        file.write("blue")
        file.close()
        root.configure(bg=getBackgroundColor())
    elif entry.lower() == "yellow":
        file = open("csc116/color.txt", "w")
        file.write("yellow")
        file.close()
        root.configure(bg=getBackgroundColor())
    elif entry.lower() == "white":
        file = open("csc116/color.txt", "w")
        file.write("white")
        file.close()
        root.configure(bg=getBackgroundColor())
    elif entry.lower() == "cyan":
        file = open("csc116/color.txt", "w")
        file.write("cyan")
        file.close()
        root.configure(bg=getBackgroundColor())
    elif entry.lower() == "magenta":
        file = open("csc116/color.txt", "w")
        file.write("magenta")
        file.close()
        root.configure(bg=getBackgroundColor())
    else:
        messagebox.showerror("Invalid color", "Error: You entered in an invalid color")
   
# Change Temperature
def changeTemperature():
    file = open("csc116/temperature.txt", "r+")
    farenheight = file.read()
    file.seek(0)
    file.truncate()
    if farenheight == "True":
        file.write("False")
    else:
        file.write("True")
    file.close()
    
# Exit settings window
def exitSettings():
    root.destroy()
    subprocess.call(['python', 'csc116/search-engine.py'])
    
# Main processing
root.configure(bg=getBackgroundColor())
colorEntry = Entry(root)
colorEntry.place(x=100, y=400)
Button(root, text="Change Background Color", width = 20, command=changeBackgroundColor).place(x=250, y=400)
Button(root, text="Change Password", width = 20, command=changePassword).place(x=100, y=100)
locations = StringVar()
locations.set("Change Location")
OptionMenu(root, location, "New York City", "Raleigh", "Washington DC", "Boston", "Atlanta", "Miami", "Chicago", "Houston", "Denver", "Phoenix", "San Francisco", "Los Angeles").place(x=100, y=200)
Button(root, text="Exit", width = 20, command=exitSettings).place(x=100, y=500)
Button(root, text="Change Temperature Setting", width = 30, command=changeTemperature).place(x=100, y=300)
root.mainloop()
