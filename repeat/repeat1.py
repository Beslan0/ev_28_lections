# num1 = 1

# while num1 >= 0:
#     num1 = input("vvedite chislo:")
#     if num1[0] == "-" and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1
# print("встреьтилось отрицательное число3!")
# --------------------------------------------------------------------------------------------------------

# from random import randint

# ls = []
# for x in range(0, 100):
#     ls.append(randint(0, 100))

# print(ls, len(ls))


# ls.sort()
# print(ls, len(ls))


# res = []
# for x in ls:
#     res.append(x)

# res.sort()
# print(res)

# x1 = int(input("vvedite 1 cordinant gde stoiit ladya"))
# y1 = int(input("vvedite 2 cordinant gde stoiit ladya"))
# ladya = [x1, y1]

# x2 = int(input("vvedite 1 cordinant kuda idet ladya"))
# y2 = int(input("vvedite 1 cordinant kuda idet ladya"))

# target = [x2, y2]

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)
# ------------------------------------------------------------------------

# import random

# ls = ["plov," , "besh-barmak", "kurdak", "oromo", "lagman"]


# p = 0
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1_000):
#     meal = random.choice(ls)
#     print(meal)
#     if meal.lower() == "plov":
#         p +=1
#     elif meal.lower() == "besh-barmak":
#         b += 1
#     elif meal.lower() == "kurdak":
#         k += 1
#     elif meal.lower() == "oromo":
#         o += 1
#     elif meal.lower() == "lagman":
#         l += 1

# print("result hunggry game")
# print(f"plov:{p}\nbesh-barmak: {b}\nkurdak:,{k}\noromo:,{o}\nlagman: {l}")

# ----------------------------------------------------------------------------------


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# nums = [4,11,2,5, 1, 6]
# target = 8

# for i in raise(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         print(f"")
            # break

