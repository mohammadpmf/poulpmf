from turtle import *

speed(0)
for i  in range(8):
    fillcolor('red')
    begin_fill()
    circle(10)
    end_fill()
    circle(100, 360/16)
    fillcolor('blue')
    begin_fill()
    circle(10)
    end_fill()
    circle(100, 360/16)

done()