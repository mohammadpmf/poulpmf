from tkinter import *

root = Tk()
l_number = Label(root, text="card number: ")
l_pin = Label(root, text="PIN: ")
e_number = Entry(root)
e_pin = Entry(root)
btn_enter = Button(root, text='Enter')
btn_exit = Button(root, text='Exit', command=root.destroy)

l_number.grid(row=1, column=1, padx=20, pady=5)
l_pin.grid(row=2, column=1, padx=20, pady=5)
e_number.grid(row=1, column=2, padx=20, pady=5)
e_pin.grid(row=2, column=2, padx=20, pady=5)
btn_enter.grid(row=3, column=1, padx=20, pady=5)
btn_exit.grid(row=3, column=2, padx=20, pady=5)

root.mainloop()