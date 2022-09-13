from tkinter import *
from tkinter import messagebox
import json
file=open('acant.json','r')
information= json.load(file)
file.close()
def open_acant(piple):
    pass
wrong=StringVar
def check():
    found=None
    print(information)
    for piple in information:
        card=e_number.get()     
        if piple['card_n'] == card:
            found=piple           
            break
    if found== None:
        messagebox.showwarning("Not True!!","cart vojod nadarad")
        return
    if found['pin'] == e_pin.get():
        messagebox.showinfo(f"welcom",{found['name']})
        open_acant(found)
      
    else :
        messagebox.showwarning("Not True!!","acant vojod nadarad")
        file=open('acant.json','w')
        json.dump(information,file,indent=4)
        file.close()
        found ['wrong'] +=1
        if found ['wrong'] >=3:
            btn1.config(state='disable')

      


           
##1218=2022\\\0909=1010\\\\3331=0000\\\\\6104=1022=pin and card_number
####root###
root = Tk()
root.config(bg='cyan')
root.geometry('370x250')
###Entry###
e_number=Entry(root)
e_pin=Entry(root)
e_number.grid(row=1,column=2,padx=20,pady=10)
e_pin.grid(row=2,column=2,padx=20,pady=10)
###Lable###
l_1=Label(root,text='Card_Number:',font=('',14),bg='black',fg='red')
l_2=Label(root,text='PIN:',font=('',14),bg='black',fg='red')
l_1.grid(row=1,column=1)
l_2.grid(row=2,column=1)
##Button###
btn1=Button(root,text='Enter',font=('',12),bg='black',fg='gold',bd=7,pady=10
,activebackground='purple',activeforeground='lightgreen',command=check)
btn2=Button(root,text='Exit',font=('',12),bg='black',fg='gold',bd=7,pady=10,padx=17,command=exit
,activeforeground='lightgreen',activebackground='purple')
btn1.grid(row=3,column=1)
btn2.grid(row=3,column=2)
###########

root.mainloop()