import logging

"""
This symbol does not displays in telegram, but also does not considered empty,
so it can be passed as message
"""
def invisible_character() -> str:
    return u'\u2061'


def add_handlers(dispatcher, handlers):
    for handler in handlers:
        dispatcher.add_handler(handler)


def get_logger():
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    return logger
