# Следующее простое число

# Функция для определения простого числа
def isPrime(number):
    for i in range(2, number - 1):
        if number % i == 0: return False
    return True

# Функция для определения след простого числа
def nextPrime(number):
    while True:
        number += 1
        if isPrime(number): 
            print("Следующее простое число -", number)
            break

# Ввод и вызов функции          
number = int(input("Введите число: "))
nextPrime(number)