# Медиана трех значений

# Функция для определения медианы
def median(first, second, third):
    minimum = min(first, second, third)
    maximal = max(first, second, third)
    regular = (first + second + third) - (minimum + maximal)
    return regular

# Ввод и вызов функции          
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
print("Медиана данных чисел -", median(first, second, third))