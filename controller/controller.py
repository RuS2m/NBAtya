import ast
from enum import Enum
from typing import List

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.ext import run_async

from controller.patterns import five_buttons_pagination_menu
from model.dao import get_previous_message
from model.dao import get_seasons_page, get_season_by_id
from model.models import SeasonPage
from utils.utils import get_logger, invisible_character, send_message_with_save, inline_keyboard_from_buttons_lists

logger = get_logger()


class AnswerMode(Enum):
    EDIT = 1,
    SEND_NEW = 2


@run_async
def start(bot: Bot, update: Update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=chat_id, text='Start!')


@run_async
def seasons(bot: Bot, update: Update):
    seasons_page(bot, update.effective_message.chat.id, 1, AnswerMode.SEND_NEW, update.effective_message)


@run_async
def seasons_navigation_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    page_num = query.data.split(sep='#')[1]
    seasons_page(bot, chat_id, int(page_num), AnswerMode.EDIT, message)


@run_async
def seasons_page(bot: Bot, chat_id: int, page_num: int, mode: AnswerMode, message_info: dict = None):
    request_is_correct = True
    seasons_list: List[SeasonPage] = get_seasons_page(page_num, 5)
    custom_navigation_keyboard = []
    if len(seasons_list) == 0:
        request_is_correct = False
    else:
        total = seasons_list[0].total
        custom_navigation_keyboard = five_buttons_pagination_menu(total, page_num, 'sn_pg', chat_id)
    if request_is_correct:
        custom_keyboard = [[InlineKeyboardButton(
            text=sn.season_name,
            callback_data='sn_#' + str(sn.season_id)
        )] for sn in seasons_list]
        custom_keyboard.append(custom_navigation_keyboard)
        if mode == AnswerMode.SEND_NEW:
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard, False)
        elif mode == AnswerMode.EDIT:
            print(message_info)
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   True)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no page with this number</b>", parse_mode='HTML')


@run_async
def season_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    season_id = query.data.split(sep='#')[1]
    season(bot, chat_id, season_id, message)


@run_async
def season(bot: Bot, chat_id: int, season_id: int, message_info: dict):
    found_season = get_season_by_id(season_id)
    current_message_id = int(message_info['message_id'])
    custom_keyboard = [[InlineKeyboardButton(text="BACK", callback_data='b_')]]
    if found_season is None:
        text = "<b>There is no season with this index</b>"
    else:
        text = str(found_season)
    send_message_with_save(bot, int(current_message_id), int(chat_id), text, custom_keyboard,True)


@run_async
def back_button(bot: Bot, update: Update):
    message_id = update.effective_message.message_id
    chat_id = update.effective_message.chat.id
    message = get_previous_message(int(chat_id), int(message_id))
    text = message.text
    custom_keyboard = inline_keyboard_from_buttons_lists(message.buttons_names, message.buttons_callbacks)
    bot.edit_message_text(text=text, message_id=message_id, chat_id=chat_id, parse_mode='HTML',
                          reply_markup=InlineKeyboardMarkup(custom_keyboard))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
