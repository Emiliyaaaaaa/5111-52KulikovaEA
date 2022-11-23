import json
name_file = input("Введите имя файла ")
f = open(name_file)
a = f.read
dictt = {}
# Для каждой строки в списке
for i in a.split(sep="\n"):
    # Подсчёт значений ключа (повтора слова в строке)
    for j in i.split():
        dictt[j] = dictt.get(j, 0) + 1
f.close()
# Создание списка пары ключ-значение
my_list = [dictt.items()]
# Сортировка наиболее часто встречающихся слов (по количеству в значениях)
my_list.sort(key=lambda x: x[1], reverse=True)
new_file = json.dumps(my_list)
print(new_file)
