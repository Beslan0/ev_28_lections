# JSON - JavaScript Objiect Notation
# Это единный текстоствый формат данных, был создан  для хранения и передачи данных между сервисами 
# <filename>.json # в формате JSON
# {
#     "id": 1,
#     "author":{
#     "name": "Ed Sheeran",
#     "age": 35,

#     },
#     "title": "don't",
#     "feat": false,
# } -------------------------------------- это JSON




# !!!
# js object = {key: value}
# Py dict = {key: value}
# JSON = {key: value}

# Процессы Сериализации и Десериализации данных (конверация)

# Сериализация (запись данных в JSON) - Это перевод из Pythona в JSON формат

# dump - записывает данных в файл формате JSON
# dumps - записывает данные в текст формата  JSON

# Десериализации (чтение данных из JSON) - это процесс переводы из JSON  в Py dict

# load - функция котороя считывает данные из файла JSON 
# loads - функция котороя считывает данные из текста JSON

# ----------------------------------------

# процесс сериализации


# import json

# dict_ = {
#     "name": "John Snow",
#     "age": 24,
#     "status": True,
#     "wife": False,
#     "children": None,
    
# }
# print(dict_,type(dict_))

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))


# import json
# dict_ = {
#     "name": "John Snow",
#     "age": 24,
#     "status": True,
#     "wife": False,
#     "children": None,
    
# }
# print(dict_,type(dict_))

# with open("new.json", "w") as file:
#     json.dump(dict_, file, indent=4)

# ------------------------------------------------------

# процесс Десериализации


# import json
# with open("new.json", "r") as file:
#     json_data = file.read()

# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_,type(dict_))

# import json

# with open("new.json", "r") as file:
#     dict_ = json.load(file)
#     print((dict_, type(dict_)))

# from urllib.request import urlopen
# import json
# import pprint as pp

# url = "https://randomuser.me/api/"
# json_data = urlopen(url)
# # print(json_data, dir(json_data)) 

# dict_ = json.load(json_data)
# pp.pprint(dict_)
