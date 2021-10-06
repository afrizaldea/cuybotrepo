import helper.constants as c

class status:
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def status_cuy(self):
    if any(word in self.user_message for word in c.request_stat):
      return await self.bot_send(':partying_face: CuyBot Masih Aktif! :partying_face:')