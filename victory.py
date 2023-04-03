import random
list_poets = ['Kiany', 'Chardi', 'Lacosta','Niletto', 'Eljey', 'Matrang', 'Scriptonit', 'Musya_Totibatze', 'Basta', 'Markul']
dict_poets = {
    'Kiany': '02.09.1964',
    'Chardi': '15.09.1977',
    'Lacosta': '19.05.1997',
    'Niletto': '01.10.1991',
    'Eljey': '09.07.1994',
    'Matrang': '20.04.1995',
    'Scriptonit': '03.06.1990',
    'Musya_Totibatze': '12.03.1996',
    'Basta': '20.04.1980',
    'Markul': '31.03.1993',
}
dict_poets_words = {
    'Kiany': 'второе сентября 1964',
    'Chardi': 'пятнадцатое сентября 1977',
    'Lacosta': 'девятнадцатое мая 1997',
    'Niletto': 'первое октября 1991',
    'Eljey': 'девятое июля 1994',
    'Matrang': 'двадцатое апреля 1995',
    'Scriptonit': 'третье июня 1990',
    'Musya_Totibatze': 'двенадцатое марта 1996',
    'Basta': 'двадцатое апреля 1980',
    'Markul': 'тридцать первое марта 1993',
}
count_poets = 5
random_poets = random.sample(list_poets, count_poets)
success = 0
failed = 0

is_repeat = True
while is_repeat:
    for index, poet in enumerate(random_poets):
        poet_birthday_dict = dict_poets[poet]
        born_poet_input = input(f'Год рождения {poet}?')
        if born_poet_input == poet_birthday_dict:
            success += 1
        else:
            print(f'Правильный ответ: {dict_poets_words[poet]}')
            failed += 1
    print('Ваши правильные ответы: ', success)
    print('Процент правильных ответов: ', (success * 100) / count_poets, '%')
    print('Ваши неправильные ответы: ', failed)
    print('Процент неправильных ответов: ', (failed * 100) / count_poets, '%')
    is_repeat = input('Хотите повторить')
    if is_repeat == ('Да' or 'да'):
        is_repeat = True
        success = 0
        failed = 0
    else:
        is_repeat = False
