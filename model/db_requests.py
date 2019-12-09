from typing import List

from sqlalchemy.orm import Session

from database_connect import engine
from model.models import SeasonPage, Season, Message, TeamsPage, Team, Game, GamePage

""" * Seasons block * """


def get_seasons_num() -> int:
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(*) FROM seasons"
    )
    session.commit()
    session.close()
    return rs.first()[0]


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


def get_season_by_id(season_id: int) -> Season:
    session = Session(engine)
    rs = session.execute(
        "SELECT season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, "
        "fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts "
        "FROM seasons WHERE season_id = :session_id",
        {"session_id": season_id})

    for row in rs:
        session.commit()
        session.close()
        return Season(season_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                      row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                      row[22])


def get_season_by_name(season_name: str) -> Season:
    session = Session(engine)
    rs = session.execute(
        "SELECT season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, "
        "fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts "
        "FROM seasons WHERE season_name = :season_name",
        {"season_name": season_name})

    for row in rs:
        session.commit()
        session.close()
        return Season(row[0], season_name, row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                      row[11],
                      row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22])


def get_seasons_with_team_num(team_id: int) -> int:
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(DISTINCT(season_id)) FROM season_team WHERE team_id = :team_id",
        {"team_id": team_id}
    )
    session.commit()
    session.close()
    return rs.first()[0]


def get_seasons_with_team_page(team_id: int, page: int, per_page: int) -> List[SeasonPage]:
    session = Session(engine)
    offset = 0
    if page != 1:
        offset = (page - 1) * per_page
    answer = []
    seasons_number_with_team = get_seasons_with_team_num(team_id)
    total = int(int(seasons_number_with_team) / per_page) + int(int(seasons_number_with_team) % per_page)
    if page > total:
        return answer
    rs = session.execute(
        "SELECT season_id, season_name, season_type, season_year FROM seasons "
        "WHERE season_id IN "
        "(SELECT season_id FROM season_team WHERE team_id = :team_id) "
        "ORDER BY season_name "
        "LIMIT :per_page OFFSET :offset", {"team_id": team_id, "per_page": per_page, "offset": offset})
    for row in rs:
        answer.append(SeasonPage(row[0], row[1], row[2], row[3], page, total))
    session.commit()
    session.close()
    return answer


def get_team_season(team_id: int, season_id: int) -> Season:
    session = Session(engine)
    rs = session.execute(
        "SELECT season_team.season_id, season_team.team_id, seasons.season_name, seasons.season_type, seasons.season_year, "
        "season_team.min, season_team.fgm, season_team.fga, season_team.fg_pct, season_team.fg3m, season_team.fg3a, "
        "season_team.fg3_pct, season_team.ftm, season_team.fta, season_team.ft_pct, season_team.oreb, season_team.dreb, "
        "season_team.reb, season_team.ast, season_team.stl, season_team.blk, season_team.tov, season_team.pf, "
        "season_team.pts FROM season_team "
        "INNER JOIN seasons ON seasons.season_id = season_team.season_id "
        "WHERE season_team.season_id = :season_id AND team_id = :team_id",
        {"team_id": team_id, "season_id": season_id}
    )
    for row in rs:
        session.commit()
        session.close()
        return Season(season_id, row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                      row[12],
                      row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23])


""" * Teams block * """


def get_teams_num() -> int:
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(*) FROM teams"
    )
    session.commit()
    session.close()
    return rs.first()[0]


def get_teams_page(page: int, per_page: int) -> List[TeamsPage]:
    session = Session(engine)
    offset = 0
    if page != 1:
        offset = (page - 1) * per_page
    answer = []
    total = int(int(get_teams_num()) / per_page) + int(int(get_teams_num()) % per_page)
    if page > total:
        return answer
    rs = session.execute(
        "SELECT team_id, abbreviation, team_name FROM teams ORDER BY team_name "
        "LIMIT :per_page OFFSET :offset", {"per_page": per_page, "offset": offset})
    for row in rs:
        answer.append(TeamsPage(row[0], row[1], row[2], page, total))
    session.commit()
    session.close()
    return answer


def get_team_by_id(team_id: int) -> Team:
    session = Session(engine)
    rs = session.execute(
        "SELECT team_id, abbreviation, team_name, foundation_year, min, fgm, fga, fg_pct, fg3m, fg3a, "
        "fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts "
        "FROM teams WHERE team_id = :team_id",
        {"team_id": team_id})

    for row in rs:
        session.commit()
        session.close()
        return Team(team_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22])


def get_team_by_name(team_name: str) -> Team:
    session = Session(engine)
    rs = session.execute(
        "SELECT team_id, abbreviation, team_name, foundation_year, min, fgm, fga, fg_pct, fg3m, fg3a, "
        "fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts "
        "FROM teams WHERE team_name = :team_name",
        {"team_name": team_name})

    for row in rs:
        session.commit()
        session.close()
        return Team(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22])


def get_teams_in_season_num(season_id: int) -> int:
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(DISTINCT(team_id)) FROM season_team WHERE season_id = :season_id",
        {"season_id": season_id}
    )
    session.commit()
    session.close()
    return rs.first()[0]


def get_season_team(team_id: int, season_id: int) -> Team:
    session = Session(engine)
    rs = session.execute(
        "SELECT season_team.season_id, season_team.team_id, teams.abbreviation, teams.team_name, teams.foundation_year, "
        "season_team.min, season_team.fgm, season_team.fga, season_team.fg_pct, season_team.fg3m, season_team.fg3a, "
        "season_team.fg3_pct, season_team.ftm, season_team.fta, season_team.ft_pct, season_team.oreb, season_team.dreb, "
        "season_team.reb, season_team.ast, season_team.stl, season_team.blk, season_team.tov, season_team.pf, "
        "season_team.pts FROM season_team "
        "INNER JOIN teams ON teams.team_id = season_team.team_id "
        "WHERE season_team.team_id = :team_id AND season_id = :season_id",
        {"team_id": team_id, "season_id": season_id}
    )
    for row in rs:
        session.commit()
        session.close()
        return Team(team_id, row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                    row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23])


def get_teams_in_seasons_page(season_id: int, page: int, per_page: int) -> List[TeamsPage]:
    session = Session(engine)
    offset = 0
    if page != 1:
        offset = (page - 1) * per_page
    answer = []
    teams_number_in_season = get_teams_in_season_num(season_id)
    total = int(int(teams_number_in_season) / per_page) + int(int(teams_number_in_season) % per_page)
    if page > total:
        return answer
    rs = session.execute(
        "SELECT team_id, abbreviation, team_name FROM teams "
        "WHERE team_id IN "
        "(SELECT team_id FROM season_team WHERE season_id = :season_id) "
        "ORDER BY team_name "
        "LIMIT :per_page OFFSET :offset", {"season_id": season_id, "per_page": per_page, "offset": offset})
    for row in rs:
        answer.append(TeamsPage(row[0], row[1], row[2], page, total))
    session.commit()
    session.close()
    return answer


""" * Games block * """


def get_games_in_season_num(season_id: int) -> int:
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(DISTINCT(game_id)) FROM games WHERE season_id = :season_id",
        {"season_id": season_id}
    )
    session.commit()
    session.close()
    return rs.first()[0]


def get_games_in_season_page(season_id: int, page: int, per_page: int) -> List[GamePage]:
    session = Session(engine)
    offset = 0
    if page != 1:
        offset = (page - 1) * per_page
    answer = []
    number_of_games = get_games_in_season_num(season_id)
    total = int(number_of_games / per_page) + int(number_of_games % per_page)
    if page > total:
        return answer
    rs = session.execute(
        "SELECT game_id, game_date, season_id, away_team_id, home_team_id, away_abbreviation, home_abbreviation FROM games "
        "WHERE season_id = :season_id "
        "ORDER BY game_date "
        "LIMIT :per_page OFFSET :offset", {"season_id": season_id, "per_page": per_page, "offset": offset})
    for row in rs:
        answer.append(GamePage(row[0], row[1], row[2], row[3], row[4], row[5], row[6], page, total))
    session.commit()
    session.close()
    return answer


def get_game_by_id(game_id: int) -> Game:
    session = Session(engine)
    rs = session.execute(
        "SELECT games.game_id, games.game_date, games.season_id, seasons.season_name, games.is_home_win, games.away_team_id, "
        "games.home_team_id, games.away_team_name, games.home_team_name, games.away_abbreviation, games.home_abbreviation, "
        "games.min_a, games.fgm_a, games.fga_a, games.fg_pct_a, games.fg3m_a, games.fg3a_a, games.fg3_pct_a, games.ftm_a, "
        "games.fta_a, games.ft_pct_a, games.oreb_a, games.dreb_a, games.reb_a, games.ast_a, games.stl_a, games.blk_a, "
        "games.tov_a, games.pf_a, games.pts_a, games.min_h, games.fgm_h, games.fga_h, games.fg_pct_h, games.fg3m_h, "
        "games.fg3a_h, games.fg3_pct_h, games.ftm_h, games.fta_h, games.ft_pct_h, games.oreb_h, games.dreb_h, games.reb_h, "
        "games.ast_h, games.stl_h, games.blk_h, games.tov_h, games.pf_h, games.pts_h "
        "FROM games INNER JOIN seasons ON games.season_id = seasons.season_id "
        "WHERE games.game_id = :game_id ",
    {"game_id": game_id})

    for row in rs:
        print(row)
        session.commit()
        session.close()
        return Game(game_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                    row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                    row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32],
                    row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43],
                    row[43], row[44], row[45], row[46], row[37])


def get_game_by_team_names_and_season_date(home_team: str, away_team: str, date, season_name) -> Game:
    session = Session(engine)
    rs = session.execute(
        "SELECT games.game_id, games.game_date, games.season_id, seasons.season_name, games.is_home_win, games.away_team_id, "
        "games.home_team_id, games.away_team_name, games.home_team_name, games.away_abbreviation, games.home_abbreviation, "
        "games.min_a, games.fgm_a, games.fga_a, games.fg_pct_a, games.fg3m_a, games.fg3a_a, games.fg3_pct_a, games.ftm_a, "
        "games.fta_a, games.ft_pct_a, games.oreb_a, games.dreb_a, games.reb_a, games.ast_a, games.stl_a, games.blk_a, "
        "games.tov_a, games.pf_a, games.pts_a, games.min_h, games.fgm_h, games.fga_h, games.fg_pct_h, games.fg3m_h, "
        "games.fg3a_h, games.fg3_pct_h, games.ftm_h, games.fta_h, games.ft_pct_h, games.oreb_h, games.dreb_h, games.reb_h, "
        "games.ast_h, games.stl_h, games.blk_h, games.tov_h, games.pf_h, games.pts_h "
        "FROM games INNER JOIN seasons ON games.season_id = seasons.season_id "
        "WHERE games.game_date = :game_date AND games.home_abbreviation = :home_team AND games.away_abbreviation = :away_team "
        "AND seasons.season_name = :season_name "
        "LIMIT 1",
        {"game_date": date, "home_team": home_team, "away_team": away_team, "season_name": season_name})

    for row in rs:
        print(row)
        session.commit()
        session.close()
        return Game(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                    row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                    row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32],
                    row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43],
                    row[43], row[44], row[45], row[46], row[37])

""" * Players block * """


def get_players_num():
    session = Session(engine)
    rs = session.execute(
        "SELECT COUNT(*) FROM players"
    )
    session.commit()
    session.close()
    return rs.first()[0]


""" * Messages block * """

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
        session.execute(
            "DELETE FROM messages WHERE message_id = :message_id AND chat_id = :chat_id AND is_available = TRUE "
            "AND date_time = "
            "(SELECT date_time FROM messages WHERE message_id = :message_id AND chat_id = :chat_id AND is_available = TRUE ORDER BY date_time DESC LIMIT 1)",
            {"message_id": message_id, "chat_id": chat_id})
        session.commit()
        session.close()
        return Message(int(row[0]), int(row[1]), int(row[2]), row[3], from_str(row[4]),
                       from_str(row[5]), True)


def get_last_message(chat_id: int) -> Message:
    session = Session(engine)
    rs = session.execute(
        "SELECT message_id, message_version, chat_id, text, buttons_names, buttons_callbacks, is_available "
        "FROM messages WHERE chat_id = :chat_id "
        "ORDER BY date_time DESC "
        "LIMIT 1",
        {"chat_id": chat_id})
    for row in rs:
        session.commit()
        session.close()
        return Message(int(row[0]), int(row[1]), int(row[2]), row[3], from_str(row[4]), from_str(row[5]),
                       row[6])


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
         "text": message.text, "buttons_names": to_str(message.buttons_names),
         "buttons_callbacks": to_str(message.buttons_callbacks),
         "is_available": message.is_available})
    session.commit()
    session.close()


def to_str(texts_list: List[List[str]]) -> str:
    return "\n".join(map(lambda sublist: "[" + "\t".join(sublist) + "]", texts_list))


def from_str(text: str) -> List[List[str]]:
    return list(map(lambda array_as_str: str(array_as_str)[1:-1].split('\t'), text.split('\n')))
