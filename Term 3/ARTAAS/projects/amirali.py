import json
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
file = open('acounts.json', 'r')
information = json.load(file)
file.close

def open_account(person):
    def withdraw():
        t = int(combo_ammount.get())
        if person['money'] >= t:
            person['money'] -=t
            write_in_json(information, 'acounts.json')
            messagebox.showinfo("", f"remained: {person['money']}")
        else:
            messagebox.showwarning("", "Not enough money")

    def change_pin():
        if pin_1.get() == person['pin']:
            if pin_2.get() == pin_3.get():
                person['pin'] = pin_2.get()
                write_in_json(information, 'acounts.json')
                messagebox.showinfo("", "Pin changed successfully.")
            else:
                messagebox.showwarning("", "Reprat does not math.")
        else:
            messagebox.showwarning("", "Wrong old pin")
    def mojodi():
        write_in_json(information, 'acounts.json')
        messagebox.showinfo("", f"remained: {person['money']}")        






    new_window = Toplevel(root)
    new_window.geometry('400x200')
    tabs = ttk.Notebook(new_window)
    tabs.grid(row=1, column=1)
    # tabs.pack()
    frame_withdraw = Frame(tabs, bg='black')
    frame_change_pin = Frame(tabs, bg='black')
    tabs.add(frame_withdraw, text='withdraw')
    tabs.add(frame_change_pin, text='Change pin')
    Label(frame_withdraw, text= "Amount: ").grid(row=1, column=1)
    combo_ammount =  ttk.Combobox(frame_withdraw, values=[2000 , 30000, 50000, 100000, 150000, 200000])
    combo_ammount.insert(0, 20000)
    combo_ammount.config(state='readonly')
    combo_ammount.grid(row=1, column=2)
    Button(frame_withdraw, text="withdraw", command= withdraw).grid(row=2, column=1)
    Button(frame_withdraw, text="Exit", command=exit).grid(row=2, column=2)
    
    Label(frame_change_pin, text= 'old pin:').grid(row=1, column=1, sticky= 'we' )
    pin_1 = Entry(frame_change_pin)
    pin_1.grid(row=1, column=2)

    Label(frame_change_pin, text='new pin:').grid(row=2, column=1, sticky='we' )
    pin_2 = Entry(frame_change_pin)
    pin_2.grid(row=2, column=2)

    Label(frame_change_pin, text= 'repeat new pin:').grid(row=3, column=1 )
    pin_3 = Entry(frame_change_pin)
    pin_3.grid(row=3, column=2)

    Button(frame_change_pin, text= 'change', command= change_pin).grid(row=5, column=1, sticky='nswe')
    Button(frame_change_pin, text= 'exit', command= exit).grid(row=5, column=2, sticky= 'nswe')


    mojodii = Frame(tabs, bg= 'black')
    tabs.add(mojodii, text='mojodi')
    Button(mojodii, text='mojodi', command=mojodi).grid(row=1, column=2)


def write_in_json(info, file):
    f = open(file, 'w')
    json.dump(info, f, indent=4)
file.close()
def check():
    found = None
    for person in information:
        card = e_number.get()
        if person['card_no'] == card:
            found = person
            break
    if found == None:
        messagebox.showwarning("warning", "account does not exist.")
        return
    if found['wrong'] >= 3:
            messagebox.showwarning("warning", "kart ghort dade shod")
            btn_enter.config(state='disable')
            return

    if found['pin'] == e_pin.get():
        messagebox.showinfo("Welcome", f"Welcome {found['name']}.")        
        found["wrong"] = 0
        write_in_json(information, 'accounts.json')
        open_account(found)
    else:
        if found['wrong'] >= 3:
            messagebox.showwarning("warning", "kart ghort dade shod")
            btn_enter.config(state='disable')
            return
        messagebox.showwarning("warning", "wrong pin")  
        found['wrong'] += 1
        write_in_json(information, 'accounts.json')

root = Tk()
l_number = Label(root, text='card number:')
l_pin = Label(root, text='PIN')
e_number = Entry(root)
e_pin = Entry(root, show='*')
l_cvv2 = Label(root, text= 'cvv2')
e_cvv2 = Entry(root)
l_date = Label(root, text='Date')
e_date = Entry(root)
btn_enter = Button(root, text='Enter', command=check)
btn_exit = Button(root, text='Exit', command=root.destroy)




l_number.grid(row=1, column=1, padx=20, pady=5)
l_pin.grid(row=2, column=1, padx=20, pady=5)
e_number.grid(row=1, column=2, padx=20, pady=5)
e_pin.grid(row=2, column=2, padx=20, pady=5)
l_cvv2.grid(row=3, column=1, padx=20, pady=5)
e_cvv2.grid(row=3, column=2, padx=20, pady=5)
l_date.grid(row=4, column=1, padx=20, pady=5)
e_date.grid(row=4, column=2, padx=20, pady=5)


btn_enter.grid(row=5, column=1, padx=20, pady=5)
btn_exit.grid(row=5, column=2, padx=20, pady=5)





root.mainloop() 

