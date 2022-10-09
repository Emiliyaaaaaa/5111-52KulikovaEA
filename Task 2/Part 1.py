symbol = input("Введите букву латинского алфавита ")
vowels = "a, e, i, o, u"
if vowels.upper().__contains__(symbol.upper()):
    print("Гласная")
elif symbol.upper().__contains__("Y"):
    print("Как гласная, так и согласная")
else:
    print("Согласная")
