class Rectangle():
    def __init__(self, width = 100, height = 50):
        self.width = width
        self.height = height
        # self.__secret_info='salam'

    def perimeter(self):
        return (self.width+self.height)*2
        
    
    def area(self):
        return self.width*self.height