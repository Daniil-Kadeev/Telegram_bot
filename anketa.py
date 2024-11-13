from utils import get_keyboard
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode

def anketa_start(update, context):
    update.message.reply_text(
        'Как тебя зовут?',
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"


def anketa_name(update, context):
    username = update.message.text
    if len(username.split()) != 2:
        update.message.reply_text('Пожалуйста, введите имя и фамилию')
        return 'name'
    else:
        context.user_data['anketa'] = {'name': username}
        reply_keyboard = [['1', '2', '3', '4', '5']]
        update.message.reply_text(
            'Пожалуйста, оцените бота от 1 до 5',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            )
        return 'raiting'
    

def anketa_raiting(update, context):
    context.user_data['anketa']['raiting'] = int(update.message.text)
    update.message.reply_text('Напишите коментарий и пожелаия по улучшению бота.\nНажмите /skip чтобы пропустить')

    return 'comment'


def anketa_skip(update, context):
    user_text = formatt_anketa(context)
    update.message.reply_text(user_text, 
                              parse_mode=ParseMode.HTML,
                              reply_markup=get_keyboard())
    return ConversationHandler.END


def anketa_comment(update, context):
    context.user_data['anketa']['comment'] = update.message.text
    user_text = formatt_anketa(context)
    update.message.reply_text(user_text, 
                              reply_markup=get_keyboard(),
                              parse_mode=ParseMode.HTML
                              )
    return ConversationHandler.END


def formatt_anketa(context):
    user_text = f"""<b>Имя, фамилия</b>: {context.user_data['anketa']['name']}
<b>Оценка</b>: {context.user_data['anketa']['raiting']}
"""
    if 'comment' in context.user_data['anketa']:
        comment = context.user_data['anketa']['comment']
        user_text += f'<b>Комментарий</b>: {comment}'
    else:
        context.user_data['anketa']['comment'] = None
    return user_text


def anketa_dontnow(update, context):
    update.message.reply_text('Я вас не понял, попробуйте ещё раз')