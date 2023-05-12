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
root.geometry("500x700")

# Important variables
location = StringVar()
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

# Change Location
def changeLocation():
    myLocation = location.get()
    file = open("csc116/city.txt", "w")
    if myLocation == "New York City":
        file.write("http://forecast.weather.gov/MapClick.php?lat=40.7142&lon=-74.0059#.V0T2XI_zzck\n")
    elif myLocation == "Raleigh":
        file.write("https://forecast.weather.gov/MapClick.php?lat=35.7855&lon=-78.6427#.Y3vC5HbMLZs\n")
    elif myLocation == "Washington DC":
        file.write("https://forecast.weather.gov/MapClick.php?lat=38.8904&lon=-77.032#.Y3vDC3bMLZs\n")
    elif myLocation == "Boston":
        file.write("https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567#.Y3vDI3bMLZs\n")
    elif myLocation == "Atlanta":
        file.write("https://forecast.weather.gov/MapClick.php?lat=33.7483&lon=-84.3911#.Y3vDRnbMLZs\n")
    elif myLocation == "Miami":
        file.write("https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977#.Y3vDXXbMLZs\n")
    elif myLocation == "Chicago":
        file.write("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.Y3vDb3bMLZs\n")
    elif myLocation == "Houston":
        file.write("https://forecast.weather.gov/MapClick.php?lat=29.7608&lon=-95.3695#.Y3vDhHbMLZs\n")
    elif myLocation == "Denver":
        file.write("https://forecast.weather.gov/MapClick.php?lat=39.74&lon=-104.992#.Y3vDlXbMLZs\n")
    elif myLocation == "Phoenix":
        file.write("https://forecast.weather.gov/MapClick.php?lat=33.4483&lon=-112.0758#.Y3vDpnbMLZs\n")
    elif myLocation == "San Francisco":
        file.write("https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4197#.Y3vDt3bMLZs\n")
    elif myLocation == "Los Angeles":
        file.write("https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2454#.Y3vDxnbMLZs\n")
    file.write(myLocation)
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
   
# Change Clock
def changeClock():
    file = open("csc116/clock.txt", "r+")
    time = file.read()
    file.seek(0)
    file.truncate()
    if time == "AM-PM":
        file.write("24-Hrs")
    else:
        file.write("AM-PM")
    file.close()

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
    subprocess.call(['python', 'csc116/search_engine/search-engine.py'])
    
# Main processing
root.configure(bg=getBackgroundColor())
colorEntry = Entry(root)
colorEntry.place(x=100, y=400)
Button(root, text="Change Background Color", width = 20, command=changeBackgroundColor).place(x=250, y=400)
Button(root, text="Change Password", width = 20, command=changePassword).place(x=100, y=100)
locations = StringVar()
locations.set("Change Location")
menu = OptionMenu(root, location, "New York City", "Raleigh", "Washington DC", "Boston", "Atlanta", "Miami", "Chicago", "Houston", "Denver", "Phoenix",
"San Francisco", "Los Angeles")
menu.place(x=100, y=200)
Button(root, text="Change Location", command=changeLocation).place(x=300, y=200)
Button(root, text="Exit", width = 20, command=exitSettings).place(x=100, y=600)
Button(root, text="Change Temperature Setting", width = 30, command=changeTemperature).place(x=100, y=300)
Button(root, text="Change clock display", width=30, command=changeClock).place(x=100, y=500)
root.mainloop()
