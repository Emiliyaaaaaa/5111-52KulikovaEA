# Запрашиваем слово у пользователя
word = input("Введите слово ").lower()
# Если слово,как и наоборот одинаково читается-палиндром
if word == word[::-1]:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

