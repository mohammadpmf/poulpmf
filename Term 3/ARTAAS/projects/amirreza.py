import json
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
############################################################################ App Codes ###########################################################################################
file = open('accounts.json','r')
information = json.load(file)
file.close()
############################################################################ Defs ################################################################################################

def open_account(person):
    pass
def back():
    new_window.destroy()
    root.deiconify()
def withdraw():
    t = int(combo_ammount.get())
    if person['money'] >= t:
        person[''] += t
        write_in_json(information,'accounts.json')
        messagebox.showinfo("info", f"remained: {person['money']}")
    else:
        messagebox.showwarning("Warning","Not Enough Money")
def change_pin():
    if old_pin.get() == person['pin']:
        if new_pin.get() == new_pin2.get():
            person['pin'] = new_pin2.get()
            write_in_json(information,'accounts.json')
            messagebox.showinfo("info","Pin Changed Successfully")
        else:
            messagebox.showwarning("Warning","Repeat Dose Not Match.")
    else:
        messagebox.showwarning("Warning","Old Wrong Pin.")
def balance_of_money():
        messagebox.showinfo("info", f"remained: {person['money']}")
    root.withdraw()


def write_in_json(info, file):
    f= open(file, 'w')
    json.dump(info,f,indent=4)
    f.close()
def check():
    found = None
    for person in  information:
        card = e_number.get()
        if person['card_no'] == card:
            found = person
            break  
    if found == None:
        messagebox.showwarning("Warning","The entered card number is incorrect.")
        return
    if found['pin'] == e_pin.get():
        if found['date'] == e_date.get():
            if found['password'] == e_password.get():
                messagebox.showinfo("Welcome",f"Welcome {found['name']}.")
                open_account(found)
            else:
               messagebox.showwarning("Warning","The password entered is not correct.")
               found['wrong'] += 1 
               write_in_json(information, 'accounts.json')
        else:
            # messagebox.showinfo("info","The date of the card is entered correctly")
            messagebox.showwarning("Warning","The date of the card is not entered correctly")
    else:
        if found['wrong'] >= 3:
            messagebox.showwarning("Warning","Your card has been blocked.")
            btn_enter.config(state='disable')
            return
        # messagebox.showinfo("info","The password entered is correct.")
        messagebox.showwarning("Warning","The card PIN entered is incorrect")
        found['wrong'] += 1
        write_in_json(information, 'accounts.json')
def toggle_password1():
    if show_pass.get() == 1:
        e_pin.config(show= '')
    else:
        e_pin.config(show= '●')
def toggle_password2():
    if show_pass2.get() == 1:
        e_password.config(show= '')
    else:
        e_password.config(show= '●')
########################################################################### Root #################################################################################################
root = Tk()
root.geometry('400x300')
root.config(bg='#F8BD06')
root.title('Mobile Bank')
#۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩ Label ۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩#
l_mobile_bank = Label(root,text='۩ Mobile Bank ۩',font=('',25),bg='#F8BD06')
l_number = Label(root,text='Card Number: ',font=('',15),bg='#F8BD06')
l_pin = Label(root,text='Card Pin: ',font=('',15),bg='#F8BD06')
l_date = Label(root,text='Date Card:',font=('',15),bg='#F8BD06')
l_password = Label(root,text='Password:',font=('',15),bg='#F8BD06')
#۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩ Entry ۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩#
e_number = Entry(root)
e_pin = Entry(root,show='●')
e_date = Entry(root)
e_password = Entry(root,show='●')
#۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩ Button ۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩#
btn_enter = Button(root, text='Enter',command=check,activebackground='#FFE800',bg='#0F0C03',fg='#FFE800',bd=7)
btn_exit = Button(root, text='Exit',command=root.destroy,activebackground='#FFE800',bg='#0F0C03',fg='#FFE800',bd=7)
#۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩ CheckButton ۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩#
show_pass = IntVar()
checkbutton = Checkbutton(root, text='', variable=show_pass,bg='#F8BD06' ,command=toggle_password1)
checkbutton.grid(row=3, column=3)
show_pass2 = IntVar()
checkbutton = Checkbutton(root, text='', variable=show_pass2,bg='#F8BD06' ,command=toggle_password2)
checkbutton.grid(row=5, column=3)
#۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩ Gird ۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩#
l_mobile_bank.grid(row=1,column=1,columnspan=2,padx=20,pady=5)
l_number.grid(row=2,column=1,padx=20,pady=5)
l_pin.grid(row=3,column=1,padx=20,pady=5)
l_date.grid(row=4,column=1,padx=20,pady=5)
l_password.grid(row=5,column=1,padx=20,pady=5)
e_number.grid(row=2,column=2,padx=20,pady=5)
e_pin.grid(row=3,column=2,padx=20,pady=5)
e_date.grid(row=4,column=2,padx=20,pady=5)
e_password.grid(row=5,column=2,padx=20,pady=5)
btn_enter.grid(row=6,column=1,padx=20,pady=5)
btn_exit.grid(row=6,column=2,padx=20,pady=5)
#۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩ Finish Code Apps ۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩۩#
new_window = Toplevel(root)
new_window.geometry('348x187')
new_window.config(bg='#FF6400')
tabs = ttk.Notebook(new_window)
passive_color = "#FF6400"
active_color = "#FFE800"
try:
    style = ttk.Style()
    style.theme_create("yummy", parent="alt", 
    settings={
            "TNotebook": 
                {"configure": 
                    {"tabmargins": [2, 5, 2, 0] }
                },
            "TNotebook.Tab": 
                {
                    "configure":
                        {"padding": [5, 1], "background": passive_color },
                    "map":
                        {
                            "background": [("selected", active_color)],
                                "expand": [("selected", [1, 1, 1, 0])]
                        }
                }
        }
    )
    style.theme_use("yummy")
    tabs.grid(row=1, column=1)
except:
    pass
frm_withdraw = Frame(tabs,bg='#FFE800')
frm_change_pin = Frame(tabs,bg='#FFE800')
frm_Money_transfer = Frame(tabs,bg='#FFE800')
frm_balaece_of_money = Frame(tabs,bg='#FFE800')
tabs.add(frm_withdraw, text='Withdraw')
tabs.add(frm_change_pin, text='Change Pin')
tabs.add(frm_Money_transfer,text='Money Transfer')
tabs.add(frm_balaece_of_money,text='Balece Of Money')
Label(frm_withdraw, text='Ammount :',bg='#FFE800').grid(row=1 ,column=1,padx=20,pady=5,sticky='w')
Label(frm_change_pin,text='Old Pin :',bg='#FFE800',font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='w')
Label(frm_change_pin,text='New Pin :',bg='#FFE800',font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='w')
Label(frm_change_pin,text='Repeat New Pin :',bg='#FFE800',font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='w')
Label(frm_Money_transfer,text='account number :',bg='#FFE800',font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='w')
Label(frm_Money_transfer,text='Amount :',bg='#FFE800',font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='w')
Label(frm_balaece_of_money,text='Balaece Of Money :',bg='#FFE800',font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='w')
old_pin = Entry(frm_change_pin)
old_pin.grid(row=1,column=2)
new_pin = Entry(frm_change_pin)
new_pin.grid(row=2,column=2)
new_pin2 = Entry(frm_change_pin)
new_pin2.grid(row=3,column=2)
account_number = Entry(frm_Money_transfer)
account_number.grid(row=1,column=2)
amount = Entry(frm_Money_transfer)
amount.grid(row=2,column=2)
balaece_of_money = Entry(frm_balaece_of_money)
balaece_of_money.grid(row=1,column=2)
combo_ammount = ttk.Combobox(frm_withdraw,values=[10000, 20000, 50000,
70000, 80000, 100000, 200000 ,500000,1000000,2000000,5000000,10000000,20000000,50000000])
combo_ammount.insert(0,20000)
combo_ammount.config(state='readonly')
combo_ammount.grid(row=1,column=2)
#################################################################################################### Butten #########################################################################################################
Button(frm_withdraw,text='Withdraw',fg='#FFE800',bd=7,bg='#0F0C03',command=withdraw,activebackground='#FFE800').grid(row=2,column=1,padx=20,pady=5,sticky='w')
Button(frm_withdraw,text='Exit',fg='#FFE800',command=exit,bd=7,bg='#0F0C03',activebackground='#0F0C03').grid(row=2,column=2)
Button(frm_change_pin,text='Save',fg='#FFE800',bd=7,bg='#0F0C03',command=change_pin,activebackground='#FFE800').grid(row=4,column=1,padx=20,pady=5,sticky='w')
Button(frm_change_pin,text='Back to the main page',fg='#FFE800',bd=7,command=back,bg='#0F0C03',activebackground='#FFE800').grid(row=4,column=2)
Button(frm_Money_transfer,text='Confirm operation',fg='#FFE800',bd=7,bg='#0F0C03',activebackground='#FFE800').grid(row=3,column=1,padx=20,pady=5,sticky='w')
Button(frm_Money_transfer,text='Back to the main page',fg='#FFE800',bd=7,bg='#0F0C03', command=back,activebackground='#FFE800').grid(row=3,column=2)
Button(frm_balaece_of_money,text='Confirm operation',fg='#FFE800',bd=7,bg='#0F0C03',command=balance_of_money,activebackground='#FFE800').grid(row=3,column=1,padx=20,pady=5,sticky='w')
root.mainloop()
