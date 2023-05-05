# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 03/05/2023
# Description: 
# Program that shows how to use a ComboBox and a SpinBox
# --------------------------------------------------------------------
# NOTES:
# Both ComboBox and Spinbox have predetermined values, and
# they are useful for the user showing a variety of options so they 
# can choose one.
# Hence, both need a list of value (as an entry) when programming them
# and both can be connected to a Tkinter variable.

import tkinter as tk
from tkinter import ttk


# --- Set up
window = tk.Tk()
window.geometry("600x400")
window.title("ComboBox and SpinBox")


# --- ComboBox
# Define the options or items in the combobox through a tuple
items = ("Ice cream", "Pizza", "Broccoli")

# Create a string variable to connect to the ComboBox
# and set it to the initial element in "items"
food_string = tk.StringVar(value = items[0])

# Create ComboBox
combo = ttk.Combobox(window, textvariable=food_string)

# Assign tuple of options to the ComboBox
combo["values"] = items
# combo.configure(values=items)
combo.pack()

# --- Event for the ComboBox
combo.bind("<<ComboboxSelected>>", lambda event: print(combo_label.config(text = f"Selected value: {food_string.get()}")))


# ---Label
# Label with "fixed" text. Text can be modified using label.config
combo_label = ttk.Label(window, text = "a label")

# Label with text connected to a tkinter variable
#combo_label = ttk.Label(window, textvariable = food_string)
combo_label.pack()


# ---Spinbox
# Connect a variable to tkinter variable
spin_int = tk.IntVar(value = 12)
# It is possible to define the values in the Spin box like this with a range
spin = ttk.Spinbox(window, 
                   from_ = 3, 
                   to = 20, 
                   increment = 3, 
                   command = lambda: print(spin_int.get()),
                   textvariable = spin_int)

# This is another way to define it with a tuple 
#spin["value"] = (1,2,3,4,5)
spin.pack()

# --- Event for the Spinbox
spin.bind("<<Increment>>", lambda event: print("up"))
spin.bind("<<Decrement>>", lambda event: print("down"))
# --- Run
window.mainloop()