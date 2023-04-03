list_size = input('Введите количество элемепнтов: ')
numbers = []
for i in range(int(list_size)):
    numbers.append(input(f'Введите {i + 1} элемент: '))
numbers.sort()
print(numbers)