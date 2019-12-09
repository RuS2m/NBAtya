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
               'Teams in season: /tms\n\n' \
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
               'Seasons, where team was participating: /sns\n\n' \
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
