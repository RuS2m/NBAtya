import sys

from telegram.ext import CommandHandler, Updater, CallbackQueryHandler

from config import BotConfig
from controller.controller import *
from database_connect import engine, Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    updater = Updater(token=BotConfig.token)
    dispatcher = updater.dispatcher
    try:
        dispatcher.add_handler(CommandHandler(command='start', callback=start))
        dispatcher.add_handler(CommandHandler(command='seasons', callback=seasons))
        dispatcher.add_handler(CommandHandler(command='teams', callback=teams))
        dispatcher.add_handler(CommandHandler(command='stat', callback=popup_statistics))
        dispatcher.add_handler(CommandHandler(command='tms', callback=teams_in_season_link))
        dispatcher.add_handler(CommandHandler(command='sns', callback=season_with_team_link))
        dispatcher.add_handler(CommandHandler(command='origin', callback=go_to_origin))
        dispatcher.add_handler(CallbackQueryHandler(seasons_navigation_button, pattern=r"sn_pg"))
        dispatcher.add_handler(CallbackQueryHandler(teams_navigation_button, pattern=r"tm_pg"))
        dispatcher.add_handler(CallbackQueryHandler(teams_in_seasons_navigation_button, pattern=r"tmsn_pg"))
        dispatcher.add_handler(CallbackQueryHandler(seasons_with_team_navigation_button, pattern=r"sntm_pg"))
        dispatcher.add_handler(CallbackQueryHandler(season_button, pattern=r"sn_"))
        dispatcher.add_handler(CallbackQueryHandler(team_button, pattern=r"tm_"))
        dispatcher.add_handler(CallbackQueryHandler(team_in_season_button, pattern=r"tmsn_"))
        dispatcher.add_handler(CallbackQueryHandler(season_with_team_button, pattern=r"sntm_"))
        dispatcher.add_handler(CallbackQueryHandler(back_button, pattern=r"b_"))
        dispatcher.add_error_handler(error)
        updater.start_polling(allowed_updates=True)
        updater.idle()
    except KeyboardInterrupt:
        sys.exit(0)
