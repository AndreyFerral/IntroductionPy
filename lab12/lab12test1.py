import numpy as np

first = [4, 2, -1]
second = [5, 3, -2]
third = [3, 2, -3]
fourth = [0., 0., 0., 0.]
fifth = []
vector = [1, 2, 0]

M2 = np.array([first, second, third]) # Матрица (левая часть системы)
v2 = np.array(vector) # Вектор (правая часть системы)

answer = np.linalg.lstsq(M2, v2)
print(answer)