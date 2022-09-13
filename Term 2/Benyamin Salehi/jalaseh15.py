foods = ['adas polo', 'hamburger', 'loobia polo',
        'pizza', 'mahi', 'mahi', 'mahi', 'kebab']
foods.append('fried chicken')
foods.insert(0, 'beafstraganof')
foods.remove('pizza')
foods.remove('mahi')
print(foods.count('mahi'))
# foods.clear() تمام اعضای داخل لیست را پاک میکند.
# ghazaha = foods.copy() یک کپی از لیست درست میکند و در متغیر جدید ذخیره میکند.
# print(foods)
# foods.sort()
# foods.reverse()
print(foods)
foods.sort()
print(foods)