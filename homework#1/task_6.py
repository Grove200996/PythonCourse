# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket = int(input('Enter a ticket number(has to be six digits tho.): '))

if len(str(ticket)) != 6:
    print('Wrong data.')
else:
    ticket = str(ticket)
    first_part = ticket[:3]
    second_part = ticket[3:]
    sum_1 = 0
    sum_2 = 0
    for i in first_part:
        sum_1 += int(i)
    for j in second_part:
        sum_2 += int(j)
    if sum_1 == sum_2:
        print('YES')
    else:
        print("NO")

