# --------------------------------------------- #
# Author: Mariana Zamudio
# Date: 28/03/2023
# --------------------------------------------- #
import tkinter as tk
from tkinter import ttk

def button_func():
	print('a button was pressed')

def hello_button_func():
	print("Hello")

# Create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry('800x500')

# Each comment ttk or tk shows how to use a different widget
# ttk widgets
label = ttk.Label(master= window, text= 'This is a test')
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# New label
my_label = ttk.Label(master = window, text = "My Label")
my_label.pack()

# New button
hello_button = ttk.Button(master =  window, text = "Hello", command= hello_button_func)
hello_button = ttk.Button(master =  window, text = "Hello", command= lambda: print("hello"))
hello_button.pack()

# ttk.Button()
button = ttk.Button(master = window, text= 'A button', command = button_func)
button.pack()

# run
window.mainloop() # Code stops here
# When the window is closed it prints the "Hello"
print("Hello")
