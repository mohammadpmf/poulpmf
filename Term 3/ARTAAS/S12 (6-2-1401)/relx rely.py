import tkinter as tk
root = tk.Tk()
btn1 = tk.Button(root, text=1, bg='#123456')
btn2 = tk.Button(root, text=2, bg='#654321')
btn3 = tk.Button(root, text=3, bg='#f01589')

btn1.place(relx=0,rely=0,relwidth=0.33, relheight=1)
btn2.place(relx=0.33,rely=0,relwidth=0.33, relheight=1)
btn3.place(relx=0.66,rely=0,relwidth=0.33, relheight=1)

root.mainloop()