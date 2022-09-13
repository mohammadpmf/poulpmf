from random import randint
answer = randint(1, 500)
guess = int(input("Guess My Number: "))
while True:
    if guess > answer:
        print("It's high. guess another number")
    elif guess < answer:
        print("It's low. guess another number")
    else:
        print(f"Excellent. answer is {answer}")
        exit()
    guess = int(input("Guess My Number: "))

