# Ввод
distance_pound = int(input("Введите расстояние в футах: "))
# Расчёт чисел
distance_inch = distance_pound * 12
distance_yards = distance_pound * 0.33333
distance_miles = distance_pound * 0.00018939
# Вывод
print("Конвертация в дюймы: ", distance_inch)
print("Конвертация в ярды:  ", distance_yards)
print("Конвертация в мили:  ", distance_miles)