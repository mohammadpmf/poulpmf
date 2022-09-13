import tkinter as tk
import datetime as dt

waiting = 0
people = []

def do(n):
    try:
        person = people.pop(0)
        print(people)
        if n==1:
            status_op1.set(f"Im doing {person} job.")
        elif n==2:
            status_op2.set(f"Im doing {person} job.")
        elif n==3:
            status_op3.set(f"Im doing {person} job.")
    except IndexError:
        print('Kasi too Saf nist.')



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
    people.append(waiting)
    waiting += 1

btn_get_number = tk.Button(root, text='Get a Number', bd=7
    , bg='green', activebackground='light green', command=get_number)
btn_exit = tk.Button(root, text='Exit', bd=7, font=('Calibri', 12),
    bg='red', activebackground='orange', command=root.destroy)
btn_get_number.pack(expand=1, fill='both', padx=30, pady=15)
btn_exit.pack(expand=1, fill='both', padx=30, pady=15)
#################################### end get number window ################
#################################### paper window ################
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
#################################### end paper window ################
#################################### operators window ################
operators.config(bg='light blue')
#################################### op1 ################
lbl_frm_op1 = tk.LabelFrame(operators, text='Ali Ahmadi', bg='light blue')
lbl_frm_op1.pack(side='left', padx=30)
status_op1 = tk.StringVar()
status_op1.set('Idle')
lbl_status_op1 = tk.Label(lbl_frm_op1, textvariable=status_op1, bg='light blue')
lbl_status_op1.pack(pady=10)
btn_op1 = tk.Button(lbl_frm_op1, text='OK', command=lambda: do(1))
btn_op1.pack(pady=20)

#################################### op2 ################
lbl_frm_op2 = tk.LabelFrame(operators, text='Radmehr Ghamkhar', bg='light blue')
lbl_frm_op2.pack(side='left', padx=30)
status_op2 = tk.StringVar()
status_op2.set('Idle')
lbl_status_op2 = tk.Label(lbl_frm_op2, textvariable=status_op2, bg='light blue')
lbl_status_op2.pack(pady=10)
btn_op2 = tk.Button(lbl_frm_op2, text='OK', command=lambda: do(2))
btn_op2.pack(pady=20)

#################################### op3 ################
lbl_frm_op3 = tk.LabelFrame(operators, text='Mohammad Fallah', bg='light blue')
lbl_frm_op3.pack(side='left', padx=30)
status_op3 = tk.StringVar()
status_op3.set('Idle')
lbl_status_op3 = tk.Label(lbl_frm_op3, textvariable=status_op3, bg='light blue')
lbl_status_op3.pack(pady=10)
btn_op3 = tk.Button(lbl_frm_op3, text='OK', command=lambda: do(3))
btn_op3.pack(pady=20)
#################################### end operators window ################


root.mainloop()