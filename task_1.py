# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите число элементов первого множества: '))
m = int(input('Введите число элементов второго множества: '))

setOfNum1 = []
for i in range(n):
    setOfNum1.append(int(input('Введите элементы множества n: ')))

setOfNum2 = []
for i in range(m):
    setOfNum2.append(int(input('Введите элементы множества m: ')))

print(setOfNum1)
print(setOfNum2)

uniqSet1 = set(setOfNum1)
uniqSet2 = set(setOfNum2)

print(uniqSet1)
print(uniqSet2)

resultSet = uniqSet1 & uniqSet2
str = ', '.join([str(i) for i in resultSet])
print(str)

