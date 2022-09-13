from tkinter import *
def test():
    print(e_name.get())
root = Tk()
root.geometry('500x500')
Label(root, text='Name: ').grid(row=1, column=1, padx=10, sticky='w', pady=5)
e_name = Entry(root, width=20)
e_name.grid(row=1, column=2, columnspan=2, padx=10, sticky='ew')
Button(root, text="ok", command=test).grid(row=4,column=54)
mainloop()