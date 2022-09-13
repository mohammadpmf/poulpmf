from tkinter import ttk
from tkinter import *

import pymysql


root = Tk()
def ff():
    pass

try:   
    connection=pymysql.connect(host="127.0.0.1",user="root".encode("utf-8"),password="root".encode("utf-8"))
except pymysql.err.OperationalError:
    print("no")
    exit()
garson=connection.cursor()
garson.execute("show databases;")
print(garson.fetchall())    
serch=Toplevel()
lbl1=Label(serch,text="name",bg="blue",fg="red")
lbl1.grid(row=1,column=1)
en1=Entry(serch)
en1.grid(row=1,column=2)
lbl2=Label(serch,text="brand",bg="blue",fg="red")
lbl2.grid(row=7,column=1)
comoo=ttk.Combobox(serch,values=("kxdskf"))
comoo.grid(row=7,column=2)
como=ttk.Combobox(serch,values=("kxdskf"))
como.grid(row=4,column=2)
lbl3=Label(serch,text="size",bg="blue",fg="red")
lbl3.grid(row=3,column=1)
en2=Entry(serch)
en2.grid(row=3,column=2)
lbl4=Label(serch,text="type",bg="blue",fg="red")
lbl4.grid(row=4,column=1)
lbl5=Label(serch,text="color",bg="blue",fg="red")
lbl5.grid(row=5,column=1)
en5=Entry(serch)
en5.grid(row=5,column=2)

lbl6=Label(serch,text="picture",bg="blue",fg="red")
lbl6.grid(row=6,column=1)
en6=Entry(serch)
en6.grid(row=6,column=2)
###############################################
root.resizable(0,0)
btn_add=Button(root,text="Add A Produkt",width=16,height=5)
btn_search=Button(root,text="Search",command=ff,width=16,height=5)
btn_exit=Button(root,text="Exit",command=root.destroy,width=16,height=5,)
btn_add.pack(side="left",padx=10,pady=10)
btn_search.pack(side="left",padx=10,pady=10)
btn_exit.pack(side="left",padx=10,pady=10)

mainloop()
