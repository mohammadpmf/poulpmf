from turtle import *

c = textinput("", "Enter command: ")
while c != 'exit':
    if c == None:
        break
    if c == 'fd':
        fd(100)
    elif c == 'back':
        back(100)
    elif c == 'l':
        d = int(textinput("", "how much?"))
        lt(d)
    elif c == 'r':
        d = int(textinput("", "how much?"))
        rt(d)
    elif c == 'p':
        pensize(10)
    elif c == 'c':
        pencolor('red')
    c = textinput("", "Enter command: ")
