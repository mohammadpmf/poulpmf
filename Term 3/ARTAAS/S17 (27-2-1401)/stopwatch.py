from time import sleep
import tkinter as tk
import threading

def get_chronometer(t):
    ms = t%1000
    t = t//1000
    s = t%60
    t = t//60
    m = t%60
    t = t//60
    h=t
    return f"{h:02}:{m:02}:{s:02}.{ms:03}"

def start(n):
    threading.Thread(target=count_up, args=(n,)).start()

def count_up(n):
    global timer1, timer2, timer3, is_running1, is_running2, is_running3
    if n==1:
        is_running1=True
        while is_running1:
            timer1 += 1
            sleep(0.001)
            t1.set(get_chronometer(timer1))
            root.update()
    elif n==2:
        is_running2=True
        while is_running2:
            timer2 += 1
            sleep(0.001)
            t2.set(get_chronometer(timer2))
            root.update()
    elif n==3:
        is_running3=True
        while is_running3:
            timer3 += 1
            sleep(0.001)
            t3.set(get_chronometer(timer3))
            root.update()

def reset(n):
    global timer1, timer2, timer3, is_running1, is_running2, is_running3
    if n==1:
        t1.set("00:00:00.000")
        is_running1 = False
        timer1 = 0
    elif n==2:
        t2.set("00:00:00.000")
        is_running2 = False
        timer2 = 0
    elif n==3:
        t3.set("00:00:00.000")
        is_running3 = False
        timer3 = 0

is_running1 = False
is_running2 = False
is_running3 = False
root = tk.Tk()
########################################################################
frame1 = tk.LabelFrame(root, text="Reza")
frame1.grid(row=1, column=1)
t1 = tk.StringVar()
timer1 = 0
lbl_time1 = tk.Label(frame1, textvariable=t1)
t1.set("00:00:00.000")
lbl_time1.grid(row=1, column=1, columnspan=2)
btn_start1 = tk.Button(frame1, text="Start", command=lambda:start(1))
btn_reset1 = tk.Button(frame1, text="Reset", command=lambda:reset(1))
btn_start1.grid(row=2, column=1)
btn_reset1.grid(row=2, column=2)

########################################################################
frame2 = tk.LabelFrame(root, text="Ali")
frame2.grid(row=1, column=2)
t2 = tk.StringVar()
timer2 = 0
lbl_time1 = tk.Label(frame2, textvariable=t2)
t2.set("00:00:00.000")
lbl_time1.grid(row=1, column=1, columnspan=2)
btn_start2 = tk.Button(frame2, text="Start", command=lambda:start(2))
btn_reset2 = tk.Button(frame2, text="Reset", command=lambda:reset(2))
btn_start2.grid(row=2, column=1)
btn_reset2.grid(row=2, column=2)

########################################################################
frame3 = tk.LabelFrame(root, text="Rastin")
frame3.grid(row=1, column=3)
t3 = tk.StringVar()
timer3 = 0
lbl_time3 = tk.Label(frame3, textvariable=t3)
t3.set("00:00:00.000")
lbl_time3.grid(row=1, column=1, columnspan=2)
btn_start3 = tk.Button(frame3, text="Start", command=lambda:start(3))
btn_reset3 = tk.Button(frame3, text="Reset", command=lambda:reset(3))
btn_start3.grid(row=2, column=1)
btn_reset3.grid(row=2, column=2)

root.mainloop()