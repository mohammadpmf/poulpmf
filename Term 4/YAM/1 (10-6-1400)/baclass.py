class Human:
    def __init__(self, name = 'Reza', family = 'Razavi', height = 170, weight = 60, age=26): # سازنده constructor
        self.name = name
        self.family = family
        self.height = height
        self.weight = weight
        self.age = age
    def birthday(self):
        self.age += 1
    def __del__(self): # مخرب destructor
        print('bye')

reza = Human()
hasan = Human(name='hasan', family='ahmadi', age=40)
ali = Human(name='Ali')
ali.birthday()
print(reza.age)
reza.birthday()
print(reza.age)