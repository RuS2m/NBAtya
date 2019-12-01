from typing import List

from database_connect import session, engine
from model.models import SeasonPage, Season


def get_seasons_num() -> int:
    rs = session.execute(
        "SELECT COUNT(*) FROM seasons"
    )
    return rs.first()[0]


def get_seasons_page(page: int, per_page: int) -> List[SeasonPage]:
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
    return answer


def get_season_by_id(season_id: int) -> Season:
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
        return Season(season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm,
                      fta, ft_pct,
                      oreb, dreb, reb, ast, stl, blk, tov, pf, pts)
    raise Exception


def get_players_num():
    rs = session.execute(
        "SELECT COUNT(*) FROM players"
    )
    return rs.first()[0]
