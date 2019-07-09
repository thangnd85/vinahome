#!/usr/bin/env python3

# -*- coding: utf-8 -*-
from helper import *
apikeyds = gih.get_config('api_darksky')

def darksky_weather():
	apikey = apikeyds
	Lisbon = [10, 106]

	fio = ForecastIO.ForecastIO(apikey,
	                            units=ForecastIO.ForecastIO.UNITS_SI,
	                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
	                            latitude=Lisbon[0], longitude=Lisbon[1])
	return fio
def darksky_currently(fio):
	if fio.has_currently() is True:
		currently = FIOCurrently.FIOCurrently(fio)

		for item in currently.get().keys():
			if item == 'humidity':
					hum = str(round(currently.get()[item]*100,1))
					hum = hum.replace('.',',')
					humidity= ('Hiện tại Độ ẩm là '+ hum + ' phần trăm. ' )
#                    humidity = humidity.replace('.',',')
			elif item == 'temperature':
					temp = str(round(currently.get()[item],1))
					temp = temp.replace('.',',')
					temperature=('Nhiệt độ là '+ temp + ' độ. ' )
#                    temperature=temperature.replace('.',',')
			elif item == 'icon':
					icon = (str(currently.get()[item]))
		return humidity,temperature,icon

def darksky_hourly(fio):
	                            
	if fio.has_hourly() is True:
		hourly = FIOHourly.FIOHourly(fio)
		translator = Translator()
		a = translator.translate(hourly.summary, dest = 'vi')
		a = 'thời tiết trong 48 giờ tới. '+ a.text

		return a
		
		# for hour in range(0, hourly.hours()):
		# 	print ('Hour', hour+1)
		# 	for item in hourly.get_hour(hour).keys():
		# 		print (item + ' : ' + str(hourly.get_hour(hour)[item]))
			
		# 	# Or access attributes directly for a given minute. 
		# 	# hourly.hour_5_time would also work
		# 	print (hourly.hour_3_time)

	else:
		print ('No Hourly data')
def darksky_daily(fio):
	if fio.has_daily() is True:
		daily = FIODaily.FIODaily(fio)
		translator = Translator()
		a = translator.translate(daily.summary, dest = 'vi')
		a = 'thời tiết trong 7 ngày tới. '+ a.text
		print(a)
		return a

def darksky_according_hours(fio,hours):
	hourly = FIOHourly.FIOHourly(fio)
	for hour in range(0, hourly.hours()):
		if hour+1 == hours:
			print('hour'+ str(hour+1))
			for item in hourly.get_hour(hour).keys():
				if item == 'humidity':
					humidity= ('Trong '+ str(hour+1)+ ' giờ tới '+ 'Độ ẩm là'+ ' : '+ str(hourly.get_hour(hour)[item]*100) + ' phần trăm ' )
				elif item == 'temperature':
					temperature=('Nhiệt độ là'+ ' : '+ str(hourly.get_hour(hour)[item])  )
				elif item == 'icon':
					icon = (str(hourly.get_hour(hour)[item]))
					if icon == 'rain':
						icon = 'mưa'
					elif icon == 'partly-cloudy-night':
						icon = 'buổi tối trời nhiều mây'
					elif icon == 'clear-day':
						icon = 'trời trong xanh'
					elif icon == 'clear-night':
						icon = 'đêm trời đẹp'
					elif icon == 'wind':
						icon = 'có gió lớn'
					elif icon == 'cloudy':
						icon = 'trời nhiều mây'
					elif icon == 'fog':
						icon = 'trời nhiều sương mù'

					# translator = Translator()
					# icon1 = translator.translate(icon,dest ='vi')
	return humidity, temperature, icon








			







