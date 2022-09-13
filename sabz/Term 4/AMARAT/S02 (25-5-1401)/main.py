from turtle import *
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def draw(self):
        penup()
        goto(self.x, self.y)
        pendown()
        dot(5)
    def __add__(self, second):
        r = Point(self.x+second.x, self.y+second.y)
        return r
    def __sub__(self, second):
        r = Point(self.x-second.x, self.y-second.y)
        return r
    def __mul__(self, second):
        r = Point((self.x*second.x)-(self.y*second.y),
        (self.x*second.y)+(self.y*second.x))
        return r
    def __truediv__(self, second):
        r = Point(0, 0)
        return r

    def __eq__(self, second):
        if self.x==second.x and self.y==second.y:
            return True
        else:
            return False

p1 = Point(200, 25)
p2 = Point(200, 25)
print(p1==p2)
