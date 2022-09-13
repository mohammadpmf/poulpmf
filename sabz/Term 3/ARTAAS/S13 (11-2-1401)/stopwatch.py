import tkinter as tk

root = tk.Tk()
frame1 = tk.LabelFrame(root, text="Reza")
frame1.grid(row=1, column=1)

t1 = tk.StringVar()
lbl_time1 = tk.Label(frame1, textvariable=t1)
t1.set("00:00:00.00")
lbl_time1.grid(row=1, column=1, columnspan=2)

btn_start1 = tk.Button(frame1, text="Start")
btn_reset1 = tk.Button(frame1, text="Reset")
btn_start1.grid(row=2, column=1)
btn_reset1.grid(row=2, column=2)

root.mainloop()