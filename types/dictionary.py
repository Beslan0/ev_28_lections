# dict() - жто у нас словарь упорядоченная  коолекция элементов (python) 3.7 -> ordered). каждый элемент внутри диктшенори зранятся  
# в виде пары: {ключ: занчания }

# ассоциативный массив, hash table, object(js), scricuter == dictinery(py)

#  ключами мокт быть толькол неизменияемые типы данных и в слваре созраняются только уникадтны е ключи

# тогда как значениями могут выступать любые типы даннах

# thisdict = {
#     "brand": "ford" ,
#     "model": "mustang",
#     "year": 1967
# }

# print(thisdict)

# print(type(thisdict))

# print(thisdict["brand"])
# print(thisdict["model"])
# print(thisdict["year"])

# thisdict["motor"] = "GTE Turbo"
# thisdict["brand"] = "Tesla"

# print(thisdict)



# a = {}
# b = dict()

# print(dir(dict))

# items, keys, values

user_info = {
    "first_name": "John",
    "last_name": "Snow",
    "age": 24,
    "email": "johnsnow@gmail",
    "role": "admin",
}

ls = user_info.keys()
ls = list(ls)
print(ls)

# ls = list(user_info.values())
# print(ls)

# items = user_info.items()
# print(items)

# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# for x in user_info.items():

#     print(f"keys: {x[0]}  values: {x[1]}")

# for key, value in user_info.items():

#     print(f"keys: {key} ,  values: {value}")


# dict_ = {"name": "jak", "age": 17,}

# print(dict_)

# dict_["name"] = "Johne"
# dict_["age"] = 24
# dict_["adress"] = "winterfel"

# print(dict_)
# dict_.update({"age": 25, "adress": "Blackcastle"})
# print(dict_)

# --------------------------------------------------------------------------------------------

# получения данных со словаря 

# dict_ = {1: "pizza", 2: "burger", 3: "steak"}
# print(dict_[2], "!!!")
# print(dict_.get(2))

# setdefault - работает так же как get  но если нет такого ключа то создает новую пару из этого ключа


# dict_ = {1: "pizza", 2: "burger", 3: "steak"}

# print(dict_.setdefault(5, "manty"))
# print(dict_)

# ---------------------------------------------------------------------------------------------------------

# создания  - fromkeys

# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, "value")
# print(new_dict)

# ------------------------------------------------------------------------------------------------------------

# удвление элементов 

# pop, popitem 

# pop(<key>) - удаляет пару по ключей

# dict_ = {"name": "john", "last_name": "Snow",}
# print(dict_)
# remove = dict_.pop("last_name")
# print(dict_)
# print(remove)

# popitem - удаляет последнию пару

# dict_ = {"name": "john", "last_name": "Snow",}
# print(dict_)
# remove = dict_.popitem()
# print(dict_)
# print(remove)
# ------------------------------------------------------------------------------------












# roles = {
#     0: "admin",
#     1: "Customer",
#     2: "Vendor",
# }

# users = {
#     1: {
#     "id": 1, "role": roles[2], "username": "Tirion", 
#     },
#     2:{
#     "id": 2, "role": roles [0], "username": "Johne",
#     },
#     3:{
#     "id": 3, "role": roles [1], "username": "Raychel",
#     }
# }
# print(users)

# product = {
#     "id": 1,
#     "title": "samsung galaxy a51",
#     "description": "lorem ipsum",
#     "prise": 250
# }

# print(product)

# id_user = int(input("vvedite ID: "))

# if users [id_user]["role"] == roles[0]:
#     product["description"] = input("vvedite opisanie: ")
# else:
#     print("you do not promissions")

# print(product)


