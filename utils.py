from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def print_active(active, upload):
    print(active, upload['message']['chat'])


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        smile = emojize(smile, use_aliases=True)
        return smile
    
    return user_data['emoji']


def get_keyboard():
    return ReplyKeyboardMarkup([['Прислать котьку'],
                                [KeyboardButton('Мои координаты', request_location=True)],
                                ['Заполнить анкету']])


def play_random_numbers(user_num):
    bot_num = randint(user_num - 10, user_num + 10)
    if user_num > bot_num:
        message = f'Твоя: {user_num}, моя: {bot_num} - ты выйграть'
    elif user_num < bot_num:
        message = f'Твоя: {user_num}, моя: {bot_num} - ты проиграть'
    else:
        message = f'Твоя: {user_num}, моя: {bot_num} - я не знать'
    return message
