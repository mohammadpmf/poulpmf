import prices
import tkinter as tk

print(prices.main_food_list)
root = tk.Tk()
root.geometry('1200x600+100+25')
##################################################################
#########################  Lable frames  #########################
frame_main_dish = tk.LabelFrame(root, text='main dish')
frame_drinks = tk.LabelFrame(root, text='drinks')
frame_salad = tk.LabelFrame(root, text='salad')
##################################################################
######################### Lable frames grid#######################
frame_main_dish.grid(row=1, rowspan=2, column=1)
frame_drinks.grid(row=1, column=2)
frame_salad.grid(row=2, column=2)
##################################################################
######################### main food ##############################
food_lbls = []
food_price_lbls = []
for item in prices.main_food_list:
    food_lbls.append(tk.Label(frame_main_dish, text=item[0], font=('', 12)))
    food_price_lbls.append(tk.Checkbutton(frame_main_dish,  text=item[1]))
######################### drinks ####################################
drink_lbls = []
drink_price_lbls = []
for item in prices.drinks_list:
    drink_lbls.append(tk.Label(frame_drinks, text=item[0], font=('', 12)))
    drink_price_lbls.append(tk.Checkbutton(frame_drinks, variable =tk.IntVar, text=item[1]))


####################################################################
########################## main food grid ##########################
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1, sticky='w')
    food_price_lbls[i].grid(row=i, column=2)
####################################################################
############################# drinks grid ##########################
for i in range(len(drink_lbls)):
    drink_lbls[i].grid(row=i, column=1, sticky='w')
    drink_price_lbls[i].grid(row=i, column=2)


root.mainloop()

