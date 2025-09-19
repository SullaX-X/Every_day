# ЭКЗАМЕН
# Задача 1
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f"""To: {mail}
#     Приветствую, {name}!
#     Вам назначен экзамен, который пройдет {date}, в {time}.
#     По адресу: {place}.
#     Экзамен будет проводить {teacher} в кабинете {number}.
#     Желаем удачи на экзамене!"""

# print(generate_letter('lara@yandex.ru', 'Лариса',
#       '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

# Задача 2
# def pretty_print(data, side='-', delimiter='|'):
#     result = f' {delimiter} '.join(map(lambda x: str(x), data))
#     print((len(result) + 2) * side, delimiter + " " + result +
#           " " + delimiter, (len(result) + 2) * side, sep='\n')
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# Задача 3
# def concat(*args, sep=' '):
#     return sep.join(map(lambda x: str(x), args))
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

# Задача 4
# from functools import reduce
# def product_of_odds(data):   # data - список целых чисел
#     return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)

# Задача 5
# words = 'the world is mine take a look what you have started'.split()
# print(*map(lambda x: f'"{x}"', words))

# Задача 6
# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908,
#            8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

# Задача 7
# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1),
#            (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
# print(sorted_numbers)

# Задача 8
# def call(func, *args):
#     return func(*args)

# Задача 9
# def compose(f, g):
#     return lambda x: f(g(x))

# Задача 10
# from operator import add, sub, mul, truediv
# def arithmetic_operation(a):
#     return lambda x, y: kw[a](x, y)
# kw = {
#     '+': add,
#     '-': sub,
#     '*': mul,
#     '/': truediv
# }
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

# Задача 11
# print(*sorted(input().split(), key=lambda x: x.lower()))

# Задача 12
# from functools import reduce
# print(*sorted(sorted([input() for _ in range(int(input()))]), key=lambda x: reduce(lambda z, y: z + ord(y) - ord('A'), [j for j in x.upper()], 1) ), sep='\n')

# Задача 13
# print(*sorted([input() for _ in range(int(input()))],
#       key=lambda x: [*map(int, x.split('.'))]), sep='\n' )
# ====================ВТОРОЙ=============ВАРИАНТ=============================================================
# def ip_result(num):
#     filter_ip = [[int(i) for i in input().split('.')] for _ in range(num)]
#     return sorted(filter_ip)
# for i in ip_result(int(input())):
#     print('.'.join([str(j) for j in i]))

