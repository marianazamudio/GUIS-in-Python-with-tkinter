# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 04/05/2023
# Description: 
# Program that shows how to use a Tkinter Widget "Canvas"
# --------------------------------------------------------------------
# NOTES:
# Canvas is a widger that allows you to "draw" shapes
# squares circles, lines, text, etc.

import tkinter as tk

# ---Setup
window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

# --- Canvas
canvas = tk.Canvas(window, bg="white")
canvas.pack()

# left and top are for the position
# right and bottom for the size                                  
canvas.create_rectangle(
    (50,20,100, 200), # (left, top, right, bottom)
    fill = "red", 
    width=10, 
    dash =(10,2),      # (how long the dash is, space between dashes)
    outline = "green")
#                 (start_x, start_y, end_x, end_y)
canvas.create_line((0,0,100,150))
# --- Run
window.mainloop()
