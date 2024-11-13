from anketa import (anketa_start, anketa_name, anketa_raiting, anketa_comment, 
                    anketa_skip, anketa_dontnow)
import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from handlers import (greet_user, guess_number, send_cat_pic, user_coords, 
                      talk_to_me, check_user_photo)


import settings


logging.basicConfig(filename='bot_log.log', level=logging.INFO)

def main():
    my_bot = Updater(settings.API_KEY, use_context=True) # создал бота

    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Заполнить анкету)$'), anketa_start)
        ],
        states={
            'name': [MessageHandler(Filters.text, anketa_name)],
            'raiting': [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), anketa_raiting)],
            'comment': [
                CommandHandler('skip', anketa_skip),
                MessageHandler(Filters.text, anketa_comment)
            ]
        },
        fallbacks=[
            MessageHandler(Filters.text, Filters.audio, Filters.video, Filters.document, Filters.location, anketa_dontnow)
        ]
    )

    disp = my_bot.dispatcher
    disp.add_handler(anketa)
    disp.add_handler(CommandHandler('Start', greet_user))
    disp.add_handler(CommandHandler('guess', guess_number))
    disp.add_handler(CommandHandler('get_photo', send_cat_pic))
    disp.add_handler(MessageHandler(Filters.regex('^(Прислать котьку)$'), send_cat_pic))
    disp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    disp.add_handler(MessageHandler(Filters.location, user_coords))
    disp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot is starting')
    my_bot.start_polling()  # n раз в секунду делает запрос у сервера
    my_bot.idle()          # крутит бота

    return 0


if __name__ == '__main__':
    main()
    
    