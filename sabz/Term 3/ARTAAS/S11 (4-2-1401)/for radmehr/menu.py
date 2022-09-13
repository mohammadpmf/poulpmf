import prices
import tkinter as tk

order_number = 1
def order():
    global order_number
    # order_number = order_number + 1
    f = open('order.txt', 'a')
    f.write(f"Order {order_number}\n")
    f.write(bill.get())
    f.write("\n\n\n")
    f.close()
    reset()
    order_number += 1
    frame_orders.config(text=f"Order {order_number}")

def reset():
    for i in str_vars_food:
        i.set(0)
    check()

def check():
    text = ""
    total_price = 0
    for i in range(len(str_vars_food)):
        if str_vars_food[i].get() == "1":
            text = text + \
            f"""{food_lbls[i]['text']:20}\t{str(food_price_lbls[i]['text']
                *int(food_numbers[i].get())):10}\n"""
            total_price = total_price +\
            food_price_lbls[i]['text']*int(food_numbers[i].get())
    text = text + "\n"
    text = text + "-"*40
    text = text + "\n"
    text = text + "Total Price: " + str(total_price)
    bill.set(text)


print(prices.main_food_list)
root = tk.Tk()
root.geometry("1000x600+100+25")
root.config(bg='light blue')

############################ Label Frames  ##################################
frame_main_dish = tk.LabelFrame(root, text="Main Dish", bg='red')
frame_drinks = tk.LabelFrame(root, text="Drinks", bg='orange')
frame_salad = tk.LabelFrame(root, text="Salad", bg='green')
frame_orders = tk.LabelFrame(root, text="Order 1", bg='sky blue')
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
food_numbers = []
str_vars_food = []
for i, item in enumerate(prices.main_food_list):
    str_vars_food.append(tk.StringVar())
    str_vars_food[i].set(0)
    food_lbls.append(tk.Label(frame_main_dish, bg='red', text=item[0], font=('', 12)))
    food_price_lbls.append(tk.Checkbutton(frame_main_dish, command=check, 
        bg='red', variable=str_vars_food[i], text=item[1], font=('', 12)))
    food_numbers.append(tk.Spinbox(frame_main_dish, from_=1, to=10, width=2, command=check))
#############################################################################
############################ Main food grid #################################
for i in range(len(food_lbls)):
    food_lbls[i].grid(row=i, column=1, sticky='news')
    food_price_lbls[i].grid(row=i, column=2, sticky='news')
    food_numbers[i].grid(row=i, column=3, sticky='news')
#############################################################################

############################ Drinks ######################################
drink_lbls = []
drink_price_lbls = []
for item in prices.drinks_list:
    drink_lbls.append(tk.Label(frame_drinks, text=item[0], font=('', 12)))
    drink_price_lbls.append(tk.Checkbutton(frame_drinks, command=check, variable=tk.IntVar(), text=item[1], font=('', 12)))
#############################################################################
############################ Drinks grid ####################################
for i in range(len(drink_lbls)):
    drink_lbls[i].grid(row=i, column=1, sticky='news')
    drink_price_lbls[i].grid(row=i, column=2, sticky='nsw')
#############################################################################
############################# Order #########################################
bill = tk.StringVar()
lbl_bill = tk.Label(frame_orders, textvariable=bill)
bill.set(0)
btn_order = tk.Button(frame_orders, text='Order', command=order)
btn_reset = tk.Button(frame_orders, text='reset', command=reset)
#############################################################################
############################# Order grid ####################################
lbl_bill.grid(row=1, column=1, columnspan=2, sticky='news')
btn_order.grid(row=2, column=1, sticky='news')
btn_reset.grid(row=2, column=2, sticky='news')
#############################################################################

root.mainloop()
