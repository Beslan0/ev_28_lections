# list() - (списки, массив) -  изменяеиый последовательный тип данных, коровый представляет их себя коллекцию каких либо обектов (значения)

# my_list = [1, "str", False, None, [1,2,3]]

# print(my_list,type(my_list))

# range() -  возвращяет последовательность чисел (элементов)
# ls = range(1,101)
# my_list = list(ls)
# print(my_list)

# /list()

# my_list = list("hello world")

# print(my_list)

# tuple_ = ("banan, qwerty, rtrt")

# print(tuple_, type(tuple_))

# ls = list(tuple_)
# print(ls, type(ls))



# индексация в списках

# ls = [1, 2, 3, 4, 5, "string", [True, False, None]]

# print(ls, len(ls))
# print(ls[1], ls[2])

# print(ls[4:])

# ls = [1, 2, 3, 4, 5, "string", [True, False, None]]
# print(ls[6][2])


# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print(num)



# ls = ["John", "sansa", "Tirion", ]
# print(ls, len(ls))

# for x in ls:
    
#     print(f"Hello mr/ms {x}! welcom to the club !")

# ls = list(range(1, 21))
# print(ls)
# for num in ls:
#     if num % 2  == 0:
#         print(f"число четное {num}, квадрат: {num**2}")
#     else:
#         print(f"нечетное читсло {num}, куб: {num**3}")
# ------------------------------------------------------------------------------------------------------------------------

# методы списков


# print(dir([]))        

# append(element) - добовляет элемент в конце списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append("Hello")
# ls.append([True, False, None])
# print(ls)

# extend(object) - расширяет список

# ls = [1, 2, 3]
# ls.append("hello")
# print(ls)
# ls.extend("hello")
# ls.extend(str(56))
# ls.extend([1,2,3])
# print(ls)

# ls = [1,2,3,]
# ls1 = [4,5,6]
# print(ls + ls1)

# sort() - сортирует список, если передать reverse=true, то список отсортиркется в убывающем порядке

# from random import randint

# ls = []

# for x in range(0, 101):
#     num = randint(0,1001)
#     ls.append(num)

# print(ls)
# ls.sort()
# print("after:")
# print(ls)

# ls = ["john", "tirion", "aizirek"]
# ls.sort(key=len, reverse=True)
# print(ls)

# insert(index, element) - добовляет элемент по указаному индексу

# ls = ["string" , 2, 3, False]

# ls.insert(2, 1)
# print(ls)

# remove(element) - удаляет элемент из списка если такого нет то выводится ошибка
# pop([index]) - удаляет и возвращяет элемент из  списка по index но если index не передать то удаляет последний элемент

# ls = [5, 1, 2, 3, 4, 5, 5, 5]
# ls.remove(5)
# print(ls)

# while 5 in ls:
#     ls.remove(5)
# print(ls)

# ls = [5, 1, 2, 3, 4, 5, 5]
# print(ls.pop(0))
# print(ls.remove(5))
# print(ls)

# deleted = ls.pop()
# print(ls)
# print(deleted)

# update------------------------

# ls = [1, "h", 3]
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ["first_item", "second_item", "third_item", "forth_item", "fifth_item", "sixth_item"]

# spisok = []

# for x in pizza:
#     if not x.startswith("f"):
#         spisok.append(x)

# print(spisok)