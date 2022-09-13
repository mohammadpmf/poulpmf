# e_to_p = {
#     'hello': 'salam',
#     'bye': 'khodahafez',
# }
# grades = {
#     'amir': 19,
#     'reza': 18.5,
#     'ali': 20,
# }
phones = {
    'mohammad': '09356640204',
    'amin': '09112541411',
    'baba': '09145126588',
}
fruits = {
    'moz': 48000,
    'sibzamini': 18000,
    'khiar': 17000,
    'shalil': 35000,
    'holoo': 40000,
    'goje': 20000,
    'piaz': 15000,
}
print(phones)
name = input("Enter name: ")
while name != 'end':
    if phones.get(name) != None:
        print(phones.get(name))
    else:
        a = input("add? y or n")
        if a=='y':
            n = input("Enter number")
            phones[name]=n
    name = input("Enter name: ")

