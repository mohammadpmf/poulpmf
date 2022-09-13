from turtle import *

for i in range(2):
    fillcolor('red')
    begin_fill()
    for i in range(4):
        fd(200)
        lt(90)
    rt(90)
    end_fill()
    begin_fill()
    for i in range(4):
        fd(200)
        lt(90)
    fillcolor('blue')
    end_fill()
    rt(90)



done()