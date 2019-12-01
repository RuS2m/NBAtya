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
        # FIXME: add logic for statistics pop-up
        return '<b>{}</b>\n\n' \
               '<i>type</i>: {}\n' \
               '<i>year</i>: {}\n\n' \
               'TBA: <a href="https://ya.ru">Statistics</a>\n' \
               ''.format(self.season_name, self.season_type, self.season_year)


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
