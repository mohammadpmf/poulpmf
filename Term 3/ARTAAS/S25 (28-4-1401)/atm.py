import json
from tkinter import *
from tkinter import messagebox 
import tkinter.ttk as ttk

file = open('accounts.json', 'r')
information = json.load(file)
file.close()


def open_account(person):
    def withdraw():
        t = int(combo_ammount.get())
        if person['money'] >= t:
            person['money'] -= t
            write_in_json(information, 'accounts.json')
            messagebox.showinfo("", f"remained: {person['money']}")
        else:
            messagebox.showwarning("", "Not enough money.")
    def change_pin():
        if old_pin.get() == person['pin']:
            if new_pin.get() == new_pin2.get():
                person['pin'] = new_pin.get()
                write_in_json(information, 'accounts.json')
                messagebox.showinfo("", "Pin changed successfully.")
            else:
                messagebox.showwarning("", "Repeat does not match.")
        else:
            messagebox.showwarning("", "Wrong Old pin")

    new_window = Toplevel(root)
    new_window.geometry('400x200')
    tabs = ttk.Notebook(new_window)
    tabs.grid(row=1, column=1)
    # tabs.pack()
    frame_withdraw = Frame(tabs)
    frame_change_pin = Frame(tabs)
    tabs.add(frame_withdraw, text ='Withdraw')
    tabs.add(frame_change_pin, text='Change Pin')
    Label(frame_withdraw, text = "Amount: ").grid(row=1, column=1)
    combo_ammount = ttk.Combobox(frame_withdraw, values=[20000, 50000, 120000, 200000])
    combo_ammount.insert(0, 20000)
    combo_ammount.config(state='readonly')
    combo_ammount.grid(row=1, column=2)
    Button(frame_withdraw, text="Withdraw", command=withdraw).grid(row=2, column=1)
    Button(frame_withdraw, text="Exit", command=exit).grid(row=2, column=2)

    Label(frame_change_pin, text = "Old Pin: ").grid(row=1, column=1)
    Label(frame_change_pin, text = "New Pin: ").grid(row=2, column=1)
    Label(frame_change_pin, text = "Repete new Pin: ").grid(row=3, column=1)
    old_pin = Entry(frame_change_pin)
    new_pin = Entry(frame_change_pin)
    new_pin2 = Entry(frame_change_pin)
    old_pin.grid(row=1, column=2)
    new_pin.grid(row=2, column=2)
    new_pin2.grid(row=3, column=2)
    Button(frame_change_pin, text="Change", command=change_pin).grid(row=4, column=1)
    Button(frame_change_pin, text="Exit", command=exit).grid(row=4, column=2)






def write_in_json(info, file):
    f = open(file, 'w')
    json.dump(info, f, indent=4)
    f.close()

def check():
    found = None
    for person in information:
        card = e_number.get()
        if person['card_no'] == card:
            found = person
            break
    if found == None:
        messagebox.showwarning("Warning", "Account does not exist.")
        return
    if found['wrong'] >= 3:
        messagebox.showwarning("Warning", "Karte shoma ghoort dadeh shod.")
        btn_enter.config(state='disable')
        return
    if found['pin'] == e_pin.get():
        messagebox.showinfo("Welcome", f"Welcome {found['name']}.")
        found['wrong'] = 0
        write_in_json(information, 'accounts.json')
        open_account(found)
    else:
        if found['wrong'] >= 3:
            messagebox.showwarning("Warning", "Karte shoma ghoort dadeh shod.")
            btn_enter.config(state='disable')
            return
        messagebox.showwarning("Warning", "Wrong pin.")
        found['wrong'] += 1
        write_in_json(information, 'accounts.json')

root = Tk()
l_number = Label(root, text="card number: ")
l_pin = Label(root, text="PIN: ")
e_number = Entry(root)
e_pin = Entry(root, show='*')
btn_enter = Button(root, text='Enter', command=check)
btn_exit = Button(root, text='Exit', command=root.destroy)

l_number.grid(row=1, column=1, padx=20, pady=5)
l_pin.grid(row=2, column=1, padx=20, pady=5)
e_number.grid(row=1, column=2, padx=20, pady=5)
e_pin.grid(row=2, column=2, padx=20, pady=5)
btn_enter.grid(row=3, column=1, padx=20, pady=5)
btn_exit.grid(row=3, column=2, padx=20, pady=5)

root.mainloop()
