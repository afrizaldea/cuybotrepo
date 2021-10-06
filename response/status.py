import helper.constants as c

class status(object):
    def __init__(self, user_message, bot_send):
        if any(word in user_message for word in c.request_stat):
            return bot_send(':partying_face: CuyBot Masih Aktif! :partying_face:')