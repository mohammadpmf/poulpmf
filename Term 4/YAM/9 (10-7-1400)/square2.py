from rectangle import Rectangle
import turtle

class Square2(Rectangle):
    def __init__(self, width=100):
        super().__init__(width=width, height=width)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

