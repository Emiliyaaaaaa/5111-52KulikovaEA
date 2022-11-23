# Запрашиваем текст у пользователя
text = input("Введите текст ")
print(text)
# Если в тексте есть символ кириллицы,подчёркиваем его
for symbol in text:
    if "а" <= symbol <= "я":
        print("-", end="")
    else:
        print("", end=" ")
