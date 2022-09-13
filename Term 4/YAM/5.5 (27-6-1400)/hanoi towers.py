# in code ro khodam az roosh zadam.
def hanoi(n, avvali, akhari, komaki):
    if n == 1:
        print(avvali, '-->', akhari)
    else:
        hanoi(n-1, avvali, komaki, akhari)
        print(avvali, '-->', akhari)
        hanoi(n-1, komaki, akhari, avvali)
print ('\n\n!!!! Enter a number less than 20 !!!!\n\n')
n = int(input("Enter n: "))
hanoi(n, 1, 3, 2)
