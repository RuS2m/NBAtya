CREATE TABLE games (
	game_id BIGINT PRIMARY KEY,
	game_date TEXT,
	season_id BIGINT REFERENCES seasons(season_id),
	is_home_win BOOLEAN,
	away_team_id BIGINT REFERENCES teams(team_id),
	home_team_id BIGINT REFERENCES teams(team_id),
	away_team_name TEXT,
	home_team_name TEXT,
	away_abbreviation TEXT,
	home_abbreviation TEXT,
	min_a BIGINT,
	fgm_a DOUBLE PRECISION,
	fga_a DOUBLE PRECISION,
	fg_pct_a DOUBLE PRECISION,
	fg3m_a DOUBLE PRECISION,
	fg3a_a DOUBLE PRECISION,
	fg3_pct_a DOUBLE PRECISION,
	ftm_a DOUBLE PRECISION,
	fta_a DOUBLE PRECISION,
	ft_pct_a DOUBLE PRECISION,
	oreb_a DOUBLE PRECISION,
	dreb_a DOUBLE PRECISION,
	reb_a BIGINT,
	ast_a DOUBLE PRECISION,
	stl_a DOUBLE PRECISION,
	blk_a DOUBLE PRECISION,
	tov_a DOUBLE PRECISION,
	pf_a DOUBLE PRECISION,
	pts_a BIGINT,
	min_h BIGINT,
	fgm_h DOUBLE PRECISION,
	fga_h DOUBLE PRECISION,
	fg_pct_h DOUBLE PRECISION,
	fg3m_h DOUBLE PRECISION,
	fg3a_h DOUBLE PRECISION,
	fg3_pct_h DOUBLE PRECISION,
	ftm_h DOUBLE PRECISION,
	fta_h DOUBLE PRECISION,
	ft_pct_h DOUBLE PRECISION,
	oreb_h DOUBLE PRECISION,
	dreb_h DOUBLE PRECISION,
	reb_h BIGINT,
	ast_h DOUBLE PRECISION,
	stl_h DOUBLE PRECISION,
	blk_h DOUBLE PRECISION,
	tov_h DOUBLE PRECISION,
	pf_h DOUBLE PRECISION,
	pts_h BIGINT
);
CREATE TABLE seasons (
	season_id BIGINT PRIMARY KEY,
	season_name TEXT,
	season_type TEXT,
	season_year BIGINT,
	min DOUBLE PRECISION,
	fgm DOUBLE PRECISION,
	fga DOUBLE PRECISION,
	fg_pct DOUBLE PRECISION,
	fg3m DOUBLE PRECISION,
	fg3a DOUBLE PRECISION,
	fg3_pct DOUBLE PRECISION,
	ftm DOUBLE PRECISION,
	fta DOUBLE PRECISION,
	ft_pct DOUBLE PRECISION,
	oreb DOUBLE PRECISION,
	dreb DOUBLE PRECISION,
	reb DOUBLE PRECISION,
	ast DOUBLE PRECISION,
	stl DOUBLE PRECISION,
	blk DOUBLE PRECISION,
	tov DOUBLE PRECISION,
	pf DOUBLE PRECISION,
	pts DOUBLE PRECISION
);
CREATE TABLE season_team (
	team_id BIGINT REFERENCES teams(team_id),
	season_id BIGINT REFERENCES seasons(season_id),
	min DOUBLE PRECISION,
	fgm DOUBLE PRECISION,
	fga DOUBLE PRECISION,
	fg_pct DOUBLE PRECISION,
	fg3m DOUBLE PRECISION,
	fg3a DOUBLE PRECISION,
	fg3_pct DOUBLE PRECISION,
	ftm DOUBLE PRECISION,
	fta DOUBLE PRECISION,
	ft_pct DOUBLE PRECISION,
	oreb DOUBLE PRECISION,
	dreb DOUBLE PRECISION,
	reb DOUBLE PRECISION,
	ast DOUBLE PRECISION,
	stl DOUBLE PRECISION,
	blk DOUBLE PRECISION,
	tov DOUBLE PRECISION,
	pf DOUBLE PRECISION,
	pts DOUBLE PRECISION,
	PRIMARY KEY(team_id, season_id)
);
CREATE TABLE teams (
	team_id BIGINT PRIMARY KEY,
	team_name TEXT,
	abbreviation TEXT,
	foundation_year DOUBLE PRECISION,
	min DOUBLE PRECISION,
	fgm DOUBLE PRECISION,
	fga DOUBLE PRECISION,
	fg_pct DOUBLE PRECISION,
	fg3m DOUBLE PRECISION,
	fg3a DOUBLE PRECISION,
	fg3_pct DOUBLE PRECISION,
	ftm DOUBLE PRECISION,
	fta DOUBLE PRECISION,
	ft_pct DOUBLE PRECISION,
	oreb DOUBLE PRECISION,
	dreb DOUBLE PRECISION,
	reb DOUBLE PRECISION,
	ast DOUBLE PRECISION,
	stl DOUBLE PRECISION,
	blk DOUBLE PRECISION,
	tov DOUBLE PRECISION,
	pf DOUBLE PRECISION,
	pts DOUBLE PRECISION
);
CREATE TABLE game_player (
	player_id BIGINT REFERENCES players(player_id),
	team_id BIGINT REFERENCES teams(team_id),
	game_id BIGINT REFERENCES games(game_id),
	season_id BIGINT REFERENCES seasons(season_id),
	is_win BOOLEAN,
	min BIGINT,
	fgm BIGINT,
	fga DOUBLE PRECISION,
	fg_pct DOUBLE PRECISION,
	fg3m DOUBLE PRECISION,
	fg3a DOUBLE PRECISION,
	fg3_pct DOUBLE PRECISION,
	ftm DOUBLE PRECISION,
	fta DOUBLE PRECISION,
	ft_pct DOUBLE PRECISION,
	oreb DOUBLE PRECISION,
	dreb DOUBLE PRECISION,
	reb DOUBLE PRECISION,
	ast DOUBLE PRECISION,
	stl DOUBLE PRECISION,
	blk DOUBLE PRECISION,
	tov DOUBLE PRECISION,
	pf DOUBLE PRECISION,
	pts BIGINT,
	plus_minus DOUBLE PRECISION,
	PRIMARY KEY(player_id, game_id)
);
CREATE TABLE players (
	player_id BIGINT PRIMARY KEY,
	secondname_name TEXT,
	playercode TEXT,
	team_id BIGINT REFERENCES teams(team_id),
	rosterstatus TEXT,
	position TEXT,
	jersey DOUBLE PRECISION,
	season_exp BIGINT,
	from_year DOUBLE PRECISION,
	to_year DOUBLE PRECISION,
	draft_year DOUBLE PRECISION,
	draft_round DOUBLE PRECISION,
	height DOUBLE PRECISION,
	weight DOUBLE PRECISION,
	min DOUBLE PRECISION,
	fgm DOUBLE PRECISION,
	fga DOUBLE PRECISION,
	fg_pct DOUBLE PRECISION,
	fg3m DOUBLE PRECISION,
	fg3a DOUBLE PRECISION,
	fg3_pct DOUBLE PRECISION,
	ftm DOUBLE PRECISION,
	fta DOUBLE PRECISION,
	ft_pct DOUBLE PRECISION,
	oreb DOUBLE PRECISION,
	dreb DOUBLE PRECISION,
	reb DOUBLE PRECISION,
	ast DOUBLE PRECISION,
	stl DOUBLE PRECISION,
	blk DOUBLE PRECISION,
	tov DOUBLE PRECISION,
	pf DOUBLE PRECISION,
	pts DOUBLE PRECISION,
	plus_minus DOUBLE PRECISION
);
CREATE TABLE bets (
	game_id BIGINT REFERENCES games(game_id),
	bets_type TEXT,
	book_name TEXT,
	book_id BIGINT,
	away_team_id BIGINT REFERENCES teams(team_id),
	home_team_id BIGINT REFERENCES teams(team_id),
	points_1 DOUBLE PRECISION,
	points_2 DOUBLE PRECISION,
	price_1 DOUBLE PRECISION,
	price_2 DOUBLE PRECISION,
	PRIMARY KEY(game_id, bets_type, book_id)
);
CREATE TABLE messages (
    message_id BIGINT,
    message_version BIGINT,
    chat_id BIGINT,
    text TEXT,
    buttons_names TEXT,
    buttons_callbacks TEXT,
    date_time TIMESTAMP WITH TIME ZONE,
    is_available BOOLEAN,
    PRIMARY KEY(message_id, message_version, chat_id)
);
