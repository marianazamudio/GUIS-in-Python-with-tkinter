# --------------------------------------------------------------------
# Author: Mariana Zamudio
# Date: 03/05/2023
# Description: 
# This programs prints "MouseWheel" when the user holds down shift 
# and uses the mousewheel while text is selected
# <Shift-MouseWheel>
# --------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

# --- Window
window = tk.Tk()
window.geometry("600x500")
window.title("Mousewheel")

# ---Text Widget
text = tk.Text(window)
text.pack()

# --- Events
text.bind("<Shift-MouseWheel>", lambda event: print("MouseWheel"))

# Run
window.mainloop()
