from tkinter import *
from hackers import Product
import pymysql

root = Tk()
root.resizable(0,0)
btn_add = Button(root, bg='green', text="Add A Product", width=16, height=5)
btn_search = Button(root, bg='light blue', text="Search", width=16, height=5)
btn_exit = Button(root, bg='orange', text="Exit", command=root.destroy, width=16, height=5)
btn_add.pack(side='left', padx=10, pady=10)
btn_search.pack(side='left', padx=10, pady=10)
btn_exit.pack(side='left', padx=10, pady=10)

mainloop()