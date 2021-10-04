import discord
import os
import requests
import json
import locale

from liveserver import liveserver
from datetime import datetime
locale.setlocale(locale.LC_ALL, '')

today = datetime.today().strftime('%YY-%MM-%DD')

stat = ["cuy/status", "cuy/stat", "cuy/st", "cuy/stats", "cuy/test", "cuy/ping", "cuy/p"]
welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai", "cuy/oy", "cuy/helo"]

client = discord.Client()

def get_lirik(lagu):
  list_lagu = requests.get('https://api-song-lyrics.herokuapp.com/search?q=' + lagu)
  datas = json.loads(list_lagu.text)
  lirik = datas['data']
  if len(lirik) > 1:
    return('liriknya banyak')
  else:
    for data in lirik:
      liriks = data['songLyrics']
      result = lirik_detail(liriks)
    return(result)

def lirik_detail(link):
  lirik = requests.get(link)
  json_data = json.loads(lirik.text)
  lirik_asli = json_data['data']['songLyrics']
  return(lirik_asli)

def get_covid_data(args, params, child):
  response = requests.get('https://data.covid19.go.id/public/api/update.json')
  json_data = json.loads(response.text)
  data = ''
  if args != '' and params != '' and child != '':
   data = json_data[args][params][child]
  elif args != '' and params != '' and child == '':
   data = json_data[args][params]
  else:
    data = json_data[args]
  return(data)

@client.event
async def on_ready():
  print('logged in as {0.user} '.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  req_msg= message.content
  bot_response = message.channel.send

  if any(word in req_msg for word in stat):
    await bot_response(':partying_face: CuyBot Masih Aktif! :partying_face:')

  if any(x in req_msg for x in welcome):
    await bot_response(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')

  if req_msg.startswith('cuy/lirik'):
    requested_song = req_msg.split(" ", 1)[1]
    daftar_lagu = get_lirik(requested_song)
    # lirik_lagu = lirik_detail(daftar_lagu)
    await bot_response(daftar_lagu)

  if req_msg.startswith('cuy/covid'):
    odp = get_covid_data('data','jumlah_odp','')
    total_spesimen_negatif = get_covid_data('data', 'total_spesimen_negatif', '')
    total_positif = get_covid_data('update', 'penambahan', 'jumlah_positif')
    total_dirawat =   get_covid_data('update', 'penambahan','jumlah_dirawat')
    total_sembuh = get_covid_data('update', 'penambahan','jumlah_sembuh')
    total_meninggal = get_covid_data('update', 'penambahan','jumlah_meninggal')
    update_per = get_covid_data('update', 'penambahan', 'created')
    data_from = 'https://data.covid19.go.id'

    await bot_response(':flag_mc: ***DATA COVID*** :flag_mc:\nUPDATE PER: ' + update_per + ' :date:\n' + ':warning: Data Resmi Dari: ' + data_from + ' :warning:\n\n' + 'Total ODP saat ini: **' + f'{odp:,}' + '** orang :thermometer_face:' + "\n" + 'Total spesimen negatif: **' + f'{total_spesimen_negatif:,}' + '** orang :thinking:' + '\n' + 'total positif: **' + f'{total_positif:,}' + '** orang :persevere:' + '\n' + 'Total sembuh: **' + f'{total_sembuh:,}' + '** orang :hugging:' + '\n' + 'Total meninggal: **' + str(total_meninggal) + '** orang :cry:' + '\n\n' + '---TERIMAKASIH CUYBOT--- :laughing:')

  if req_msg.startswith('cuy/cuaca'):
    print('cari prediksi cuaca hari ini')
    await bot_response('ramalan cuaca: ' + req_msg)

liveserver()
client.run(os.getenv('TOKEN'))