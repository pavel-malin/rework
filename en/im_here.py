#! usr/bin/env python3.7

from random import random

from tkinter import *

def hide_show():
    if label.winfo_viewable():
        label.grid_remove()
    else:
        label.grid()

root = Tk()
label = Label(text="I'm here!") # Displays text
label.grid()
button = Button(command=hide_show, text='Hide/Show') # button that hides the text when pressed
button.grid()
root.mainloop()