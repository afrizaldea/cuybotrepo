import requests
import json
import random

def get_cuaca(param):
  return 'get ramalan cuaca' + param

def get_lirik(lagu):
  list_lagu = requests.get('https://api-song-lyrics.herokuapp.com/search?q=' + lagu)
  datas = json.loads(list_lagu.text)
  lirik = datas['data']
  if len(lirik) > 1:
    return('mohon judul lebih spesifik lagi, terlalu banyak list (fitur masih ongoing cuy).\ncoba cari misalnya cuy/lirik kala cinta menggoda')
  elif len(lirik) == 1:
    for data in lirik:
      liriks = data['songLyrics']
      result = lirik_detail(liriks)
      return(result)
  else:
    return('maaf gw kurang paham cuy, cari lirik lainnya ya. jangan lupa pake command\ncuy/lirik [nama lagu selengkap lengkapnya, kalau bisa nama band nya juga masukin]')

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

def get_quotes():
  response = requests.get('https://backend-ihsandevs.herokuapp.com/api/quotes%20keren/')
  json_data = json.loads(response.text)
  random_length = random.randint(0,len(json_data['result']) - 1)
  tokoh_quotes = json_data['result'][random_length]
  responseQuotes = requests.get('https://backend-ihsandevs.herokuapp.com/api/quotes%20keren/?name=' + tokoh_quotes)
  json_data_quotes = json.loads(responseQuotes.text)
  random_length_quotes = random.randint(0,len(json_data_quotes['result']) - 1 )
  quotes = json_data_quotes['result'][random_length_quotes]
  return(quotes)