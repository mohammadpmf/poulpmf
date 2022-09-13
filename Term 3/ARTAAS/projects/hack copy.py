import string as st
from tkinter import *

real_pasword="a"
guess=""

my_list= st.ascii_letters + st.punctuation +st.digits

def hack() :
    for i in my_list:
        guess=i
        
        if guess == real_pasword:
           
            return
    for i in my_list:
        for i2 in my_list:
            guess=i+i2
            print(guess)
            if guess == real_pasword:
                
                return
    for i in my_list:
        for i2 in my_list:
            for i3 in my_list:
                guess=i+i2+i3
                print(guess)
                if guess == real_pasword:
                    
                    return
    for i in my_list:
        for i2 in my_list:
            for i3 in my_list:
                for i4 in my_list:
                    guess=i+i2+i3+i4
                    print(guess)
                    if guess == real_pasword:
                        
                        return
    for i in my_list:
        for i2 in my_list:
            for i3 in my_list:
                for i4 in my_list:
                    for i5 in my_list:
                        guess=i+i2+i3+i4+i5
                        print(guess)
                        if guess == real_pasword:
                            
                            return

    for i in my_list:
        for i2 in my_list:
            for i3 in my_list:
                for i4 in my_list:
                    for i5 in my_list:
                        for i6 in my_list:
                            guess=i+i2+i3+i4+i5+i6
                            print(guess)
                            if guess == real_pasword:
                                
                                return

hack()
root=Tk()
root.geometry('300x200')
f_pasword=Label(root,text=guess)
f_pasword.grid()
root.mainloop()


