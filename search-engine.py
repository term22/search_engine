# David Burg
# 5/26/22
# My Search Engine

# Imports
from tkinter import *
from datetime import *
import tkinter as tk
import urllib.request
import webbrowser
import subprocess

# Important Data Structures and variables
results = {}
titles = []
urls = []

# Get date and time method
def getDateAndTime():
    today = date.today()
    myDate = ""
    dateFile = open("csc116/date.txt", "r")
    fmat = dateFile.read()
    dateFile.close()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%y")
    if int(day) >= 1 and int(day) < 10:
        day = day[1:]
    if fmat == "M/D/Y":
        myDate = today.strftime(month + "/" + day + "/" + year)
    else:
        myDate = today.strftime(day + "/" + month + "/" + year)
    now = datetime.now()
    hourFile = open("csc116/clock.txt", "r")
    statement = hourFile.read()
    hourFile.close()
    if statement == "AM-PM":
        hour = now.strftime("%I")
        if (int(hour) < 10):
            hour = hour[1:]
        minute = now.strftime("%M")
        time = hour + ":" + minute
        return myDate + "\n" + time + " " + now.strftime("%p")
    else:
        hour = now.strftime("%H")
        if (int(hour) < 10):
            hour = hour[1:]
        minute = now.strftime("%M")
        time = hour + ":" + minute
        return day + "\n" + time

# Converts from farenheight to celsius
def fToC(temp):
    return str(round((5 / 9) * (temp - 32)))

# Obtains the current temperature of NYC
def getWeather():
    filename1 = "csc116/city.txt"
    filename2 = "csc116/temperature.txt"
    city = open(filename1, "r")
    url = city.readline()
    name = city.readline()
    city.close()
    req = urllib.request.Request(url)
    web = urllib.request.urlopen(req)
    page = web.readlines()
    before_temp = '<p class="myforecast-current-lrg">'
    after_temp = "&deg;F</p>"

    for line in page:
        current = line.decode("utf-8")
        if before_temp in current and after_temp in current:
            temp = current.replace(before_temp, "")
            temp = temp.replace(after_temp, "")
            temp = temp.strip()
            temperature = open(filename2, "r")
            isFarenheight = temperature.read()
            if isFarenheight == "True":
                return name + "\n" + temp + " F"
            else:
                myTemp = int(temp)
                return name + "\n" + fToC(myTemp) + " C" 

# Place weather method
def placeWeather():
    city = open("csc116/city.txt", "r")
    url = city.readline()
    city.close()
    temperature = tk.Label(text=getWeather())
    temperature.bind("<Button>", lambda e: callback(url))
    temperature.place(x=900, y=850)

# Update Time method
def updateDateAndTime():
    date_and_time = tk.Label(text=getDateAndTime())
    date_and_time.place(x=900, y=900)

# Callback method
def callback(url):
    webbrowser.open_new_tab(url)

# Get keyword method
def getKeyword():
    clearResults(results, titles, urls)
    updateDateAndTime()
    keyword = e.get()
    e.delete(0, END)
    if keyword != "":

        # Set up important variables
        filename = "news.txt"
        file = open(filename, "r")
        numLines = len(file.readlines())
        file.close()

        # Loop through the text file
        file = open(filename, "r")
        for i in range(0, numLines, 1):
            line = file.readline().split("@")
            if (keyword.upper() in line[0].upper() or keyword.upper() in line[1].upper()):
                results.update({line[0]: line[1]})

        # Display results
        if (len(results) > 0):
            y_coord = 100
            for a in results:
                result = tk.Label(text=(a + "\n"))
                titles.append(result)
                result.place(x=200, y=y_coord)
                y_coord += 20
                link = tk.Label(text=results[a], fg="blue")
                urls.append(link)
                link.bind("<Button>", lambda e: callback(results[a]))
                link.place(x=200, y=y_coord)
                y_coord += 40                     
        else:
            result = tk.Label(text="Sorry, could not find any results based on your keyword(s)")
            result.place(x=200, y=100)
        
        file.close()

# Obtains the current background color
def getBackgroundColor():
    file = open("csc116/color.txt", "r")
    color = file.read()
    file.close()
    return color

# Obtain and goto selected app
def gotoSelectedApp():
    selectedApp = currentApp.get()
    if selectedApp == "Docs":
        window.destroy()
        subprocess.call(['python', 'csc116/search_engine/editor.py'])
    elif selectedApp == "Settings":
        window.destroy()
        subprocess.call(['python', 'csc116/search_engine/settings.py'])
    elif selectedApp == "Drive":
        window.destroy()
        subprocess.call(['python', 'csc116/search_engine/drive.py'])
    elif selectedApp == "Environmental Science Game":
        window.destroy()
        subprocess.Popen("csc116/search_engine/educational_game.exe")

# Clear Resultsq
def clearResults(results, titles, urls):
    results.clear()
    for label in titles:
        label.destroy()
    for label in urls:
        label.destroy()

# Main processing

# Set up GUI window
window = tk.Tk()
window.title("Results:")
window.geometry("1000x1000")

# Set Window Background
window.configure(bg=getBackgroundColor())

# Place important labels
updateDateAndTime()
placeWeather()

# Set up Apps
currentApp = StringVar(window)
currentApp.set("Apps")
apps = OptionMenu(window, currentApp, "Docs", "Drive", "Settings", "Environmental Science Game")
apps.place(x=700, y=10)

# User input
e = Entry(window)
e.place(x=500, y=10)
Button(window, text="Search", command=getKeyword).place(x=600, y=10)
Button(window, text="Goto App", command=gotoSelectedApp).place(x=700, y=50)

# Letting the program run
window.mainloop()