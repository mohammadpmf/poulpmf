from turtle import *
class Point():
    def __init__(self, x, y): # constructor
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
    def __truediv__(self,second):
        s1 = (self.x*second.x)+(self.y*second.y)
        m = (second.x*second.x)+(second.y*second.y)
        s2 = (self.y*second.x)-(self.x*second.y)
        r=Point(s1/m, s2/m)
        return r

    def __eq__(self, second):
        if self.x==second.x and self.y==second.y:
            return True
        else:
            return False

    def __gt__(self, second): # greater than
        d1 = self.x**2 + self.y**2
        d2 = second.x**2 + second.y**2
        if d1>d2:
            return True
        else:
            return False
    def __lt__(self, second): # greater than
        d1 = self.x**2 + self.y**2
        d2 = second.x**2 + second.y**2
        if d1<d2:
            return True
        else:
            return False

    def __ge__(self, second): # greater than or equal
        d1 = self.x**2 + self.y**2
        d2 = second.x**2 + second.y**2
        if d1>=d2:
            return True
        else:
            return False
    def __le__(self, second): # less than or equal
        d1 = self.x**2 + self.y**2
        d2 = second.x**2 + second.y**2
        if d1<=d2:
            return True
        else:
            return False

    def __ne__(self, second):  # not equal
        if self.x != second.x:
            return True
        elif self.y != second.y:
            return True
        else:
            return False
    
    # def __del__(self): # destructor
    #     print(f"{self} has been destroyed")


if __name__ == "__main__":
    p1 = Point(200, 25)
    p2 = Point(200, 25)
    p3 = Point(200, 100)
    p4 = Point(25, 200)
    print(p1!=p2)
    p1=4