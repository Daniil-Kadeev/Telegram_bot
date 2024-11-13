from glob import glob
import os
from random import choice
from utils import get_smile, play_random_numbers, print_active, get_keyboard


def greet_user(update, context):
    print_active('Старт', update)
    
    context.user_data['emoji'] = get_smile(context.user_data)
    smile = context.user_data['emoji'] # какая то бага если напрямую в ф строку поодставить

    update.message.reply_text(
        f'Привет\nЯ умею играть - /guess\nА ещё я знаю что тебе понравится{smile} - /get_photo',
        reply_markup=get_keyboard()
        )


def talk_to_me(update, context):
    text = update.message.text
    context.user_data['emoji'] = get_smile(context.user_data)
    smile = context.user_data['emoji']
    print_active(text, update)
    update.message.reply_text(
        f"{text}{smile}",
        reply_markup=get_keyboard()
        )
    

def guess_number(update, context):
    print_active('Играет', update)
    if context.args:
        try:
            user_num = int(context.args[0])
            message = play_random_numbers(user_num)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    
    update.message.reply_text(
        message,
        reply_markup=get_keyboard()
        )
    

def send_cat_pic(update, context):
    cat_list = glob('images/named_img/*')
    cat_pic_name = choice(cat_list)
    chat_id = update.effective_chat.id
    print_active('Котька', update)
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_name, 'rb'))


def user_coords(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    smile = context.user_data['emoji']
    coords = update.message.location
    update.message.reply_text(
        f'Ваши координаты {coords}{smile}',
        reply_markup=get_keyboard()
    )


def check_user_photo(update, context):
    update.message.reply_text('Загружаю фото')
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{update.message.photo[-1].file_id}.jpg')
    photo_file.download(file_name)
    update.message.reply_text('Файл сохранён')