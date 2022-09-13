import json

person = {
    'name': 'mohammad',
    'family': 'fallah',
    'father': {
        'name':'ali',
        'age': 70
        },
    'age': 30,
    'nat_code': '1234567890',
    'phone': ['09356640204', '09112545142', '09915487777']
}

list_of_persons = [
    {
    'name': 'reza',
    'family': 'alavi',
    'father': {
        'name':'ahmad',
        'age': 65
        },
    'age': 25,
    'nat_code': '1234567890',
    'phone': ['09356640204', '09112545142', '09915487777']
},
{
    'name': 'ahmad',
    'family': 'niazi',
    'father': {
        'name':'kazem',
        'age': 60
        },
    'age': 28,
    'nat_code': '1234567890',
    'phone': ['09356640204', '09112545142']
},
{
    'name': 'mohammad',
    'family': 'fallah',
    'father': {
        'name':'ali',
        'age': 70
        },
    'age': 30,
    'nat_code': '1234567890',
    'phone': ['09356640204', '09112545142', '09915487777']
}
]

f = open('test.json', 'w')
json.dump(person, f, indent=1)
f.close()
