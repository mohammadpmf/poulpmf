import prices
import tkinter as tk

print(prices.main_food_list)
root = tk.Tk()
root.geometry("1250x600+100+25")
root.config(bg='light blue')

############################ Label Frames  ##################################
frame_main_dish = tk.LabelFrame(root, text="Main Dish", bg='red')
frame_drinks = tk.LabelFrame(root, text="Drinks", bg='green')
frame_salad = tk.LabelFrame(root, text="Salad", bg='yellow')
frame_orders = tk.LabelFrame(root, text="Order", bg='blue')
frame_pishghaza = tk.LabelFrame(root, text="pishghaza", bg='purple')
frame_mokhalafat = tk.LabelFrame(root, text="mokhalafat", bg='pink')
frame_ghazahayepeykghabelersal= tk.LabelFrame(root, text="ghazahayepeykghabelersal", bg='black')
#############################################################################
############################ Label Frames grid ##############################
frame_main_dish.grid(row=1, rowspan=1, column=1, sticky='news')
frame_drinks.grid(row=1, column=2, sticky='news')
frame_salad.grid(row=2, column=2, sticky='news')
frame_orders.grid(row=2, column=1, sticky='news')
frame_pishghaza.grid(row=1, column=3, sticky='news')
frame_mokhalafat.grid(row=2, column=3, sticky='news')
frame_ghazahayepeykghabelersal.grid(row=2, column=4, sticky='news')
#############################################################################
############################ Main food ######################################
food_lbls = []
food_price_lbls = []
for item in prices.main_food_list:
    food_lbls.append(tk.Label(frame_main_dish, text=item[0], font=('', 12), bg='#ff3838'))
    food_price_lbls.append(tk.Checkbutton(frame_main_dish, variable=tk.IntVar(), text=item[1], font=('', 12), bg='#ff3838'))
#############################################################################
############################ Main food grid #################################
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1, sticky='news',)
    food_price_lbls[i].grid(row=i, column=2, sticky='news')
##############################################################################
############################ main Drinks #####################################
drink_lbls = []
drink_price_lbls = []
for item in prices.drinks_list:
    drink_lbls.append(tk.Label(frame_drinks, text=item[0], font=('', 12), bg='#53ff38'))
    drink_price_lbls.append(tk.Checkbutton(frame_drinks, variable=tk.IntVar(), text=item[1], font=('', 12), bg='#53ff38'))
#############################################################################
############################ main Drinks grid ####################################
for i in range(len(drink_lbls)):
    drink_lbls[i].grid(row=i, column=1, sticky='news')
    drink_price_lbls[i].grid(row=i, column=2, sticky='news')
#############################################################################
########################### main salad ######################################
salad_lbls = []
salad_price_lbls = []
for item in prices.salad_list:
    salad_lbls.append(tk.Label(frame_salad, text=item[0], font=('', 12), bg='#dbf531'))
    salad_price_lbls.append(tk.Checkbutton(frame_salad, variable=tk.IntVar(), text=item[1], font=('', 12), bg='#dbf531'))
#############################################################################
############################# main salad grid ###############################
for i in range(len(salad_lbls)):
    salad_lbls[i].grid(row=i, column=1, sticky='news')
    salad_price_lbls[i].grid(row=i, column=2, sticky='news')
############################# main pishghaza #################################
pishghaza_lbls = []
pishghaza_price_lbls = []
for item in prices.pishghaza_list:
    pishghaza_lbls.append(tk.Label(frame_pishghaza, text=item[0], font=('', 15), bg='#236465'))
    pishghaza_price_lbls.append(tk.Checkbutton(frame_pishghaza, variable=tk.IntVar(), text=item[1], font=('', 12), bg='#901592'))
###############################################################################
############################ main pishghaza grid ##############################
for i in range(len(pishghaza_lbls)):
    pishghaza_lbls[i].grid(row=i, column=1, sticky='news')
    pishghaza_price_lbls[i].grid(row=i, column=2, sticky='news')
###############################################################################
########################### main mokhalafat ###################################
mokhalafat_lbls = []
mokhalafat_price_lbls = []
for item in prices.mokhalafat_list:
    mokhalafat_lbls.append(tk.Label(frame_mokhalafat, text=item[0], font=('', 12), bg='#901592'))
    mokhalafat_price_lbls.append(tk.Checkbutton(frame_mokhalafat, variable=tk.IntVar(), text=item[1], font=('', 12), bg='#901592'))
################################################################################
########################### main mokhalafat grid ###############################
for i in range(len(mokhalafat_lbls)):
    mokhalafat_lbls[i].grid(row=i, column=1, sticky='news')
    mokhalafat_price_lbls[i].grid(row=i, column=2, sticky='news')
################################################################################
########################### main ghazahayepeykghabelersal ######################
ghazahayepeykghabelersal_lbls = []
ghazahayepeykghabelersal_price_lbls = []
for item in prices.ghazahayepeykghabelersal_list:
    ghazahayepeykghabelersal_lbls.append(tk.Label(frame_ghazahayepeykghabelersal, text=item[0], font=('', 12),))
    ghazahayepeykghabelersal_price_lbls.append(tk.Checkbutton(frame_ghazahayepeykghabelersal, variable=tk.IntVar(), text=item[1], font=('', 12),))
################################################################################
########################## main ghazahayepeykghabelersal grid ##################
for i in range(len(ghazahayepeykghabelersal_lbls)):
    ghazahayepeykghabelersal_lbls[i].grid(row=i, column=1, sticky='news')
    ghazahayepeykghabelersal_price_lbls[i].grid(row=i, column=2, sticky='news')
################################################################################
############################# main Order #######################################
bill = tk.StringVar()
lbl_bill = tk.Label(frame_orders, textvariable=bill)
bill.set(0)
##################################################################################
############################# main Order grid ####################################
lbl_bill.grid(row=1, column=1, sticky='news')
#################################################################################


root.mainloop()