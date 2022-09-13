class House():
    def __init__(self,a,n_of_f,p):
        self.area = a
        self.number_of_floors = n_of_f
        self.price = p
    def __str__(self):
        return f"Information House \nArea: {self.area} m2 \nNumber of floors: {self.number_of_floors} \nPrice: {self.price}\n"
home1 = House(380,5,3000000000.0)
home2 = House(150,3,290000000.0)
home3 = House(500,1,12500000000.0)
home4 = House(85,4,3100000000.0)
home5 = House(100,2,380000000.0)
home6 = House(95,20,3200000000.0)
print(home1)
print(home2)
print(home3)
print(home4)
print(home5)
print(home6)
