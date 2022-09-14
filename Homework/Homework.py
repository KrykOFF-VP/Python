
#Первое задание
num = int(input('Введите целое число: '))
li = []
simple = 2
while num > 1:
    if num % simple == 0:
        li.append(simple)
        num = num/simple
    else:
        simple += 1
print(li)

Второе задание
a = [int(s) for s in input('Введите последовательность чисел: ').split()]
li = []
for i in a:
   if a.count(i) == 1:
       li.append(i)
print(li)      

#Третье задание
from random import randint
from polynomial import Polynomial

def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print('Формирование многочлена и запись его в файл')

while True:
    s = input('Введите колличество коэффициентов (k >= 2): ')
    if s == '':
        exit()
    k = try_to_int(s)
    if k == None or k < 2:
        print('Некорректный ввод! Повторите попытку...')
        continue
    p = Polynomial(*[randint(0, 100) for _ in range(k)])
    file_name = 'file.txt'
    with open(file_name, 'w') as file:
        file.write(str(p))
    print(f'Многочлен {p} записан в файл {file_name}')