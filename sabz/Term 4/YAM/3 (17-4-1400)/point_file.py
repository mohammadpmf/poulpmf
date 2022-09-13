class Point():
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
    def __gt__ (self, second): # gt >   ge  >=    lt <    le <=    eq == 
        if self.x > second.x:
            return True
        else:
            return False
    def __ge__ (self, second): # gt >   ge  >=    lt <    le <=    eq == 
        if self.x >= second.x:
            return True
        else:
            return False
    def __eq__ (self, second): # gt >   ge  >=    lt <    le <=    eq == 
        if self.x == second.x and self.y == second.y:
            return True
        else:
            return False
    def __repr__ (self): # representation
        # return ('(' + str(self.x) + ', '+ str(self.y) + ')')
        return f"({self.x}, {self.y})"
    def __del__ (self):
        print("bye", self.x, self.y)
    
    def distance(self, second):
        return ((self.x-second.x)**2 + (self.y-second.y)**2)**(0.5)
    
    def add(self, second):
        return (self.x + second.x, self.y + second.y)

    def sub(self, second):
        return (self.x - second.x, self.y - second.y)

