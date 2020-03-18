#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
import queue
import urllib.request
import urllib.parse
import gih
import chsv
import processss
import onoff
import random
import speaking
import ptz
import time
import amlich
import thu
import ngayle
import tintuc
import loto 
import fun 
import execute
import re 
import radio 
import weth
import wk
import spot
import speech_recognition as sr
import wether as wt
from pygame import mixer
spotify = gih.get_config('spotify')
spotify_username = gih.get_config('spotify_username')
spotify_client_id = gih.get_config('spotify_client_id')
spotify_client_secret = gih.get_config('spotify_client_secret')
def recordAudio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	data = ""
	try:
		data = r.recognize_google(audio, language = "vi-VN")
		print('BOT nghe được: '+ data)
	except sr.UnknownValueError:	
		print('Sao bạn không nói gì')
		data ='ĐƯỢC RỒI'
		pass
	except sr.RequestError as e:
		print('èo èo'+ e)
		pass
	return data
def recordFPT():
#	print ('FPT')
	r = sr.Recognizer()
	import random
#	print ('FPT1')
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	with open('tmp/record.wav', "wb") as f:
		f.write(audio.get_wav_data())
	data = ""
	keys = ['Os1MlynwG2W7eNFecfME0EOHZ9hCcobk','hFewll7iiYesYsc5TQO9RyPWogvYGXff','1E9dz9Oyax0WFbqVxIsBQSTuCf04yA6I']
	api_fpt_key = random.choice(keys)
#	print (api_fpt_key)
	try:
		import requests
		url = 'https://api.fpt.ai/hmi/asr/general'
		payload = open('tmp/record.wav', 'rb').read()
		headers = {'api-key': api_fpt_key}
		response = requests.post(url=url, data=payload, headers=headers)
		txt = response.json()
#		print (txt)
		import json
		for element in txt['hypotheses']:
			data = element['utterance']	
#	print(response.json())
#		data = r.recognize_google(audio, language = "vi-VN")
		print('BOT nghe được: '+ data)
	except sr.UnknownValueError:	
		print('Sao bạn không nói gì')
		data ='ĐƯỢC RỒI'
		pass
	except sr.RequestError as e:
		print('èo èo'+ e)
		pass
	return data
def recordVTCC():
	import requests
	from pathlib import Path
	import os.path
	import speech_recognition as sr
	r = sr.Recognizer()
	dirname = os.path.dirname(os.path.abspath('_file_'))
	path = os.path.dirname(os.path.abspath('_file_'))
	url = "https://vtcc.ai/voice/api/asr/v1/rest/decode_file"
	headers = {
		'token': 'OOGW-uNFk3vFBoZ3T9BDp9OZLWeFmPcxxGHkqMHpjqXXF9oIuExGs5pSbsWv7jMM',
		#'sample_rate': 16000,
		#'format':'S16LE',
		#'num_of_channels':1,
		#'asr_model': 'mode
		# l code'
	}
	s = requests.Session()
	cert_path = (dirname+'/wwwvtccai.crt')
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	with open('tmp/vtcc.wav', "wb") as f:
		f.write(audio.get_wav_data())
	try:
		files = {'file': open('tmp/vtcc.wav', 'rb')}
		response = requests.post(url,files=files, headers=headers, verify=cert_path, timeout=None)
		txt = response.json()
		if len(t) > 0:
			t = txt[0]
			text = t['result']
			import json
			for element in text['hypotheses']:
				data = element['transcript']	
				print('BOT nghe được: '+ data)
		else:
			data = 'cảm ơn'
			print('không nghe thấy gì')
	except:
		print('Lỗi Viettel')
		pass
	return data
def answer(ans1,ans2,ans3):
	caunoi=[ans1,ans2,ans3]
	spea=random.choice(caunoi)
	speaking.speak(spea)
def hamthucthi(row0_in_db,data,friendly_name_hass,sta):
	global player
	print('[MAIN] - THỰC THI TÁC VỤ')
	print('---------')
	processss.timlenhtrongdata(data)
	if row0_in_db== "KHỎE KHÔNG":
		answer("tôi khỏe.","khỏe lắm chủ nhân","khỏe chứ chủ nhân.")
#camera - dieu khien xoay
	elif row0_in_db == "CAMERA":
		print('vao camera')
		a=ptz.control('http://192.168.9.121','admin','Emilybro2013')
		datapreset=data
		datapreset=datapreset.split()
		iiii=0
		while iiii < len(datapreset):
			if datapreset[iiii].isnumeric() ==True:
				preset_number=datapreset[iiii]
				break
			else:
				iiii+=1
		try:
			a.set_preset(preset_number)
		except:
			pass
		if 'LÊN' in data.upper():
			print('vao len')
			a.len()
			time.sleep(2)
			return
		if 'XUỐNG' in data.upper():
			a.xuong()
			time.sleep(2)
			return
		if 'TRÁI' in data.upper():
			a.trai()
			time.sleep(2)
			return
		if 'PHẢI' in data.upper():
			a.phai()
			time.sleep(2)
			return				  
# Âm lịch
	elif row0_in_db == "ÂM LỊCH":
		check_day=[]
		if 'MAI' in data:
			check_day=amlich.ngaymai()
		elif 'MỐT' in data:
			check_day=amlich.ngaymot()
		elif 'QUA' in data:
			check_day=amlich.homqua()
		elif 'NAY' in data:
			check_day=amlich.homnay()
		else:
			check_day=amlich.ngaykhac(data)
		amlich.kiemtra_amlich(check_day[0],check_day[1],check_day[2],check_day[3],check_day[4])
#Hỏi thứ
	elif row0_in_db == "THỨ MẤY":
		check_thu=[]
		if 'MAI' in data:
			check_thu=thu.ngaymai()
		elif 'MỐT' in data:
			check_thu=thu.ngaymot()
		elif 'QUA' in data:
			check_thu=thu.homqua()
		elif 'NAY' in data:
			check_thu=thu.homnay()
		else:
			check_thu=thu.ngaykhac(data)
		result_thu=thu.kiemtra_thu(check_thu[0],check_thu[1],check_thu[2],check_thu[3],check_thu[4])
		speaking.speak(result_thu[0]+" là " + result_thu[1] +  result_thu[2] + ' tháng '+ str(result_thu[3]))
# Ngày lễ
	elif row0_in_db == "NGÀY LỄ":
		ngayle_res=[]
		ngayle_res=ngayle.ngayle_check(data)
		speaking.speak(ngayle_res[0] + ' Còn '+str(ngayle_res[1])+' ngày nữa là đến '+ngayle_res[2]  + '. Đó là ngày '+ngayle_res[3] +' tháng '+ngayle_res[4] +' năm '+ngayle_res[5] )
#Cảm ơn	
	elif row0_in_db == "CẢM ƠN":
		answer('không có chi. ','rất vui vì giúp được chủ nhân ',' đừng bận tâm ')
#HELP
	elif row0_in_db == "TRỢ GIÚP":
		if 'THỜI TIẾT' in data:
			speaking.speak('Có thể hỏi các câu hỏi bao gồm các từ như, Thời tiết hôm nay, ngày mai')
		elif 'GIỜ' in data:
			speaking.speak('Đặt câu hỏi mấy giờ rồi')
		elif 'NGÀY' in data:
			speaking.speak('Hỏi thứ mấy, ngày nào. Có thể hỏi ngày mai là thứ mấy, ngày 30 tháng 4 là thứ mấy, vv.')
		elif 'ÂM LỊCH' in data:
			speaking.speak('Hỏi âm lịch hôm nay, ngày mai, ngày bất kì')
		elif 'DỊCH' in data:
			speaking.speak('Dịch từ tHoặc dịch cả câu với cấu trức: Dịch câu sau sang tiếng nào đó. Sau đó chờ âm báo rồi đọc câu. Ngôn ngữ hỗ trợ: Việt, chủ nhân, Trung, Nhật, Hàn.')
		elif 'THÔNG TIN' in data:
			speaking.speak('Có thể hỏi thông tin bằng câu với kết thúc là gì hoặc là ai. Ví dụ, Hồ Chí Minh là ai.')		
		elif 'LỆNH' in data:
			speaking.speak('Có thể bật, tắt, điều chỉnh nhiệt độ máy lạnh .... bằng các câu lệnh đơn giản như: bật đèn, tắt đèn, ....')
		elif 'NHẠC' in data:
			speaking.speak('Dùng lệnh Phát rồi gọi tên bài hát, playlist muốn nghe. Muốn qua bài thì dùng lệnh Tiếp theo. Dừng với lệnh Dừng nhạc')
		elif 'HẸN GIỜ' in data:
			speaking.speak('Dùng lệnh hẹn giờ cộng thời gian, hủy với lệnh hủy hẹn giờ')
		elif 'NGÀY LỄ' in data:
			speaking.speak('Hỏi còn bao nhiêu ngày nữa là đến ngày lễ. Các ngày lễ có sẵn bao gồm, Tết Tây, Tết ta, 30 tháng 4, trung thu, giỗ tổ, quốc khánh. ')
		else:
			speaking.speak('Các lệnh thường dùng, Hỏi giờ, thời tiết, thứ ngày tháng, thông tin, lệnh, phát nhạc, hẹn giờ, dịch từ, dịch câu, âm lịch, ngày lễ. Dùng lệnh trợ giúp kèm theo các lệnh muốn tra cứu để được hướng dẫn chi tiết hơn.')
#Hỏi giờ
	elif row0_in_db == "MẤY GIỜ":
		import speaking
		from time import ctime, strftime
		gio = strftime("%H")
		gio = list(gio)
		phut=strftime("%M")
		phut=list(phut)
		if gio[0]=='1':
			if gio[1]=='0':
				docgio='mười giờ '
			else:
				docgio='mười '+gio[1]+ ' giờ '
		elif gio[0]=='0':
			docgio= gio[1] +' giờ '
		elif gio[0]=='2':
			if gio[1]=='0':
				docgio='hai mươi giờ '
			elif gio[1]=='1':
				docgio='hai mươi mốt giờ '
			else:
				docgio='hai mươi '+ gio[1] + ' giờ '
		
		if phut[0]=='0':
			docphut = phut[1]+ ' phút '
		elif phut[0]=='1':
			if phut[1]=='0':
				docphut= ' mười phút '
			else:
				docphut = ' mười '+ phut[1]+ ' phút '
		else:
			if phut[1]=='0':
				docphut=phut[0] + ' mươi phút '
			elif phut[1]=='1':
				docphut=phut[0] + ' mươi mốt phút '
			else:
				docphut = phut[0]+ ' mươi '+ phut[1]+ ' phút '
		speaking.speakvn("BÂY GIỜ LÀ " + docgio + docphut)
#Tin tức (TTS)
	elif row0_in_db == "TIN TỨC":
		tintuc.tintucmoi()
	elif row0_in_db == "XỔ SỐ":
		print ('Kết quả xổ số')
		loto.check(data)
#Truyện cười	
	elif row0_in_db == "CƯỜI":
		truyen = fun.truyen()
		speaking.speak(truyen)
	elif row0_in_db == "RADIO":
		try:
			player.stop()
		except:
			pass
		player=radio.phat_radio(data)
	elif row0_in_db=="ĐI NGỦ":
		pass
	elif row0_in_db=="LÀ GÌ":
		def wifi(data):
			data = data[0:len(data)-6]
			rep = wk.find_info(data)
			rep = rep.find_wiki()
			speaking.speak('Theo wikipedia: '+rep)
		speaking.speak('để tôi tìm xem nào')
		execute.run_thread(wifi,data) 
# Phát video
	elif row0_in_db=="PHÁT" :
		if spotify == 1:
			global spotipy
			try:
				player.stop()
			except:
				pass
			spotipy=spot.play_current_playlist(spotify_username,spotify_client_id,spotify_client_secret,'http://localhost:9999/',data)
		if spotify == 0:
			global link_yt
			try:
				we.put('quit')
				w.put('quit')
				wet.put('quit')
			except:
				print('er put')
			we=queue.Queue()
			locationtim=data.find('PHÁT')
			data=data[locationtim+5:len(data)]
			query_string = urllib.parse.urlencode({"search_query" : data})
			html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
			random_song=random.randint(0,10)
			urlyt="http://www.youtube.com/watch?v=" + search_results[random_song]
			search_pre_write = (search_results[0],search_results[1],search_results[2],search_results[3],search_results[4],search_results[5],search_results[6],search_results[7],search_results[8],search_results[9],search_results[10],random_song)
			import speaking
			import threading
			import vlc
			import pafy
			import gih
			speaking.speakvn('Chuẩn bị phát nhạc')
			def yt_play(urlyt,we):  
				try:
					video = pafy.new(urlyt)
					best = video.getbestaudio()
					playurl = best.url
					Instance = vlc.Instance()
					player = Instance.media_player_new()
					Media = Instance.media_new(playurl)
					Media.get_mrl()
					player.set_media(Media)
					player.play()
					we.put('start')
					m= alsaaudio.Mixer()
					vol = m.getvolume()
					vol = int(vol[0])
					player_volume = vol
					player.audio_set_volume(player_volume)
					while True: 
						player.play()
						item = we.get()
						if item == 'quit':
							player.stop()
							break
						if item == 'listen_mode':
							m= alsaaudio.Mixer()
							vol = m.getvolume()
							vol = int(vol[0])
							player_volume = vol
							player.audio_set_volume(player_volume - 35)
						if item == 'normal_mode':
							m= alsaaudio.Mixer()
							vol = m.getvolume()
							vol = int(vol[0])
							player_volume = vol
							player.audio_set_volume(player_volume - 35)
							time.sleep(0.7)
							player.audio_set_volume(player_volume - 25)
							time.sleep(0.7)
							player.audio_set_volume(player_volume - 15)
							time.sleep(0.7)
							player.audio_set_volume(player_volume)
				except Exception as e:
					print('error vlc')
					print(e)
			t=threading.Thread(target = yt_play, args = (urlyt,we))
			t.start()
			link_yt = gih.info_user()
			with link_yt:
				link_yt_ex = link_yt.cursor()
				link_yt_ex.execute("INSERT INTO link_music_youtube VALUES(?,?,?,?,?,?)",search_pre_write)
		else:
			player= radio.play_nhac(data,friendly_name_hass)
			player.play()
	elif row0_in_db=="TIẾP THEO":
		if spotify == 1:
			try:
				player.stop()
			except:
				pass
			spotipy=spot.play_current_playlist(spotify_username,spotify_client_id,spotify_client_secret,'http://localhost:9999/',data)
		else:
			player=radio.phat_tiep_theo()
# Google word translate
	elif row0_in_db=="CÓ NGHĨA" :
		from googletrans import Translator
		translator = Translator()
		print (data)
		data = data.replace('TỪ ','')
		data = data.replace('TRONG ','')
#		print ('Edit ' + data)
# To Vietnamese
		if 'VIỆT' in data:
			m = re.search ('(.+?) TIẾNG VIỆT', data)
			dataen = m.group(1)
			print (dataen)
			translations = translator.translate (dataen, dest = 'vi')
			print (translations.text)
			speaking.speak('Từ ')
			speaking.speaken (dataen)
			speaking.speak('trong tiếng việt nghĩa là: '+ translations.text)		
#To English
		elif 'TIẾNG chủ nhân' in data:
			m = re.search ('(.+?) TIẾNG chủ nhân', data)
			dataen = m.group(1)
			print (dataen)
			translations = translator.translate (dataen, dest = 'en')
			print (translations.text)
			speaking.speak ('Từ '+dataen +' trong tiếng chủ nhân nghĩa là: ')
			speaking.speaken(translations.text)
# To Korean
		elif 'TIẾNG HÀN' in data:
			m = re.search ('(.+?) TIẾNG HÀN', data)
			dataen = m.group(1)
			print (dataen)
			translations = translator.translate (dataen, dest = 'ko')
			print (translations.text)
			speaking.speak ('Từ '+dataen +' trong tiếng Hàn nghĩa là: ')
			speaking.speakko(translations.text)
# To Japanese
		elif 'TIẾNG NHẬT' in data:
			m = re.search ('(.+?) TIẾNG NHẬT', data)
			dataen = m.group(1)
			print (dataen)
			translations = translator.translate (dataen, dest = 'ja')
			print (translations.text)
			speaking.speak ('Từ '+dataen +' trong tiếng Nhật nghĩa là: ')
			speaking.speakja(translations.text)
# To Chinese
		elif 'TIẾNG TRUNG' in data:
			m = re.search ('(.+?) TIẾNG TRUNG', data)
			dataen = m.group(1)
			print (dataen)
			translations = translator.translate (dataen, dest = 'zh-cn')
			print (translations.text)
			speaking.speak ('Từ '+dataen +' trong tiếng TRUNG nghĩa là: ')
			speaking.speakzh(translations.text)
# Google sentence translate
	elif row0_in_db=="DỊCH CÂU" :
		from googletrans import Translator
		translator = Translator()
		continue_go=1
		speaking.speak ('OK, đọc câu cần dịch đi chủ nhân')
		processss.mixer.music.load('resources/ding.wav')
		processss.mixer.music.play()
		more_data = processss.re_ask()
		print (more_data)		
		if len(more_data) > 0:
			while True:
				print ('Google translate: '+data)
				print ('Data translate: '+more_data)
				processss.mixer.music.load('resources/dong.wav')
				processss.mixer.music.play()
				if 'TIẾNG ANH' in data:
					translations = translator.translate (more_data, dest = 'en')
					print (translations.text)
					speaking.speaken(translations.text)
					continue_go = 1
				if 'TIẾNG VIỆT' in data:
					translations = translator.translate (more_data, dest = 'vi')
					print (translations.text)
					speaking.speak(translations.text)
					continue_go = 1
				if 'TIẾNG HÀN' in data:
					translations = translator.translate (more_data, dest = 'ko')
					print (translations.text)
					speaking.speakko(translations.text)
					continue_go = 1
				if 'TIẾNG TRUNG' in data:
					translations = translator.translate (more_data, dest = 'zh-cn')
					print (translations.text)
					speaking.speakzh(translations.text)
					continue_go = 1
				if 'TIẾNG NHẬT' in data:
					translations = translator.translate (more_data, dest = 'ja')
					print (translations.text)
					speaking.speakja(translations.text)
					continue_go = 1
				if 'HỦY' in more_data:
					speaking.speak('thoát khỏi chế độ dịch')
					continue_go = 0
					break
				else:
					break
		else:
			speaking.speakvn('Xin lỗi, tôi không nghe được câu hỏi')
# Hẹn giờ		
	elif row0_in_db == "HẸN GIỜ":
		onoff.hen_gio(data)
	elif row0_in_db=="HỦY HẸN GIỜ":
		onoff.t1.cancel()
		speaking.speak("đã hủy hẹn giờ ")
	elif row0_in_db=="DỪNG":
		if spotify ==1:
			try:
				player.stop()
			except Exception as e:
				print(e)
				pass
			at=spot.spo(spotify_username,spotify_client_id,spotify_client_secret,'http://localhost:9999/')
			sp=at.assign()
			de=sp.devices()
			de=de['devices']
			for des in de:
				print(des['id'])
				try:
					at.pause(sp,des['id'])
				except Exception as t:
					print(t)
					pass
		else:
			try:
				w.put('quit')
			except:
				pass
			try:
				we.put('quit')
			except:
				pass
			try:
				wet.put('quit')
			except:
				pass
	elif row0_in_db=="TO LÊN":
		radio.to_len()
	elif row0_in_db=="NHỎ XUỐNG":
		radio.nho_xuong()
	elif row0_in_db=="ÂM LƯỢNG":
		vol_extract = radio.amluong(data)
		speaking.speak("thiết lập âm lượng mức "+ str(vol_extract))
	elif row0_in_db=="THIẾT LẬP":
		onoff.thietlap(friendly_name_hass,sta,data)
	elif row0_in_db=="MỞ":
		onoff.on_mo(friendly_name_hass,data)
	elif row0_in_db=="TẮT":
		onoff.off_tat(friendly_name_hass,data)
	elif row0_in_db=="TÊN":
		if "tôi" in data: 
			answer('tôi là BOT LB','tôi là LB ','tôi tên LB',)
	elif row0_in_db=="":
		speaking.speak('tôi không hiểu rồi đại ca ơi')
# Trạng thái
	elif row0_in_db=="TRẠNG THÁI":   
		onoff.trangthai(sta)
#Thời tiết		
	elif row0_in_db=="THỜI TIẾT":
		import speaking
		import gih
		latlong=gih.get_config('toado')
		import datetime
		from datetime import timedelta
		x = datetime.datetime.now()
		answer('đang kiểm tra thông tin thời tiết', 'để tôi kiểm tra', 'tôi kiểm tra ngay')
		if 'NGÀY MAI' in data:
			y = x+datetime.timedelta(1)
			day = str(y.day)
			tt = wt.weekly('latlon',latlong)
			speaking.speakvn('Ngày mai '+tt[day]['overal']+', Nhiệt độ thấp nhất '+str(tt[day]['mintemp']) +' độ C, Nhiệt độ cao nhất '+str(tt[day]['maxtemp']) +' độ C,  độ ẩm là ' + str(tt[day]['hum']) + ' phần trăm, tốc độ gió trung bình ' + str(tt[day]['wind']) + ' km/h.')
		elif 'HÔM NAY' in data:
			tt = wt.current('latlon',latlong)
			speaking.speakvn('Hôm nay '+tt['overal']+', Nhiệt độ là '+str(tt['temp']) +' độ C,  độ ẩm là ' + str(tt['hum']) + ' phần trăm, tốc độ gió trung bình ' + str(tt['wind']) + ' km/h.')
		elif 'GIỜ TỚI' in data:
			string = data
			num = [int(s) for s in string.split() if s.isdigit()]
			if len(num) > 0:
				from datetime import timedelta
				y = x + timedelta(hours=num[0])
				if y.hour < 25:
					day = 'today'
					ngay = ' giờ hôm nay '
				elif y.hour > 24:
					day = 'tomorrow'
					ngay = ' giờ ngày mai '
				tt = wt.hourly('latlon',latlong)
				speaking.speakvn('Thời tiết lúc ' + str(y.hour) + ngay+ tt[day]["%.1f" %y.hour]['overal']+', Nhiệt độ là '+str(tt[day]["%.1f" %y.hour]['temp']) +' độ C,  độ ẩm là ' + str(tt[day]["%.1f" %y.hour]['hum']) + ' phần trăm, tốc độ gió trung bình ' + str(tt[day]["%.1f" %y.hour]['wind']) + ' km/h.')
			else:
				pass
		elif 'TUẦN' in data.upper():
			for i in range (1,7):
				y = x+datetime.timedelta(i)
				day = str(y.day)
				tt = wt.weekly('latlon',latlong)
				speaking.speakvn('Ngày '+ day + tt[day]['overal']+', Nhiệt độ thấp nhất '+str(tt[day]['mintemp']) +' độ C, Nhiệt độ cao nhất '+str(tt[day]['maxtemp']) +' độ C,  độ ẩm là ' + str(tt[day]['hum']) + ' phần trăm, tốc độ gió trung bình ' + str(tt[day]['wind']) + ' km/h.')
		elif 'NGÀY TỚI' in data.upper():
			string = data
			num = [int(s) for s in string.split() if s.isdigit()]
			if len(num) > 0:
				for i in range (0,num):
					y = x+datetime.timedelta(i)
					day = str(y.day)
					tt = wt.weekly('latlon',latlong)
					speaking.speak('Ngày '+ day + tt[day]['overal']+' Nhiệt độ thấp nhất '+str(tt[day]['mintemp']) +' độ C '+' Nhiệt độ cao nhất '+str(tt[day]['maxtemp']) +' độ C,  độ ẩm là ' + str(tt[day]['hum']) + ' phần trăm, tốc độ gió trung bình ' + str(tt[day]['wind']) + ' km/h.')
		else:
			tt = wt.current('latlon',latlong)
			speaking.speakvn('Hôm nay '+tt['overal']+', Nhiệt độ là '+str(tt['temp']) +' độ C,  độ ẩm là ' + str(tt['hum']) + ' phần trăm, tốc độ gió trung bình ' + str(tt['wind']) + ' km/h.')			
	else:
		answer('tôi không hiểu','tôi nghe không rõ',' vui lòng nói lại đi')
def mainloop():
	processss.maintain()
			
	



