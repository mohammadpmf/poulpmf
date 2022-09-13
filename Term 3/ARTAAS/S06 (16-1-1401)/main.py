import tkinter as tk

def up():
    a = int(lbl_1['text'])
    a = a + 1
    lbl_1 ['text'] = a
    # lbl_1['text'] = int(lbl_1['text'])+1
    if a > 30:
        lbl_2 ['text'] = "Fan is On"
        lbl_2 ['bg'] = "red"
def down():
    a = int(lbl_1['text'])
    a = a - 1
    lbl_1 ['text'] = a
    # lbl_1['text'] = int(lbl_1['text'])+1
    if a < 15:
        lbl_2 ['text'] = "Heater is on"
        lbl_2 ['bg'] = "blue"
    elif a < 25:
        lbl_2 ['text'] = "Fan is off"
        lbl_2 ['bg'] = "green"


root = tk.Tk()
root.geometry("300x200")
lbl_frame = tk.LabelFrame(root, text="Termometer")
btn_up = tk.Button(lbl_frame, text = "UP", command=up, font=('', 20))
btn_down = tk.Button(lbl_frame, text = "DOWN", command=down, font=('', 20))
btn_up.grid(row=1, column=1, sticky='news')
btn_down.grid(row=2, column=1, sticky='news')
lbl_frame.pack()
lbl_1 = tk.Label(lbl_frame, text="20", font=('', 20))
lbl_2 = tk.Label(lbl_frame, text="Fan is off", font=('', 20))
lbl_1.grid(row=1, column=2, sticky='news')
lbl_2.grid(row=2, column=2, sticky='news')
root.mainloop()
