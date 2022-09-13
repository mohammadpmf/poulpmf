from tkinter import *
root=Tk()

class Person():
    def __init__(self,name, family, age, weight, height):
        self.name=name
        self.family=family
        self.age=age
        self.weight=weight
        self.height=height
    def __str__(self):
        return self.name
class Student(Person):
    def __init__(self,name, family, age, weight, height,student_id ):
        super().__init__(name, family, age, weight, height)
        self.student_id=student_id
class techer(Person):
    def __init__(self,name, family, age, weight, height,major):
        super().__init__(name, family, age, weight, height)
        self.major=major

root.mainloop()