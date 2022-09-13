from datetime import datetime as dt
from tkinter import *
from mytime import MyTime
import threading
def count(t, lbl, name):
    while True:
        t.count()
        lbl['text'] = name+str(t)
now = dt.now()
root = Tk()
lbl_ir = Label(root, text="00:00:00")
lbl_sw = Label(root, text="00:00:00")
ir = MyTime(now.hour,now.minute,now.second)
if now.minute>30:
    sw = MyTime(now.hour-2,now.minute-30, now.second)
else:
    sw = MyTime(now.hour-3,now.minute+30, now.second)
lbl_ir.pack()
lbl_sw.pack()
threading.Thread(target=count, daemon=True, args=(ir,lbl_ir, 'iran: ')).start()
threading.Thread(target=count, daemon=True, args=(sw,lbl_sw, 'swed: ')).start()
root.mainloop()