from pulp import *

# Задаем переменные для поиска
# lowbound - нижняя граница, upBound - верхняя граница
X1A = LpVariable("X1A", lowBound = 0)
X2A = LpVariable("X2A", lowBound = 0)
X3A = LpVariable("X3A", lowBound = 0)
X4A = LpVariable("X4A", lowBound = 0)

X1B = LpVariable("X1B", lowBound = 0)
X2B = LpVariable("X2B", lowBound = 0)
X3B = LpVariable("X3B", lowBound = 0)
X4B = LpVariable("X4B", lowBound = 0)

Y1 = LpVariable("Y1", lowBound = 0, upBound = 1000)
Y2 = LpVariable("Y2", lowBound = 0, upBound = 2000)
Y3 = LpVariable("Y3", lowBound = 0, upBound = 3000)

# Устанавливаем максимилизацию прибыли
problem = LpProblem('0', LpMaximize)

# Определяем целевую функцию
Y1_cost, Y2_cost, Y3_cost = 30, 40, 50 # Цена за руды
A_cost, B_cost = 200, 210 # Цена за сплавы
A = (A_cost * (X1A + X2A + X3A + X4A))
B = (B_cost * (X1B + X2B + X3B + X4B))
Y = (Y1_cost * Y1 + Y2_cost * Y2 + Y3_cost * Y3)
problem += A + B - Y

# Ограничения на состав сплавов А
problem += X1A <= 0.8 * (X1A + X2A + X3A + X4A)
problem += X2A <= 0.3 * (X1A + X2A + X3A + X4A)
# Ограничения на состав сплавов B
problem += X2B <= 0.6 * (X1B + X2B + X3B + X4B)
problem += X2B >= 0.4 * (X1B + X2B + X3B + X4B)
problem += X3B >= 0.3 * (X1B + X2B + X3B + X4B)
problem += X4B <= 0.7 * (X1B + X2B + X3B + X4B)

# Ограничения на состав металлов
problem += X1A + X1B <= 0.2 * Y1 + 0.1 * Y2 + 0.05 * Y3
problem += X2A + X2B <= 0.1 * Y1 + 0.2 * Y2 + 0.05 * Y3
problem += X3A + X3B <= 0.3 * Y1 + 0.3 * Y2 + 0.7 * Y3
problem += X4A + X4B <= 0.3 * Y1 + 0.3 * Y2 + 0.2 * Y3

problem.solve()

print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Функция цели:", abs(pulp.value(problem.objective)))