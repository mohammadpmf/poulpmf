from  turtle import*
c=textinput("","enter command")
while c != 'exit':
    if c == None:
        break
    if c =='fd':
        fd(100)
    elif c == 'back':
        back(100)
    elif c=="l":
        lt(90)
    elif c =="r":
        rt(90)
    elif c =='p':
        pensize(10)
    c=textinput('',"enter command")
