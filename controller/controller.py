from enum import Enum
from typing import List

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.ext import run_async

from controller.patterns import five_buttons_pagination_menu, two_buttons_pagination_menu
from model.dao import get_seasons_page, get_season_by_id
from model.models import SeasonPage
from utils.utils import get_logger, invisible_character

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
    seasons_page(bot, update.message.chat.id, 1, AnswerMode.SEND_NEW)


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
            bot.send_message(chat_id=chat_id, text=invisible_character(),
                             reply_markup=InlineKeyboardMarkup(custom_keyboard),
                             parse_mode='HTML')
        elif mode == AnswerMode.EDIT:
            bot.edit_message_text(text=invisible_character(), message_id=int(message_info['message_id']),
                                  chat_id=chat_id, parse_mode='HTML',
                                  reply_markup=InlineKeyboardMarkup(custom_keyboard))
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
    current_message_id = 1  # FIXME: add caching logic for `BACK` procedure
    custom_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(
        text="BACK", callback_data='b_#' + str(current_message_id))]])
    if found_season is None:
        bot.edit_message_text(text="<b>There is no season with this index</b>",
                              message_id=int(message_info['message_id']), chat_id=chat_id,
                              parse_mode='HTML', reply_markup=custom_keyboard, disable_web_page_preview=True)
    else:
        bot.edit_message_text(text=str(found_season), message_id=int(message_info['message_id']), chat_id=chat_id,
                              parse_mode='HTML', reply_markup=custom_keyboard, disable_web_page_preview=True)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
