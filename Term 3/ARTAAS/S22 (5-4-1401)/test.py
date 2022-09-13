import json

phone_numbers = {
    'amirreza': '09114526532',
    'alireza': '09145874215',
}
    
file = open('phone.json', 'w', encoding='utf-8')
json.dump(phone_numbers, file, indent=4, ensure_ascii=False)
file.close()