from tkinter import *
from mytime import MyTime
import threading
def count(t, lbl, name):
    while True:
        t.count()
        lbl['text'] = name+str(t)
root = Tk()
lbl_ir = Label(root, text="00:00:00")
lbl_sw = Label(root, text="00:00:00")
ir = MyTime(20,11,19)
sw = MyTime(17,41)
lbl_ir.pack()
lbl_sw.pack()
threading.Thread(target=count, daemon=True, args=(ir,lbl_ir, 'iran: ')).start()
threading.Thread(target=count, daemon=True, args=(sw,lbl_sw, 'swed: ')).start()
root.mainloop()