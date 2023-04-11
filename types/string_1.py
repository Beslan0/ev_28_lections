#  индксация в строке
# name = "Johne"
#     # J = 0 = -4
#     # o = 1 = -3
#     # h = 2 = -3
#     # h = 3 = -1
# print(name)
# print(name[1])
# str = "kani"
# print(str[-1], str[0])

# str = "birthday"
# print(str[5] + str[6] + str[7])
# print(str[0] + str[1] + str[2] + str[3] + str[4])

# срезы по индексам
# [start: end: <step>]

# str1 = "birthday"
# print(str1[5:])
# print(str1[:5])

# text = "Hello world! my name is John I\"m King of north!"
# # print(text[:13])
# # print(text[::2])

# print(text[::-1])

# Конкатенация строк (соединение)
# a = "hello"
# b = "world"
# c = ""
# print(a + b + c)

# экранирование  - способ записи в строку, которые невозможно ввести с клавиатуры

# \n -> перенос строки
# \t ->  горизонталтная табуляция 
# \v ->  вертикальная табуляция 
# \f -> перевод страниц
# \r -> возврат указателя 
# print("\vHello \tworld!\nMy name is john snow!")

# форматирования строк
#  1.  с помощью %
#  2.  ч исподьзованием .format()
#  3.  интерподяция строк (преоброзоаония, f - строки)

# %
# name = input("введите имя:")
# last_name   = input("введите фамилия:")
# # print("ДОЬРО пожаловать к нам " + name  + "" + last_name + "!")
# print("Hello mr/mstr %s %s!" %(name, last_name))

# .format

# name = input("введите имя:")
# last_name   = input("введите фамилия:")
# print("Приветсвую вас, {} {}, в наш клуб!" .format(name, last_name))

# f - stroki
# a = input("enter mr/mrs:
# ")
# name = input("введите имя:")
# last_name   = input("введите фамилия:")
# print(f"Hello {a} {name} {last_name}! welcome to the party!")

# text = "запомни питтер с большой с силой приходит большая отвественность"
# reversed_text = text[::-1]
# # print(reversed_text)
# i = 0
# count_t = 0
# len_text = len(reversed_text)
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == "т" or symbol == "Т":
#         count_t += 1
#     # print(symbol)
#     i += 1

# print(f"в тексте т встретились {count_t} раз!")