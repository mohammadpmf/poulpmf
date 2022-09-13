import prices 
import tkinter as tk
root = tk.Tk()
root.geometry("1250x600+100+25")

############################ Label Frames  ##################################
frame_main_dish = tk.LabelFrame(root, text="main dish")
frame_drinks = tk.LabelFrame(root, text="Drinks")
frame_salad = tk.LabelFrame(root, text="salad")
############################ Label Frames grid  ##################################
frame_main_dish.grid(row=1, rowspan=2, column=1, sticky='news')
frame_drinks.grid(row=1, column=2, sticky='news')
frame_salad.grid(row=2, column=2, sticky='news')
############################ main food ##################################
food_lbls = []
food_prices_lbls = []
food_ivs= []
for item in prices.main_food_list:
    food_lbls.append(tk.Label(frame_main_dish, text=item[0]))
    food_prices_lbls.append(tk.Checkbutton(frame_main_dish, text=item[1]))
#############################food grid####################  
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1, sticky='news')
    food_prices_lbls[i].grid(row=i, column=2, sticky='news')
############################ main drinks ##################################
drinks_lbls = []
drinks_prices_lbls = []
for item in prices.drinks_list:
    drinks_lbls.append(tk.Label(frame_drinks, text=item[0]))
    drinks_prices_lbls.append(tk.Checkbutton(frame_drinks, text=item[1]))
#############################drinks grid####################  
for i in range(len(drinks_lbls)):
    drinks_lbls[i].grid(row=i, column=1, sticky='news')
    drinks_prices_lbls[i].grid(row=i, column=2, sticky='news')
#########################################################################



root.mainloop()