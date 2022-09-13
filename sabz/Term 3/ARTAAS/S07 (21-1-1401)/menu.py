import prices
import tkinter as tk

print(prices.main_food_list)
root = tk.Tk()
root.geometry("1000x600+100+25")
root.config(bg='light blue')

############################ Label Frames  ##################################
frame_main_dish = tk.LabelFrame(root, text="Main Dish")
frame_drinks = tk.LabelFrame(root, text="Drinks")
frame_salad = tk.LabelFrame(root, text="Salad")
#############################################################################
############################ Label Frames grid ##############################
frame_main_dish.grid(row=1, rowspan=2, column=1)
frame_drinks.grid(row=1, column=2)
frame_salad.grid(row=2, column=2)
#############################################################################
############################ Main food ######################################
food_lbls = []
food_price_lbls = []
for item in prices.main_food_list:
    food_lbls.append(tk.Label(frame_main_dish, text=item[0], font=('', 12)))
    food_price_lbls.append(tk.Checkbutton(frame_main_dish, text=item[1], font=('', 12)))
#############################################################################
############################ Main food grid #################################
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1, sticky='w')
    food_price_lbls[i].grid(row=i, column=2)
#############################################################################



root.mainloop()
