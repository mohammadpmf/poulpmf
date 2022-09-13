s = 0
item = input("Enter item: ")
while item!='end':
    if item == 'pofak':
        s = s + 10000
    elif item == 'bastani':
        s = s + 12000
    elif item == 'bisquit':
        s = s + 8000
    else:
        print("item not found")
    item = input("Enter item: ")
print(f"Your total income is: {s}") # income = پولی که به دست می آوریم.
