from emoji import emojize
from glob import glob
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings


logging.basicConfig(filename='bot_log.log', level=logging.INFO)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        smile = emojize(smile, use_aliases=True)
        return smile
    
    return user_data['emoji']


def greet_user(update, context):
    print(update['message']['chat'])
        
    context.user_data['emoji'] = get_smile(context.user_data)
    emoji = context.user_data['emoji'] # какая то бага если напрямую в ф строку поодставить
    update.message.reply_text(f'Привет\nЯ умею играть - /guess\nА ещё я знаю что тебе понравится{emoji} - /get_photo')


def talk_to_me(update, context):
    text = update.message.text
    smile = get_smile(context.user_data)
    print(text, update['message']['chat'])
    update.message.reply_text(f"{text}{context.user_data['emoji']}")
    

def play_random_numbers(user_num):
    bot_num = randint(user_num - 10, user_num + 10)
    print('Играет')
    if user_num > bot_num:
        message = f'Твоя: {user_num}, моя: {bot_num} - ты выйграть'
    elif user_num < bot_num:
        message = f'Твоя: {user_num}, моя: {bot_num} - ты проиграть'
    else:
        message = f'Твоя: {user_num}, моя: {bot_num} - я не знать'
    return message


def guess_number(update, context):
    if context.args:
        try:
            user_num = int(context.args[0])
            message = play_random_numbers(user_num)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    
    update.message.reply_text(message)


def send_cat_pic(update, context):
    cat_list = glob('images/named_img/*')
    cat_pic_name = choice(cat_list)
    chat_id = update.effective_chat.id
    print('кот', update)
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_name, 'rb'))


def main():
    my_bot = Updater(settings.API_KEY, use_context=True) # создал бота

    disp = my_bot.dispatcher
    disp.add_handler(CommandHandler('Start', greet_user))
    disp.add_handler(CommandHandler('guess', guess_number))
    disp.add_handler(CommandHandler('get_photo', send_cat_pic))
    disp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot is starting')
    my_bot.start_polling()  # n раз в секунду запрашивает у сервера запросы
    my_bot.idle()          # крутит бола

    return 0


if __name__ == '__main__':
    main()
    
    