import telebot, eng_rus, rus_eng, adding_word, super_quiz
from telebot import types
from random import randint
import time

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, это бот Толмач!'
                     '\nТолмач - примитивный англо-русский переводчик. '
                     '\nА ещё он может поиграть с тобой, чтобы ты лучше запомнил новые слова! '
                     '\nПросто введи нужную команду и наслаждайся :) '
                     '\nНадеемся ,он будет тебе полезен!'
                     '\n\n/help - расскажет, как собой пользоваться,'
                     '\n/perevod - переведет слово,'
                     '\n/add_slovo - добавит слово, если его нет в словаре толмача,'
                     '\n/quiz - поможет выучить новые слова и просто развлечет.')


@bot.message_handler(commands=['perevod'])
def ask_language(message):
    keyboard = types.InlineKeyboardMarkup()
    key_rus_eng = types.InlineKeyboardButton(text='rus->eng', callback_data='rus->eng')
    key_eng_rus = types.InlineKeyboardButton(text='eng->rus', callback_data='eng->rus')
    keyboard.row(key_eng_rus, key_rus_eng)
    question = 'С какого языка на какой хотите переводить?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def perevod(call):
    stop_answer = ['That\'s your choice)', 'As you wish :)', 'You\'re the boss']
    correct = ['Great job!', 'You are the best!', 'All that hard work is paying off!', 'Nice work!',
               'You nailed it! Good job!', 'Perseverance, that is the answer', 'You got it right!',
               'You are quite good my friend!', 'Your dedication is inspiring!', 'You are amazing!',
               'That is a job well done!', 'You are doing so well!','Keep working like that and you will get there!']
    wrong = ['That is not the answer I was looking for...']
    if call.data == 'rus->eng':
        bot.send_message(call.message.chat.id, 'Что вы хотите перевести? \nЧтобы остановиться наберите \"stop\".')
        bot.register_next_step_handler(call.message, ruseng)
    elif call.data == 'eng->rus':
        bot.send_message(call.message.chat.id, 'Что вы хотите перевести?\nЧтобы остановиться наберите \"стоп\".')
        bot.register_next_step_handler(call.message, engrus)
    elif call.data == 'stop':
        bot.send_message(call.message.chat.id, stop_answer[randint(0, len(stop_answer)-1)])
    elif call.data == 'correct':
        bot.send_message(call.message.chat.id, correct[randint(0, len(correct)-1)])
        question, correct_answer, wrong_answer = super_quiz.main()
        time.sleep(3)
        keyboard_quiz = types.InlineKeyboardMarkup()
        key_correct = types.InlineKeyboardButton(text= correct_answer, callback_data='correct')
        key_wrong = types.InlineKeyboardButton(text= wrong_answer, callback_data='wrong')
        key_stop = types.InlineKeyboardButton(text= 'stop the game', callback_data='stop')
        if randint(0, 1) == 0:
            keyboard_quiz.add(key_correct)
            keyboard_quiz.add(key_wrong)
            keyboard_quiz.add(key_stop)
        else:
            keyboard_quiz.add(key_wrong)
            keyboard_quiz.add(key_correct)
            keyboard_quiz.add(key_stop)
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard_quiz)
    elif call.data == 'wrong':
        bot.send_message(call.message.chat.id, wrong[randint(0, len(wrong)-1)])
        question, correct_answer, wrong_answer = super_quiz.main()
        time.sleep(3)
        keyboard_quiz = types.InlineKeyboardMarkup()
        key_correct = types.InlineKeyboardButton(text= correct_answer, callback_data='correct')
        key_wrong = types.InlineKeyboardButton(text= wrong_answer, callback_data='wrong')
        key_stop = types.InlineKeyboardButton(text= 'stop the game', callback_data='stop')
        if randint(0, 1) == 0:
            keyboard_quiz.add(key_correct)
            keyboard_quiz.add(key_wrong)
            keyboard_quiz.add(key_stop)
        else:
            keyboard_quiz.add(key_wrong)
            keyboard_quiz.add(key_correct)
            keyboard_quiz.add(key_stop)
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard_quiz)


def engrus(message):
    stop_answer = ['That\'s your choice)', 'As you wish :)', 'You\'re the boss']
    zapros = message.text.lower()
    if zapros == "стоп":
        bot.send_message(message.chat.id, stop_answer[randint(0, len(stop_answer) - 1)])
    else:
        bot.send_message(message.chat.id, eng_rus.main(zapros))
        bot.send_message(message.chat.id, 'Что вы хотите перевести?')
        bot.register_next_step_handler(message, engrus)

def ruseng(message):
    stop_answer = ['That\'s your choice)', 'As you wish :)', 'You\'re the boss']
    zapros = message.text.lower()
    if zapros == "stop":
        bot.send_message(message.chat.id, stop_answer[randint(0, len(stop_answer) - 1)])
    else:
        bot.send_message(message.chat.id, rus_eng.main(zapros))
        bot.send_message(message.chat.id, 'Что вы хотите перевести?')
        bot.register_next_step_handler(message, ruseng)

@bot.message_handler(commands=['add_slovo'])
def add_slovo(message):
    bot.send_message(message.chat.id, 'Введите слово с его переводом в следующем формате:'
                                      '\nСлово на английском, символ \';\', перевод на русский. Без пробелов и прочих символов.'
                                      '\nWord;перевод'
                                      '\n\nЧто вы хотите добавить? ')
    bot.register_next_step_handler(message, adding)

def adding(message):
    new_slovo = message.text.lower()
    bot.send_message(message.chat.id, adding_word.adding(new_slovo))

@bot.message_handler(commands=['quiz'])
def quiz(message):
    question, correct_answer, wrong_answer = super_quiz.main()
    bot.send_message(message.chat.id, 'Вам будет предложено выбрать перевод для слова. '
                                      '\nПросто выберите правильный ответ.')
    keyboard_quiz = types.InlineKeyboardMarkup()
    key_correct = types.InlineKeyboardButton(text= correct_answer, callback_data='correct')
    key_wrong = types.InlineKeyboardButton(text= wrong_answer, callback_data='wrong')
    key_stop = types.InlineKeyboardButton(text= 'stop the game', callback_data='stop')
    if randint(0, 1) == 0:
        keyboard_quiz.add(key_correct)
        keyboard_quiz.add(key_wrong)
        keyboard_quiz.add(key_stop)
    else:
        keyboard_quiz.add(key_wrong)
        keyboard_quiz.add(key_correct)
        keyboard_quiz.add(key_stop)
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard_quiz)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     'Этот бот способен переводить какое-то количесво слов с английского и'
                     ' давать к ним толкования, если слова не совсем простые. '
                     '\nПопросить бота что-то перевести можно через команду /perevod. '
                     '\nПостарайтесь вводить слова без опечаток и ошибок, иначе Толмач не справится.'
                     '\nЕсли в ответ на ваш запрос пришло такое сообщение: --, значит Толмач не знает слова или его толкования.'
                     '\nВ этом случае вы можете воспользоваться командой /add_slovo и пополнить словарный запас Толмача.'
                     '\nМожно поиграть с Толмачом через команду /quiz! Толмач будет показывать слово на английском и '
                     'просить выбрать подходящий перевод.')


bot.polling(none_stop=True)
