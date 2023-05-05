# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 04/05/2023
# Description: 
# Program that creates a Spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased
# --------------------------------------------------------------------
import tkinter as tk 
from tkinter import ttk


# ---Set up
window = tk.Tk()
window.geometry("500x600")
window.title("SpinBox")


# ---SpinBox
# Spin items
items = ("A", "B", "C", "D", "E")

# String variable connected to the spin
spin_string = tk.StringVar(value=items[0])

# Create Spinbox
spin = ttk.Spinbox(window, text="Choose a letter: ", textvariable= spin_string)

# Assign values to the Spinbox
spin["value"] = items

# Spin Event
spin.bind("<<Decrement>>", lambda event: print(spin_string.get()))
spin.pack()


# ---Run
window.mainloop()
