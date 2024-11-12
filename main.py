import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, guess_number, send_cat_pic, user_coords, 
                      talk_to_me)

import settings

logging.basicConfig(filename='bot_log.log', level=logging.INFO)

def main():
    my_bot = Updater(settings.API_KEY, use_context=True) # создал бота

    disp = my_bot.dispatcher
    disp.add_handler(CommandHandler('Start', greet_user))
    disp.add_handler(CommandHandler('guess', guess_number))
    disp.add_handler(CommandHandler('get_photo', send_cat_pic))
    disp.add_handler(MessageHandler(Filters.regex('(Прислать котьку)$'), send_cat_pic))
    disp.add_handler(MessageHandler(Filters.location, user_coords))
    disp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot is starting')
    my_bot.start_polling()  # n раз в секунду запрашивает у сервера запросы
    my_bot.idle()          # крутит бола

    return 0


if __name__ == '__main__':
    main()
    
    