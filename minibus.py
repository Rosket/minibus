
import telebot
from telebot import types
import random
bot = telebot.TeleBot("")
 # в скобки вставляешь уникальный номер токена в кавычках ""


@bot.message_handler(commands=['start'])
def hello_command(message):
    bot.send_message(
        message.chat.id,
        'Привет, {0.first_name}!!! '.format(message.from_user) +
        'Это бот который поможет тебе узнать расписание маршруток.\n' +
        'Если хочешь начать, напиши /go.\n' +
        'Вдруг что то не получается /help.'
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        'Команды работы с ботом: \n' +
        'Запуск программы бота /go.\n' +
        'Список ключевых команд /help.'
    )


@bot.message_handler(commands=['go'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    town1 = types.KeyboardButton('Минск')
    town2 = types.KeyboardButton('Брест')
    town3 = types.KeyboardButton('Гомель')
    town4 = types.KeyboardButton('Могилев')
    town5 = types.KeyboardButton('Витебск')
    town6 = types.KeyboardButton('Гродно')
    item1 = types.KeyboardButton('🔸 Рандомное число')

    markup.add(town1, town2, town3, town4, town5, town6, item1)

    bot.send_message(message.chat.id, 'отлично, {0.first_name}!'.format(message.from_user) + 'Откуда поедем?',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🔸 Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 1000)))

        elif message.text == 'Минск':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town2 = types.KeyboardButton('Брест')
            town3 = types.KeyboardButton('Гомель')
            town4 = types.KeyboardButton('Могилев')
            town5 = types.KeyboardButton('Витебск')
            town6 = types.KeyboardButton('Гродно')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(town2, town3, town4, town5, town6, back)

            bot.send_message(message.chat.id, 'куда хочешь попасть?', reply_markup=markup)

        elif message.text == 'Брест':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town1 = types.KeyboardButton('Минск')
            town3 = types.KeyboardButton('Гомель')
            town4 = types.KeyboardButton('Могилев')
            town5 = types.KeyboardButton('Витебск')
            town6 = types.KeyboardButton('Гродно')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(town1, town3, town4, town5, town6, back)

            bot.send_message(message.chat.id, 'куда хочешь попасть?', reply_markup=markup)

        elif message.text == 'Гомель':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town2 = types.KeyboardButton('Брест')
            town1 = types.KeyboardButton('Минск')
            town4 = types.KeyboardButton('Могилев')
            town5 = types.KeyboardButton('Витебск')
            town6 = types.KeyboardButton('Гродно')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(town2, town1, town4, town5, town6, back)

            bot.send_message(message.chat.id, 'куда хочешь попасть?', reply_markup=markup)

        elif message.text == 'Могилев':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town2 = types.KeyboardButton('Брест')
            town3 = types.KeyboardButton('Гомель')
            town1 = types.KeyboardButton('Минск')
            town5 = types.KeyboardButton('Витебск')
            town6 = types.KeyboardButton('Гродно')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(town2, town3, town1, town5, town6, back)

            bot.send_message(message.chat.id, 'куда хочешь попасть?', reply_markup=markup)

        elif message.text =='Витебск':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town2 = types.KeyboardButton('Брест')
            town3 = types.KeyboardButton('Гомель')
            town4 = types.KeyboardButton('Могилев')
            town1 = types.KeyboardButton('Минск')
            town6 = types.KeyboardButton('Гродно')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(town2, town3, town4, town1, town6, back)

            bot.send_message(message.chat.id, 'куда хочешь попасть?', reply_markup=markup)

        elif message.text == 'Гродно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town2 = types.KeyboardButton('Брест')
            town3 = types.KeyboardButton('Гомель')
            town4 = types.KeyboardButton('Могилев')
            town5 = types.KeyboardButton('Витебск')
            town1 = types.KeyboardButton('Минск')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(town2, town3, town4, town5, town1, back)

            bot.send_message(message.chat.id, 'куда хочешь попасть?', reply_markup=markup)

        elif message.text == '⬅️ Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town1 = types.KeyboardButton('Минск')
            town2 = types.KeyboardButton('Брест')
            town3 = types.KeyboardButton('Гомель')
            town4 = types.KeyboardButton('Могилев')
            town5 = types.KeyboardButton('Витебск')
            town6 = types.KeyboardButton('Гродно')
            item1 = types.KeyboardButton('🔸 Рандомное число')

            markup.add(town1, town2, town3, town4, town5, town6, item1)

            bot.send_message(message.chat.id, 'отлично, {0.first_name}!'.format(message.from_user) + 'Откуда поедем?',
                             reply_markup=markup)

        elif message.text == '📟 Поисковик 📟':  # кнопка в чате, в данном случае идет ссыль на сайт
            keyboard = types.InlineKeyboardMarkup()
            url_button = tyes.InlineKeyboardButton(text="Перейти на Яндекс",
                                                    url="https://ya.ru")  # url = сылка
            keyboard.add(url_button)
            bot.send_message(message.chat.id,
                             "Привет! Нажми на кнопку и перейди в поисковик.",
                             reply_markup=keyboard)

bot.polling(none_stop=True)