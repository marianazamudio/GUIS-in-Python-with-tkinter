# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 01/05/2023
# Description: 
# Create a checkbutton and 2 radiobuttons
# RADIO BUTTON:
#   * Values for the Buttons are A and B
#   * Ticking either prints the value of the checkbuttton
#   * Ticking the radio button unchecks the checkbutton
# CHECK BUTTON:
#   * Ticking the checkbutton prints the value of the radio button value
#   * Use tkinter var for Booleans
# --------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# --- Variables
check_var = tk.BooleanVar(value= 0)
radio_var = tk.StringVar(value= "A")


# --- Commands
def ticking_radiobutton():
    print(check_var.get())
    check_var.set(0)

# --- Checkbuttons
check_button = ttk.Checkbutton(window, 
                              text="checkbutton",
                              variable= check_var,
                              command=lambda: print(radio_var.get()))
check_button.pack()

# --- Radiobuttons
radiobutton_1 =ttk.Radiobutton(window,
                              text="Radio A",
                              variable= radio_var,
                              command=ticking_radiobutton,
                              value = "A")
radiobutton_1.pack()
radiobutton_2 = ttk.Radiobutton(window,
                               text="Radio B",
                               variable= radio_var,
                               command=ticking_radiobutton,
                               value = "B")
radiobutton_2.pack()

# Run 
window.mainloop()