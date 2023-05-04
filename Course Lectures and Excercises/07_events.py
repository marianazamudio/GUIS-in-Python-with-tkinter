# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 02/05/2023
# Description: 
# This programs shows how to bind an event to a widget. 
# --------------------------------------------------------------------
# NOTES:
# An event can be: keyboard inputs, widgets getting changed, 
# widget being selected/unselected, mouse click/motion/wheel. 
# Events can be oberved and used. 

# To bind events to a widget:
# Widget.bind(event, function)

# Format: modifier-type-detail
# Alt-Keypress-a

# For more events visit:
# pythontutorial.net/tkinter/tkinter-event-binding

import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")

# ---Window
window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# --- Widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "A button")
btn.pack()

# --- Events
# The event data is printed when the user presses Alt + a, and has the button selected
# btn.bind("<Alt-KeyPress-a>", lambda event: print(event))

# The position of the mouse is printed when the user moves it through
# the window
# window.bind("<Motion>", get_pos)

# When the user is in the window, and a key is pressed, that key is printed
# window.bind("<KeyPress>", lambda event: print(f"a button was pressed ({event.char})"))

# When the user selects/unselects the entry field, a message is printed
entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("entry field was unselected"))

# Run
window.mainloop()
