# Cоздание словаря
my_dictionary = {}
key = 0
while True:
    value = input("Введите слово ")
    # При отсутствии значения остановка цикла
    if not value:
        break
    # Проверка вхождения значения в словарь
    elif value not in my_dictionary.values():
        key += 1
        # Добавление в словарь пары ключ - значение
        my_dictionary.update({key: value})
# Переменная с доступом всех значений словаря
m = my_dictionary.values()
# Распаковка значений
print(*m)
