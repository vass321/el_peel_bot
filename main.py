import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from time import sleep
URL = "https://muzland.ru/search.html?query=кишлак"
page = requests.get(URL)
print(soup)
soup = BeautifulSoup(page.content, "html.parser")

bot = telebot.TeleBot("7123878509:AAHHK1E0f2L-_O26ecRoptHv-brtJi8_x74")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔎Искать аккорды")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🔎Искать аккорды"):
        bot.send_message(message.chat.id, text="Напиши имя исполнителя\n*Пример: face*", parse_mode= "Markdown")
        bot.register_next_step_handler(message, input_promocod)

def input_promocod(message):
        sleep(5)
        input_el = driver.find_element(By.TAG_NAME, 'input')
        input_el.send_keys(message.text)
        input_el.send_keys(Keys.ENTER)
        sleep(3)

        bot.send_message(message.chat.id, text="Напиши название песни")
        bot.register_next_step_handler(message, inputvass)
def inputvass(message):

        element.click()
        sleep(3)
        bot.send_message(message.chat.id, element2.text)



bot.infinity_polling()