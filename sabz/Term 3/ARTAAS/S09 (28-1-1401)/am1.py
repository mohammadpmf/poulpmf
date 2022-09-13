import tkinter as tk
import am


root = tk.Tk()
root.geometry('1800x1300+100+25')
root.config(bg='light blue')
################################## Label Frames  ######################################
frame_main_dish = tk.LabelFrame(root, text='Main Dish')
frame_drinks = tk.LabelFrame(root, text='Drinks')
frame_salad = tk.LabelFrame(root, text='Salad')
frame_appertizers = tk.LabelFrame(root,text='Appertizers')
#######################################################################################
################################# Lable Framres Grid ##################################
frame_main_dish.grid(row=1, rowspan=2,column=1, sticky='ns')
frame_drinks.grid(row=1, column=2)
frame_salad.grid(row=1,column=3, sticky='ns')
frame_appertizers.grid(row= 3,column=3)
#######################################################################################
#################################  Main Food  #########################################
food_lbls = []
food_price_lbls = []
for item in am.main_food_list:
    food_lbls.append(tk.Label(frame_main_dish,text=item[0],font=('',12)))
    food_price_lbls.append(tk.Checkbutton(frame_main_dish,text=item[1],font=('', 12)))
#######################################################################################
################################  Main Food Grid ######################################
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1,sticky = 'w' )
    food_price_lbls[i].grid(row=i, column= 2,sticky = 'w')
#######################################################################################
################################  Main Drink  ##########################################
drink_lbls = []
drink_price_lbls = []
for item in am.drinks_list:
    drink_lbls.append(tk.Label(frame_drinks,text=item[0],font=('',12)))
    drink_price_lbls.append(tk.Checkbutton(frame_drinks,text=item[1],font=('',12)))
######################################################################################    
for i in range(len(drink_lbls)):
    drink_lbls[i].grid(row=i, column=1,sticky = 'wn' )
    drink_price_lbls[i].grid(row=i, column= 2,sticky = 'wn')
#################################  Main Salad  #######################################
salad_lbls = []
salad_price_lbls = []
for item in am.salad_list:
    salad_lbls.append(tk.Label(frame_salad,text=item[0],font=('',12)))
    salad_price_lbls.append(tk.Checkbutton(frame_salad,text=item[1],font=('',12)))
#####################################################################################   
for i in range(len(salad_lbls)):
    salad_lbls[i].grid(row=i, column=1,sticky = 'wne' )
    salad_price_lbls[i].grid(row=i, column= 2,sticky = 'wne')
root.mainloop()