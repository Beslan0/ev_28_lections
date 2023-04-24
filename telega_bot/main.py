# import telebot
# from telebot import types
# import random

# token = "6113686647:AAHHeTZ_JWpszExKQHNWn_4xG2mv70UFBA0"

# bot = telebot.TeleBot(token)

# keyboard = types.ReplyKeyboardMarkup()
# btn1 = types.KeyboardButton("Play!")
# btn2 = types.KeyboardButton("No, I pass")
# keyboard.add(btn1, btn2)

# @bot.message_handler(commands=["start", "game"])
# def start_massage(message):
#     bot_message = bot.send_message(message.chat.id, "Hello King, start game?", reply_markup=keyboard)
#     bot.register_next_step_handler(bot_message, check_answer)
# def check_answer(message):
#     if message.text == "Yes":
#         bot.send_message(message.chat.id, "Okey Тогда лови правмла игры!\n Нужно угадать читслоб которое я загадаю в диопозоне от 1 10 выключительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)")
#         number = random.randint(1, 10)
#         print(number,"!!!")
#         game(message, 3, number)
#     elif message.text == "No, I pass":
#         bot.send_message(message.chat.id, "Not go out, Buy!")
#     else:
#         bot_message = bot.send_message(message.chat.id, "You enter ireguler answer!\n Enter new message!:",reply_markup=keyboard)
#         bot.register_next_step_handler(bot_message, check_answer)

# def game(message, attempts, number):
#     message_bot = bot.send_message(message.chat.id, "Выбери число!:")
#     bot.register_next_step_handler(message_bot, check_number, attempts-1, number)

# def check_number(message, attempts, number):
#     if message.text == str(number):
#         bot.send_message(message.chat.id, "Вы победили!")
#     elif attempts == 0:
#         bot.send_message(message.chat.id, "Ты проиграл")
#     else:
#         bot.send_message(message.chat.id, "Нет ты не угадал читсло прпробуй ещё раз!")
#         game(message, attempts, number)
# bot.polling()


# # В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

lines = 0
words = 0
symbols = 0
with open("requirements.txt") as file:  
    for line in file:
        lines += 1
        words += len(line.split())
        symbols += len(line.strip('\n'))

print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)

  
  