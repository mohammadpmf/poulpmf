# Code #3: Binding keyboard buttons with the root window (tkinter main window).
from tkinter import *

def key_press(harchi: Event):
    print(harchi)
    print(type(harchi))
    print(harchi.char, 'is pressed')

def enter_pressed(mohemnist):
    print("Enter is pressed")

def escape_pressed(event):
# def escape_pressed(mohemnist):
    exit()

root = Tk()
root.geometry('200x100')
root.bind('<Key>', key_press)  # kelidhaye safhe kelid
root.bind('<Return>', enter_pressed)  # Enter
root.bind('<Escape>', escape_pressed)  # Esc
# va chizhaye dg mesle: '<Delete>' baraye delete      '<Insert>', '<Home>', '<End>' hatman bazam hast. testesh bifaydast. Age lazem bood search konam. karam rah oftadeh bood dg edameh nadadam. vali in site ham baz kardeh boodam. sarsari negah kardam khoob bood be nazaram. manzooram jadval event hash hast. https://www.python-course.eu/tkinter_events_binds.php

mainloop()