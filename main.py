import os
import locale
import constants as c
from botReply import botReply

from liveserver import liveserver
locale.setlocale(locale.LC_ALL, '')

@c.client.event
async def on_ready():
  print('logged in as {0.user} '.format(c.client))

botReply()

liveserver()
c.client.run(os.getenv('TOKEN'))