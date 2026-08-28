# ЭКЗАМЕН
# Задача 1
# with open(f"{input()}", encoding='utf-8') as f:
#     print(len(f.readlines()))

# Задача 2
# with open('ledger.txt', encoding='utf-8') as f:
#     print("$" + str(sum([int(i.strip('\n$')) for i in f])))

# Задача 3
# with open('grades.txt', encoding='utf-8') as f:
#     total = 0
#     for name, *grade in [i.strip().split() for i in f]:
#         n1, n2, n3 = map(int, grade)
#         if 65 <= n1 and 65 <= n2 and 65 <= n3:
#             total += 1
#     print(total)

# Задача 4
# with open('words.txt', encoding='utf-8') as f:
#     words = f.read().split()
#     maxW = len(max(words, key=len))
#     print(*filter(lambda x: len(x) >= maxW,  words), sep='\n')

# Задача 5
# with open(f"{input()}", encoding='utf-8') as f:
#     print(*f.readlines()[-10:], sep='')

# Задача 6
# with open(f"{input()}", encoding='utf-8') as f, open(f"forbidden_words.txt", encoding='utf-8') as forbidden:
#     f_w = list(forbidden.read().split())
#     result = str(f.read())
#     r_l = result.lower()
#     for word in f_w:
#         if word in f_w:
#             r_l = r_l.replace(word, '*' * len(word))
#     for k, char in enumerate(r_l):
#         if char == '*':
#             print(char, end='')
#         else:
#             print(result[k], end='')

# Задача 7
# d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'
# }
# with open('cyrillic.txt', encoding='utf-8') as f, open('transliteration.txt','a', encoding='utf-8') as o:
#     for i in f:
#         for j in i:
#             if j in d:
#                 o.write(d.get(j))
#             else:
#                 o.write(j)

# Задача 8
# with open(f"{input()}", encoding='utf-8') as f:
#     done = 0
#     func = 0
#     flag = False
#     for i in f.readlines():

#         if i.startswith('#'):
#             done += 1
#             func += 1
#             flag = True
#             continue
#         if flag == True:
#             flag = False
#             continue

#         if i.startswith('def ') and flag == False:
#             print(i[4:i.find('(')])
#             func += 1
#     if done == func:
#         print('Best Programming Team')
