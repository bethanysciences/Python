#!/usr/bin/env python3
# https://forecast-v3.weather.gov/documentation

import arrow
import json
import requests
import xml.etree.ElementTree as ET

site = 'https://www.aviationweather.gov'
product = '/adds/dataserver_current/httpparam?'
payload = {'dataSource': 'metars',
           'requestType': 'retrieve',
           'format': 'xml',
           'stationString': 'KAPA',
           'hoursBeforeNow': '1'
           }

murl = site + product

curr = requests.get(murl, params=payload)
# print(r.text)
root = ET.fromstring(curr.text)
for METAR in root.iter('METAR'):
    cur_statn = METAR.find('station_id')
    cur_obstZ = METAR.find('observation_time')
    cur_tempC = METAR.find('temp_c')
    cur_dewpC = METAR.find('dewpoint_c')
    cur_windK = METAR.find('wind_speed_kt')
    cur_windr = METAR.find('wind_dir_degrees')
    cur_barMB = METAR.find('sea_level_pressure_mb')

cur_tempF = int(float(cur_tempC.text)*1.8 + 32)
cur_dewpF = int(float(cur_dewpC.text)*1.8 + 32)
cutc = arrow.get(cur_obstZ.text)
cur_obstL = cutc.to('US/Mountain')

print('----------------')
print('Current conditions for station '
      + cur_statn.text
      + ' updated '
      + str(cur_obstL.humanize()) + ' at '
      + str(cur_obstL.format('h:mmA on dddd MMM Do, YYYY')))

print("{0:<15} {1:<10}".format('Temperature', str(cur_tempF) + '°f'))
print("{0:<15} {1:<10}".format('Dew Point', str(cur_dewpF) + '°f'))
print("{0:<15} {1:<10}".format('Wind Speed', cur_windK.text + ' knots'))
print("{0:<15} {1:<10}".format('From', str(cur_windr.text) + '°'))
print("{0:<15} {1:<10}".format('Barometer', cur_barMB.text + 'mb'))


# forecast

site = 'https://api.weather.gov'
location = 'points/33.8774,-84.3046'
report = 'forecast'
furl = site+'/'+location+'/'+report

headers = {'Accept': 'application/ld+json',
           'User-Agent': 'bob@bethanysciences.net/pyth01'
           }
# fcst = requests.get(furl, params=headers)

fcst = requests.get(furl)

obj = json.loads(fcst.text)

gnrted = obj['properties']['generatedAt']
Perd_0 = obj['properties']['periods'][0]['name']
Perd_9 = obj['properties']['periods'][9]['name']
top = 'NOAA Weather Report Covering '
futc = arrow.get(gnrted)
flocal = futc.to('US/Mountain')

print('----------------')
print(top+Perd_0+' thru '+Perd_9+' updated '
      + str(flocal.humanize()) + ' at '
      + str(flocal.format('h:mmA on dddd MMM Do, YYYY')))

for x in range(0, 9):
    print("{0:<15} {1:<10} {2:<5}".format(
          obj['properties']['periods'][x]['name'],
          str(obj['properties']['periods'][x]['temperature']) + '°f',
          obj['properties']['periods'][x]['shortForecast']))
