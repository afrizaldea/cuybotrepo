import helper.constants as c
import api.data_quote as api


class quote(object):
    def __init__(self, user_message, bot_send):
        if user_message.startswith('cuy/quotes'):
            data = api.get_quotes()
            return bot_send(data)
