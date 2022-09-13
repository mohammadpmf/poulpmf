from turtle import *
speed(0)

for w in range(4):
    for j in range(4):
        for i in range(4):
            fd(20)
            lt(90)
        fd(20)
        begin_fill()
        for i2 in range(4):
            fd(20)
            lt(90)
        end_fill()
        fd(20)
    fd(-20*8)
    lt(90)
    fd(20)
    rt(90)
    for j in range(4):
        begin_fill()
        for i in range(4):
            fd(20)
            lt(90)
        end_fill()
        fd(20)
        for i2 in range(4):
            fd(20)
            lt(90)
        fd(20)
    fd(-20*8)
    lt(90)
    fd(20)
    rt(90)

done()