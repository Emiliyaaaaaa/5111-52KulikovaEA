#создали переменную с весом одного сувенира в граммах
suvenir_weight = 75
#создали переменную с весом одной безделушки в граммах
useless_weight = 112
#запрашиваем у пользователя количество купленных сувениров,безделушек
suvenir_count= int(input("Введите количество сувениров "))
useless_count = int(input("Введите количество безделушек "))
#создали переменные, содержащие массу сувениров,безделушек в граммах
suvenir_m = suvenir_weight * suvenir_count
useless_m = useless_weight * useless_count
#выводим в консоль общую массу сувениров и безделушек в кг
print("Общий вес покупки в кг =", (suvenir_m+useless_m)/1000)
