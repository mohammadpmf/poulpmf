import turtle as t
import threading

def go(turtle: t.Turtle):
    turtle.fd(400)

turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtle3 = t.Turtle()
turtle1.speed(1)
turtle2.speed(1)
turtle3.speed(1)
turtle1.goto(-200, -200)
turtle2.goto(-200, 0)
turtle3.goto(-200, 200)

thread1 = threading.Thread(target=go, args=(turtle1, ))
thread2 = threading.Thread(target=go, args=(turtle2, ))
thread3 = threading.Thread(target=go, args=(turtle3, ))
thread1.start()
thread2.start()
thread3.start()
# go(turtle1)
# go(turtle2)
# go(turtle3)

t.done()