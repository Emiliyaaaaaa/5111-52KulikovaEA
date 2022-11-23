import re


# Функция возвращения дубликатов в тексте
def get_duplicates(a):
    return re.findall(r"{word}{word}", a)


# Функция возвращения нового текста без дубликатов
def remove_dublicates(a):
    # Переменная содержит список слов из текста(w+ - без отдельных пробелов)
    words = re.findall(r"\b(\w+)\b", a)
    # Для слова в списке
    for word in words:
        # Пока в тексте содержатся дубликаты
        while get_duplicates(a):
            # Замена дубликатов на одно слово - текст без повторов
            a = re.sub(r"{word}{word}", word, a)
    return a


text = input("Введите текст ")
print(remove_dublicates(text))
