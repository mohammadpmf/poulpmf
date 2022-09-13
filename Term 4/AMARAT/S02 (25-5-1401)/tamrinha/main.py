class Restorant:
    def __init__(self,i,l,h,y,w):
        self.price=i
        self.restorant_type=l
        self.restorant_address=h
        self.size=y
        self.floor=w

    def __str__(self):
        return f"{self.size} m2\nprice: ${self.price}\nrestorant type: {self.restorant_type}\naddress:{self.restorant_address}\nfloor:{self.floor}"

###################
m1=Restorant(580000,"restorant","Alman berlin", "50 21" ,21)
m2=Restorant(700000,"restorant","US kalifornia", "200 81" ,45)
###################
print(m1)
print(m2)