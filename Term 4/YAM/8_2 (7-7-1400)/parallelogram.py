import math

class Parallelogram():
    def __init__(self, width = 100, height = 50, angle=30):
        self.width = width
        self.height = height
        self.angle1 = angle
        self.angle2 = 180-angle
        self.length = height/math.sin(angle*math.pi/180)
        # self.__secret_info='salam'

    def show_width(self):
        return self.width
    def show_height(self):
        return self.height
    def show_length(self):
        return self.length
    def perimeter(self):
        return (self.width+self.length)*2
    def area(self):
        return self.width*self.height