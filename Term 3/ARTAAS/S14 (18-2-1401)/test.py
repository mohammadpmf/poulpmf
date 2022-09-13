import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
style = ttk.Style()
style.theme_create('appstyle', parent='alt',
                   settings={
                       'TLabelframe': {
                           'configure': {
                               'background': 'red'
                           }
                       },
                       'TLabelframe.Label': {
                           'configure': {
                               # 'background': 'red'     uncomment this to make even label red
                            }
                       }
                   }
                   )
style.theme_use('appstyle')


labelframe = ttk.LabelFrame(root, text="Group")
labelframe.grid(padx=20, pady=20)

left = tk.Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()