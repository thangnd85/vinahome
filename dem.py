#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
from helper import *
import pyximport
pyximport.install(build_dir=”./build”)
import chsv
import processss
import onoff
import speech_recognition as sr
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
import news
sp_act = gih.get_config('spotify')
if sp_act == 1:
	import spot
s_user = gih.get_config('spotify_username')
s_id = gih.get_config('spotify_client_id')
s_secret = gih.get_config('spotify_client_secret')
seed = gih.get_config('seed')
if seed == 1:
	import apa102
	from pixels import pixels
def recordAudio():
	r = sr.Recognizer()
	with sr.Microphone(device_index = 0, sample_rate = 44100, chunk_size = 512) as source:
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
#import begin
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
		if seed == 1:
			pixels.speak()
		answer("em khỏe. ","khỏe lắm anh ","khỏe chứ anh. ",)
		if seed == 1:
			pixels.off()

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
		if seed == 1:
			pixels.speak()
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
		if seed == 1:
			pixels.off()		

#Hỏi thứ
	elif row0_in_db == "THỨ MẤY":
		check_thu=[]
		if seed == 1:
			pixels.speak()
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
		speaking.speak(result_thu[0]+" là " + result_thu[1] + ' '+ result_thu[2] + ' tháng '+ str(result_thu[3]))
		if seed == 1:
			pixels.off()		
# Ngày lễ
	elif row0_in_db == "NGÀY LỄ":
		if seed == 1:
			pixels.speak()
#		answer('không có chi. ','rất vui vì giúp được anh ',' đừng bận tâm ')
		ngayle_res=[]
		ngayle_res=ngayle.ngayle_check(data)
		speaking.speak(ngayle_res[0] + ' Còn '+str(ngayle_res[1])+' ngày nữa là đến '+ngayle_res[2]  + '. Đó là ngày '+ngayle_res[3] +' tháng '+ngayle_res[4] +' năm '+ngayle_res[5] )
		if seed == 1:
			pixels.off()
#Cảm ơn	
	elif row0_in_db == "CẢM ƠN":
		if seed == 1:
			pixels.speak()
		answer('không có chi. ','rất vui vì giúp được anh ',' đừng bận tâm ')
		if seed == 1:
			pixels.off()
#Gass	
	elif row0_in_db == "BAO NHIÊU TUỔI":
			import textinput
			textinput.main()
#HELP
	elif row0_in_db == "TRỢ GIÚP":
		if seed == 1:
			pixels.speak()
		if 'THỜI TIẾT' in data:
			speaking.speak('Có thể hỏi các câu hỏi bao gồm các từ như, Thời tiết hôm nay, ngày mai')
		elif 'GIỜ' in data:
			speaking.speak('Đặt câu hỏi mấy giờ rồi')
		elif 'NGÀY' in data:
			speaking.speak('Hỏi thứ mấy, ngày nào. Có thể hỏi ngày mai là thứ mấy, ngày 30 tháng 4 là thứ mấy, vv.')
		elif 'ÂM LỊCH' in data:
			speaking.speak('Hỏi âm lịch hôm nay, ngày mai, ngày bất kì')
		elif 'DỊCH' in data:
			speaking.speak('Dịch từ tHoặc dịch cả câu với cấu trức: Dịch câu sau sang tiếng nào đó. Sau đó chờ âm báo rồi đọc câu. Ngôn ngữ hỗ trợ: Việt, Anh, Trung, Nhật, Hàn.')
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
		if seed == 1:
			pixels.off()
#Hỏi giờ
	elif row0_in_db == "MẤY GIỜ":
		if seed == 1:
			pixels.speak()
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

		speaking.speak("BÂY GIỜ LÀ " + docgio + docphut)
		if seed == 1:
			pixels.off()
#Tin tức (TTS)
	elif row0_in_db == "TIN TỨC":
		pixels.speak()
		tintuc.tintucmoi()

	elif row0_in_db == "XỔ SỐ":
		pixels.speak()
		print ('Kết quả xổ số')
		loto.check(data)
#Truyện cười	
	elif row0_in_db == "CƯỜI":
		pixels.speak()	
		truyen = fun.truyen()
		speaking.speak(truyen)

#Hỏi ngày			
	# if row0_in_db=="VỊ TRÍ":
	#	 if "CỦA" in data:
	#		 locationcua = data.find('CỦA')
	#		 data = data[locationcua+4:len(data)]
	#		 location = data.strip(" ")
	#		 speaking.speak("đây là vị trí của  " + location )
	#		 webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
	# elif row0_in_db == 'NHẮC':

	elif row0_in_db == "RADIO":
		pixels.speak()
		try:
			player.stop()
		except:
			pass
		player=radio.phat_radio(data)

	elif row0_in_db=="ĐI NGỦ":
		pass
	elif row0_in_db=="LÀ GÌ":
		if seed == 1:
			pixels.speak()
		def wifi(data):
			data = data[0:len(data)-6]
			rep = wk.find_info(data)
			rep = rep.find_wiki()
			print (rep)
			rep = '. '.join(rep)
			speaking.speak('Theo wikipedia: '+rep)
		speaking.speak('để em tìm xem nào')
		execute.run_thread(wifi,data) 
		if seed == 1:
			pixels.off()

# Phát video
	elif row0_in_db=="PHÁT" :
		if seed == 1:
			pixels.speak()
		global spotipy
		try:
			player.stop()
		except:
			pass
		if sp_act == 1:
			spotipy=spot.play_current_playlist(s_user,s_id,s_secret,'http://localhost:9999/',data)
		else:
			player= radio.play_nhac(data,friendly_name_hass)
		if seed == 1:
			pixels.off()
	elif row0_in_db=="TIẾP THEO":
		try:
			player.stop()
		except:
			pass
		player=radio.phat_tiep_theo()
		if seed == 1:
			pixels.off()
# Google word translate
	elif row0_in_db=="CÓ NGHĨA" :
		if seed == 1:
			pixels.speak()
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
			speaking.speak ('trong tiếng việt nghĩa là: '+ translations.text)		
#To English
		elif 'TIẾNG ANH' in data:
			m = re.search ('(.+?) TIẾNG ANH', data)
			dataen = m.group(1)
			print (dataen)
			translations = translator.translate (dataen, dest = 'en')
			print (translations.text)
			speaking.speak ('Từ '+dataen +' trong tiếng anh nghĩa là: ')
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
		speaking.speak ('OK, đọc câu cần dịch đi anh')		
		more_data = processss.re_ask()
		print (more_data)		
#		def gconv (data,more_data):
#			continue_go = 1
#			empty = []
		if len(more_data) > 0:
			while True:
				print ('Google translate: '+data)
				print ('Data translate: '+more_data)
#			   speaking.speak('')
				processss.mixer.music.load('resources/ding.wav')
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
		
#		return more_data, continue_go
# Hẹn giờ		
	elif row0_in_db == "HẸN GIỜ":
		onoff.hen_gio(data)
	elif row0_in_db=="HỦY HẸN GIỜ":
		onoff.t1.cancel()
		speaking.speak("đã hủy hẹn giờ ")
	elif row0_in_db=="DỪNG":
		try:
			player.stop()
		except Exception as e:
			print(e)
			pass
		at=spot.spo(s_user,s_id,s_secret,'http://localhost:9999/')
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
	elif row0_in_db=="TO LÊN":
		pixels.speak()
		radio.to_len()
	elif row0_in_db=="NHỎ XUỐNG":
		pixels.speak()
		radio.nho_xuong()
	elif row0_in_db=="ÂM LƯỢNG":
		pixels.speak()
		vol_extract = radio.amluong(data)
		speaking.speak("thiết lập âm lượng mức "+ str(vol_extract))
	elif row0_in_db=="THIẾT LẬP":
		pixels.speak()
		onoff.thietlap(friendly_name_hass,sta,data)
	elif row0_in_db=="MỞ":
		pixels.speak()
		onoff.on_mo(friendly_name_hass,data)
	elif row0_in_db=="TẮT":
		onoff.off_tat(friendly_name_hass,data)
	elif row0_in_db=="TÊN":
		if "EM" in data: 
			answer('em là BOT LB','em là LB ','em tên LB',)

	elif row0_in_db=="":
		speaking.speak('em không hiểu rồi đại ca ơi')
# Trạng thái
	elif row0_in_db=="TRẠNG THÁI":
		if seed == 1:
			pixels.speak()	
		onoff.trangthai(sta)
		if seed == 1:
			pixels.off()		
#Thời tiết		
	elif row0_in_db=="THỜI TIẾT":
		if seed == 1:
			pixels.speak()
		def wt(data):
			fio=weth.darksky_weather()
			if "HIỆN TẠI" in data or "HÔM NAY" in data :
				icon=''
				current_weather = weth.darksky_currently(fio)
				if current_weather[2].upper() == 'RAIN':
					icon = 'mưa'
				elif current_weather[2].upper() == 'PARTLY-CLOUDY-NIGHT':
					icon = 'buổi tối trời nhiều mây'
				elif current_weather[2].upper() == 'PARTLY-CLOUDY-DAY':
					icon = 'trời nhiều mây'
				elif current_weather[2].upper() == 'CLEAR-DAY':
					icon = 'trời trong xanh'
				elif current_weather[2].upper() == 'CLEAR-NIGHT':
					icon = 'đêm trời đẹp'
				elif current_weather[2].upper() == 'WIND':
					icon = 'có gió lớn'
				elif current_weather[2].upper() == 'CLOUDY':
					icon = 'trời nhiều mây'
				elif current_weather[2].upper() == 'FOG':
					icon = 'trời nhiều sương mù'
				
				speaking.speak(current_weather[0]+ current_weather[1] + icon)
			elif "NGÀY MAI" in data:
				hourly_weather = weth.darksky_hourly(fio)
				speaking.speak(' nhìn chung ' + hourly_weather)
			else:
				speaking.speak('em không hiểu')
		answer('đang kiểm tra thông tin thời tiết', 'để em kiểm tra', 'em kiểm tra ngay')
		execute.run_thread(wt,data)
# TIN RADIO
	elif row0_in_db=="TIN VẮN":
		import zing
		if seed == 1:
			pixels.speak()
		playlist = news.getlink(data)
		player = zing.phat_zing(playlist)
		speaking.speak('Đang chuẩn bị phát tin vắn radio')
		player.play()
		if 'TIẾP' in data:
			print ('Next')
			player.next()
		if 'TRƯỚC' in data:
			print ('Prev')
			player.previous()
		if seed == 1:
			pixels.off()
# ZING
	elif row0_in_db=="ZING":
		if seed == 1:
			pixels.speak()
		import zing, vlc
		playlist = zing.zing_song(data)
		player = zing.phat_zing(playlist)
		speaking.speak('Đang chuẩn bị phát top 100 ca khúc trên Zing')
		player.play()
		if 'TIẾP' in data:
			print ('Next')
			player.next()
		if 'TRƯỚC' in data:
			print ('Prev')
			player.previous()		
		if seed == 1:
			pixels.off()

	else:
		if seed == 1:
			pixels.speak()
		answer('em không hiểu','em nghe không rõ',' vui lòng nói lại đi')
		if seed == 1:
			pixels.off()


def mainloop():
	processss.maintain()
			
	



