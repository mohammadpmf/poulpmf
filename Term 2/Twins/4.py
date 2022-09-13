fruits={
    'moz': 48000,
    'khiar': 18000,
    'kharbozeh': 15000,
    'hendooneh': 5000,
    'potato': 400000,
    'sibzamini': 15000,
    'holo': 30000,
    'anbeh': 80000,
    'shalil': 35000,
    'piaz': 15000,
    'goje': 20000,
    'sabzi': 20000,
    'anar': 120000,
}

potato_chips = {
    'ilya': '09218702911',
    'ilmah': '09218702937',
    'baba': '09118542154',
    'maman': '09115625478',
    'abbas booazar': '09356640204',
}
name = input('Enter name: ')
while name!= 'end':
    if name in potato_chips:
        print(potato_chips[name])
    else:
        answer = input("Mikhay ezafash koni?")
        if answer=='yes':
            n = input("shomarash chande?")
            potato_chips[name] = n
        else:
            print('bashe.')
    name = input('Enter name: ')
