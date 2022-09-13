import prices
import tkinter as tk

print(prices.main_food_list)
root = tk.Tk()
root.geometry("1000x600+100+25")
root.config(bg='light blue')

############################ Label Frames  ##################################
frame_main_dish = tk.LabelFrame(root, text="Main Dish", bg='red')
frame_drinks = tk.LabelFrame(root, text="Drinks", bg='orange')
frame_salad = tk.LabelFrame(root, text="Salad", bg='green')
frame_orders = tk.LabelFrame(root, text="Order", bg='blue')
#############################################################################
############################ Label Frames grid ##############################
frame_main_dish.grid(row=1, rowspan=2, column=1, sticky='news')
frame_drinks.grid(row=1, column=2, sticky='news')
frame_salad.grid(row=2, column=2, sticky='news')
frame_orders.grid(row=3, column=1, sticky='news')
#############################################################################
############################ Main food ######################################
food_lbls = []
food_price_lbls = []
for item in prices.main_food_list:
    food_lbls.append(tk.Label(frame_main_dish, bg='red', text=item[0], font=('', 12)))
    food_price_lbls.append(tk.Checkbutton(frame_main_dish, bg='red', variable=tk.IntVar(), text=item[1], font=('', 12)))
#############################################################################
############################ Main food grid #################################
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1, sticky='news')
    food_price_lbls[i].grid(row=i, column=2, sticky='news')
#############################################################################

############################ Drinks ######################################
drink_lbls = []
drink_price_lbls = []
for item in prices.drinks_list:
    drink_lbls.append(tk.Label(frame_drinks, text=item[0], font=('', 12)))
    drink_price_lbls.append(tk.Checkbutton(frame_drinks, variable=tk.IntVar(), text=item[1], font=('', 12)))
#############################################################################
############################ Drinks grid ####################################
for i in range(len(drink_lbls)):
    drink_lbls[i].grid(row=i, column=1, sticky='news')
    drink_price_lbls[i].grid(row=i, column=2, sticky='news')
#############################################################################
############################# Order #########################################
bill = tk.StringVar()
lbl_bill = tk.Label(frame_orders, textvariable=bill)
bill.set(0)
#############################################################################
############################# Order grid ####################################
lbl_bill.grid(row=1, column=1, sticky='news')
#############################################################################


root.mainloop()
