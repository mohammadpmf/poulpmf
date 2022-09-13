class House():
    def __init__(self, m, t, g): 
        self.metraj = m
        self.tedad_tabaghe = t 
        self.gheymat = g

    def __str__(self): 
        return f"{self.metraj}\n{self.tedad_tabaghe}\n{self.gheymat}"


h1 = House(170, 5, 1700)
h2 = House(100, 3, 900)
print(h1.metraj)
print(h2)
