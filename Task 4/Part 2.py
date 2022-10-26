# Cоздание словаря
my_dictionary = {}
# Создание списка
my_list = []
key = input("Введите слово ")
while key != "":
    value_by_key = my_dictionary.get(key)
    # Если слово не найдено в словаре
    if not value_by_key:
        my_dictionary.update({key: 1})
    else:
        # Если найдено, то количество повторений увеличиваем на 1
        my_dictionary.update({key: value_by_key + 1})
    key = input("Введите слово ")
print(my_dictionary)
# Переменная с доступом всех ключей словаря
m = my_dictionary.keys()
# Распаковка значений
print(*m)
