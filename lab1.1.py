# Ввод
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
# Определение мин, среднего и максимального
min = min(first, second, third)
max = max(first, second, third)
regular = (first + second + third) - (min + max)
# Вывод
print("Числа по возрастанию: ", min, regular, max)