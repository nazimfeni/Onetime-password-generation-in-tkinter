# importing everything from tkinter
from tkinter import *

# creating the tkinter window
win = Tk()

# variable
my_text = "ddddd"

# function define for
# updating the my_label
# widget content
def counter():

	# use global variable
	global my_text
	
	# configure
	my_label.config(text = my_text)

# create a button widget and attached
# with counter function
my_button = Button(win,
				text = "Please update",
				command = counter)

# create a Label widget
my_label = Label(win,
				text = "Show Verify code here")

# place the widgets
# in the gui window
my_label.pack()
my_button.pack()

# Start the GUI
win.mainloop()
