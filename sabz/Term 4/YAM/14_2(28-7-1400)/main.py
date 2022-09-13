from tkinter import *
from connector import Connector
my_db_name = 'jjjjj'

def create_connection():
    global connection1
    connection1 = Connector()
    if connection1.is_connected:
        print(connection1.mydb)
    else:
        print('is not connected')

def connect_to_selected_db():
    pass

root = Tk()
root.geometry('600x600')
btn_connect_to_mysql = Button(root, text=f'Connect to mysql', command=create_connection)
entry_db_name = Entry(root)
btn_connect_to_db = Button(root, text=f'Connect to {my_db_name}', command=connect_to_selected_db)

btn_connect_to_mysql.grid(row=1, column=1)
entry_db_name.grid(row=2, column=1)
btn_connect_to_db.grid(row=3, column=1)

mainloop()