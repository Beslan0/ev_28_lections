# list comprehensions  - это генераторы  списков

# list comprehensions - упрощеная подход к созлонию списков которые задействует в себе цикл for  
# а так же конструкцию if  для определения того что в итоге поподает в наш список

# list -> 0 -200 -> num % 2 == 0

# ls = []

# for x in range(1, 201):
#     if x % 2 == 0:
#         ls.append(x)


# ls = [x for x in range(1, 201) if x % 2 != 0 ]

# print(ls)


# list: 0 - 300 -> num  % 2 == 0


# ls = [x for x in range(0, 301) if x % 2 == 0  and  x % 3 == 0]

# print(ls)


# list: 0 - 100 -> num % 2 == 0: num ** 2 


# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0, 101) if  x % 2 == 0 or x % 3 == 0]

# print(ls)


# newlist = [expression for item in iterable <if condition == True > ]

# ls = [str(i * 2) for i in range(1, 11) ]

# print(ls)


# ls = [[1,2,3], [4,5,6], [7,8,9]]

# res = []
# for x in ls:
#     for item in x:
#         res.append(item)
# print(res)


# ls = [[1,2,3], [4,5,6], [7,8,9]]

# res = [item for x in ls for item in x]
# print(res)
# ------------------------------------------------------------------------------------


# from datetime import datetime

# start = datetime.now()
# ls = []

# ls = [x for x in range(0, 100_000_000)]
# # for x in range(0, 100_000_000):
# #     ls.append(x)
# finish = datetime.now()
# print(finish - start)
# ------------------------------------------------------------------------


# set comprehensions
# set1 = {x for x in range(1, 100)}
# print(set1, type(set1))
# -----------------------------------------------------------------


# dict comprehensions

# dict1 = {
#     key: value,
#     key: value,
# }

# dict1 = {x: x ** 2 for x in range(0, 16)}

# print(dict1)

# names = ["Johne" , "Tirion", "Eygan", "Sansa", "Ramsi"]
# dict1 = {x: len(x) for x in names}

# print(dict1)
# ------------------------------------------------------------------

# dict1 = {
#     "Soke": {"history": 99, "fizik": 95, "math": 94},
#     "Omoke":{"history": 84, "fizik": 75, "math": 86},
#     "John":{"history": 100, "fizik": 87, "math": 90},
# }


# # res = {}
# # for key, value in dict1.items():
# #     for innner_key, inner_value in value.items():
# #         if max (value.values()) == inner_value:
# #             res[key] = innner_key
# # print(dict1)
# # print(res) 

# res = {key: inner_key for key, value in dict1.items() for inner_key, inner_value in value.items() if max(value.values()) == inner_value }
# print(res)


   
