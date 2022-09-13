import tkinter as tk
def toggle_password():
    if show_pass.get() == 1:
        entry.config(show= '')
    else:
        entry.config(show= '*')

root = tk.Tk()
entry = tk.Entry(root, show='*')
show_pass = tk.IntVar()
checkbutton = tk.Checkbutton(root, text='show password', variable=show_pass, command=toggle_password)
entry.grid(row=1, column=1)
checkbutton.grid(row=1, column=2)
root.mainloop()