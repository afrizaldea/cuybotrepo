import os
import locale

from liveserver import liveserver
import constants as c
import api as api

locale.setlocale(locale.LC_ALL, '')

@c.client.event
async def on_ready():
  print('logged in as {0.user} '.format(c.client))

@c.client.event
async def on_message(message):
  if message.author == c.client.user:
    return

  req_msg= message.content
  bot_response = message.channel.send

  if any(word in req_msg for word in c.request_stat):
    await bot_response(':partying_face: CuyBot Masih Aktif! :partying_face:')

  if any(x in req_msg for x in c.request_welcome):
    await bot_response(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')

  if req_msg.startswith('cuy/lirik'):
    requested_song = req_msg.split(" ", 1)[1]
    daftar_lagu = api.get_lirik(requested_song)
    # lirik_lagu = lirik_detail(daftar_lagu)
    await bot_response(daftar_lagu)

  if req_msg.startswith('cuy/covid'):
    odp = api.get_covid_data('data','jumlah_odp','')
    total_spesimen_negatif = api.get_covid_data('data', 'total_spesimen_negatif', '')
    total_positif = api.get_covid_data('update', 'penambahan', 'jumlah_positif')
    total_sembuh = api.get_covid_data('update', 'penambahan','jumlah_sembuh')
    total_meninggal = api.get_covid_data('update', 'penambahan','jumlah_meninggal')
    update_per = api.get_covid_data('update', 'penambahan', 'created')

    await bot_response(':flag_mc: ***DATA COVID*** :flag_mc:\nUPDATE PER: ' + update_per + ' :date:\n' + ':warning: Data Resmi Dari: ' + c.data_covid_from + ' :warning:\n\n' + 'Total ODP saat ini: **' + f'{odp:,}' + '** orang :thermometer_face:' + "\n" + 'Total spesimen negatif: **' + f'{total_spesimen_negatif:,}' + '** orang :thinking:' + '\n' + 'total positif: **' + f'{total_positif:,}' + '** orang :persevere:' + '\n' + 'Total sembuh: **' + f'{total_sembuh:,}' + '** orang :hugging:' + '\n' + 'Total meninggal: **' + str(total_meninggal) + '** orang :cry:' + '\n\n' + '---TERIMAKASIH CUYBOT--- :laughing:')

  if req_msg.startswith('cuy/cuaca'):
    print('request => ' + req_msg)
    data = api.get_cuaca('hari ini')
    await bot_response(data)

liveserver()
c.client.run(os.getenv('TOKEN'))