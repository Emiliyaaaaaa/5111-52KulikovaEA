# Используем библиотеку рандом
import random
# Cоздаём функцию вывода пароля
def password_generate() -> str:
    Pass = ""
    # Для каждого места в длине пароля (от 7 до 10)
    for i in range(random.randint(7, 10)):
        # Подбор символа из таблицы ASCII
        Pass += chr(random.randint(33, 126))
    return Pass
# Вызываем функцию
print(password_generate())
