#!/usr/bin/env python3
from Tkinter import *
root = Tk() 							# Create the root (base) window 
w = Label(root, text="Hello, world!") 	# Create a label with words
w.pack() 								# Put the label into the window
root.mainloop() 						# Start the event loop