#Первое задание
print('Введите a');
a=int(input())
print('Введите b');
b=int(input())
is_sqrt=a*a==b
print(is_sqrt)

#Второе задание
a=[1,2,3,4,6,7,99,88,999]
max= 0
for i in a:
  if i > max:
   max=i
print(max)

#Третье задание
print('Введите a');
a=int(input())

print('Введите b');
b=int(input())

for i in range(a,b):
    print(i)

#Четвертое задание
y = float(input('Введите дробное число:'))
print(int(y * 10) % 10)

#Пятое задание
n = int(input('Введите число: '))

if  n%5==0 and n%10==0 and n%15==0 and n!=30 :
    print('Число кратно 5 и 10 или 15' )
elif n==30:
    print('Число равно 30')
else:
    print('Число не кратно не 5  10 и 15 и не является 30')

#Шестое задание
q = int(input('Введите день: '))
if q == 1:
    print('Понедельник')
elif q == 2:
    print('Вторник')
elif q == 3:
    print('Среда')
elif q == 4:
    print('Четверг')
elif q == 5:
    print('Пятница')
elif q == 6:
    print('Суббота')
else:
    print('Воскресенье')
if q==6 or q==7:
    print('Выходной')

#Седьмое задание
print('Введите X');
X=int(input())
print('Введите Y');
Y=int(input())
print('Введите Z');
Z=int(input())

is_exp=-(X and Y and Z)==(-X and -Y and -Z)
print(is_exp)

#Восьмое задание
x = float(input("x="))
y = float(input("y="))
if x>0 and y>0:
    print('I')
elif x<0 and y>0:
    print('II')
elif x<0 and y<0:
    print('III')
elif x>0 and y<0:
    print('IV')

#Девятое задание
quart = int(input("Укажите номер четверти: "))
if quart==1:
    print('x>0 а y>0')
elif quart==2:
    print('x<0 а y>0')
elif quart==3:
    print('x<0 a y<0')
elif quart==4:
    print('x>0 a y<0')

#Десятое задание
import math
print('Введите координаты первой точки')
x1 = float(input("x1="))
y1 = float(input("y1="))
p1=[x1,y1]
print('Введите координаты второй точки')
x2 = float(input("x2="))
y2 = float(input("y2="))
p2=[x2,y2]

distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)
