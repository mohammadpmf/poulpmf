import math
import turtle

class Parallelogram():
    def __init__(self, width = 100, height = 50, angle=30):
        self.width = width
        self.height = height
        self.angle1 = angle  # angle1 in degrees.
        self.angle2 = 180-angle  # angle2 in degrees.
        angle1_in_radians = angle*math.pi/180
        self.length = height/math.sin(angle1_in_radians)
    def __repr__(self) -> str:
        return self.__secret_info

    def get_width(self):
        return round(self.width, 1)
    def get_height(self):
        return round(self.height, 1)
    def get_length(self):
        return round(self.length, 1)
    def get_angle1(self):
        return self.angle1
    def get_angle2(self):
        return self.angle2
    def perimeter(self):
        return round((self.width+self.length)*2, 1)
    def area(self):
        return round(self.width*self.height, 1)
    def draw(self):
        for i in range(2):
            turtle.fd(self.width)
            turtle.left(self.angle1)
            turtle.fd(self.length)
            turtle.left(self.angle2)