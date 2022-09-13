from tkinter import*


root = Tk()
root.geometry("300x300")

b1 = Button(root ,text= "start" )
b2 = Button(root,text = "start" )
l1 = Label(root)
l2 = Label(root)

b1.grid(row=0,column=0,padx=50)
b2.grid(row=0,column=1)
l1.grid(row=1,column=0,padx=50)
l2.grid(row=1,column=1)


root.mainloop()