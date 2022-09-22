
# # x = "hello"

# # #if condition returns False, AssertionError is raised:
# # assert x == "hello", "x should be 'hello'"
# # from collections.abc import Iterable
 
# # name = 'Roster'
 
# # if isinstance(name, Iterable):
# #   print(f"{name} is iterable")
   
# # else:
# #   print(f"{name} is not iterable")

# # def method(text):
# #   print(text)

# # method("hello")

# # import re

# #Check if the string starts with "The" and ends with "Spain":

# # txt = "The rain- in Spain"
# # x = re.search("^The.*Spain$", txt)

# # if x:
# #   print("YES! We have a match!")
# # else:
# #   print("No match")

# # import glob
# # import os
# # import time
# # glob.glob('*Dec*.py')
# # meta = os.stat('set.py')
# # time.localtime(meta.st_mtime)
# # import re

# # target_string = "PINEAPPLE 20 PINEAPPLE 20 PINEAPPLE PINEAPPLE The price of PINEAPPLE ice cream is 20"

# # # two groups enclosed in separate ( and ) bracket
# # result = re.search(r"(\bPINEAPPLE+\b).+(\b20+)", target_string)

# # # Extract matching values of all groups
# # print(result.groups())
# # # Output ('PINEAPPLE', '20')

# # # Extract match value of group 1
# # print(result.group(1))
# # # Output 'PINEAPPLE'

# # # Extract match value of group 2
# # print(result.group(2))
# # # Output 20

# import re
# import itertools


# def solve(puzzle):
#     words = re.findall('[A-Z]+', puzzle.upper())
#     unique_characters = set(''.join(words))
#     assert len(unique_characters) <= 10, 'Too many letters'
#     first_letters = {word[0] for word in words}
#     n = len(first_letters)
#     sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
#     characters = tuple(ord(c) for c in sorted_characters)
#     digits = tuple(ord(c) for c in '0123456789')
#     zero = digits[0]
#     for guess in itertools.permutations(digits, len(characters)):
#         if zero not in guess[:n]:
#             equation = puzzle.translate(dict(zip(characters, guess)))
#             if eval(equation):
#                 return equation

# if __name__ == '__main__':
#     import sys
#     dum = "MAD + KAR == RKJ"
#     print(dum)
#     solution = solve(dum)
#     if solution:
#         print(solution)

# first_letters={'m','s'}
# unique_characters={'m','a','d','y','s'}
# sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
# print(sorted_characters)
# print('mad'.join(unique_characters-first_letters))

# lst = [0,1,2,5]
# more = lst*10
# print(more)




# class say_name:
#     def printName(self,name):
#         print(name)
# nm = say_name()
# nm.printName("maddy")


# print(type(nm))
# print("++++")
# print(nm.__class__)

print("hello")
print(5/0)
print("bye")