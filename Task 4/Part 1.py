# Создание списка
my_list = []
while True:
    i = int(input("Введите целое число "))
    # Добавление введенного числа в список
    my_list += [i]
    # При нуле остановка цикла
    if i == 0:
        break
# Подсчёт длины списка
length = len(my_list)
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
# Удаляем второй элемент списка
my_list.pop(1)
print("Удалён второй элемент", my_list)
