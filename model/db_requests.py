from typing import List

from sqlalchemy.orm import Session

from database_connect import engine
from model.models import SeasonPage, Season, Message

"""
* Seasons block *
"""

"""
Request to get number of all seasons in `seasons` table
"""
def get_seasons_num() -> int:
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(*) FROM seasons"
    )
    session.commit()
    session.close()
    return rs.first()[0]


"""
Request to get a single seasons page from `seasons` table
"""
def get_seasons_page(page: int, per_page: int) -> List[SeasonPage]:
    session = Session(engine)
    offset = 0
    if page != 1:
        offset = (page - 1) * per_page
    answer = []
    total = int(int(get_seasons_num()) / per_page) + int(int(get_seasons_num()) % per_page)
    if page > total:
        return answer
    rs = session.execute(
        "SELECT season_id, season_name, season_type, season_year FROM seasons ORDER BY season_name "
        "LIMIT :per_page OFFSET :offset", {"per_page": per_page, "offset": offset})
    for row in rs:
        answer.append(SeasonPage(row[0], row[1], row[2], row[3], page, total))
    session.commit()
    session.close()
    return answer


"""
Request to get season by id
"""
def get_season_by_id(season_id: int) -> Season:
    session = Session(engine)
    rs = session.execute(
        "SELECT season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, "
        "fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts "
        "FROM seasons WHERE season_id = :session_id",
        {"session_id": season_id})

    for row in rs:
        season_name = row[1]
        season_type = row[2]
        season_year = row[3]
        min = row[4]
        fgm = row[5]
        fga = row[6]
        fg_pct = row[7]
        fg3m = row[8]
        fg3a = row[9]
        fg3_pct = row[10]
        ftm = row[11]
        fta = row[12]
        ft_pct = row[13]
        oreb = row[14]
        dreb = row[15]
        reb = row[16]
        ast = row[17]
        stl = row[18]
        blk = row[19]
        tov = row[20]
        pf = row[21]
        pts = row[22]
        session.commit()
        session.close()
        return Season(season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm,
                      fta, ft_pct,
                      oreb, dreb, reb, ast, stl, blk, tov, pf, pts)


def get_season_by_name(season_name: str) -> Season:
    session = Session(engine)
    rs = session.execute(
        "SELECT season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, "
        "fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts "
        "FROM seasons WHERE season_name = :season_name",
        {"season_name": season_name})

    for row in rs:
        season_id = row[0]
        season_type = row[2]
        season_year = row[3]
        min = row[4]
        fgm = row[5]
        fga = row[6]
        fg_pct = row[7]
        fg3m = row[8]
        fg3a = row[9]
        fg3_pct = row[10]
        ftm = row[11]
        fta = row[12]
        ft_pct = row[13]
        oreb = row[14]
        dreb = row[15]
        reb = row[16]
        ast = row[17]
        stl = row[18]
        blk = row[19]
        tov = row[20]
        pf = row[21]
        pts = row[22]
        session.commit()
        session.close()
        return Season(season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm,
                      fta, ft_pct,
                      oreb, dreb, reb, ast, stl, blk, tov, pf, pts)

"""
* Players block *
"""

"""
Request to get number of all players in `players` table
"""
def get_players_num():
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(*) FROM players"
    )
    session.commit()
    session.close()
    return rs.first()[0]


"""
* Messages block *
"""

"""
Request to get previous message from `messages` table:

It scans all messages in current chat(which is specified with `chat_id`), orders it by date, they were added
and looks for last `message_id`, except for current, and rebuilds it's message from row
"""
def get_previous_message(chat_id: int, message_id: int) -> Message:
    session = Session(engine)
    rs = session.execute(
        "SELECT message_id, message_version, chat_id, text, buttons_names, buttons_callbacks, is_available "
        "FROM messages WHERE chat_id = :chat_id AND is_available = TRUE "
        "AND date_time < "
        "(SELECT date_time FROM messages WHERE message_id = :message_id AND chat_id = :chat_id AND is_available = TRUE ORDER BY date_time DESC LIMIT 1) "
        "ORDER BY date_time "
        "DESC LIMIT 1",
        {"message_id": message_id, "chat_id": chat_id})
    for row in rs:
        new_message_id = int(row[0])
        message_version = int(row[1])
        chat_id = int(row[2])
        text = row[3]
        buttons_names = row[4]
        buttons_callbacks = row[5]
        session.execute(
            "DELETE FROM messages WHERE message_id = :message_id AND chat_id = :chat_id AND is_available = TRUE "
            "AND date_time = "
            "(SELECT date_time FROM messages WHERE message_id = :message_id AND chat_id = :chat_id AND is_available = TRUE ORDER BY date_time DESC LIMIT 1)",
            {"message_id": message_id, "chat_id": chat_id})
        session.commit()
        session.close()
        return Message(new_message_id, message_version, chat_id, text, from_str(buttons_names), from_str(buttons_callbacks), True)

def get_last_message(chat_id: int) -> Message:
    session = Session(engine)
    rs = session.execute(
        "SELECT message_id, message_version, chat_id, text, buttons_names, buttons_callbacks, is_available "
        "FROM messages WHERE chat_id = :chat_id "
        "ORDER BY date_time DESC "
        "LIMIT 1",
        {"chat_id": chat_id})
    for row in rs:
        message_id = int(row[0])
        message_version = int(row[1])
        chat_id = int(row[2])
        text = row[3]
        buttons_names = row[4]
        buttons_callbacks = row[5]
        is_available = row[6]
        session.commit()
        session.close()
        return Message(message_id, message_version, chat_id, text, from_str(buttons_names), from_str(buttons_callbacks), is_available)


"""
Request to put new message into `messages` table:

It scans all messages in current chat, orders it by date, they were added
and looks for last `message_id`, except for current, adding also simple logic to get new message's version
"""
def put_message(message: Message) -> None:
    session = Session(engine)
    session.execute(
        "INSERT INTO messages(message_id, message_version, chat_id, text, buttons_names, buttons_callbacks, date_time, is_available) "
        "SELECT :message_id, (CASE "
        "WHEN (SELECT message_version FROM messages WHERE message_id = :message_id AND chat_id = :chat_id LIMIT 1) IS NULL THEN 1 "
        "ELSE (SELECT (COALESCE(message_version, 0)+1) AS answer FROM messages WHERE message_id = :message_id AND chat_id = :chat_id ORDER BY date_time DESC LIMIT 1) "
        "END) AS answer, :chat_id, :text, :buttons_names, :buttons_callbacks, now(), :is_available",
        {"message_id": message.message_id, "message_version": message.message_version, "chat_id": message.chat_id,
         "text": message.text, "buttons_names": to_str(message.buttons_names), "buttons_callbacks": to_str(message.buttons_callbacks),
         "is_available": message.is_available})
    session.commit()
    session.close()


def to_str(texts_list: List[List[str]]) -> str:
    return "\n".join(map(lambda sublist: "[" + "\t".join(sublist) + "]", texts_list))

def from_str(text: str) -> List[List[str]]:
    return list(map(lambda array_as_str: str(array_as_str)[1:-1].split('\t'), text.split('\n')))
