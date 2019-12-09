from enum import Enum
from typing import List

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.ext import run_async

from controller.view_patterns import five_buttons_pagination_menu
from model.db_requests import get_previous_message, get_last_message, get_season_by_name, get_teams_page, \
    get_team_by_id, get_team_by_name, get_teams_in_seasons_page, get_season_team, get_seasons_with_team_page, \
    get_team_season, get_games_in_season_page, get_game_by_id, get_game_by_team_names_and_season_date
from model.db_requests import get_seasons_page, get_season_by_id
from model.models import SeasonPage, TeamsPage, GamePage
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
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   False)
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
    send_message_with_save(bot, int(current_message_id), int(chat_id), text, custom_keyboard, True)


@run_async
def seasons_with_team_navigation_button(bot: Bot, update: Update):
    query = update.callback_query
    print(query)
    message = update.effective_message
    print(message)
    chat_id = update.effective_chat['id']
    team_id = query.data.split(sep='#')[1]
    page_num = query.data.split(sep='#')[2]
    seasons_with_team_page(bot, chat_id, int(team_id), int(page_num), AnswerMode.EDIT, message)


@run_async
def season_with_team_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    team_id = query.data.split(sep='#')[1]
    season_id = query.data.split(sep='#')[2]
    season_with_team(bot, chat_id, int(season_id), int(team_id), message)


@run_async
def seasons_with_team_page(bot: Bot, chat_id: int, team_id: int, page_num: int, mode: AnswerMode,
                        message_info: dict = None):
    request_is_correct = True
    seasons_list: List[SeasonPage] = get_seasons_with_team_page(team_id, page_num, 5)
    custom_navigation_keyboard = []
    if len(seasons_list) == 0:
        request_is_correct = False
    else:
        total = seasons_list[0].total
        custom_navigation_keyboard = five_buttons_pagination_menu(total, page_num, 'sntm_pg#' + str(team_id), chat_id)
    if request_is_correct:
        custom_keyboard = [[InlineKeyboardButton(
            text=sn.season_name,
            callback_data='sntm_#' + str(sn.season_id) + "#" + str(team_id)
        )] for sn in seasons_list]
        custom_keyboard.append(custom_navigation_keyboard)
        custom_keyboard.append([InlineKeyboardButton(text="BACK", callback_data='b_')])
        if mode == AnswerMode.SEND_NEW:
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   False)
        elif mode == AnswerMode.EDIT:
            print(message_info)
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   True)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no page with this number</b>", parse_mode='HTML')


@run_async
def season_with_team(bot: Bot, chat_id: int, team_id: int, season_id: int, message_info: dict):
    found_season = get_team_season(team_id, season_id)
    current_message_id = int(message_info['message_id'])
    custom_keyboard = [[InlineKeyboardButton(text="BACK", callback_data='b_')]]
    if found_season is None:
        text = "<b>There are problems with team and/or season indexes</b>"
    else:
        text = found_season.fake_str()
    send_message_with_save(bot, int(current_message_id), int(chat_id), text, custom_keyboard, True)


@run_async
def teams(bot: Bot, update: Update):
    teams_page(bot, update.effective_message.chat.id, 1, AnswerMode.SEND_NEW, update.effective_message)


@run_async
def teams_navigation_button(bot: Bot, update: Update):
    query = update.callback_query
    print(query)
    message = update.effective_message
    chat_id = update.effective_chat['id']
    page_num = query.data.split(sep='#')[1]
    teams_page(bot, chat_id, int(page_num), AnswerMode.EDIT, message)


@run_async
def teams_page(bot: Bot, chat_id: int, page_num: int, mode: AnswerMode, message_info: dict = None):
    request_is_correct = True
    teams_list: List[TeamsPage] = get_teams_page(page_num, 5)
    custom_navigation_keyboard = []
    if len(teams_list) == 0:
        request_is_correct = False
    else:
        total = teams_list[0].total
        custom_navigation_keyboard = five_buttons_pagination_menu(total, page_num, 'tm_pg', chat_id)
    if request_is_correct:
        custom_keyboard = [[InlineKeyboardButton(
            text=tm.team_name + " (" + tm.abbreviation + ")",
            callback_data='tm_#' + str(tm.team_id)
        )] for tm in teams_list]
        custom_keyboard.append(custom_navigation_keyboard)
        if mode == AnswerMode.SEND_NEW:
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   False)
        elif mode == AnswerMode.EDIT:
            print(message_info)
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   True)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no page with this number</b>", parse_mode='HTML')


@run_async
def team_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    team_id = query.data.split(sep='#')[1]
    team(bot, chat_id, team_id, message)


@run_async
def team(bot: Bot, chat_id: int, team_id: int, message_info: dict):
    found_team = get_team_by_id(team_id)
    current_message_id = int(message_info['message_id'])
    custom_keyboard = [[InlineKeyboardButton(text="BACK", callback_data='b_')]]
    if found_team is None:
        text = "<b>There is no team with this index</b>"
    else:
        text = str(found_team)
    send_message_with_save(bot, int(current_message_id), int(chat_id), text, custom_keyboard, True)


@run_async
def team_in_season(bot: Bot, chat_id: int, team_id: int, season_id: int, message_info: dict):
    found_team = get_season_team(team_id, season_id)
    current_message_id = int(message_info['message_id'])
    custom_keyboard = [[InlineKeyboardButton(text="BACK", callback_data='b_')]]
    if found_team is None:
        text = "<b>There are problems with team and/or season indexes</b>"
    else:
        text = found_team.fake_str()
    send_message_with_save(bot, int(current_message_id), int(chat_id), text, custom_keyboard, True)


@run_async
def teams_in_season_navigation_button(bot: Bot, update: Update):
    query = update.callback_query
    print(query)
    message = update.effective_message
    print(message)
    chat_id = update.effective_chat['id']
    season_id = query.data.split(sep='#')[1]
    page_num = query.data.split(sep='#')[2]
    team_in_season_page(bot, chat_id, int(season_id), int(page_num), AnswerMode.EDIT, message)


@run_async
def team_in_season_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    season_id = query.data.split(sep='#')[1]
    team_id = query.data.split(sep='#')[2]
    team_in_season(bot, chat_id, int(season_id), int(team_id), message)


@run_async
def team_in_season_page(bot: Bot, chat_id: int, season_id: int, page_num: int, mode: AnswerMode,
                        message_info: dict = None):
    request_is_correct = True
    teams_list: List[TeamsPage] = get_teams_in_seasons_page(season_id, page_num, 5)
    custom_navigation_keyboard = []
    if len(teams_list) == 0:
        request_is_correct = False
    else:
        total = teams_list[0].total
        custom_navigation_keyboard = five_buttons_pagination_menu(total, page_num, 'tmsn_pg#' + str(season_id), chat_id)
    if request_is_correct:
        custom_keyboard = [[InlineKeyboardButton(
            text=tm.team_name + " (" + tm.abbreviation + ")",
            callback_data='tmsn_#' + str(tm.team_id) + "#" + str(season_id)
        )] for tm in teams_list]
        custom_keyboard.append(custom_navigation_keyboard)
        custom_keyboard.append([InlineKeyboardButton(text="BACK", callback_data='b_')])
        if mode == AnswerMode.SEND_NEW:
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   False)
        elif mode == AnswerMode.EDIT:
            print(message_info)
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   True)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no page with this number</b>", parse_mode='HTML')


@run_async
def games_in_season_navigation_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    season_id = query.data.split(sep='#')[1]
    page_num = query.data.split(sep='#')[2]
    games_in_season_page(bot, chat_id, int(season_id), int(page_num), AnswerMode.EDIT, message)


@run_async
def games_in_season_page(bot: Bot, chat_id: int, season_id: int, page_num: int, mode: AnswerMode,
                        message_info: dict = None):
    request_is_correct = True
    games_list: List[GamePage] = get_games_in_season_page(season_id, page_num, 5)
    custom_navigation_keyboard = []
    if len(games_list) == 0:
        request_is_correct = False
    else:
        total = games_list[0].total
        custom_navigation_keyboard = five_buttons_pagination_menu(total, page_num, 'gmsn_pg#' + str(season_id), chat_id)
    if request_is_correct:
        custom_keyboard = [[InlineKeyboardButton(
            text=gm.home_abbreviation + " vs " + gm.away_abbreviation + " on " + gm.game_date,
            callback_data='gmsn_#' + str(gm.game_id)
        )] for gm in games_list]
        custom_keyboard.append(custom_navigation_keyboard)
        custom_keyboard.append([InlineKeyboardButton(text="BACK", callback_data='b_')])
        if mode == AnswerMode.SEND_NEW:
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   False)
        elif mode == AnswerMode.EDIT:
            print(message_info)
            send_message_with_save(bot, message_info['message_id'], chat_id, invisible_character(), custom_keyboard,
                                   True)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no page with this number</b>", parse_mode='HTML')


@run_async
def game_in_season_button(bot: Bot, update: Update):
    query = update.callback_query
    message = update.effective_message
    chat_id = update.effective_chat['id']
    game_id = query.data.split(sep='#')[1]
    game_in_season(bot, chat_id, int(game_id), message.__dict__)


@run_async
def game_in_season(bot: Bot, chat_id: int, game_id: int, message_info: dict):
    found_game = get_game_by_id(game_id)
    current_message_id = int(message_info['message_id'])
    custom_keyboard = [[InlineKeyboardButton(text="BACK", callback_data='b_')]]
    if found_game is None:
        text = "<b>There is no game with such index</b>"
    else:
        text = str(found_game)
    send_message_with_save(bot, int(current_message_id), int(chat_id), text, custom_keyboard, True)


@run_async
def season_with_team_link(bot: Bot, update: Update):
    chat_id = update.message.chat.id
    message = get_last_message(chat_id)
    message_parts = str(message.text).split('\n')
    if len(message_parts) >= 3 and message_parts[3] == 'Seasons, where team was participating: /sns':
        team_name = message_parts[0].split('</b>')[0][3:]
        team = get_team_by_name(team_name)
        seasons_with_team_page(bot, chat_id, int(team.team_id), 1, AnswerMode.EDIT, message.__dict__)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no season link in previous message</b>", parse_mode='HTML')

@run_async
def teams_in_season_link(bot: Bot, update: Update):
    chat_id = update.message.chat.id
    message = get_last_message(chat_id)
    message_parts = str(message.text).split('\n')
    if len(message_parts) >= 2 and message_parts[2] == 'Teams in season: /tms':
        season_name = message_parts[0][3:-4]
        season = get_season_by_name(season_name)
        team_in_season_page(bot, chat_id, int(season.season_id), 1, AnswerMode.EDIT, message.__dict__)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no teams link in previous message</b>", parse_mode='HTML')

@run_async
def games_in_season_link(bot: Bot, update: Update):
    chat_id = update.message.chat.id
    message = get_last_message(chat_id)
    message_parts = str(message.text).split('\n')
    if len(message_parts) >= 3 and message_parts[3] == 'Games in season: /gms':
        season_name = message_parts[0][3:-4]
        season = get_season_by_name(season_name)
        games_in_season_page(bot, chat_id, season.season_id, 1, AnswerMode.EDIT, message.__dict__)
    else:
        bot.send_message(chat_id=chat_id, text="<b>There is no games link in previous message</b>", parse_mode='HTML')

@run_async
def go_to_origin(bot: Bot, update: Update):
    chat_id = update.message.chat.id
    message = get_last_message(chat_id)
    custom_keyboard = inline_keyboard_from_buttons_lists(message.buttons_names, message.buttons_callbacks)
    message_parts = str(message.text).split('\n')
    if len(message_parts) >= 2:
        if message_parts[2] == 'Go to team\'s page: /origin':
            team_name = str(message.text).split('</b>')[0][3:]
            team(bot, chat_id, get_team_by_name(team_name).team_id, message.__dict__)
        if message_parts[2] == 'Go to season\'s page: /origin':
            season_name = message_parts[0].split('\n')[0][3:-4]
            season(bot, chat_id, get_season_by_name(season_name).season_id, message.__dict__)
    else:
        send_message_with_save(bot, message.message_id, chat_id, '<b>There is no links to entities\' origin in previous message</b>',
                               custom_keyboard, False, False)


@run_async
def popup_statistics(bot: Bot, update: Update):
    chat_id = update.message.chat.id
    # users_message_id = update.message.message_id
    # bot.delete_message(chat_id, users_message_id)
    message = get_last_message(chat_id)
    custom_keyboard = inline_keyboard_from_buttons_lists(message.buttons_names, message.buttons_callbacks)
    new_text = ""
    message_parts = str(message.text).split('---')
    if len(message_parts) > 1:
        # part for seasons
        if message_parts[1].find('Show season statistics') != -1:
            season_name = message_parts[0].split('\n')[0][3:-4]
            season = get_season_by_name(season_name)
            new_text = message_parts[0] + '---\nRemove season statistics: /stat\n' + str(season.statistics)
        elif message_parts[1].find('Remove season statistics') != -1:
            new_text = message_parts[0] + '---\nShow season statistics: /stat\n'
        elif message_parts[1].find('Show team statistics') != -1:
            team_name = message_parts[0].split('</b>')[0][3:]
            team = get_team_by_name(team_name)
            new_text = message_parts[0] + '---\nRemove team statistics: /stat\n' + str(team.statistics)
        elif message_parts[1].find('Remove team statistics') != -1:
            new_text = message_parts[0] + '---\nShow team statistics: /stat\n'
        elif message_parts[1].find('Show game statistics') != -1:
            home_team = message_parts[0].split('\n')[0].split('</b> vs <b>')[0][3:]
            away_team = message_parts[0].split('\n')[0].split('</b> vs <b>')[1][:-4]
            date = message_parts[0].split('\n')[2].split('</i>')[0].split('<i>')[1]
            season_name = message_parts[0].split('\n')[2].split('<i>')[2][:-4]
            game = get_game_by_team_names_and_season_date(home_team, away_team, date, season_name)
            new_text = message_parts[0] + '---\nRemove game statistics: /stat\n' + str(game.statistics)
        elif message_parts[1].find('Remove game statistics') != -1:
            new_text = message_parts[0] + '---\nShow game statistics: /stat\n'
        send_message_with_save(bot, message.message_id, chat_id, new_text, custom_keyboard, True, False)
    else:
        send_message_with_save(bot, message.message_id, chat_id, '<b>There is no statistics in previous message</b>',
                               custom_keyboard, False, False)


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
