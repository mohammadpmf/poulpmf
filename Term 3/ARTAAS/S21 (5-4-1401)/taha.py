import tkinter as tk
import datetime as dt


waiting=0

people=[]

def do(n):
    person=people.pop(0)
    
    if n==1: 
        status_op1.set(f"{person}")               
    if n==2: 
        status_op2.set(f"{person}")               
    if n==3: 
        status_op3.set(f"{person}")               

root=tk.Tk()
root.title("GET A NUMBER")
root.geometry("200x200+0+200")
operators=tk.Toplevel(root)
operators.title("OPERATORS")
paper=tk.Toplevel(root)
paper.geometry("200x200+250+200")
paper.title("paper")
operators.geometry("600x400+500+200")


root.config(bg="orange")

def get_number():
    global waiting
    now=dt.datetime.now()
    date.set(f"Date: {now.date()}")
    temp=now.time()
    temp=str(temp)
    temp=temp[0:8]
    time.set(f"Time")
    wait.set(f"Your cue number is: {waiting}")
    people.append(waiting)
    waiting+=1
btn_get_number=tk.Button(root,text="GET A NUMBER",bg="green",activebackground="light green",font=("",10),command=get_number,bd=10)
btn_exit=tk.Button(root,text="EXIT", bg="red",activebackground="orange",font=("",10),command=root.destroy,bd=10)
btn_get_number.pack(expand=1,fill="both",padx=30,pady=20)
btn_exit.pack(expand=1,fill="both",padx=30,pady=20)
date=tk.StringVar()
time=tk.StringVar()
wait=tk.StringVar()
lbl_date=tk.Label(paper,textvariable=date)
lbl_time=tk.Label(paper,textvariable=time)
lbl_wait=tk.Label(paper,textvariable=wait)
lbl_date.pack()
lbl_time.pack()
lbl_wait.pack()


lbl_frm_op1=tk.LabelFrame(operators,text="PRO_V",bg="orange")
lbl_frm_op1.pack(side="left",padx=30)
status_op1=tk.StringVar()
status_op1.set("Idle")
lbl_status_op1=tk.Label(lbl_frm_op1,textvariable=status_op1,bg="orange")
lbl_status_op1.pack()
btn_op1=tk.Button(lbl_frm_op1,text="OK",command=lambda:do(1))
btn_op1.pack(pady=20)


lbl_frm_op2=tk.LabelFrame(operators,text="PRO_B",bg="orange")
lbl_frm_op2.pack(side="left",padx=30)
status_op2=tk.StringVar()
status_op2.set("Idle")
lbl_status_op2=tk.Label(lbl_frm_op2,textvariable=status_op2,bg="orange")
lbl_status_op2.pack()
btn_op2=tk.Button(lbl_frm_op2,text="OK",command=lambda:do(2))
btn_op2.pack(pady=20)


lbl_frm_op3=tk.LabelFrame(operators,text="PRO_K",bg="orange")
lbl_frm_op3.pack(side="left",padx=30)
status_op3=tk.StringVar()
status_op3.set("Idle")
lbl_status_op3=tk.Label(lbl_frm_op3,textvariable=status_op3,bg="orange")
lbl_status_op3.pack()
btn_op3=tk.Button(lbl_frm_op3,text="OK",command=lambda:do(3))
btn_op3.pack(pady=20)




root.mainloop()
