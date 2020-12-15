class PasswordError(Exception):
    pass

def check_password(a):
    bad_sequence = ['qwertyuiop', 'asdfghjkl',
                    'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    num = list('1234567890')
    if len(a) <= 9:
        return 'LengthError'
    if a.islower() or a.isupper():
        return 'LetterError'

    if a.isdigit() or a.isalpha():
        return 'DigitError'

    b = a.lower()
    for i in bad_sequence:
        for j in range(len(i) - 2):
            if i[j: j + 3] in b:
                return 'SequenceError'

    for i in num:
        if i not in a:
            return 'ok'

    return 'DigitError'