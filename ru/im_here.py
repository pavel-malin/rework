#! usr/bin/env python3.7

from random import random

from tkinter import *

def hide_show():
    if label.winfo_viewable():
        label.grid_remove()
    else:
        label.grid()

root = Tk()
label = Label(text='Я здесь!') # Выводит текст 
label.grid()
button = Button(command=hide_show, text='Спрятать/Показать') # кнопка которая прячет текс при нажатии
button.grid()
root.mainloop()