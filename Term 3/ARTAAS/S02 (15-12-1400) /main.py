from tkinter import *

def save():
    name = e_name.get()
    family = e_family.get()
    f = open('info.txt', 'w')
    f.write(name + ' ' + family)
    f.close()


def make_window():
    def return_to_root():
        root.deiconify()
        new.destroy()
    new = Tk()
    new.title('New window')
    btn = Button(new, text='-', command=return_to_root)
    btn.pack()
    root.withdraw()

root=Tk()
root.title("poulstar")
root.geometry("240x260+600+260")
root.config(bg="#8d74a9")
lbl_name=Label(root,text="Name:",bg="#8d74a9",fg="#da1704", font=('', 16))
lbl_name.pack()
e_name = Entry(root)
e_name.pack()
lbl_family=Label(root,text="Family:",bg="#8d74a9",fg="#da1704", font=('', 16))
lbl_family.pack()
e_family = Entry(root, show='0')
e_family.pack()
btn_save = Button(root, text='Save', command=save)
btn_exit = Button(root, text='Exit', command=exit)
btn_add = Button(root, text='+', command=make_window)
btn_save.pack(pady=10)
btn_exit.pack(pady=10)
btn_add.pack(pady=10)

root.mainloop()