import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import tkinter as tk
from tkinter import simpledialog

def printInput():
    inp = USER_INP.get(1.0, "end-1c")
    lbl.config(text = inp)

ROOT = tk.Tk()
ROOT.withdraw()

# the input dialog
USER_INP = phonenumbers.parse(simpledialog.askstring(title = "fast",prompt="Enter the Phone Number : "))
print(geocoder.description_for_number(USER_INP,"en"))
print(carrier.name_for_number(USER_INP,"en"))

#Lable Creation
lbl = tk.Label(ROOT,text = " ")
lbl.pack()

#print(USER_INP)