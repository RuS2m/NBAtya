from telegram.ext import CommandHandler, Updater, CallbackQueryHandler

from config import BotConfig
from controller.controller import *
from database_connect import engine, Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    updater = Updater(token=BotConfig.token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(command='start', callback=start))
    dispatcher.add_handler(CommandHandler(command='seasons', callback=seasons))
    dispatcher.add_handler(CallbackQueryHandler(seasons_navigation_button, pattern=r"sn_pg"))
    dispatcher.add_handler(CallbackQueryHandler(season_button, pattern=r"sn_"))
    dispatcher.add_error_handler(error)
    updater.start_polling(poll_interval=1)
    updater.idle()
