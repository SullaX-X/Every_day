# Задача 1
# file = open(input(), 'r', encoding='utf-8')
# print(file.readline())
# file.close()

# Задача 2
# file = open(input(), 'r', encoding='utf-8')
# print(file.readlines()[-2].rstrip())
# file.close()

# Задача 3
# from random import choice
# file = open('lines.txt', 'r', encoding='utf-8')
# print(choice(file.readlines()).rstrip())
# file.close()

# Задача 4
# file = open('numbers.txt')
# print(sum(map(int, file)))
# file.close()

# Задача 5
# file = open('nums.txt')
# print(sum(map(int, file.read().split())))
# file.close()

# Задача 6
# file = open('prices.txt')
# print(sum(map(lambda x: int(x[1]) * int(x[2]), map(lambda x: x.split(), file.readlines()))))
# file.close()