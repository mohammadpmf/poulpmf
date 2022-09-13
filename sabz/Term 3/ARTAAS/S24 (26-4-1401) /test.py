# import tkinter as tk					
# from tkinter import ttk


# root = tk.Tk()
# root.title("Tab Widget")
# tabControl = ttk.Notebook(root)

# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)

# tabControl.add(tab1, text ='Tab 1')
# tabControl.add(tab2, text ='Tab 2')
# tabControl.pack(expand = 1, fill ="both")

# ttk.Label(tab1,
# 		text ="Welcome to \
# 		GeeksForGeeks").grid(column = 0,
# 							row = 0,
# 							padx = 30,
# 							pady = 30)
# ttk.Label(tab2,
# 		text ="Lets dive into the\
# 		world of computers").grid(column = 0,
# 									row = 0,
# 									padx = 30,
# 									pady = 30)

# root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

mygreen = "#d2ffd2"
myred = "#dd0202"

style = ttk.Style()

style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": mygreen },
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

note = ttk.Notebook(root)
f1 = ttk.Frame(note, width=300, height=200)
note.add(f1, text = 'First')
f2 = ttk.Frame(note, width=300, height=200)
note.add(f2, text = 'Second')
note.pack(expand=1, fill='both', padx=5, pady=5)

tk.Button(root, text='yummy!').pack(fill='x')

root.mainloop()