class Human():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __gt__(self, self2):
        return self.age>self2.age
    def __str__(self):
        return self.name

ali = Human("Ali", 20)
reza = Human("Reza", 16)

if ali>reza:
    print(f"{ali} is greater than {reza}")
else:
    print(f"{ali} is not greater than {reza}")
