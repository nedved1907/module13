print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

def number_inverse(number):
  N = number
  number_inv = 0
  n = 0
  number = number // 10
  while number != 0:
    number //= 10
    n += 1  
  for n_inv in range(n,-1,-1):
    number_inv += (N % 10)*10**n_inv
    N = N // 10
  return number_inv

number_inv1 = number_inverse(number1)
number_inv2 = number_inverse(number2)
print('\nПервое число наоборот:', number_inv1)
print('Второе число наоборот:', number_inv2)

summ = number_inv1 + number_inv2

print('\nСумма:', summ)

summ_inv = number_inverse(summ)
print('Сумма наоборот:', summ_inv)