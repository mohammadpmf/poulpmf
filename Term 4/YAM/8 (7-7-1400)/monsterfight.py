from soldier import *
from monster import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from random import randint

my_soldiers = []
# defining functions
def start():
    def show_end(winner):
        if winner == 'soldiers':
            showinfo(title='Winner', message='Soldiers Won!!!')
        elif winner == 'monster':
            showinfo(title='Winner', message='Monster Won!!!')
        play_ground.destroy()
        root.destroy()

    def attack(attacker):
        if attacker == 'soldier':
            btn_attack_monster['state'] = 'normal'
            btn_attack['state'] = 'disabled'
            current_soldier = combo_soldiers.get()
            if current_soldier == '':
                info_soldier.set('No soldier selected!!!')
            for i in my_soldiers:
                if current_soldier == i.name:
                    monster.decrease_health(i.attack())
                    if monster.is_alive == FALSE:
                        info_monster.set(f'{monster.name} is dead!!!')
                        show_end('soldiers')
                        
                    else:
                        info_monster.set(monster.show_all_info())
        elif attacker == 'monster':
            btn_attack_monster['state'] = 'disabled'
            btn_attack['state'] = 'normal'
            current_soldier = combo_soldiers.get()
            if current_soldier == '':
                info_soldier.set('No soldier selected!!!')
            for i in my_soldiers:
                if current_soldier == i.name:
                    i.decrease_health(monster.attack())
                    if i.is_alive == False:
                        info_soldier.set(f'{i.name} is dead!!!')
                        my_soldiers.remove(i)
                        combo_soldiers['values'] = my_soldiers
                        if len(my_soldiers) == 0:
                            show_end('monster')
                        try:
                            combo_soldiers.current(0)
                        except:
                            pass
                    else:
                        info_soldier.set(i.show_all_info())
    def test_refresh(event):
        current_soldier = combo_soldiers.get()
        if current_soldier == '':
            info_soldier.set('Choose a soldier!!!')
        for i in my_soldiers:
            if current_soldier == i.name:
                info_soldier.set(i.show_all_info())
        temp = monster.show_all_info()
        info_monster.set(temp)

    def refresh():
        current_soldier = combo_soldiers.get()
        if current_soldier == '':
            info_soldier.set('Choose a soldier!!!')
        for i in my_soldiers:
            if current_soldier == i.name:
                # print(i.show_all_info())
                info_soldier.set(i.show_all_info())
        temp = monster.show_all_info()
        # print(temp)
        info_monster.set(temp)
    root.withdraw()
    play_ground = Toplevel()
    play_ground.deiconify()
    play_ground.geometry('400x400')
    play_ground.title('Play ground')
    play_ground.resizable(0, 0)
    monster = Monster(name='Shrek', health=randint(200, 350),
                    shield=randint(50, 100), attack_damage=randint(30, 45))
    combo_soldiers = ttk.Combobox(play_ground, values=my_soldiers, state='readonly')
    try:
        combo_soldiers.current(0)
    except:
        pass
    combo_soldiers.bind("<<ComboboxSelected>>", test_refresh)
    btn_refresh = Button(play_ground, text = 'refresh', command = refresh)
    btn_attack = Button(play_ground, text = 'attack', command = lambda: attack('soldier'))
    btn_attack_monster = Button(play_ground, text = 'attack', command = lambda: attack('monster'), state='disabled')
    info_soldier = StringVar()
    lbl_info_soldiers = Label(play_ground, textvariable=info_soldier, bg='cyan')
    info_monster = StringVar()
    lbl_info_monster = Label(play_ground, textvariable=info_monster, bg='cyan')
    btn_exit = Button(play_ground, text='exit', command=exit)

    combo_soldiers.place(x=20, y=20, width=150)
    btn_refresh.place(x=20, y=60, width=150)
    btn_attack.place(x=20, y=100, width=150)
    btn_attack_monster.place(x=220, y=60, width=150, height=70)
    lbl_info_soldiers.place(x=20, y=140, width=150, height=200)
    lbl_info_monster.place(x=220, y=140, width=150, height=200)
    btn_exit.pack(side='bottom')
    refresh()

def show_soldiers():
    names = ''
    for i in my_soldiers:
        names += i.show_all_info()
        # names = names + i.show_all_info()
        names += '\n\n'
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
            showwarning(title='money', message="You don't have enough money to buy strong soldier!!!")
    elif n == 2:
        temp_soldier = Soldier(name=entered_name, health=150, attack_damage = 25)
        m = money.get()
        if m >= 250:
            money.set(m-250)
            my_soldiers.append(temp_soldier)
        else:
            showwarning(title='money', message="You don't have enough money to buy normal soldier!!!")
    elif n == 3:
        temp_soldier = Soldier(name=entered_name, health=75, attack_damage = 18)
        m = money.get()
        if m >= 150:
            money.set(m-150)
            my_soldiers.append(temp_soldier)
        else:
            showwarning(title='money', message="You don't have enough money to buy weak soldier!!!")
    else:
        pass
    entry_name.insert(0, 'a')
    # entry_name.delete(0, END)


# defining root window
root = Tk()
root.geometry('400x600')
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
entry_name.insert(2,'ab')
my_soldiers_strvar = StringVar()
lbl_my_army = Label(root, textvariable=my_soldiers_strvar)

# showing widgets
lbl_money.place(x=10, y=10, width=200, height=50)
btn_soldier1.place(x=10, y=60, width=100, height=40)
btn_soldier2.place(x=10, y=110, width=100, height=40)
btn_soldier3.place(x=10, y=160, width=100, height=40)
entry_name.place(x=110, y=60, width=100, height=40)
lbl_my_army.place(x=10, y=210)
btn_show_my_army.pack(side='bottom')
btn_lets_fight.pack(side='bottom')

mainloop()