from tkinter import *
from tkinter import ttk
from hackers import Product
from tkinter import messagebox
import pymysql
def a2():
    def back():
        root.deiconify()
        win.destroy()
    win=Toplevel(root)
    def alaki():
        pass
    win.protocol("WM_DELETE_WINDOW", alaki)
    root.withdraw()
    win.resizable(0,0)
    win.config(bg='red')
    btn_back=Button(win,text="back",command=back)
    treev = ttk.Treeview(win, selectmode ='browse')
    treev.grid(row=1,column=1)
    verscrlbar = ttk.Scrollbar(win,orient ="vertical",command = treev.yview)
    verscrlbar.grid(row=1,column=2,sticky='ns')
    treev.configure(yscrollcommand = verscrlbar.set)
    treev["columns"] = ("1", "2", "3","4", "5")
    treev['show'] = 'headings'
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 40, anchor ='c')
    treev.column("4", width = 90, anchor ='c')
    treev.column("5", width = 90, anchor ='c')
    treev.heading("1", text ="Name")
    treev.heading("2", text ="brand")
    treev.heading("3", text ="size")
    treev.heading("4",text="type")
    treev.heading("5",text="color")
    treev.insert("", 'end', text ="L1",values =("t_shirt", "zara", "25","wool","red"))
    btn_back.grid(row=9000,column=9000)
    
    
def a1():
    def save():
        name =e0.get()
        brand =combo11.get()
        size=combo12.get()
        type=combo13.get()
        color=e4.get()
        Address=e5.get()
        if name =="":
            messagebox.showwarning("name","enter name of product")
            return
        if brand =="":
            messagebox.showwarning("brand","enter brand of product")
            return
        if size =="":
            messagebox.showwarning("size","enter size of product")
            return
        if type =="":
            messagebox.showwarning("type","enter type of product")
            return
        if color =="":
            messagebox.showwarning("color","enter color of product")
            return
        q ="INSERT INTO `hackers`.`products` (`name`, `brand`, `size`, `type`, `color`, `picture_address`) VALUES (%s, %s, %s, %s, %s, %s);"
        v=name,brand,size,type,color,Address
        garson.execute(q ,v)
        connection.commit()
    win=Toplevel(root)
    def back():
        root.deiconify()
        win.destroy()
        def alaki ():
            pass
        win.protocol("WM_DELETE_WINDOW", alaki)
    root.withdraw()
    win.resizable(0,0)
    win.config(bg='red')
    l0=Label(win,text='name',bg='red')
    e0=Entry(win)
    l1=Label(win,text='brand',bg='red')
    combo11=ttk.Combobox(win,values=('Gucci', 'Louis Vuitton','Chanel','Zara','Burberry','Fendi','Christian Dior','Guess','Prada','Dolce & Gabbana','christion Louboutin Prada','Versace','Armani','Hermes'))
    l2=Label(win,text='size',bg='red')
    combo12=ttk.Combobox(win,values=('30','35','40','45','50','55','60','65','70','75','80','85','90'))
    l3=Label(win,text='type',bg='red')
    combo13=ttk.Combobox(win,values=('Cotton','Wool','Polyester','Linen','Denim','Leather','Fur'))
    l4=Label(win,text='color',bg='red')
    e4=Entry(win)
    l5=Label(win,text='picture',bg='red')
    e5=Entry(win)
    btn_save = Button(win, text='Save',bg='yellow',command=save)
    btn_back = Button(win, text='Back',bg='yellow', command=back)
    
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
    btn_save.grid(row=6,column=1,padx=5,pady=5, sticky='ew')
    btn_back.grid(row=6,column=2,padx=5,pady=5, sticky='ew')


try:
    connection = pymysql.connect(host="127.0.0.1",
    user="root",
    password="root")
    garson = connection.cursor()
    garson.execute("create database if not exists hackers;")
    garson.execute("CREATE TABLE if not exists `hackers`.`products` (`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,`name` VARCHAR(50) NOT NULL,`brand` VARCHAR(50) NOT NULL,`size` VARCHAR(20) NOT NULL,`type` VARCHAR(20) NOT NULL,`color` VARCHAR(50) NOT NULL,`picture_address` VARCHAR(150) NULL,PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC));")


except pymysql.err.OperationalError:
    print("not ok")
    exit()


root = Tk()
root.resizable(0,0)
btn_add = Button(root, text="Add A Product", width=20,height=5,bg='yellow', command=a1)
btn_search = Button(root, text="Search", width=20,height=5,bg='#dffac5',command=a2)
btn_exit = Button(root, text="Exit", command=root.destroy, width=20,height=5,bg='yellow')
btn_add.pack(side='left', padx=10,pady=10)
btn_search.pack(side='left', padx=10,pady=10)
btn_exit.pack(side='left', padx=10,pady=10)


mainloop()