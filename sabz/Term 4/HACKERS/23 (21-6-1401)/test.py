from tkinter import ttk
import tkinter as tk
window = tk.Tk()
treev = ttk.Treeview(window, selectmode ='browse')
treev.grid(row=1, column=1)
verscrlbar = ttk.Scrollbar(window,orient ="vertical",command = treev.yview)
verscrlbar.grid(row=1, column=2, sticky='ns')
treev.configure(yscrollcommand = verscrlbar.set)
treev["columns"] = ("1", "2", "3", "4", "5")
treev['show'] = 'headings'
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='c')
treev.column("3", width = 40, anchor ='c')
treev.column("4", width = 90, anchor ='c')
treev.column("5", width = 90, anchor ='c')
treev.heading("1", text ="Name")
treev.heading("2", text ="Brand")
treev.heading("3", text ="Size")
treev.heading("4", text ="Type")
treev.heading("5", text ="Color")
treev.insert("", 'end', text ="L1",values =("T-Shirt", "Puma", "75", "Wool", "Red"))
window.mainloop()