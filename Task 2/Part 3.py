import math
year = int(input("Введите год "))
day_of_the_week = (year + math.floor((year - 1)/4)
                   - math.floor((year - 1)/100)
                   + math.floor((year - 1)/400)) % 7
if day_of_the_week == 0:
    print("Воскресенье")
if day_of_the_week == 1:
    print("Понедельник")
if day_of_the_week == 2:
    print("Вторник")
if day_of_the_week == 3:
    print("Среда")
if day_of_the_week == 4:
    print("Четверг")
if day_of_the_week == 5:
    print("Пятница")
if day_of_the_week == 6:
    print("Суббота")
