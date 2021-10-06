import helper.constants as c

class welcome(object):
    async def __init__(self, user_message, bot_send):
        if any(x in user_message for x in c.request_welcome):
            await bot_send(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')