#Первое задание
num = str(input('Введите число: '))

sp=num.replace('.','')
num_list=list(int(x)for x in sp)

print(sum(num_list))

#Второе задание
import math

n = int(input('Введите число: '))

def f(x):return((x==1)and 1) or x * math.factorial(x-1)

listn=list(f(i) for i in range (1, n+1))

print(listn)

#Третье задание
import random 

y = [1, 5, 6, 20, 45 ,50 , 120]
random.shuffle(y) 

print(y)