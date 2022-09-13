# Code #2: Binding Mouse buttons with Tkinter Frame
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.geometry('600x400')

# function to be called when button-2 of mouse is pressed
def bt(event):
	print('Middle click pressed at x = % d, y = % d' % (event.x, event.y))

# function to be called when button-3 of mouse is pressed
def right(event):
	if int(event.y) < 200:
		exit()
	print('Right click pressed at x = % d, y = % d' % (event.x, event.y))

# function to be called when button-1 is double clocked
def double_click(event):
	print('Double clicked at x = % d, y = % d' % (event.x, event.y))

# these lines are binding mouse buttons with the Frame widget
root.bind('<Button-2>', bt)
root.bind('<Button-3>', right)
root.bind('<Double-1>', double_click)
mainloop()