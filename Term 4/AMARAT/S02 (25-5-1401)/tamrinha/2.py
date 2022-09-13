class House():
    def __init__(khone, m, t , g):
       khone.metr = m
       khone.tabaghe = t
       khone.gheymat = g


    def __str__(khone):
        return f"\nmetr:{khone.metr}\ntabaghe: {khone.tabaghe}\ngheymat: {khone.gheymat}"

h1 = House(200, 5, 1250000000000)
h2 = House(150, 1, 500000000)
h3 = House(300, 8, 500000000000000)
h4 = House(250, 3, 67000000000)
print(h1)
print(h2)
print(h3)
print(h4)
