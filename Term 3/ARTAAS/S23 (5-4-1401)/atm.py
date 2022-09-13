import json
from tkinter import *
from tkinter import messagebox 

file = open('accounts.json', 'r')
information = json.load(file)
file.close()
def open_account(person):
    pass

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
    if found['pin'] == e_pin.get():
        messagebox.showinfo("Welcome", f"Welcome {found['name']}.")
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
