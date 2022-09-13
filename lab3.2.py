# Никаких центов

# Обработка ввода
list = []
while True:
    try:
        number = int(input("Введите число: "))
        list.append(number)
    except: 
        break

# Расчёт и вывод
sum = sum(list)
left = sum % 5
# Тернарная операция
new_sum = sum - left if left < 2.5 else sum + (5 - left)
print(sum, new_sum)