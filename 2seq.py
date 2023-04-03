input_numbers = input('Введите цифры через запятую: ')
list_numbers = list(input_numbers.replace(',', '.').replace(';', '.').replace('/', '.').split('.'))
uniq_numbers = set(list_numbers)
print(uniq_numbers)
