morse = {
    'A':  	'· –',
    'B':  	'– · · ·',
    'C':  	'– · – ·',
    'D':  	'– · ·',
    'E':  	'·',
    'F':  	'· · – ·',
    'G':  	'– – ·',
    'H':  	'· · · ·',
    'I':  	'· ·',
    'J':  	'· – – –',
    'K':  	'– · –',
    'L':  	'· – · ·',
    'M':  	'– –',
    'N':  	'– ·',
    'O':  	'– – –',
    'P':  	'· – – ·',
    'Q':  	'– – · –',
    'R':  	'· – ·',
    'S':  	'· · ·',
    'T':  	'–',
    'U':  	'· · –',
    'V':  	'· · · –',
    'W':  	'· – –',
    'X':  	'– · · –',
    'Y':  	'– · – –',
    'Z':  	'– – · ·',
    '1': 	'· – – – –',
    '2': 	'· · – – –',
    '3': 	'· · · – –',
    '4': 	'· · · · –',
    '5': 	'· · · · ·',
    '6': 	'– · · · ·',
    '7': 	'– – · · ·',
    '8': 	'– – – · ·',
    '9': 	'– – – – ·',
    '0': 	'– – – – –',
}
class Translator():    
    def __init__(self, my_string:str =''):
        self.my_string = my_string.upper()
    
    def translate_to_morse(self):
        temp = ''
        for i in self.my_string:
            try:
                temp += morse[i]
            except:
                if i =='\n':
                    temp += '\n'
                else:
                    temp += ' ? '
        return temp