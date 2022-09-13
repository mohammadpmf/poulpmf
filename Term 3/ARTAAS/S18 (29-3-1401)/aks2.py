import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('300x300')
image_data = Image.open('1.jpg')
image_data = image_data.resize((300, 300))
image = ImageTk.PhotoImage(image_data)
# img = tk.PhotoImage(file='1.jpg')
label = tk.Label(root, image=image)
label.place(x=0, y=0)
tk.Entry(root).pack(pady=5)
tk.Entry(root).pack(pady=5)
tk.Entry(root).pack(pady=5)
tk.Entry(root).pack(pady=5)
root.mainloop()