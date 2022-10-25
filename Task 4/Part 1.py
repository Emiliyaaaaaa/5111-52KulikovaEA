# Создание списка
my_list = []
i = int(input("Введите целое число "))
while i != 0:
    # Добавление введенного числа в список
    my_list += [i]
    i = int(input("Введите целое число "))
# Подсчёт длины списка
length = 0
for l in my_list:
    length += 1
# Количество итераций для внешнего цикла
for i in range(length - 1):
    # Количество итераций для внутреннего цикла
    for j in range(length - i - 1):
        # Если взятый элемент больше,чем последующий, меняем  местами
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
print("Список:", my_list)
length = len(my_list)
# Находим минимум и максимум при помощи индексации
minimum = my_list[0]
maximum = my_list[-1]
# Cоздаём кортеж
my_tuple = (minimum, maximum)
print("Минимальное и максимальное значения", my_tuple)
print("Количество элементов в списке", length)
# Удаляем каждый второй элемент списка
del my_list[1::2]
print("Удалён  каждый второй элемент", my_list)
