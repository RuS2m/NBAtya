class Statistics:
    def __init__(self, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk,
                 tov, pf, pts):
        self.min = round(min, 3)
        self.fgm = round(fgm, 3)
        self.fga = round(fga, 3)
        self.fg_pct = round(fg_pct, 3)
        self.fg3m = round(fg3m, 3)
        self.fg3a = round(fg3a, 3)
        self.fg3_pct = round(fg3_pct, 3)
        self.ftm = round(ftm, 3)
        self.fta = round(fta, 3)
        self.ft_pct = round(ft_pct, 3)
        self.oreb = round(oreb, 3)
        self.dreb = round(dreb, 3)
        self.reb = round(reb, 3)
        self.ast = round(ast, 3)
        self.stl = round(stl, 3)
        self.blk = round(blk, 3)
        self.tov = round(tov, 3)
        self.pf = round(pf, 3)
        self.pts = round(pts, 3)

    def __str__(self):
        return '\n<i>🏀🏀-Point shots</i>\n' \
               '- number of successful shots: {} \n' \
               '- number of shots: {} \n' \
               '- percentage of successful shots: {} \n' \
               '<i>🏀🏀🏀-Point shots</i>\n' \
               '- number of successful shots: {} \n' \
               '- number of shots: {} \n' \
               '- percentage of successful shots: {} \n' \
               '<i>🚫 ‍Free throws</i>\n' \
               '- number of successful shots: {} \n' \
               '- number of shots: {} \n' \
               '- percentage of successful shots: {} \n' \
               '<i>⛹️‍♂️Technique</i>\n' \
               '- minutes played: {} \n' \
               '- number of rebounds: {} \n' \
               '- number of rebounds in attack: {} \n' \
               '- number of rebounds in defense: {} \n' \
               '- number of passes: {} \n' \
               '- number of steals: {} \n' \
               '- number of blocked shots: {} \n' \
               '- number of ball\' possessions: {} \n' \
               '- number of personal fouls: {} \n' \
               '- number of points: {} \n' \
               ''.format(self.fgm, self.fga, self.fg_pct, self.fg3m, self.fg3a, self.fg3_pct, self.ftm, self.fta,
                         self.ft_pct, self.min, self.oreb, self.dreb, self.reb, self.ast, self.stl, self.blk, self.tov,
                         self.pf, self.pts
                         )


class Season:
    def __init__(self, season_id, season_name, season_type, season_year, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct,
                 ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts):
        self.season_id = season_id
        self.season_name = season_name
        self.season_type = season_type
        self.season_year = season_year
        self.statistics = Statistics(min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast,
                                     stl, blk, tov, pf, pts)

    def __str__(self):
        return '<b>{}</b>\n\n' \
               'Teams in season: /tms\n' \
               'Games in season: /gms\n\n' \
               '---\n' \
               'Show season statistics: /stat\n' \
               ''.format(self.season_name)

    def fake_str(self):
        return '<b>{}</b>\n\n' \
               'Go to season\'s page: /origin\n\n' \
               '---\n' \
               'Show season statistics: /stat\n' \
               ''.format(self.season_name)


class SeasonPage:
    def __init__(self, season_id, season_name, season_type, season_year, page, total):
        self.season_id = season_id
        self.season_name = season_name
        self.season_type = season_type
        self.season_year = season_year
        self.page = page
        self.total = total

    def __str__(self):
        return '<b>{}</b>\n' \
               '<i>type</i>: {}\n' \
               '<i>year</i>: {}' \
               ''.format(self.season_name, self.season_type, int(self.season_year))


class Team:
    def __init__(self, team_id, abbreviation, team_name, foundation_year, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct,
                 ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts):
        self.team_id = team_id
        self.abbreviation = abbreviation
        self.team_name = team_name
        self.foundation_year = foundation_year
        self.statistics = Statistics(min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast,
                                     stl, blk, tov, pf, pts)

    def __str__(self):
        return '<b>{}</b> <b>({})</b>\n\n' \
               '<i>Foundation year</i>: {}\n' \
               'Seasons, where team was participating: /sns\n' \
               'Team\'s games: /gms\n' \
               'Team\'s players: /plrs\n' \
               '---\n' \
               'Show team statistics: /stat\n' \
               ''.format(self.team_name, self.abbreviation, int(self.foundation_year))

    def fake_str(self):
        return '<b>{}</b> <b>({})</b>\n\n' \
               'Go to team\'s page: /origin\n\n' \
               '---\n' \
               'Show team statistics: /stat\n' \
               ''.format(self.team_name, self.abbreviation)


class TeamsPage:
    def __init__(self, team_id, abbreviation, team_name, page, total):
        self.team_id = team_id
        self.abbreviation = abbreviation
        self.team_name = team_name
        self.page = page
        self.total = total


class GamePage:
    def __init__(self, game_id, game_date, season_id, away_team_id, home_team_id, away_abbreviation, home_abbreviation,
                 page, total):
        self.game_id = game_id
        self.season_id = season_id
        self.game_date = game_date
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.away_abbreviation = away_abbreviation
        self.home_abbreviation = home_abbreviation
        self.page = page
        self.total = total


class GameStatistics:
    def __init__(self, min_a, fgm_a, fga_a, fg_pct_a, fg3m_a, fg3a_a, fg3_pct_a, ftm_a, fta_a, ft_pct_a, oreb_a, dreb_a,
                 reb_a, ast_a, stl_a, blk_a, tov_a, pf_a, pts_a, min_h, fgm_h, fga_h, fg_pct_h, fg3m_h, fg3a_h,
                 fg3_pct_h, ftm_h, fta_h, ft_pct_h, oreb_h, dreb_h, reb_h, ast_h, stl_h, blk_h, tov_h, pf_h, pts_h):
        self.min_a = round(min_a, 3)
        self.fgm_a = round(fgm_a, 3)
        self.fga_a = round(fga_a, 3)
        self.fg_pct_a = round(fg_pct_a, 3)
        self.fg3m_a = round(fg3m_a, 3)
        self.fg3a_a = round(fg3a_a, 3)
        self.fg3_pct_a = round(fg3_pct_a, 3)
        self.ftm_a = round(ftm_a, 3)
        self.fta_a = round(fta_a, 3)
        self.ft_pct_a = round(ft_pct_a, 3)
        self.oreb_a = round(oreb_a, 3)
        self.dreb_a = round(dreb_a, 3)
        self.reb_a = round(reb_a, 3)
        self.ast_a = round(ast_a, 3)
        self.stl_a = round(stl_a, 3)
        self.blk_a = round(blk_a, 3)
        self.tov_a = round(tov_a, 3)
        self.pf_a = round(pf_a, 3)
        self.pts_a = round(pts_a, 3)
        self.min_h = round(min_h, 3)
        self.fgm_h = round(fgm_h, 3)
        self.fga_h = round(fga_h, 3)
        self.fg_pct_h = round(fg_pct_h, 3)
        self.fg3m_h = round(fg3m_h, 3)
        self.fg3a_h = round(fg3a_h, 3)
        self.fg3_pct_h = round(fg3_pct_h, 3)
        self.ftm_h = round(ftm_h, 3)
        self.fta_h = round(fta_h, 3)
        self.ft_pct_h = round(ft_pct_h, 3)
        self.oreb_h = round(oreb_h, 3)
        self.dreb_h = round(dreb_h, 3)
        self.reb_h = round(reb_h, 3)
        self.ast_h = round(ast_h, 3)
        self.stl_h = round(stl_h, 3)
        self.blk_h = round(blk_h, 3)
        self.tov_h = round(tov_h, 3)
        self.pf_h = round(pf_h, 3)
        self.pts_h = round(pts_h, 3)

    def __str__(self):
        return '\n<i>🏀🏀-Point shots</i>\n' \
               '- number of successful shots: {} vs {}\n' \
               '- number of shots: {} vs {}\n' \
               '- percentage of successful shots: {} vs {}\n' \
               '<i>🏀🏀🏀-Point shots</i>\n' \
               '- number of successful shots: {} vs {}\n' \
               '- number of shots: {} vs {}\n' \
               '- percentage of successful shots: {} vs {}\n' \
               '<i>🚫 ‍Free throws</i>\n' \
               '- number of successful shots: {} vs {}\n' \
               '- number of shots: {} vs {}\n' \
               '- percentage of successful shots: {} vs {}\n' \
               '<i>⛹️‍♂️Technique</i>\n' \
               '- minutes played: {} vs {}\n' \
               '- number of rebounds: {} vs {}\n' \
               '- number of rebounds in attack: {} vs {}\n' \
               '- number of rebounds in defense: {} vs {}\n' \
               '- number of passes: {} vs {}\n' \
               '- number of steals: {} vs {}\n' \
               '- number of blocked shots: {} vs {}\n' \
               '- number of ball\' possessions: {} vs {}\n' \
               '- number of personal fouls: {} vs {}\n' \
               '- number of points: {} vs {}\n' \
               ''.format(self.fgm_h, self.fgm_a, self.fga_h, self.fga_a, self.fg_pct_h, self.fg_pct_a, self.fg3m_h,
                         self.fg3m_a, self.fg3a_h, self.fg3a_a, self.fg3_pct_h, self.fg3_pct_a, self.ftm_h, self.ftm_a,
                         self.fta_h, self.fta_a, self.ft_pct_h, self.ft_pct_a, self.min_h, self.min_a, self.oreb_h,
                         self.oreb_a, self.dreb_h, self.dreb_a, self.reb_h, self.reb_a, self.ast_h, self.ast_a,
                         self.stl_h, self.stl_a, self.blk_h, self.blk_a, self.tov_h, self.tov_a, self.pf_h, self.pf_a,
                         self.pts_h, self.pts_a)


class Game:
    def __init__(self, game_id, game_date, season_id, season_name, is_home_win, away_team_id, home_team_id,
                 away_team_name, home_team_name, away_abbreviation, home_abbreviation, min_a, fgm_a, fga_a, fg_pct_a,
                 fg3m_a, fg3a_a, fg3_pct_a, ftm_a, fta_a, ft_pct_a, oreb_a, dreb_a, reb_a, ast_a, stl_a, blk_a, tov_a,
                 pf_a, pts_a, min_h, fgm_h, fga_h, fg_pct_h, fg3m_h, fg3a_h, fg3_pct_h, ftm_h, fta_h, ft_pct_h, oreb_h,
                 dreb_h, reb_h, ast_h, stl_h, blk_h, tov_h, pf_h, pts_h):
        self.game_id = game_id
        self.game_date = game_date
        self.season_id = season_id
        self.seasom_name = season_name
        self.is_home_win = is_home_win
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.away_team_name = away_team_name
        self.home_team_name = home_team_name
        self.away_abbreviation = away_abbreviation
        self.home_abbreviation = home_abbreviation
        self.statistics = GameStatistics(min_a, fgm_a, fga_a, fg_pct_a, fg3m_a, fg3a_a, fg3_pct_a, ftm_a, fta_a,
                                         ft_pct_a, oreb_a, dreb_a, reb_a, ast_a, stl_a, blk_a, tov_a, pf_a, pts_a,
                                         min_h, fgm_h, fga_h, fg_pct_h, fg3m_h, fg3a_h, fg3_pct_h, ftm_h, fta_h,
                                         ft_pct_h, oreb_h, dreb_h, reb_h, ast_h, stl_h, blk_h, tov_h, pf_h, pts_h)

    def __str__(self):
        home_emodji = '🏆' if self.is_home_win else '🦀'
        away_emodji = '🦀' if self.is_home_win else '🏆'
        return '{} <b>{}</b> vs <b>{}</b> {} ({}:{})\n\n' \
               'Match on <i>{}</i> during <i>{}</i>\n' \
               'Players in game: /plrs\n\n' \
               '---\n' \
               'Show game statistics: /stat\n' \
               "".format(home_emodji, self.home_abbreviation, self.away_abbreviation, away_emodji,
                         int(self.statistics.pts_h), int(self.statistics.pts_a), self.game_date,
                         self.seasom_name)


class Player:
    def __init__(self, player_id, secondname_name, playercode, team_id, team_name, team_abbreviation, rosterstatus, position,
                 jersey, season_exp,
                 from_year, to_year, draft_year, draft_round, height, weight, min, fgm, fga, fg_pct, fg3m, fg3a,
                 fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts, plus_minus):
        self.player_id = player_id
        self.secondname_name = secondname_name
        self.playercode = playercode
        self.team_id = team_id
        self.team_name = team_name
        self.team_abbreviation = team_abbreviation
        self.rosterstatus = rosterstatus
        self.position = position
        self.jersey = jersey
        self.season_exp = season_exp
        self.from_year = from_year
        self.to_year = to_year
        self.draft_year = draft_year
        self.draft_round = draft_round
        self.height = height
        self.weight = weight
        self.statistics = Statistics(min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast,
                                     stl, blk, tov, pf, pts)

    def __str__(self):
        return '' \
               '<b>{}</b>\n\n' \
               '{} at <b>{} ({})</b> <i>from {} to {}</i>\n' \
               'Player\'s games: /gms\n' \
               'Player\'s team: /tm\n\n' \
               '---\n' \
               'Show player\'s statistics: /stat' \
               ''.format(self.secondname_name, self.position, self.team_name, self.team_abbreviation, int(self.from_year),
                         int(self.to_year))


class PlayerPage:
    def __init__(self, player_id, secondname_name, rosterstatus, team_id, page, total):
        self.player_id = player_id
        self.secondname_name = secondname_name
        self.rosterstatus = rosterstatus
        self.team_id = team_id
        self.page = page
        self.total = total

    def __str__(self):
        return '{}, {}, {}, {}\npage {} from {}'.format(self.player_id, self.secondname_name, self.rosterstatus,
                                                        self.team_id, self.page, self.total)


class Message:
    def __init__(self, message_id, message_version, chat_id, text, buttons_names, buttons_callbacks, is_available):
        self.message_id = message_id
        self.message_version = message_version
        self.chat_id = chat_id
        self.text = text
        self.buttons_names = buttons_names
        self.buttons_callbacks = buttons_callbacks
        self.is_available = is_available

    def __str__(self):
        return 'message {}\n' \
               'message_version {}\n' \
               'chat {}\n' \
               'text {}\n' \
               'buttons_names {}\n' \
               'buttons_callbacks {}\n' \
               'is_available: {}' \
               ''.format(self.message_id, self.message_version, self.chat_id, self.text, self.buttons_names,
                         self.buttons_callbacks, self.is_available)
