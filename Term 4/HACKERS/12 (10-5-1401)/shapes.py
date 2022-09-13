from turtle import *
class Rectangle():
    def __init__(self, width=50, height=60):
        ht()
        self.width = width
        self.height = height
    def masahat(self):
        return self.width * self.height
    def mohit(self):
        return (self.width+self.height)*2
    def draw(self):
        for i in range(2):
            fd(self.width)
            lt(90)
            fd(self.height)
            lt(90)
r1 = Rectangle(width=100, height=40)
print(r1.draw())
done()