import os
import locale
import helper.constants as c

from response.status import status
from response.welcome import welcome
from response.covid import covid
from response.quote import quote
from response.cuaca import cuaca

from config.liveserver import liveserver
locale.setlocale(locale.LC_ALL, '')

@c.client.event
async def on_ready():
    print('logged in as {0.user} '.format(c.client))

@c.client.event
async def on_message(message):
  if message.author == c.client.user:
    return

  user_message = message.content
  bot_send = message.channel.send

  await status(user_message, bot_send)
  await welcome(user_message, bot_send)
  await covid(user_message, bot_send)
  await quote(user_message, bot_send)
  await cuaca(user_message, bot_send)

liveserver()
c.client.run(os.getenv('TOKEN'))
