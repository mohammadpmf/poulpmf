from parallelogram import Parallelogram


class Rectangle(Parallelogram):
    def __init__(self, width=100, height=50):
        super().__init__(width=width, height=height, angle=90)
