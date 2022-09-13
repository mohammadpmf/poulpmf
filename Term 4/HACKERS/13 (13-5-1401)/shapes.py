from turtle import *
class Rectangle():
    def __init__(self, width=50, height=60, color='black', pensize=5):
        ht()
        self.width = width
        self.height = height
        self.color = color
        self.pensize = pensize
    def masahat(self):
        return self.width * self.height
    def mohit(self):
        return (self.width+self.height)*2
    def draw(self):
        pencolor(self.color)
        pensize(self.pensize)
        for i in range(2):
            fd(self.width)
            lt(90)
            fd(self.height)
            lt(90)

class Square(Rectangle):
    def __init__(self, width, color, pensize):
        super().__init__(width, width, color, pensize)

s1 = Square(width=150, color='purple', pensize=100)
s1.draw()
done()
