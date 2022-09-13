# Таблица умножения

# Функция для форматирования вывода
def format(number):
    if number < 10: print("  ", number, end="")
    else: print(" ", number, end="")

# Вывод верхнего заголовка
print("    ", end="")
for i in range(1, 11):
    format(i)
print()

# Вывод таблицы умножения
for i in range(1, 11):
    # Вывод бокового заголовка
    format(i)
    # Вывод основной части
    for j in range(1, 11):
        format(i * j)
    print()