#задача1
while True:
    num=int(input('Введите число от 1 до 9: '))

    if 0<num<10:
        for i in  range(10):
            print(f'{num} * {i+1} = {num*(i+1)}')
        break
print()

#задача2
for i in range(300,431):
    if i%11==0 and i%5!=0:
        print(i, end=' ')
print()
print()

#задача3
year=int(input('Введите год: '))
if year%400==0:print('Високостный')
elif  year%100!=0 and year%4==0:
    print('Високостный')
else: print('Обычный')
print()

#звдача4
dct={}
for i in range(1,11):
    dct[i]=i*i
print(dct)
print()

#задача5
a=int(input('Первое число:'))
b=int(input('Второе число:'))
operation=input('Операция:')
def calculator(a,b,operation):
    if operation=='+':
        return a+b
    elif operation=='-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return a/b
print(f'Результат: {calculator(a,b,operation)}')
print()

#задача6
lst = [96, 186, 11, 116, 183,  95, 181, 95, 55, 128, 54, 24, 21, 198, 118, 46, 166, 137, 24]

def filt1(lst):
    return list(filter(lambda x: 9<x<100, lst))
print(filt1(lst))
print()