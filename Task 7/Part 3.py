import re


# Функция возвращения дубликатов в тексте
def get_duplicates(text, word):
    return re.findall(f"{word} {word}", text)


# Функция возвращения нового текста без дубликатов
def remove_dublicates(text):
    # Переменная содержит список слов из текста(w+ - без отдельных пробелов)
    words = re.findall(r"\b(\w+)\b", text)
    # Для слова в списке
    for word in words:
        # Пока в тексте содержатся дубликаты
        while get_duplicates(text, word):
            # Замена дубликатов на одно слово - текст без повторов
            text = re.sub(f"{word} {word}", word, text)
    return text


# Прописал текст, чтобы каждый раз не использовать ввод.
text_example = 'в сравнение сравнение сравнение Сравнение с собаками, кошками Кошки не претерпели серьезных изменений в процессе одомашнивания'

# text = input("Введите текст ")
print(remove_dublicates(text_example))
