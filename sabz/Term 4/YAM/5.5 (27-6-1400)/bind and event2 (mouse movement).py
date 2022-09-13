# # Code #1: Binding mouse movement with tkinter Frame.
# # Import all files from tkinter and overwrite all the tkinter files by tkinter.ttk
# from tkinter import *
# from tkinter.ttk import *

# # creates tkinter window or root window
# root = Tk()
# root.geometry('300x200')
# # function to be called when mouse enters in a frame
# def enter(event):
#     print('Entered at x = % d, y = % d' % (event.x, event.y))
# # decimal  # h
# #
# # function to be called when mouse exits the frame
# def exit_(event):
# 	print('Exited at x = % d, y = % d' % (event.x, event.y))

# # frame with fixed geometry

# # these lines are showing the working of bind function it is universal widget method
# root.bind('<Enter>', enter)
# root.bind('<Leave>', exit_)
# mainloop()

name = 'ali'
family = 'rezayi'
age = '45'

print('Your name is: '+name+' Your family is: ' + family+' Your age is: ' + age)
print(f'Your name is: {name} Your family is: {family} Your age is: {age}')
print('Your name is: %s  Your family is: %s,  Your age is: %s' %(name, family, age))
