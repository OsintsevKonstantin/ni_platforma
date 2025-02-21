#задача1
rainbow = ["каждый", "охотник", "желает", "знать", "где", "сидит", "фазан"]
for i in rainbow:
    print(i, end = ' ')
print()
print()

#задача2
purchases = [1200, 800, 468, 235, 5800, 1350, 110, 243,
                767, 3500, 5400, 4389, 3690, 2420, 894,
                1766, 2100, 450, 328, 1890, 233, 766, 1765,
                237, 679, 1983, 389, 1760, 2100, 253, 789]
summ=0 #сумма расходов
it=0 #счетчик
while it<len(purchases):
    summ+=purchases[it]
    it+=1
print('Траты за месяц составили:', summ, 'рубля')

summ=0
for elem in purchases:
    summ+=elem
print('Траты за месяц составили:', summ, 'рубля')

summ=0
summ=sum(purchases)
print('Траты за месяц составили:', summ, 'рубля')
print()

#задача3
def del_from_tuple(tpl, elem):
    lst = list(tpl)
    if elem in tpl:
        lst.remove(elem)
    return tuple(lst)

tuple_1 = (1, 2, 3)
element_1 = 1
print("Кортеж: ", tuple_1, ". Элемент: ", element_1)
print("Кортеж без заданного элемента: ", del_from_tuple(tuple_1, element_1))
print()

tuple_2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
element_2 = 3
print("Кортеж: ", tuple_2, ". Элемент: ", element_2)
print("Кортеж без заданного элемента: ", del_from_tuple(tuple_2, element_2))
print()

tuple_3 = (2, 4, 6, 6, 4, 2)
element_3 = 9
print("Кортеж: ", tuple_3, ". Элемент: ", element_3)
print("Кортеж без заданного элемента: ", del_from_tuple(tuple_3, element_3))

#задача4
phrase = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"
number_of_characters=0
for symbol in phrase:
    if symbol!='е':
        number_of_characters+=1
    else:
        print('Количество символов  во фраззе до буквы "е": ',number_of_characters)
print()

#задача5
def to_list(*args):
    return list(args)

tuple_1 = (1, 2, 3)
print("Кортеж аргументов: ", tuple_1)
print("Список элементов: ", to_list(tuple_1))
print()

tuple_2 = ('Молоко', 5, '2020 год')
print("Кортеж аргументов: ", tuple_2)
print("Список элементов: ", to_list(tuple_2))
print()

tuple_3 = ([3, 4, 7], 8.3, True, 'Строка')
print("Кортеж аргументов: ", tuple_3)
print("Список элементов: ", to_list(tuple_3))