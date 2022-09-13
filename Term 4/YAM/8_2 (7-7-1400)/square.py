class Square():
    def __init__(self, width = 100):
        self.width = width
        # self.__secret_info='salam'

    def perimeter(self):
        return self.width*4
        
    
    def area(self):
        return self.width*self.width