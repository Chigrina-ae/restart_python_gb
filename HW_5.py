# a = int(input('Введите число a \n'))
# b = int(input('Введите числ b \n'))

# def f(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     elif b < 0:
#         return 1 / f(a, -b)
#     else:
#         return a * f(a, b-1)

# res = f(a, b)
# print(res)



# # Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# # Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# # Функция не должна ничего выводить, только возвращать значение.

# # Пример:


# # sum(2, 2)
# # # 4

# a = int(input("Введите первое неотрицительное число "))
# b = int(input("Введите второе неотрицательно число "))


# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a-1, b+1)


# print(sum(a, b))


def print_operation_table(operation, num_rows , num_columns ):
  if num_rows < 2 or num_columns < 2:
    print('ОШИБКА! Размерности таблицы должны быть больше 2!')
  else:
    print(' '.join([str(i) for i in range(1, num_columns + 1)]))
  for i in range(2, num_rows + 1):
    print(i, end = ' ')
    for j in range(2, num_columns + 1):
        print(operation(i, j), end = ' ')
    print()