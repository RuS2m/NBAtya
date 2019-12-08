import re
from typing import List

from telegram import InlineKeyboardButton

"""
* Pagination block *
"""

"""
This function provides type of pagination with 5 buttons:
- 1st or current -10
- previous
- current
- next
- last or current +10

You must pass such parameters as chat_id or callback_pattern for naming callback_function,
which will be refered each button

Actually it works only for lists, contains at least 4 pages of elements,
otherwise it will not work
"""
def five_buttons_pagination_menu(total: int, page_num: int, callback_pattern: str, chat_id: int) \
        -> List[InlineKeyboardButton]:
    custom_navigation_keyboard = []
    if page_num == 1:
        custom_navigation_keyboard.append('·1·')
        custom_navigation_keyboard.append('2›')
        custom_navigation_keyboard.append('3»')
        custom_navigation_keyboard.append(str(total) + '»')
    elif page_num == 2:
        custom_navigation_keyboard.append('‹1')
        custom_navigation_keyboard.append('·2·')
        custom_navigation_keyboard.append('3›')
        custom_navigation_keyboard.append(str(total) + '»')
    elif page_num == total - 1:
        custom_navigation_keyboard.append('«1')
        custom_navigation_keyboard.append('‹' + str(page_num - 1))
        custom_navigation_keyboard.append('·' + str(page_num) + '·')
        custom_navigation_keyboard.append(str(page_num + 1) + '›')
    elif page_num == total:
        custom_navigation_keyboard.append('«1')
        custom_navigation_keyboard.append('«' + str(page_num - 2))
        custom_navigation_keyboard.append('‹' + str(page_num - 1))
        custom_navigation_keyboard.append('·' + str(page_num) + '·')
    elif total > page_num > 1:
        max_prev_number = page_num - 10 if page_num - 10 > 0 else 1
        max_next_number = page_num + 10 if page_num + 10 < total else total
        custom_navigation_keyboard.append('«' + str(max_prev_number))
        custom_navigation_keyboard.append('‹' + str(page_num - 1))
        custom_navigation_keyboard.append('·' + str(page_num) + '·')
        custom_navigation_keyboard.append(str(page_num + 1) + '›')
        custom_navigation_keyboard.append(str(max_next_number) + '»')
    return [InlineKeyboardButton(
        text=s,
        callback_data=callback_pattern + '#' + re.search(r'\d+', str(s)).group()
    ) for s in custom_navigation_keyboard]

"""
This function provides type of pagination with 2 buttons:
- previous
- next

You must pass such parameters as chat_id or callback_pattern for naming callback_function,
which will be referred each button
"""
def two_buttons_pagination_menu(total: int, page_num: int, callback_pattern: str, chat_id: int) \
        -> List[InlineKeyboardButton]:
    custom_navigation_keyboard = []
    if page_num == 1:
        custom_navigation_keyboard.append('›')
    elif page_num == total:
        custom_navigation_keyboard.append('‹')
    else:
        custom_navigation_keyboard.append('‹')
        custom_navigation_keyboard.append('›')
    return [InlineKeyboardButton(
        text=s,
        callback_data=callback_pattern + '#' + str(page_num + 1 if (s == '›') else page_num - 1) + "#chat_id_#" + str(
            chat_id)
    ) for s in custom_navigation_keyboard]
