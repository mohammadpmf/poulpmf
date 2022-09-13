import tkinter as tk
from tkinter import ttk

root = tk.Tk()
combo = ttk.Combobox(root, values=['1', '2', '3'])
combo['state'] = 'readonly'
combo.pack()
tk.Entry(root).pack()

style = ttk.Style()
style.map('TCombobox', selectbackground=[('readonly', 'red')])
#style.map('TCombobox', fieldbackground=[('readonly', 'blue')]) #not working as well
root.mainloop()