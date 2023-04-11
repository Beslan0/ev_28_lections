# set() - множество\
# Это изменяемые не упорядоченныйб интерируемый не индексируемый тип данных

# множество хранят в себе только не изменяемый типы данных

# 1 -> set()
# a = set([1,2,3,4])
# print(a) 

# a = set({1:2, 3:4})
# print(a) 

# 2 - {}

# set2 = {1, 2, 3, 4}
# print(set2)

# set1 = {1, 2, 2, 2, 3 }
# print(set1)

# set1 = {0,}
# print(type(set1))

# set1 = {1, 2, True, False}
# print(set1)

# a = 0
# print(bool(a))

# Методы set

# add -> для добавления 

# set1 = {1, 2, 3}
# set1.add(4)
# print(set1)
# set1.add((1,2,3,4))
# set1.add((1,2,3,4,5))
# print(set1)

# update / он может добовлять но не повторяя имеющеся добовляет все итериуемые 

# set1.update({3: "1", 2: "2", 4: "4"}) 
# set1.update("string", {1,2,3,4})
# print(set1)

# set1 = {[1,2,3,45,6]}

# удаление  в set

# clear - очищает все множестоа

# remove(element) - удаляет элемент если его нету выдает ошибку

# discard - если эдемента нету ничего не происходит 

# pop() - удаляет  из set (FIFO) first in first out

# set1 = {1, 2, 3, 4, 5}
# set1.remove(1)
# set1.clear(2)
# set1.discard(2)
# print(set1.pop())
# print(set1)


# difference - выводть отличие 

# set1 = {1,2,3,4}
# set2 = {2,3,5,7}

# # print(set1.difference(set2))
# # print(set1 - set2)
# # print(set2.difference(set1))
# print(set1.symmetric_difference(set2))
# print(set1^set2)

# set1 = {1,2,3,4}
# set2 = {2,3,5,7}

# print(set1.intersection(set2))
# print(set1&set2)

# print(set1.union(set2))
# print(set1 | set2)

# set1 = set([1,2,3,4,5])
# set2 = set([1,2,3,7,6])
# print(set1.difference(set2))

# num = list(input("vvedite spisok"))
# print(len(num) == len(set(num)))


# frozenset неизменяемый мнржество 

# a = frozenset([1,2,3,4,])
# print(a)

# tuple - неизменяеиый, индексируенмый, итерируемый, упорядоченый

#  index() - возвращяет индекс этого элемента в кортеж       литералы ()
# a = (True, "a" ,1)
# print(a)
# print(type(a))
# b = tuple()




# # count() -  возвращает число вхождении этого элемента в кортеж

# print(a.count(1))


