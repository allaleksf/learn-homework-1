"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    text_an=govor(user_text)
    print(text_an)
    update.message.reply_text(text_an)

def govor(text):
    return "Привет"

def planet_ans(update, context):
    text = update.message.text
    ans = (text.split(' ', 2))

    today = str(date.today())
    today = datetime.strptime(str(date.today()), "%Y-%m-%d").strftime('%Y/%m/%d')


    if ans[1] == "Mars":
        planet = ephem.Mars(today)
        constellation = str(ephem.constellation(planet))
        ans = (ans[1]+"//"+constellation)
        print(ans)
        update.message.reply_text(ans)
    else:
        print(ans[1])
        update.message.reply_text(ans[1])

def main():
    mybot = Updater("1802019533:AAGh0ynWygrbHOIT16ihqgMWVUR0sa1GnR8",  use_context=True) #request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_ans))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
