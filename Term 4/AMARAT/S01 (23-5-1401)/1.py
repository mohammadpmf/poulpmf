class Human():
    def __init__(khodam, n, f, h, a):
        khodam.name = n
        khodam.family = f
        khodam.height = h
        khodam.age = a
    
    def __str__(khodam):
        return f"{khodam.name} {khodam.family}\nheight: {khodam.height}\nSen:{khodam.age}"

h1 = Human('amirreza', 'moosavi', 180, 15)
h2 = Human('taha', 'hatami', 170, 13)
h3 = Human('Radmehr', 'Ghamkhar', 175, 14)

print(h2)

# a = 5
# s = "salam"
# p = 3.14
# print(type(a), type(s), type(p), type(h1))