class Statistics:
    def __init__(self,
                 min,
                 fgm,
                 fga,
                 fg_pct,
                 fg3m,
                 fg3a,
                 fg3_pct,
                 ftm,
                 fta,
                 ft_pct,
                 oreb,
                 dreb,
                 reb,
                 ast,
                 stl,
                 blk,
                 tov,
                 pf,
                 pts):
        self.min = min
        self.fgm = fgm
        self.fga = fga
        self.fg_pct = fg_pct
        self.fg3m = fg3m
        self.fg3a = fg3a
        self.fg3_pct = fg3_pct
        self.ftm = ftm
        self.fta = fta
        self.ft_pct = ft_pct
        self.oreb = oreb
        self.dreb = dreb
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        self.pf = pf
        self.pts = pts

    def __str__(self):
        return 'min: {} \n' \
               'fgm: {} \n' \
               'fga: {} \n' \
               'fg_pct: {} \n' \
               'fg3m: {} \n' \
               'fg3a: {} \n' \
               'fg3_pct: {} \n' \
               'ftm: {} \n' \
               'fta: {} \n' \
               'ft_pct: {} \n' \
               'oreb: {} \n' \
               'dreb: {} \n' \
               'reb: {} \n' \
               'ast: {} \n' \
               'stl: {} \n' \
               'blk: {} \n' \
               'tov: {} \n' \
               'pf: {} \n' \
               'pts: {} \n' \
               ''.format(
            self.min,
            self.fgm,
            self.fga,
            self.fg_pct,
            self.fg3m,
            self.fg3a,
            self.fg3_pct,
            self.ftm,
            self.fta,
            self.ft_pct,
            self.oreb,
            self.dreb,
            self.reb,
            self.ast,
            self.stl,
            self.blk,
            self.tov,
            self.pf,
            self.pts
        )


class Season:
    def __init__(self,
                 season_id,
                 season_name,
                 season_type,
                 season_year,
                 min,
                 fgm,
                 fga,
                 fg_pct,
                 fg3m,
                 fg3a,
                 fg3_pct,
                 ftm,
                 fta,
                 ft_pct,
                 oreb,
                 dreb,
                 reb,
                 ast,
                 stl,
                 blk,
                 tov,
                 pf,
                 pts):
        self.season_id = season_id
        self.season_name = season_name
        self.season_type = season_type
        self.season_year = season_year
        self.statistics = Statistics(
            min,
            fgm,
            fga,
            fg_pct,
            fg3m,
            fg3a,
            fg3_pct,
            ftm,
            fta,
            ft_pct,
            oreb,
            dreb,
            reb,
            ast,
            stl,
            blk,
            tov,
            pf,
            pts)

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
               ''.format(self.season_name, self.season_type, self.season_year)


class Team:
    def __init__(self,
                 team_id,
                 abbreviation,
                 team_name,
                 foundation_year,
                 min,
                 fgm,
                 fga,
                 fg_pct,
                 fg3m,
                 fg3a,
                 fg3_pct,
                 ftm,
                 fta,
                 ft_pct,
                 oreb,
                 dreb,
                 reb,
                 ast,
                 stl,
                 blk,
                 tov,
                 pf,
                 pts):
        self.team_id = team_id
        self.abbreviation = abbreviation
        self.team_name = team_name
        self.foundation_year = foundation_year
        self.statistics = Statistics(
            min,
            fgm,
            fga,
            fg_pct,
            fg3m,
            fg3a,
            fg3_pct,
            ftm,
            fta,
            ft_pct,
            oreb,
            dreb,
            reb,
            ast,
            stl,
            blk,
            tov,
            pf,
            pts)

    def __str__(self):
        return '<b>{}</b> <b>({})</b>\n\n' \
               '<i>Foundation year</i>: {}\n' \
               'Seasons, where team was participating: /sns\n' \
               'Team\'s games: /gms\n' \
               '---\n' \
               'Show team statistics: /stat\n' \
               ''.format(self.team_name, self.abbreviation, self.foundation_year)

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
    def __init__(self,
                 min_a,
                 fgm_a,
                 fga_a,
                 fg_pct_a,
                 fg3m_a,
                 fg3a_a,
                 fg3_pct_a,
                 ftm_a,
                 fta_a,
                 ft_pct_a,
                 oreb_a,
                 dreb_a,
                 reb_a,
                 ast_a,
                 stl_a,
                 blk_a,
                 tov_a,
                 pf_a,
                 pts_a,
                 min_h,
                 fgm_h,
                 fga_h,
                 fg_pct_h,
                 fg3m_h,
                 fg3a_h,
                 fg3_pct_h,
                 ftm_h,
                 fta_h,
                 ft_pct_h,
                 oreb_h,
                 dreb_h,
                 reb_h,
                 ast_h,
                 stl_h,
                 blk_h,
                 tov_h,
                 pf_h,
                 pts_h):
        self.min_a = min_a
        self.fgm_a = fgm_a
        self.fga_a = fga_a
        self.fg_pct_a = fg_pct_a
        self.fg3m_a = fg3m_a
        self.fg3a_a = fg3a_a
        self.fg3_pct_a = fg3_pct_a
        self.ftm_a = ftm_a
        self.fta_a = fta_a
        self.ft_pct_a = ft_pct_a
        self.oreb_a = oreb_a
        self.dreb_a = dreb_a
        self.reb_a = reb_a
        self.ast_a = ast_a
        self.stl_a = stl_a
        self.blk_a = blk_a
        self.tov_a = tov_a
        self.pf_a = pf_a
        self.pts_a = pts_a
        self.min_h = min_h
        self.fgm_h = fgm_h
        self.fga_h = fga_h
        self.fg_pct_h = fg_pct_h
        self.fg3m_h = fg3m_h
        self.fg3a_h = fg3a_h
        self.fg3_pct_h = fg3_pct_h
        self.ftm_h = ftm_h
        self.fta_h = fta_h
        self.ft_pct_h = ft_pct_h
        self.oreb_h = oreb_h
        self.dreb_h = dreb_h
        self.reb_h = reb_h
        self.ast_h = ast_h
        self.stl_h = stl_h
        self.blk_h = blk_h
        self.tov_h = tov_h
        self.pf_h = pf_h
        self.pts_h = pts_h

    def __str__(self):
        return "" \
               "min_a: {} \n" \
               "fgm_a: {} \n" \
               "fga_a: {} \n" \
               "fg_pct_a: {} \n" \
               "fg3m_a: {} \n" \
               "fg3a_a: {} \n" \
               "fg3_pct_a: {} \n" \
               "ftm_a: {} \n" \
               "fta_a: {} \n" \
               "ft_pct_a: {} \n" \
               "oreb_a: {} \n" \
               "dreb_a: {} \n" \
               "reb_a: {} \n" \
               "ast_a: {} \n" \
               "stl_a: {} \n" \
               "blk_a: {} \n" \
               "tov_a: {} \n" \
               "pf_a: {} \n" \
               "pts_a: {} \n" \
               "min_h: {} \n" \
               "fgm_h: {} \n" \
               "fga_h: {} \n" \
               "fg_pct_h: {} \n" \
               "fg3m_h: {} \n" \
               "fg3a_h: {} \n" \
               "fg3_pct_h: {} \n" \
               "ftm_h: {} \n" \
               "fta_h: {} \n" \
               "ft_pct_h: {} \n" \
               "oreb_h: {} \n" \
               "dreb_h: {} \n" \
               "reb_h: {} \n" \
               "ast_h: {} \n" \
               "stl_h: {} \n" \
               "blk_h: {} \n" \
               "tov_h: {} \n" \
               "pf_h: {} \n" \
               "pts_h: {} \n" \
               "".format(
            self.min_a,
            self.fgm_a,
            self.fga_a,
            self.fg_pct_a,
            self.fg3m_a,
            self.fg3a_a,
            self.fg3_pct_a,
            self.ftm_a,
            self.fta_a,
            self.ft_pct_a,
            self.oreb_a,
            self.dreb_a,
            self.reb_a,
            self.ast_a,
            self.stl_a,
            self.blk_a,
            self.tov_a,
            self.pf_a,
            self.pts_a,
            self.min_h,
            self.fgm_h,
            self.fga_h,
            self.fg_pct_h,
            self.fg3m_h,
            self.fg3a_h,
            self.fg3_pct_h,
            self.ftm_h,
            self.fta_h,
            self.ft_pct_h,
            self.oreb_h,
            self.dreb_h,
            self.reb_h,
            self.ast_h,
            self.stl_h,
            self.blk_h,
            self.tov_h,
            self.pf_h,
            self.pts_h
        )


class Game:
    def __init__(self,
                 game_id,
                 game_date,
                 season_id,
                 season_name,
                 is_home_win,
                 away_team_id,
                 home_team_id,
                 away_team_name,
                 home_team_name,
                 away_abbreviation,
                 home_abbreviation,
                 min_a,
                 fgm_a,
                 fga_a,
                 fg_pct_a,
                 fg3m_a,
                 fg3a_a,
                 fg3_pct_a,
                 ftm_a,
                 fta_a,
                 ft_pct_a,
                 oreb_a,
                 dreb_a,
                 reb_a,
                 ast_a,
                 stl_a,
                 blk_a,
                 tov_a,
                 pf_a,
                 pts_a,
                 min_h,
                 fgm_h,
                 fga_h,
                 fg_pct_h,
                 fg3m_h,
                 fg3a_h,
                 fg3_pct_h,
                 ftm_h,
                 fta_h,
                 ft_pct_h,
                 oreb_h,
                 dreb_h,
                 reb_h,
                 ast_h,
                 stl_h,
                 blk_h,
                 tov_h,
                 pf_h,
                 pts_h
                 ):
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
                                         ft_pct_h, oreb_h, dreb_h, reb_h, ast_h, stl_h, blk_h, tov_h, pf_h, pts_h
                                         )

    def __str__(self):
        return '<b>{}</b> vs <b>{}</b>\n\n' \
               'Match on <i>{}</i> during <i>{}</i>\n' \
               '---\n' \
               'Show game statistics: /stat\n' \
               "".format(self.home_abbreviation, self.away_abbreviation, self.game_date, self.seasom_name)


class Message:
    def __init__(self, message_id,
                 message_version,
                 chat_id,
                 text,
                 buttons_names,
                 buttons_callbacks,
                 is_available):
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
