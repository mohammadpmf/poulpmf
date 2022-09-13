import json

file = open('phone.json', 'r', encoding='utf-8')
data = json.load(file)
print(type(data))