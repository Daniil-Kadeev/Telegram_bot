import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings


logging.basicConfig(filename='bot_log', level=logging.INFO)


def greet_user(update, context):
    print('Вызвал старт')
    print(update)
    update.message.reply_text('Привет')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
    


def main():
    my_bot = Updater(settings.API_KEY, use_context=True) # создал бота

    disp = my_bot.dispatcher
    disp.add_handler(CommandHandler('Start', greet_user))
    disp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot is starting')
    my_bot.start_polling()  # n раз в секунду запрашивает у сервера запросы
    my_bot.idle()          # крутит бола

    return 0


if __name__ == '__main__':
    print(main())