import re
symboll = "#"
name_file = input("Введите имя файла ")
# Открытие исходного файла
f = open(name_file, "r+")
# Для каждой строки в списке
for line in f.split(sep="\n"):
    # Если в начале строки не встречается "#"
    if not re.search(symboll, line):
        # Сохранение нового файла без комментариев
        f.write(line)
f.clouse()


