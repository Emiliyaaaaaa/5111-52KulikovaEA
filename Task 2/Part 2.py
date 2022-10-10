magnitude = float(input("Введите значение магнитуды "))
if magnitude < 2.0:
    print("Минимальное")
elif magnitude >= 2.0 and magnitude < 3.0:
    print("Очень слабое")
elif magnitude >= 3.0 and magnitude < 4.0:
        print("Слабое")
elif magnitude >= 4.0 and magnitude < 5.0:
    print("Промежуточное")
elif magnitude >= 5.0 and magnitude < 6.0:
    print("Умеренное")
elif magnitude >= 6.0 and magnitude < 7.0:
    print("Сильное")
elif magnitude >= 7.0 and magnitude < 8.0:
    print("Очень сильное")
elif magnitude >= 8.0 and magnitude < 10.0:
    print("Огромное")
elif magnitude >= 10.0:
    print("Разрушительное")