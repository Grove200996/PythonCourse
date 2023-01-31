# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

n = int(input('Enter a number: '))
result = [1]
i = 1
stop = 0
while n > stop:
    result.append(2**i)
    stop += 2**i
    i += 1
print(*(result))