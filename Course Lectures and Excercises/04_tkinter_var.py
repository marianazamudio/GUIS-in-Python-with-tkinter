# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 28/03/2023
# Description: Program that uses a labela and two entry labels 
# connected via a StringVar. When the button is pressed, the 
# content of the labels is printed in console and a new message
# appears in the labels. 
# --------------------------------------------------------------------
# Tkinter has inbuilt variables that are designed to work with widgets
# They are automatically updated by a widget and they update a widget
# Although they still store basic data like string, integers and Booleans

import tkinter as tk
from tkinter import ttk

def button_func():
	print(string_var.get()) 
	string_var.set("button pressed")

# window
window = tk.Tk()
window.title("Tkinter Variables")

# tkinter variable
string_var = tk.StringVar(value="test")#(value='start value')

# --- Widgets ---
# Label
label = ttk.Label(master=window, text= "label", textvariable=string_var)
label.pack()

# Entry label connected via string_var
entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()
# Second entry label connected via string_var
entry_2 = ttk.Entry(master=window, textvariable=string_var)
entry_2.pack()

# Button connected to buton_func
button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

# run
window.mainloop()