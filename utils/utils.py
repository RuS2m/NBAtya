import logging
from typing import Tuple, List

from telegram import InlineKeyboardButton, Bot, InlineKeyboardMarkup

from model.db_requests import put_message
from model.models import Message

"""
This symbol does not displays in telegram, but also does not considered empty,
so it can be passed as message
"""
def invisible_character() -> str:
    return u'\u2061'


def get_logger():
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    return logger


"""
Parse list of lists buttons to list of buttons texts and list of buttons callbacks
"""
def parse_inline_keyboard(custom_keyboard: List[List[InlineKeyboardButton]]) -> Tuple[List[List[str]], List[List[str]]]:
    buttons_texts = [[button.text for button in buttons_list] for buttons_list in custom_keyboard]
    buttons_callbacks = [[button.callback_data for button in buttons_list] for buttons_list in custom_keyboard]
    print(buttons_texts)
    print(buttons_callbacks)
    return buttons_texts, buttons_callbacks


"""
Build inline keyboard from list of buttons texts and buttons callbacks
"""
def inline_keyboard_from_buttons_lists(buttons_texts: List[List[str]], buttons_callbacks: List[List[str]]) -> List[
    List[InlineKeyboardButton]]:
    return [[InlineKeyboardButton(text, callback_data=callback) for text, callback in zip(texts, callbacks)]
            for texts, callbacks in zip(buttons_texts, buttons_callbacks)]


"""
send message with save it to database
"""
def send_message_with_save(bot: Bot, message_id: int, chat_id: int, text: str,
                           custom_keyboard: List[List[InlineKeyboardButton]], edit_mode: bool, is_available: bool = True):
    buttons_texts, buttons_callbacks = parse_inline_keyboard(custom_keyboard)
    print(Message(message_id, 0, chat_id, text, buttons_texts, buttons_callbacks, is_available))
    put_message(Message(message_id, 0, chat_id, text, buttons_texts, buttons_callbacks, is_available))
    if edit_mode is False:
        bot.send_message(text=text, message_id=message_id, chat_id=chat_id, parse_mode='HTML',
                         disable_web_page_preview=True, disable_notification=True,
                         reply_markup=InlineKeyboardMarkup(custom_keyboard))
    else:
        bot.edit_message_text(text=text, message_id=message_id, chat_id=chat_id, parse_mode='HTML',
                              reply_markup=InlineKeyboardMarkup(custom_keyboard))
