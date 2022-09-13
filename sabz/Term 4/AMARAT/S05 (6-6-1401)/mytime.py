from time import sleep
class MyTime():
    def __init__(self, h=0, m=0, s=0, us=0):
        self.h=h
        self.m=m
        self.s=s
        self.us = us
    
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}.{self.us:02}"
    
    def count(self):
        sleep(0.01)
        self.us+=1
        if self.us==100:
            self.us = 0
            self.s+=1
            if self.s == 60:
                self.s = 0
                self.m += 1
                if self.m == 60:
                    self.m = 0
                    self.h += 1
                    if self.h == 24:
                        self.h = 0

    def count_down(self):
        sleep(1)
        self.s-=1
        if self.s < 0:
            if self.m > 0:
                self.s = 59
                self.m -= 1
            else:
                if self.h > 0:
                    self.m = 59
                    self.s = 59
                    self.h -=1
                else:
                    self.s = 0

if __name__ == "__main__":
    ir_time = MyTime(0,0,2)
    sw_time = MyTime(17, 30)
    while str(ir_time)!="00:00:00.00":
        print(f"{ir_time}")
        ir_time.count()
