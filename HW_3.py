# list_1 = [1, 2, 3, 4, 5, 3, 3] 
# k = 1 
# count_k = 0 
# for i in list_1: 
#     if i == k: 
#         count_k += 1 
# print(count_k)

# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list = [2, 4, -1, 6, 8, 2, 9, 3, 2, 5] 
# k = -4 

# nearest_num = list[0]
# diff = abs(k - nearest_num)
# for i in range(len(list)):
#     if k >= 0:
#         diff = abs(k - list[i])
#         if  nearest_num >= diff:
#             nearest_num = diff
#             j = i
#     else: 
#         diff = k + list[i]
#         if  nearest_num >= diff:
#             nearest_num = diff
#             j = i
    

# print(list[j])


# import re 
# def Scrabble(text): return bool(re.search("[а-яА-Я]", text)) 
# Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"} 
# Eng = { 1:"A, E, I, O, U, L, N, S, T, R ", 2:"D, G", 3:"B, C, M, P", 4:"F, H, V, W, Y", 5:"K", 8:"J, X"} 
# text = input("Введите слово: ").upper() 
# if Scrabble(text): 
#     print(sum([k for i in text for k, v in Rus.items() if i in v])) 
# else: print(sum([k for i in text for k, v in Eng.items() if i in v]))


# def fun(x):
#     for key in dct:
#         if x in key:
#             return dct.get(key)
 
# dct = {
#     'AEIOULNSTR' : 1, 'DG' : 2, 'BCMP' : 3,
#     'FHVWY' : 4, 'K' : 5, 'JX' : 8, 'QZ' :10
#     }
# print(sum(map(fun, input())))

# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# text = input().upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))




# LATIN_BASE = ord('a')
# LATIN_BOUNDARY = ord('z')
# CYRILIC_BASE = ord('а')
# CYRILIC_BOUNDARY = ord('я')

# LATIN_COSTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# CYRILIC_COSTS = [1, 3, 1, 3, 2, 1, 3, 5, 5, 1, 4, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 10, 5, 5, 5, 8, 10, 10, 4, 3, 8, 8, 3]
                 
# word = input('Enter word: ').lower()

# if LATIN_BASE <= ord(word[0]) <= LATIN_BOUNDARY:
#     costs = LATIN_COSTS
#     base = LATIN_BASE
# else:
#     costs = CYRILIC_COSTS
#     base = CYRILIC_BASE

# cost = sum(map(lambda c: costs[ord(c) - base], word))
# print(cost)

# Дмитрий Кубаткин, [23.01.2022 13:32]
# LATIN_BASE = ord('a')
# LATIN_BOUNDARY = ord('z')
# CYRILIC_BASE = ord('а')

# LATIN_COSTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 
#                4, 4, 8, 4, 10]
# CYRILIC_COSTS = [1, 3, 1, 3, 2, 1, 5, 5, 1, 4, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 
#                  10, 5, 5, 5, 8, 10, 10, 4, 3, 8, 8, 3]

# word = input('Enter word: ').lower()

# if LATIN_BASE <= ord(word[0]) <= LATIN_BOUNDARY:
#     costs = LATIN_COSTS
#     base = LATIN_BASE
# else:
#     costs = CYRILIC_COSTS
#     base = CYRILIC_BASE

# cost = sum(map(lambda c: costs[ord(c) - base], word))
# # print(cost)

# import string

# POINTS_EN = {'AEIOULNSTR': 1,
#              'DG': 2,
#              'BCMP':3,
#              'FHVWY': 4,
#              'K': 5,
#              'JX': 8,
#              'QZ': 10}
# POINTS_RU = {'АВЕИНОРСТ': 1,
#              'ДКЛМПУ': 2,
#              'БГЁЬЯ':3,
#              'ЙЫ': 4,
#              'ЖЗХЦЧ': 5,
#              'ШЭЮ': 8,
#              'ФЩЪ': 10}


# def count_score(word):
#     if word[0] in string.ascii_uppercase:
#         points = POINTS_EN
#     else:
#         points = POINTS_RU
#     return sum(v for c in word.upper() for k, v in points.items() if c in k)

# word = 'laptop'
# print(count_score(word))