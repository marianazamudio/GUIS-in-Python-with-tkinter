import tkinter as tk
from tkinter import ttk

def button_func():
	# Get the content of the entry
	entry_text = entry.get()

	# Update the label
	#label.configure(text = "some other text")
	label['text'] = entry_text  #MORE CONCISE
	# Disable the entry label
	entry['state'] = "disabled"
	# print all posible configurations
	#print(label.configure())

	
def enab_button_func():
	label["text"] = "some text"
	entry["state"] = "enabled"

# window
window = tk.Tk()
window.title("Getting and setting widgets")

# widgets
# label
label = ttk.Label(master=window, text="MyLabel")
label.pack()

# entry
entry = ttk.Entry(master=window)
entry.pack()

# button
button = ttk.Button(master=window, text="Button", command = button_func)
button.pack()

button_enable = ttk.Button(master=window, text="Enable entry", command=enab_button_func)
button_enable.pack()

# run
window.mainloop()




# NOTES
# It makes sense for the entry label to have the function get, it is useful to retrieve
# the user's input.

# Other widgets like label, dont have the get method, as it is not really useful



# METHOD CONFIG
# It helps updating the widgwts.
#Label.config(text="some new text")    This might disappear, use configure
#Label.configure
#Label['text'] = "some new text"