import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

import pymysql
from config import host, user, password, db_name
try:
    coonnection = pymysql.connect(
        host=host,
        port=user,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected")
except Exception as ex:
    print("Connection refused...")
    print(ex)


MainList = []

bot = telebot.TeleBot("5189417073:AAH73dnRMnHX1MTWn6zh6jJtcIRjmgmRhBI")  # Токен бота

VKkey = '1aef94f11aef94f11aef94f1ec1a93a5f411aef1aef94f178b514c16c04a348b2878471'  # Ключ доступа вконтакте


@bot.message_handler(commands=['start'])
def start(message):  # Кнопки меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('#Konkurs')
    item2 = types.KeyboardButton('#KvantNews')
    item3 = types.KeyboardButton('#IASF2022')
    item4 = types.KeyboardButton('#ФестивальОКК')
    item5 = types.KeyboardButton('#Нейрофест')
    item6 = types.KeyboardButton('#НевидимыйМир')
    item7 = types.KeyboardButton('#КонкурсНИР')
    item8 = types.KeyboardButton('#VRARFest3D')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):  # Команды для бота
    commandslist = ['#help', '#Konkurs', 'KvantNews', '#IASF2022', 'ФестивальОКК', '#Нейрофест', '#Невидимый мир',
                    '#КонкурсНИР', '#VRARFest3D']

    if message.text == "#help":
        bot.send_message(message.from_user.id, "Вот список новостных групп: \n#TechnoCom\n#IT-fest_2022\n"
                                               "#IASF2022'\n#ФестивальОКК\n#Нейрофест\n#НевидимыйМир\n"
                                               "#КонкурсНИР\n#VRARFest3D")
    if message.text == "#Konkurs":
        mesg = bot.send_message(message.from_user.id, '\nВы подписались на рассылки этой группы')
        bot.register_next_step_handler(mesg, Konkurs)
    if message.text == "#KvantNews":
        mesg = bot.send_message(message.from_user.id, '\nВы подписались на рассылки этой группы')
        bot.register_next_step_handler(mesg, Konkurs)
    if message.text == "#IASF2022":
        bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
    if message.text == "#IASF2022":
        bot.register_next_step_handler(message, IASF2022)
    if message.text == '#ФестивальОКК':
        bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
    if message.text == '#ФестивальОКК':
        bot.register_next_step_handler(message, FestOKK)
    if message.text == '#Нейрофест':
        bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
    if message.text == '#Нейрофест':
        bot.register_next_step_handler(message, Neuron)
    if message.text == '#НевидимыйМир':
        bot.send_message(message.from_user.id, 'https://vk.com/nauchim.online')
    if message.text == '#КонкурсНИР':
        bot.send_message(message.from_user.id, 'https://vk.com/nauchim.online')
    if message.text == '#VRARFest3D':
        bot.send_message(message.from_user.id, 'https://vk.com/nauchim.online')

    if message.text not in commandslist:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши #help')


@bot.message_handler(chat_types=['text'])
def Konkurs(message):  # Парсер Конкурсов
    parser = True
    while parser == True:
        url = 'https://kvantorium69.ru/konkurs/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_="post-content")
        for i in quotes:
            if i not in MainList:
                MainList.append(i)
                bot.send_message(message.from_user.id, "Новая статься с новостью")
    if message.text == '#Konkurs':
         mesg1 = bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
         bot.register_next_step_handler(mesg1, get_text_messages)


@bot.message_handler(chat_types=['text'])
def KvantNews(message):  # Парсер IT-fest_2022
    parser = True
    bot.send_message(message.from_user.id, "\nВы подписались на рассылку этой группы")
    while parser == True:
        url = 'https://kvantorium69.ru/%d0%bd%d0%be%d0%b2%d0%be%d1%81%d1%82%d0%b8/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('h2', class_="entry-title")
        for i in quotes:
            if i not in MainList:
                MainList.append(i)
                bot.send_message(message.from_user.id, "Новый конкурс")
    if message.text == '#Konkurs':
        mesg1 = bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
        bot.register_next_step_handler(mesg1, get_text_messages)


@bot.message_handler(chat_types=['text'])
def IASF2022(message):  # Парсер IASF2022
    parser = True
    bot.send_message(message.from_user.id, "\nВы подписались на рассылку этой группы")
    while parser == True:
        url = 'https://vk.com/aerospaceproject'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_="wall_posts")
        quotesList = [quotes]
        """bot.send_message(message.from_user.id, len(quotesList))"""


@bot.message_handler(chat_types=['text'])
def FestOKK(message):  # Парсер FestOKK
    parser = True
    bot.send_message(message.from_user.id, "\nВы подписались на рассылку этой группы")
    while parser == True:
        url = 'https://vk.com/okk_fest'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_="wall_posts")
        quotesList = [quotes]
        """bot.send_message(message.from_user.id, len(quotesList))"""


@bot.message_handler(chat_types=['text'])
def Neuron(message):  # Парсер Neuron
    parser = True
    bot.send_message(message.from_user.id, "\nВы подписались на рассылку этой группы")
    while parser == True:
        url = 'https://vk.com/neurofest2022'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_="wall_posts")
        quotesList = [quotes]
        """bot.send_message(message.from_user.id, len(quotesList))"""


bot.polling(none_stop=True, interval=0)
