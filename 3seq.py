input_numbers_first = input('Введите цифры 1-го списка через запятую: ')
list_numbers_first = list(input_numbers_first.replace(',', '.').replace(';', '.').replace('/', '.').split('.'))
uniq_numbers_first = set(list_numbers_first)
input_numbers_second = input('Введите цифры 2-го списка через запятую: ')
list_numbers_second = list(input_numbers_second.replace(',', '.').replace(';', '.').replace('/', '.').split('.'))
uniq_numbers_second = set(list_numbers_second)
cut_first_by_second = uniq_numbers_first-uniq_numbers_second
print(cut_first_by_second)