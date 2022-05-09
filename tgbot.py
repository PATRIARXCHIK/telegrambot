import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

# KvantNews - name
# KvantNewsBot - username
MainList = []

bot = telebot.TeleBot("5338841830:AAHjWuQeCIVcf6zU6Zzxjxn88W8P_R4JWos")  # Токен бота

VKkey = '1aef94f11aef94f11aef94f1ec1a93a5f411aef1aef94f178b514c16c04a348b2878471'  # Ключ доступа вконтакте


@bot.message_handler(commands=['start'])
def start(message):  # Кнопки меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('#Konkurs')
    item2 = types.KeyboardButton('#KvantNews')

    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):  # Команды для бота
    commandslist = ['#help', '#Konkurs', '#KvantNews', '#IASF2022', 'ФестивальОКК', '#Нейрофест', '#Невидимый мир',
                    '#КонкурсНИР', '#VRARFest3D']

    if message.text == "#help":
        bot.send_message(message.from_user.id, "Вот список новостных групп: \n#Konkurs\n#KvantNews\n"
                                               "#IASF2022'\n#ФестивальОКК\n#Нейрофест\n#НевидимыйМир\n"
                                               "#КонкурсНИР\n#VRARFest3D")
    if message.text == "#Konkurs":
        mesg = bot.send_message(message.from_user.id, '\nВы подписались на рассылку этой группы')
        bot.callback_query_handler(Konkurs)
    if message.text == "#KvantNews":
        mesg = bot.send_message(message.from_user.id, '\nВы подписались на рассылку этой группы')
        bot.register_next_step_handler(mesg, KvantNews)

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
                bot.send_message(message.from_user.id, "Новый конкурс")
    if message.text == '#Konkurs':
        bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
        bot.message_handler(get_text_messages)


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
                bot.send_message(message.from_user.id, "Новая статься с новостью")
    if message.text == '#Konkurs':
        bot.send_message(message.from_user.id, '\nВы отписались от рассылки этой группы')
        bot.message_handler(get_text_messages)


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
