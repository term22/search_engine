# David Burg
# 10/11/2022
# Login program to log into the search Engine

# Imports
import os.path
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import askyesno
from tkinter import messagebox
import subprocess

# Important variables
pw = ""
filename1 = "csc116/search_engine/password.txt"
filename2 = "csc116/search_engine/temperature.txt"
root = Tk()

# Main Processing
if (os.path.exists(filename1) == False and os.path.exists(filename2) == False):

    # Enter the password
    file1 = open(filename1, "w")
    pw = askstring("Input", "Enter a Password:", show='*')
    if pw != None:
        file1.write(pw)
    else:
        exit(1)
    file1.close()

    # Enter Temperature settings
    file2 = open(filename2, "w")
    temp = askyesno("Temperature Settings", message="Would you like to display temperature in Celsius?")
    if temp:
        file2.write("False")
    else:
        file2.write("True") 
    file2.close() 
else:
    file = open(filename1, "r")
    pw = askstring("Input", "Enter a Password:", show='*')
    if pw == None:
        exit(1)
    pwFromFile = file.readline()
    file.close()
    while pw != pwFromFile:
        messagebox.showerror("Error", "Incorrect Password")
        pw = askstring("Input", "Enter a Password:", show='*')
        if pw == None:
            exit(1)
    messagebox.showinfo("Welcome!", "Welcome!")

# Main Loop
root.destroy()
subprocess.call(['python', 'csc116/search_engine/search-engine.py'])
root.mainloop()
