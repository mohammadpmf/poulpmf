
import json
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox


def Login():
    pass
def Singup():
    def save():
        info ={}
        info['firstname']= e_firstname.get()
        info['lastname']= 'A'
        info['date_birthday']= f"{date_year.get()}/{date_month.get()}/{date_day.get()}"
        info['age']= 'A'
        info['gender']= 'A'
        info['nationality']= 'A'
        info['username']= 'A'
        info['password']= 'A'
        info['email']= 'A'
        information = open('information.json','w')
        json.dump(info, information)
        information.close()
    window2 = Tk()
    window2.title('Singup')
    window2.geometry('850x500')
    window2.config(bg='#ED6B5B')
    l_welcome = Label(window2,text='Sing up',font=('',40),bg='#ED6B5B',fg='#F9AC66')
    l_Firstname = Label(window2,text='Firstname: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Lastname = Label(window2,text='Lastname: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Date_on_birthday = Label(window2,text='Date on birthday: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Age = Label(window2,text='Age: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Gender = Label(window2,text='Gender: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    g = StringVar()
    frm_rbuttons = Frame(window2)
    frm_rbuttons.grid(row=4,column=6,sticky='e')
    rb1 = Radiobutton(frm_rbuttons, text="Male", variable=g, value='Male')
    rb2 = Radiobutton(frm_rbuttons, text="Female", variable=g, value='Female')
    rb3 = Radiobutton(frm_rbuttons, text="Rather Not to say", variable=g, value='_')
    rb1.grid(row=1,column=1,sticky='e')
    rb2.grid(row=1,column=2,sticky='e')
    rb3.grid(row=1,column=3,sticky='e')
    g.get()
    l_Nationality = Label(window2,text='Nationality: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Email = Label(window2,text='Email: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Uaername = Label(window2,text='Username: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    l_Password = Label(window2,text='Password: ',font=('',18),bg='#ED6B5B',fg='#F9AC66')
    e_firstname = Entry(window2)
    e_lastname = Entry(window2)
    e_age = Entry(window2)
    e_natinality = Entry(window2)
    e_email = Entry(window2)
    e_username = Entry(window2)
    e_password = Entry(window2)
    e_firstname.grid(row=2,column=4)
    e_lastname.grid(row=2,column=6)
    e_age.grid(row=4,column=4)
    e_natinality.grid(row=5,column=4)
    e_email.grid(row=7,column=4)
    e_username.grid(row=6,column=4)
    e_password.grid(row=6,column=6)
    date_year = Spinbox(window2,from_=1960,to=2022)
    date_year.config(state='readonly')
    date_year.grid(row=3,column=4,padx=30,pady=5)
    date_month = Spinbox(window2,from_=1,to=12)
    date_month.config(state='readonly')
    date_month.grid(row=3,column=5,padx=30,pady=5)
    date_day = Spinbox(window2,from_=1,to=31)
    date_day.insert(0,1)
    date_day.config(state='readonly')
    date_day.grid(row=3,column=6,padx=30,pady=5)
    l_welcome.grid(row=1,column=4,padx=20,pady=5,sticky='news')
    l_Firstname.grid(row=2,column=3,padx=20,pady=5,sticky='news')
    l_Lastname.grid(row=2,column=5,padx=20,pady=5,sticky='news')
    l_Date_on_birthday.grid(row=3,column=3,padx=20,pady=5,sticky='news')
    l_Age.grid(row=4,column=3,padx=20,pady=5,sticky='news')
    l_Gender.grid(row=4,column=5,padx=20,pady=5,sticky='news')
    l_Nationality.grid(row=5,column=3,padx=20,pady=5,sticky='news')
    l_Uaername.grid(row=6,column=3,padx=20,pady=5,sticky='news')
    l_Password.grid(row=6,column=5,padx=20,pady=5,sticky='news')
    l_Email.grid(row=7,column=3,padx=20,pady=5,sticky='news')
    btn_save = Button(window2,text='Save',font=('',15),command=save,activebackground='#165954',bg='#165954',fg='#F9AC66')
    btn_exit = Button(window2,text='Exit',font=('',15),command=exit,activebackground='#165954',bg='#165954',fg='#F9AC66') 
    btn_save.grid(row=8,column=3)
    btn_exit.grid(row=8,column=5)
    
#--------------------------------------------------------------------------------------------------
login = Tk()
login.title('Login')
login.geometry('550x350')
login.config(bg='#165954')
#--------------------------------------------------------------------------------------------------
l_welcome = Label(login,text='Welcome',font=('',40),bg='#165954',fg='#F9AC66')
l_Username = Label(login,text='Username: ',font=('',18),bg='#165954',fg='#ED6B5B')
l_Password = Label(login,text='Password: ',font=('',18),bg='#165954',fg='#ED6B5B')
l_dont_account = Label(login,text='Dont Have ann account? ',font=('',12),bg='#165954',fg='gray')
e_Username = Entry(login)
e_Password = Entry(login,show='●')
btn_login = Button(login,text='Log in',activebackground='#F9AC66',command=Login,fg='#165954',bg='#ED6B5B')
btn_Singup = Button(login,text='Sing Up',activebackground='#F9AC66',command=Singup,fg='#165954',bg='#ED6B5B')
#---------------------------------------------------------------------------------------------------
l_welcome.grid(row=1,column=3,columnspan=2,padx=20,pady=5)
l_Username.grid(row=2,column=2,padx=20,pady=5)
l_Password.grid(row=3,column=2,padx=20,pady=5)
l_dont_account.grid(row=5,column=3,padx=20,pady=5,sticky='e')
e_Username.grid(row=2,column=3,padx=20,pady=5)
e_Password.grid(row=3,column=3,padx=20,pady=5)
btn_login.grid(row=4,column=3,padx=20,pady=5)
btn_Singup.grid(row=5,column=4,padx=20,pady=5,sticky='w')
login.mainloop()