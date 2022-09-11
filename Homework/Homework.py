
#Первое задание
numbers=list(map(int,input('Введите целые числа для создания массива: ').split()))
res=sum(numbers[1::2])
print(res)


#Второе задание
import math
numb=list(map(int,input('Введите целые числа для создания массива: ').split()))
res=[numb[i] * numb[-(i + 1)] for i in range(math.ceil(len(numb) / 2))]
print(res)

#Третье задание
def diff_of_numb(list):
    min = list[0]
    max = 0
    li = []
    for i in list:
        res = round(i % 1, 10)
        if res != 0:
            li.append(res)
    for i in li:
        if i < min:
            min = i
        if i > max:
            max = i
    return max -min

numb=list(map(float,input('Введите вещественные числа для создания массива: ').split()))
out=diff_of_num(numb)

print(round(out, 5))

#Четветрая задача
n = int(input('Введите десятичное число: '))
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print('Двоичное число:', b)

#Пятая задача

def fib(x):
    result = [0]
    a, b = 1, 1
    c, d = 1, -1
    for i in range(1, x + 1):
        result.append(a)
        result.insert(0, c)
        a, b = b, a + b
        c, d = d, c - d
    return result
x=int(input('Введите целое число :'))
print(fib(x))   