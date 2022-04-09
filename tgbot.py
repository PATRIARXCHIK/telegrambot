import telebot
import requests
from bs4 import BeautifulSoup

# GregoryyyyBot -  Айдишник
# Gregory - Имя
bot = telebot.TeleBot("5189417073:AAH73dnRMnHX1MTWn6zh6jJtcIRjmgmRhBI", parse_mode=None)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    list = []

    commands = ['#help', '#TechnoCom', 'IT-fest_2022', '#IASF2022', 'ФестивальОКК', '#Нейрофест', '#Невидимый мир',
                '#КонкурсНИР', '#VRARFest3D']
    if message.text == "#help":
        bot.send_message(message.from_user.id, "Вот список новостных групп: \n#TechnoCom\n#IT-fest_2022\n"
                                               "#IASF2022'\n#ФестивальОКК\n#Нейрофест\n#НевидимыйМир\n"
                                               "#КонкурсНИР\n#VRARFest3D")


    while message.text == "#TechnoCom":
        count = 2
        Tcount = count % 2
        if Tcount == 0:
            bot.send_message(message.from_user.id,
                             "\nВы подписались на рассылку этой группы")
            while Tcount == 0:
                url = 'https://vk.com/public212541280'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                quotes = soup.find_all('wall', class_="get")
                for quote in quotes:
                    if quote != 0 and quotes not in list[quote]:
                        quote.append(list)
                        bot.send_message(message.from_user.id, "Новая запись на #TechnoCom")
                    if quote == 0:
                        continue
            count += 1
        if Tcount == 1:
            bot.send_message(message.from_user.id, 'Вы отписались от рассылки этой группы')
            count += 1


    if message.text == "#IT-fest_2022":
        bot.send_message(message.from_user.id, "https://vk.com/itfest2022")
    if message.text == "#IASF2022":
        bot.send_message(message.from_user.id, 'https://vk.com/aerospaceproject')
    if message.text == '#ФестивальОКК':
        bot.send_message(message.from_user.id, 'https://vk.com/okk_fest')
    if message.text == '#Нейрофест':
        bot.send_message(message.from_user.id, 'https://vk.com/neurofest2022')
    if message.text == '#НевидимыйМир':
        bot.send_message(message.from_user.id, 'https://vk.com/nauchim.online')
    if message.text == '#КонкурсНИР':
        bot.send_message(message.from_user.id, 'https://vk.com/nauchim.online')
    if message.text == '#VRARFest3D':
        bot.send_message(message.from_user.id, 'https://vk.com/nauchim.online')
    if message.text not in commands:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши #help')


bot.polling(none_stop=True, interval=1)
global signal

""""
def scrapering():
    list = []

    url = 'https://vk.com/public212541280'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_="wall_post_text")

    for quote in quotes:
        signal = 0
        if quote != 0 and quotes not in list[quote]:
            quotes.append(list)
            signal = 1
            return signal
        if quote == 0:
            return
    return signal
"""
