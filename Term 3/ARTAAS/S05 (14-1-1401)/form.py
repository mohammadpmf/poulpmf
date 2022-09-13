from tkinter import *

def reset():
    e_name.delete(0, END)
    e_family.delete(0, END)
    s_age.config(state='normal')
    s_age.delete(0, END)
    s_age.insert(0, 18)
    s_age.config(state='readonly')
    s.set(1)

def save():
    f = open(e_name.get(), 'w')
    info = f"Name: {e_name.get()}\nFamily: {e_family.get()}\nAge: {s_age.get()}\nGender: "
    if s.get() == 1:
        info = info + "Female"
    elif s.get() == 2:
        info = info + "Male"
    f.write(info)
    f.close()

root2 = Tk()
root2.config(bg='sky blue')
# root2.geometry('500x500')
root = Frame(root2)
root.pack()
l_name = Label(root, text='Name: ', fg='#369147')
e_name = Entry(root, width=20)
l_family = Label(root, text='Family: ')
e_family = Entry(root)
l_age = Label(root, text='Age: ')
# s_age = Spinbox(root, from_=1, to=5, state='readonly', wrap=True)
s_age = Spinbox(root, from_=1, to=80, state='readonly')
l_gender=Label(root, text="Gender: ")
s = IntVar()
r1 = Radiobutton(root, text='Female', variable=s, value=1)
r2 = Radiobutton(root, text='Male', variable=s, value=2)
btn_save = Button(root, text='Save', command=save)
btn_reset = Button(root, text='Reset', command=reset)
btn_exit = Button(root, text='Exit', command=exit)

l_name.grid(row=1, column=1, padx=10, sticky='w', pady=5)
e_name.grid(row=1, column=2, columnspan=2, padx=10, sticky='ew')
l_family.grid(row=2, column=1, padx=10, sticky='w', pady=5)
e_family.grid(row=2, column=2, columnspan=2, padx=10, sticky='ew')
l_age.grid(row=3, column=1, padx=10, sticky='w', pady=5)
s_age.grid(row=3, column=2, columnspan=2, padx=10, sticky='ew')
l_gender.grid(row=4, column=1, padx=10, sticky='w', pady=5)
r1.grid(row=4, column=2, padx=10, sticky='ew')
r2.grid(row=4, column=3, padx=10, sticky='ew')
btn_save.grid(row=5, column=1, padx=10, sticky='ew')
btn_reset.grid(row=5, column=2, padx=10, sticky='we')
btn_exit.grid(row=5, column=3, padx=10, sticky='ew')
mainloop()