# Task2. Homework ---> Atabek
# 1)
# nums = [1,2,3,4,5,6,7,8,9]
# squared_numbers = [i ** 2 for i in nums]
# print(squared_numbers)

# 2)
# nums = [1,2,3,4,5]
# print(sum(nums))

# 3)

# nums = [1, 2, 3, 4, 5]
# if all(x >0 for x in nums):
#     print('True')
# else:
#     ('False')

# 4)
# nums = [1, 3, 5, 9]
# if any( i < 0 for i in nums):
#     print('True')
# else:
#     print('False')

# 5)
# nums = [1, 4, 5, 7, -1, 3, -5, -6]
# odd_list = list(filter(lambda num: num < 0, (nums)))
# print(odd_list)



# 6)
# nums = [1,3,4,56,76,43,5, 6, 10, 66]
# even_numbers = list(filter(lambda num: num %2 ==0, (nums)))
# print(even_numbers)

# 7)
# some_string = ['Atabek', 'United Kingdom', 'America', 'Dream', 'Programmer']
# some_word = list(filter(lambda word: len(word) > 6, (some_string)))
# print(some_word)

# 8)
# from functools import reduce
# nums = [1,2,3,4]
# result = reduce(lambda a,b : a+b, nums)
# print(result)

# 9)
# nums = [1,2,3,4,5,6,7,8,9,4,5,6,2,4,24,54323,425325,62435,6665,4244,3425345]
# chetnoe = list(filter(lambda i : i % 2 == 0, (nums)))
# ne_chetnoe = list(filter(lambda i : i % 2 == 1, (nums)))
# print(f'Kolichestvo nechetnyh chisel: {len(ne_chetnoe)}')
# print(f'Kolichestvo chetnyh chisel: {len(chetnoe)}')

# 10)
# nums = [-2,4,-1,0,54,2,-22,-12,23,-43,4,0,23,5,8,0,3]
# even_nums = list(filter(lambda i : i > 0, (nums)))
# odd_nums = list(filter(lambda i : i < 0, (nums)))
# print(f'Even nums: {even_nums}')
# print(f'Odd nums: {odd_nums}')

# 11)
# numbers = [-1, 2, 3, 4, -5, 6, 7, -8, 9, 0, 4, 43]
# new_numbers = list(map(lambda i: -1 if i < 0 else 1 if i != 0 else 0, (numbers)))
# print(new_numbers)

# 12)
# nums = [1,3,2,4,5,64,6,7,8,33,4,56]
# def best(shagi = int(input('Shag sdviga: '))):
#     if shagi < 0:
#         shagi = abs(shagi)
#         for i in range(shagi):
#             nums.append(nums.pop(0))
#     else:
#         for i in range(shagi):
#             nums.insert(0,nums.pop())
# best()
# print(nums)

# 13)
# def reverseArray(a):
#     return [::-1]

# 14)
# def isBalanced(s):
#    otvet = []
#    brackets = {'{':'}', '(':')', '[':']'}
#    for i in s:
#         if i in ['{', '(', '[']:
#             otvet.append(i)
#         else:
#             if otvet:
#                 del_ = otvet.pop()
#                 if brackets [del_ ] != i:
#                     return 'NO'
#             else:
#                 return 'NO'
#    return 'NO' if otvet else 'YES'



