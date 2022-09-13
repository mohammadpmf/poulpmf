import tkinter as tk
import datetime as dt

waiting = 0

#################################### windows ################
root = tk.Tk()
root.title('Get a Number')
root.geometry('200x200+0+200')
paper = tk.Toplevel(root)
paper.title("Paper")
paper.geometry('200x200+250+200')
operators = tk.Toplevel(root)
operators.title('Operators')
operators.geometry('600x400+500+200')
#################################### end windows ################
#################################### get number window ################
root.config(bg='sky blue')
def get_number():
    global waiting
    now = dt.datetime.now()
    date.set(f"Date: {now.date()}")
    temp = now.time()
    temp = str(temp)
    temp = temp[0:8]
    time.set(f"Time: {temp}")
    wait.set(f"Waiting people: {waiting}")
    waiting += 1

btn_get_number = tk.Button(root, text='Get a Number', bd=7
    , bg='green', activebackground='light green', command=get_number)
btn_exit = tk.Button(root, text='Exit', bd=7, font=('Calibri', 12),
    bg='red', activebackground='orange', command=root.destroy)
btn_get_number.pack(expand=1, fill='both', padx=30, pady=15)
btn_exit.pack(expand=1, fill='both', padx=30, pady=15)
#################################### end get number window ################
paper.config(bg='light blue')
date = tk.StringVar()
time = tk.StringVar()
wait = tk.StringVar()
lbl_date = tk.Label(paper, textvariable=date, pady=10, bg='light blue')
lbl_time = tk.Label(paper, textvariable=time, pady=10, bg='light blue')
lbl_wait = tk.Label(paper, textvariable=wait, pady=30, bg='light blue')
lbl_date.pack()
lbl_time.pack()
lbl_wait.pack()

root.mainloop()