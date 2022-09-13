from tkinter import *
from tkinter import ttk
from hackers import Product
import pymysql

def a1():
    win=Toplevel()
    win.resizable(0,0)
    win.config(bg='pink')
    l0=Label(win,text='name',bg='pink')
    e0=Entry(win)
    l1=Label(win,text='brand',bg='pink')
    combo11=ttk.Combobox(win,values=('Gucci', 'Louis Vuitton','Chanel','Zara','Burberry','Fendi','Christian Dior','Guess','Prada','Dolce & Gabbana','christion Louboutin Prada','Versace','Armani','Hermes'))
    l2=Label(win,text='size',bg='pink')
    combo12=ttk.Combobox(win,values=('30','35','40','45','50','55','60','65','70','75','80','85','90'))
    l3=Label(win,text='type',bg='pink')
    combo13=ttk.Combobox(win,values=('Cotton','Wool','Polyester','Linen','Denim','Leather','Fur'))
    l4=Label(win,text='color',bg='pink')
    e4=Entry(win)
    l5=Label(win,text='picture',bg='pink')
    e5=Entry(win)
    
    #---grid---#
    l0.grid(row=0,column=1,pady=5, sticky='ew') 
    e0.grid(row=0,column=2,padx=5,pady=5, sticky='ew')
    l1.grid(row=1,column=1,pady=5, sticky='ew') 
    combo11.grid(row=1,column=2,padx=5,pady=5, sticky='ew')
    l2.grid(row=2,column=1,pady=5, sticky='ew') 
    combo12.grid(row=2,column=2,padx=5,pady=5, sticky='ew')
    l3.grid(row=3,column=1,pady=5, sticky='ew')
    combo13.grid(row=3,column=2,padx=5,pady=5, sticky='ew')
    l4.grid(row=4,column=1,pady=5, sticky='ew') 
    e4.grid(row=4,column=2,padx=5,pady=5, sticky='ew')
    l5.grid(row=5,column=1,pady=5, sticky='ew')
    e5.grid(row=5,column=2,padx=5,pady=5, sticky='ew')

try:
    connection = pymysql.connect(host="127.0.0.1",
    user='root'.encode('utf-8'),
    password='root'.encode('utf-8'))

except pymysql.err.OperationalError:
    print("username or password is wrong")
    exit()

garson = connection.cursor()
garson.execute("show databases;")
print(garson.fetchall())


root = Tk()
root.resizable(0,0)
btn_add = Button(root, text="Add A Product", width=20,height=5,bg='pink', command=a1)
btn_search = Button(root, text="Search", width=20,height=5,bg='#dffac5')
btn_exit = Button(root, text="Exit", command=root.destroy, width=20,height=5,bg='pink')
btn_add.pack(side='left', padx=10,pady=10)
btn_search.pack(side='left', padx=10,pady=10)
btn_exit.pack(side='left', padx=10,pady=10)

mainloop()