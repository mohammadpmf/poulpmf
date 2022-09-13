real_password = "ilmah"

wrong = 0
p = input("Enter your password: ")
while p != real_password:
    print("wrong passwrod")
    wrong += 1
    if wrong == 3:
        print("You are not Ilmah. Looser.")
        exit()
    p = input("Enter your password: ")
print("Welcome Ilmah")
