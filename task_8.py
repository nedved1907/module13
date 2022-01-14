print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def exponentiation(n, x):
  exp = 1
  for N in range(n):
    exp *= x
  return exp

def factorial(n):
  fact = 1
  for N in range(1, n+1):
    fact *= N  
  return fact

precision = float(input('Введите точность: '))
x = float(input('Введите x: '))
n = 0
summ = 0
addNumber = 1
while abs(addNumber) > precision:
  exp_1 = exponentiation(n, -1)
  exp_2 = exponentiation(2*n, x)
  fact_1 = factorial(2*n)
  addNumber = exp_1 * (exp_2 / fact_1)
  summ += addNumber
  n += 1
print('Сумма ряда', summ)