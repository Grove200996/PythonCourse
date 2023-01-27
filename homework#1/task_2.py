# Задача 2: - HARD необязательная, идет за 3 обязательных 
# Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.


number = float(input('Enter a number: '))
number = str(number)
summ = 0
a,b = number.split('.')
    

int_number = int(a+b)
while int_number > 10:
    summ += int_number % 10
    int_number = int_number // 10
print(summ + int_number)