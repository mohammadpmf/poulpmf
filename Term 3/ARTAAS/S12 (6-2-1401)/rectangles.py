import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(expand=1)
# frame.place(x=670, y=100)

btn1 = tk.Button(frame, text=1, bg='#123456')
btn2 = tk.Button(frame, text=2, bg='#654321')
btn3 = tk.Button(frame, text=3, bg='#f01589')
btn4 = tk.Button(frame, text=4, bg='red')
btn5 = tk.Button(frame, text=5, bg='orange')
btn6 = tk.Button(frame, text=6, bg='sky blue')
btn7 = tk.Button(frame, text=7, bg='lime')
btn8 = tk.Button(frame, text=8, bg='light green')
btn9 = tk.Button(frame, text=9, bg='cyan')
btn10 = tk.Button(frame, text=10, bg='#741021')
btn11 = tk.Button(frame, text=11, bg='purple')
btn12 = tk.Button(frame, text=12, bg='#158799')


# btn1.grid(row=5, column=5, rowspan=1, columnspan=1, sticky='news')
# btn2.grid(row=3, column=4, rowspan=1, columnspan=1, sticky='news')
# btn3.grid(row=2, column=1, rowspan=1, columnspan=1, sticky='news')
# btn4.grid(row=4, column=2, rowspan=1, columnspan=1, sticky='news')
# btn5.grid(row=1, column=3, rowspan=1, columnspan=1, sticky='news')
# btn6.grid(row=4, column=3, rowspan=1, columnspan=3, sticky='news')
# btn7.grid(row=2, column=2, rowspan=2, columnspan=2, sticky='news')
# btn8.grid(row=1, column=1, rowspan=1, columnspan=2, sticky='news')
# btn9.grid(row=1, column=4, rowspan=2, columnspan=2, sticky='news')
# btn10.grid(row=3, column=1, rowspan=3, columnspan=1, sticky='news')
# btn11.grid(row=3, column=5, rowspan=1, columnspan=1, sticky='news')
# btn12.grid(row=5, column=2, rowspan=1, columnspan=3, sticky='news')
btn1.place(x=100,y=100,width=100, height=100)


frame.mainloop()