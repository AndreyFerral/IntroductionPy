import numpy as np

first = [0, 0, 12, -18, 5]
second = [-2, 4, 3, 5, 0]
third = [-1, 2, 3, 0, 1]
fourth = [-4, 8, 12, -6, 13]
fifth = [0, 0, 0, 0, 0]
vector = [-9, -7, -4, -1, 0]

M2 = np.array([first, second, third, fourth, fifth]) # Матрица (левая часть системы)
v2 = np.array(vector) # Вектор (правая часть системы)

print(first, second, third, fourth, fifth)
print(vector)

answer = np.linalg.lstsq(M2, v2)
print(answer)