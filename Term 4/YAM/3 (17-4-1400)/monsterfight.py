from soldier import *
from monster import *
from tkinter import *

my_soldiers = []

# defining functions
def show_soldiers():
    names = ''
    for i in my_soldiers:
        names += i.name
        # names = names + my_soldiers.name
        names += '\t'
    print(names)

def buy_soldier(n):
    pass
    if n == 1:
        temp_soldier = Soldier(name='Ali', health=200)
        m = money.get()
        if m >= 300:
            money.set(m-300)
            my_soldiers.append(temp_soldier)
        else:
            print('Not enought money.')
    elif n == 2:
        temp_soldier = Soldier(name='Reza', health=150)
        m = money.get()
        if m >= 250:
            money.set(m-250)
            my_soldiers.append(temp_soldier)
        else:
            print('Not enought money.')
    elif n == 3:
        temp_soldier = Soldier(name='Hasan', health=75)
        m = money.get()
        if m >= 150:
            money.set(m-150)
            my_soldiers.append(temp_soldier)
        else:
            print('Not enought money.')
    else:
        pass


# defining root window
root = Tk()
root.geometry('600x600')
root.title('Monster fight')
root.resizable(0, 0)

# defining widgets
money = IntVar()
lbl_money = Label(root, textvariable=money)
money.set(1000)
btn_soldier1 = Button(root, text='Big', command=lambda: buy_soldier(1))
btn_soldier2 = Button(root, text='Normal', command=lambda: buy_soldier(2))
btn_soldier3 = Button(root, text='Small', command=lambda: buy_soldier(3))
btn_show_my_army = Button(root, text='show my army',
                         command=lambda: show_soldiers())
entry_name = Entry(root)

# showing widgets
lbl_money.place(x=10, y=10, width=200, height=50)
btn_soldier1.place(x=10, y=60, width=100, height=40)
btn_soldier2.place(x=10, y=110, width=100, height=40)
btn_soldier3.place(x=10, y=160, width=100, height=40)
entry_name.place(x=110, y=60, width=100, height=40)
btn_show_my_army.pack(side='bottom')

mainloop()