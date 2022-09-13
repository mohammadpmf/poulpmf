class house:
    def __init__(self,s,p,ht,ha,f):
        self.size=s
        self.price=p
        self.house_type=ht
        self.house_address=ha
        self.floor=f
    def __str__(self):
        if self.floor == None:
            return f"{self.size} m2\nprice: ${self.price}\nhouse type: {self.house_type}\naddress:{self.house_address}"
        else:
            return f"{self.size} m2\nprice: ${self.price}\nhouse type: {self.house_type}\naddress:{self.house_address}\nfloor:{self.floor}"
h1=house(120,120000,"apartment","UK London codingway 16","3")
h2=house(76,80000,"house","US NewYork pythonway 212",'')
print(h2)