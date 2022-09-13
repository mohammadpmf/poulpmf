from time import sleep
class MyTime():
    def __init__(self, h=0, m=0, s=0):
        self.h=h
        self.m=m
        self.s=s
    
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def count(self):
        sleep(1)
        self.s+=1
        if self.s == 60:
            self.s = 0
            self.m += 1
            if self.m == 60:
                self.m = 0
                self.h += 1
                if self.h == 24:
                    self.h = 0
if __name__ == "__main__":
    ir_time = MyTime(20,0, 56)
    sw_time = MyTime(17, 30)
    while True:
        print(f"{ir_time}")
        ir_time.count()
