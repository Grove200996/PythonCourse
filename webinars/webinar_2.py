# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# number = int(input('Enter a positive number: '))
# summ = 1
# while number > 0:
#     summ = summ * number
#     number = number - 1
# print(summ)


# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# num = int(input('Enter a number larger than 1: '))

# def fibonacchi(n):
#      f1 = 1
#      f2 = 1
#      lists = [0,1,1]
#      while n > 2:
#           f1, f2 = f2, f2+f1
#           n -= 1
#           lists.append(f2)
#      return lists
# numbers = fibonacchi(num)
# print(numbers)
# if num in numbers:
#     print(numbers.index(num) + 1)
# else:
#     print('-1')

import random
# n = int(input('Enter a number: '))
# temperature = ([random.randint(-50,50) for i in range(1,n)])
# print(temperature)
# count = []
# maxi = 1
# for i in temperature:
#     if i > 0:
#         maxi += 1
#     else:
#         count.append(maxi)
#         maxi = 0
# print(max(count))


# number = int(input('Enter a number: '))
# array = ([random.randint(1, 10) for i in range(0, number)])
# print(array)
# minimum = 10
# maximum = 0
# for i in range(len(array)):
#     if array[i] < minimum:
#         minimum = array[i]
# print(minimum)

# for i in range(len(array)):
#     if array[i] > maximum:
#         maximum = array[i]
# print(maximum)

