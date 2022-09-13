from myclass import *

root = Tk()
root.geometry('600x400')
dama1 = Thermometer(root, 'gold', '#c97b06', 20)
dama2 = Thermometer(root, 'silver', 'green', 60)
dama1.grid(row=1, column=1)
dama2.grid(row=2, column=1)

root.mainloop()