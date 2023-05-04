# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 01/05/2023
# Description: 
# --------------------------------------------------------------------
# NOTES:
# There are 3 major kinds of buttons
#   * Button
#   * Checkbutton
#   * Radiobutton
# To use them properly it is needed to use tkinter variables

import tkinter as tk
from tkinter import ttk

# --- Setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# --- Button 
def button_func():
    print("a basic button")
    print(radio_var.get())

button_string = tk.StringVar(value = "A button with string var")
# Note: "A simple button is being overwritten by the text variable"
button =  ttk.Button(window, text="A simple button", command=button_func, textvariable=button_string)
button.pack()

# ---Checkbutton
# Note check_var could be a StringVar, BooleanVar or IntVar. The 0/1 
# value of the checkbox will be stored accordingly in the variable. 
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(window, 
                        text="checkbox 1", 
                        command=lambda:print(check_var.get()),
                        variable=check_var,
                        onvalue= 10,
                        offvalue= 5,)
check.pack()

check2 = ttk.Checkbutton(window, 
                         text="checkbox 2",
                         command=lambda:check_var.set(5))
check2.pack()

# --- Radio button
# The main idea of radio buttons is that only one is activated
# They are connected by default, so only one can be activated at the time
radio_var = tk.StringVar()
radio1= ttk.Radiobutton(window, 
                        text="Radiobutton 1", 
                        value='radio 1', 
                        variable= radio_var,
                        command=lambda:print(radio_var.get()),)
radio1.pack()
radio2= ttk.Radiobutton(window, 
                        text="Radiobutton 2",
                        value = 2,
                        variable= radio_var
                        #command=lambda:print()
                        )
radio2.pack()

# --- Run 
window.mainloop()




