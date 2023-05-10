import random

passowrd = ''
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'
count_len = n = int(input('Введите длинну пароля'))

count_digitals = input("Пароль будет включать цифры? да/нет").lower()
count_lowercase = input("Включать ли строчные "
                            "буквы abcdefghijklmnopqrstuvwxyz? да/нет").lower()
count_uppercase = input("Включать ли строчные"
                            " буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет").lower()
count_symbols = input("Включать ли символы !#$%&*+-=?@^_? да/нет").lower()
count_special_symbols = input("Исключать ли неоднозначные символы? il1Lo0O да/нет").lower()

def create_cahrs():
    chars = ''
    if count_digitals == 'да':
        chars += digits
    if count_lowercase == 'да':
         chars += lowercase_letters
    if count_uppercase == 'да':
            chars += uppercase_letters
    if count_symbols == 'да':
        chars += symbols
    if count_special_symbols == 'да':
        chars = [i for i in chars if i not in 'il1Lo0O']
    return ''.join(chars)

def generate_password(length, chars):
    password = ''
    for i in range(1, length+1):
        password += random.choice(chars)
    return password

print(generate_password(count_len, create_cahrs()))