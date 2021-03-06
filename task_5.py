print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def num_count(number):
  Num_count = 0
  while number != 0:
   Num_count += 1
   number //= 10
  return Num_count

def new_numbers(number, count):
  last_digit = number % 10 
  first_digit = number // 10 ** (count - 1)
  number //= 10
  between_digits = number % 10 ** (count - 2)
  new_number = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
  return new_number


first_n = int(input('\nВведите первое число: '))
second_n = int(input('Введите второе число: '))

first_num_count = num_count(first_n)
second_num_count = num_count(second_n)
#print(first_num_count, second_num_count)
if first_num_count >= 3 and second_num_count >= 4:
  new_first_num = new_numbers(first_n, first_num_count)
  new_second_num = new_numbers(second_n, second_num_count)
  print('\nИзменённое первое число:', new_first_num)
  print('Изменённое второе число:', new_second_num)
  print('\nСумма чисел:', new_first_num + new_second_num)
else:
  print('Ошибка ввода! Введите корректное число (в первом  числе должно быть не меньше трёх цифр, в втором числе должно быть не меньше четырёх цифр)')