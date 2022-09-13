from soldier import *
from monster import *
from tkinter import *
from tkinter import ttk
from random import randint

my_soldiers = []

# defining functions
def start():
    def attack():
        pass
        current_soldier = combo_soldiers.get()
        # for i in my_soldiers:
        #     print(i)
        # else:
        #     print('No soldier selected.')

    root.withdraw()
    play_ground = Tk()
    play_ground.geometry('400x400')
    play_ground.title('Monster fight')
    play_ground.resizable(0, 0)
    enemy = Monster(name='Shrek', health=randint(200, 350),
                    shield=randint(50, 100), attack_damage=randint(30, 45))
    combo_soldiers = ttk.Combobox(play_ground, values=my_soldiers)
    btn_attack = Button(play_ground, text = 'attack', command = attack)

    combo_soldiers.place(x=20, y=20, width=150)
    btn_attack.place(x=20, y=60, width=150)

def show_soldiers():
    names = ''
    for i in my_soldiers:
        names += i.name
        # names = names + my_soldiers.name
        names += '\t'
    my_soldiers_strvar.set(names)

def buy_soldier(n):
    entered_name = entry_name.get()
    if n == 1:
        temp_soldier = Soldier(name=entered_name, health=200, attack_damage=30)
        m = money.get()
        if m >= 300:
            money.set(m-300)
            my_soldiers.append(temp_soldier)
        else:
            print('Not enought money.')
    elif n == 2:
        temp_soldier = Soldier(name=entered_name, health=150, attack_damage = 25)
        m = money.get()
        if m >= 250:
            money.set(m-250)
            my_soldiers.append(temp_soldier)
        else:
            print('Not enought money.')
    elif n == 3:
        temp_soldier = Soldier(name=entered_name, health=75, attack_damage = 18)
        m = money.get()
        if m >= 150:
            money.set(m-150)
            my_soldiers.append(temp_soldier)
        else:
            print('Not enought money.')
    else:
        pass
    entry_name.delete(0, END)


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
btn_lets_fight = Button(root, text='Start fighting', command=start)
entry_name = Entry(root)
my_soldiers_strvar = StringVar()
lbl_my_army = Label(root, textvariable=my_soldiers_strvar)

# showing widgets
lbl_money.place(x=10, y=10, width=200, height=50)
btn_soldier1.place(x=10, y=60, width=100, height=40)
btn_soldier2.place(x=10, y=110, width=100, height=40)
btn_soldier3.place(x=10, y=160, width=100, height=40)
entry_name.place(x=110, y=60, width=100, height=40)
lbl_my_army.place(x=10, y=210, height=40)
btn_show_my_army.pack(side='bottom')
btn_lets_fight.pack(side='bottom')

mainloop()