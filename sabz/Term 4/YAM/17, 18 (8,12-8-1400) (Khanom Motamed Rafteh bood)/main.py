from tkinter import *
from connector import Connector
from tkinter import ttk
my_db_name = 'jjjjj'

def create_connection():
    global connection1
    connection1 = Connector()
    if connection1.is_connected:
        print(connection1.mydb)
    else:
        print('is not connected')

def connect_to_selected_db():
    global connection1
    print(connection1.connect_to_selected_db(entry_db_name.get()))

def show_tbl_info():
    global connection1
    sv_information.set(connection1.get_tbl_info(entry_tbl_name.get()))
    
def insert_to_tbl():
    def send():
        a = entry_p_name.get(), entry_p_brand.get(), entry_p_remained.get(), entry_p_price.get()
        connection1.insert_to_tbl(a)
        temp.destroy()
    global connection1
    temp=Toplevel(root)
    entry_p_name=Entry(temp)
    lbl_p_name=Label(temp,text="name")
    entry_p_brand = Entry(temp)
    lbl_p_brand= Label(temp, text="brand")
    entry_p_remained = Entry(temp)
    lbl_p_remained = Label(temp, text="remained")
    entry_p_price = Entry(temp)
    lbl_p_price = Label(temp, text="price")
    lbl_p_name.grid(row=1 , column=1)
    entry_p_name.grid(row=1 , column=2)
    lbl_p_brand.grid(row=2 , column=1)
    entry_p_brand.grid(row=2 , column=2)
    lbl_p_remained.grid(row=3 , column=1)
    entry_p_remained.grid(row=3 , column=2)
    lbl_p_price.grid(row=4 , column=1)
    entry_p_price.grid(row=4 , column=2)
    btn_ok = Button(temp, text='OK', command=send)
    btn_ok.grid(row=5, column=1, columnspan=2, sticky='EW')

def update_tbl():
    def send():
        id= entry_p_id.get()
        name = entry_p_name.get()
        brand=entry_p_brand.get()
        remained= entry_p_remained.get() 
        price= entry_p_price.get()
        connection1.update_tbl(id, name, brand, remained, price,"products")
        temp.destroy()
    temp=Toplevel(root)
    entry_p_id=Entry(temp)
    lbl_p_id=Label(temp,text="id")
    entry_p_name=Entry(temp)
    lbl_p_name=Label(temp,text="name")
    entry_p_brand = Entry(temp)
    lbl_p_brand= Label(temp, text="brand")
    entry_p_remained = Entry(temp)
    lbl_p_remained = Label(temp, text="remained")
    entry_p_price = Entry(temp)
    lbl_p_price = Label(temp, text="price")
    lbl_p_id.grid(row=1 , column=1)
    entry_p_id.grid(row=1 , column=2)
    lbl_p_name.grid(row=2 , column=1)
    entry_p_name.grid(row=2 , column=2)
    lbl_p_brand.grid(row=3 , column=1)
    entry_p_brand.grid(row=3 , column=2)
    lbl_p_remained.grid(row=4 , column=1)
    entry_p_remained.grid(row=4 , column=2)
    lbl_p_price.grid(row=5 , column=1)
    entry_p_price.grid(row=5 , column=2)
    btn_ok = Button(temp, text='OK', command=send)
    btn_ok.grid(row=6, column=1, columnspan=2, sticky='EW')

    
def search_product():
    txt = search_entry.get()
    option= combo_search.get()
    global connection1
    sv_information.set(connection1.search_data("products", option, txt))

def delete_product():
    id= delete_entry.get()
    global connection1
    connection1.delete_data("products", id)

    


root = Tk()
root.geometry('600x600')
btn_connect_to_mysql = Button(root, text=f'Connect to mysql', command=create_connection)
entry_db_name = Entry(root)
entry_db_name.insert(0, 'jjjjj')
btn_connect_to_db = Button(root, text=f'Connect to {my_db_name}', command=connect_to_selected_db)
entry_tbl_name = Entry(root)
entry_tbl_name.insert(0 ,'products')
btn_show_tbl_info = Button(root, text='Show this tables information', command=show_tbl_info)
sv_information = StringVar()
sv_information.set('Info')
lbl_tbl_info = Label(root, textvariable=sv_information, wraplength=100)
btn_insert_item = Button(root, text='Insert', command=insert_to_tbl)
btn_update_item = Button(root, text='Update', command=update_tbl)

btn_connect_to_mysql.grid(row=1, column=1)
entry_db_name.grid(row=2, column=1)
btn_connect_to_db.grid(row=3, column=1)
entry_tbl_name.grid(row=4, column=1)
btn_show_tbl_info.grid(row=5, column=1)
lbl_tbl_info.grid(row=6, column=1)
btn_insert_item.grid(row=7, column=1)
btn_update_item.grid(row=8, column=1)

search_entry = Entry(root)
search_entry.grid(row= 9, column=1)

combo_search=ttk.Combobox(root, values=["id_products", "product_name", "price", "brand", "remained"])
combo_search.grid(row=10 , column=1)
btn_search=Button(root,text="search", command=search_product)
btn_search.grid(row=11 , column=1)


delete_entry = Entry(root)
delete_entry.grid(row = 12,column=1 )
btn_delete = Button(text="delete", command=delete_product)
btn_delete.grid(row=12, column=2)



mainloop()