# Cоздание словаря
my_dictionary = {}
# Создание списка
my_list = []
key = input("Введите слово ")
while key != "":
    value = 0
    # Добавление введенного слова в список
    my_list.append(key)
    for key in my_list:
        # Если слово повторяется, то значение увеличивается на один
        if key == key in my_list:
            value += 1
        else:
            value = 1
    # Добавление в словарь пары ключ - значение
    my_dictionary.update({key: value})
    key = input("Введите слово ")
print(my_dictionary)
# Переменная с доступом всех ключей словаря
m = my_dictionary.keys()
# Распаковка значений
print(*m)
