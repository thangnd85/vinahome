try:
	from pyA20.gpio import gpio
	from pyA20.gpio import port
except:
  
	pass
#import begin
from helper import *
from pygame import mixer
import dem
import chsv
import gih
import execute
import sqlite3 as lite
import speaking
import tsm
import time
from termcolor import colored
from pygame import mixer
import snowboydecoder
import os
import gser
import legal
import sys
from time import ctime, strftime
import requests
interrupted = False
reminder = gih.get_config('reminder')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
api_boolean= gih.get_config('api_active')
hotword=gih.get_config('hotword')
con = lite.connect('data.db',check_same_thread=False)
timlenh = lite.connect('data.db',check_same_thread=False)
hehe = lite.connect('hehe.db',check_same_thread=False)
model = gih.get_config('model')
sensitivity = gih.get_config('sensitivity')
detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)
domain = gih.get_config('domain')
password = gih.get_config('hass_password')
version = gih.get_config('version_above084')
longlivedtoken = gih.get_config('longlived-token')
voice = gih.get_config('voice')
con1 = gih.data_init()
con_command = gih.data_command_init()
spotify = gih.get_config('spotify')
if spotify ==1:
	import spot
seed = gih.get_config('seed')
if seed == 1:
	import pixels
spotify_username = gih.get_config('spotify_username')
spotify_client_id = gih.get_config('spotify_client_id')
spotify_client_secret = gih.get_config('spotify_client_secret')
if spotify == 1:
	spo=spot.spo(spotify_username,spotify_client_id,spotify_client_secret,'http://localhost:9999/')
	spotipy=spo.assign()
#khiển led-------------
led_xanh = gih.get_config('led_xanh')
led_do = gih.get_config('led_do')
try:
	gpio.init()
	gpio.setcfg(led_xanh, 1)
	gpio.setcfg(led_do, 1)
except:
	pass
#khiển led-------------
serial_pi = gser.getserial()
serial_dangky = legal.check_legal()
print(colored('[CHECK SERIAL] - Kiểm tra Serial','red'))
time.sleep(0.1)

print('Serial Pi: '+ serial_pi)
if serial_pi == serial_dangky:
	ok = 1
	time.sleep(0.1)
	print("MÃ ĐĂNG KÝ HỢP LỆ")
	time.sleep(0.1)
else:
	print(">>>>>>>>>>> CHƯA ĐĂNG KÝ LICENSE. KÍCH HOẠT BẢN DÙNG THỬ <<<<<<<<<<<<<<<<<")
	print('')
	print(">>>>>>>>>>> BẠN CÓ 20 LẦN GỌI MỖI LẦN KHỞI ĐỘNG BOT <<<<<<<<<<<<<<<<<")
	print(">>>>>>>>>>> HẾT GIỚI HẠN CHƯƠNG TRÌNH TỰ ĐỘNG THOÁT <<<<<<<<<<<<<<<<<")
	print(">>>>>>>>>>> KHỞI ĐỘNG LẠI BOT ĐỂ DÙNG 20 LẦN TIẾP THEO <<<<<<<<<<<<<<<")
	print('')
	print(">>>>>>>>>>> BẠN CẦN LICENSE XIN LIÊN HỆ LBMINH AUTOMATION <<<<<<<<<<<<<<<")
	print('')
	ok = 0
	trial_times = 0


def interrupt_callback():

	global interrupted
	return interrupted
with con_command:
	cur_command =con_command.cursor()
	cur_command.execute("SELECT * FROM customcommand")
	rows_command = cur_command.fetchall()
if version == 'right':
	password = longlivedtoken
else:
	pass

def hamcat(data):
	data1=data
	print('-------------Thực hiện xử lý ngôn ngữ---------------')
	with con:
		cur=con.cursor()
		cur.execute("SELECT * FROM hamcat")
		rows=cur.fetchall()
		for row in rows:
			for i in range(0,2):
				if row[i].upper() in data1.upper():
					print('tìm thấy '+ row[i])
					data1=data1.replace(str(row[i]),"")
					data1.strip()
	return data1


def timlenhtrongdata(data):
	with timlenh:
		cur=timlenh.cursor()
		cur.execute("SELECT * FROM hamthucthi2")
		rows=cur.fetchall()
		taplenh=[]
		for row in rows:
			
			for i in range(0,11):
				if row[i].upper() in data.upper():
					taplenh.append(row[0])
					break

	print(taplenh)


def timkiemthucthi(data,friendly_name_hass,sta):
	with con:
		cur=con.cursor()
		cur.execute("SELECT * FROM hamthucthi2")
		rows=cur.fetchall()
		for row in rows:
			b = 0
			for i in range(0,11):
				if row[i].upper() in data.upper():
					dem.hamthucthi(row[0],data,friendly_name_hass,sta)
					b = 1
					break  
			if b==1:
				break   
		if b==0:
			speaking.speak('xin lỗi, tôi không hiểu')
	
def find_hass_friendly_name(data):
	print('[MAIN] - KIỂM TRA TÊN THIẾT BỊ')
	print('')
	friendly_name = chsv.check_fr(data)
	ex,ey = chsv.export_e_d(friendly_name)
	domain_ex = ex
	entity_id_ex = ey
	domain = gih.get_config('domain')
	password = gih.get_config('hass_password')
	version = gih.get_config('version_above084')
	longlivedtoken = gih.get_config('longlived-token')
	if version == 'right':
		password = longlivedtoken
	else:
		pass								  
	m = 0
	object = [execute.define(domain_ex,entity_id_ex,domain,password) for x in range(len(domain_ex))]
	while m < len(domain_ex): 
		object[m] = execute.define(domain_ex[m],entity_id_ex[m],domain,password)
		object[m] = object[m].define()
		m += 1
					 
	return object
def check_sta(data):
	print('[MAIN] - KIỂM TRA TRẠNG THÁI')
	print('')
	friendly_name = chsv.check_fr(data)
	ex,ey = chsv.export_e_d(friendly_name)
	domain_ex= ex
	entity_id_ex= ey
	domain = gih.get_config('domain')
	password = gih.get_config('hass_password')
	version = gih.get_config('version_above084')
	longlivedtoken = gih.get_config('longlived-token')
	if version == 'right':
		password = longlivedtoken
	else:
		pass								  
	i=0
	sta = [0 for x in range(len(domain_ex))]
	while i < len(domain_ex):
		try:
			sta[i] = [friendly_name[i],domain_ex[i],entity_id_ex[i],domain,password]
			i+=1
		except:
			i+=1
			pass
	
	return sta

def execute_command(data,rows_command,domain,password):
	print('[MAIN] - THỰC THI CUSTOM COMMAND')
	print('')
	try:
		import json
		for row in rows_command:
			if row[0].upper().strip() in data.upper().strip():
				
				domain_com = row[1].split('.')
				domain_com = domain_com[0]
				if version == 'right':
					url = domain+'/api/services/'+domain_com+'/'+row[2]
					headers = {
			'Authorization': 'Bearer '+ password,
			'content-type': 'application/json',
		}
				else:
					url = domain + '/api/services/'+domain_com+'/'+row[2]+'?api_password='+password
					headers = {'content-type': 'application/json'}
				payload = {'entity_id': row[1]}
		
				r = requests.post(url, data=json.dumps(payload), headers=headers)
				
				
				if str(r)=='<Response [200]>':
					print('[DEBUG] Thực thi Custom Command: ok')
					dem.answer('ok','có ngay','đã xong')
					r = 1
					return r
				else:
					pass
				break
	except:
		pass
def re_ask():
	print('[MAIN] - HỎI LẠI')
	print('')
	if api_boolean==1:
		more_data = tsm.main()
		return more_data
	elif api_boolean ==0:
		more_data = dem.recordAudio()
		return more_data

def jarvis(data):
	print('[MAIN] - XỬ LÝ')
	print('')
	data1 = data.upper()
	data=data1
	r = execute_command(data,rows_command,domain,password)
	if r ==1:
		pass
	else:  
		try:
			friendly_name_hass = find_hass_friendly_name(data)
			print('')
		except:
			pass
		sta = check_sta(data)
		timkiemthucthi(data,friendly_name_hass,sta)

def xuly():
	if seed == 1:
		pixels.pixels.wakeup() 
	if ok == 0:
		trial_times=0
		speaking.speak('đây là bản dùng thử')
		trial_times +=1
		if trial_times < 20:
			print(colored('Số lần request còn lại: '+ str(21 - trial_times),'red'))
		else:
			print(colored('[ERROR] - Hết giới hạn dùng thử. Vui lòng khởi động lại BOT','red'))
			speaking.speak('Hết giới hạn dùng thử. Khởi động lại bot để dùng tiếp')
			sys.exit(0)
	print('[MAIN] - TIẾP NHẬN XỬ LÝ')
	print('')
	spotify = gih.get_config('spotify')
	if spotify == 1:
		try:
			dem.player.audio_set_volume(40)
		except:
			pass
		try:
			global volume
			volume=spotipy.devices()
			volume=volume['devices'][0]['volume_percent']
#			print('volume truoc khi giam '+ str(volume))
			spotipy.volume(36)
		except:
			pass
	else:
		player_volume=dem.radio.lay_am_luong()
		dem.player.audio_set_volume(player_volume - 35)
# Nếu không chạy thì gõ dấu # vào 2 dong bên trên và bỏ dấu # ở dòng bên dưới nhé
#		pass
	data ='interruptinterrupt'
	while data =='interruptinterrupt':
		print(colored('tôi ĐANG CHỜ RA LỆNH - BẬT TẮT <TÊN THIẾT BỊ> HAY HỎI MẤY GIỜ RỒI...','green'))
		conti = 1
		from pygame import mixer
		mixer.init(48000, -16, 1, 4096)
		mixer.music.load('resources/ding.wav')
		mixer.music.play()
		try:
#	Dùng API Google
			if api_boolean == 1:
				print('------------------------------------------------------')
				print(colored('-------------------------CÓ DÙNG API GOOGLE-----------------','green'))
				print('------------------------------------------------------')
				data = tsm.main()
				conti = 1
#	Không dùng API Google
			elif api_boolean == 0:
				print('------------------------------------------------------')
				print(colored('---------------KHÔNG DÙNG API, SẼ NHẬN CHẬM LẮM ĐÂY, MÔI TRƯỜNG ÍT ỒN SẼ DỄ NHẬN HƠN (TRÁNH QUẠT, MÁY LẠNH)-------------','red'))
				print('------------------------------------------------------')
				data=dem.recordAudio()
				conti = 1
				if hotword.upper() in str(data).upper():
					data == 'interruptinterrupt'
#	Dùng API FPT
			elif api_boolean == 2:
				print('------------------------------------------------------')
				print(colored('---------------DÙNG API FPT-------------','yellow'))
				print('------------------------------------------------------')
				data=dem.recordFPT()
				conti = 1
				if hotword.upper() in str(data).upper():
					data == 'interruptinterrupt'
#	Dùng API VTCC
			elif api_boolean == 3:
				print('------------------------------------------------------')
				print(colored('---------------DÙNG API VIETTEL-------------','blue'))
				print('------------------------------------------------------')
				data=dem.recordVTCC()
				conti = 1
				if hotword.upper() in str(data).upper():
					data == 'interruptinterrupt'
#	Sử dụng text input
			else:
				data=input("Nhập lệnh cần thực thi:  ")
				conti = 1
		except:
			conti = 0
			break
		
	mixer.music.load('resources/dong.wav')
	mixer.music.play()
	if seed == 1:
		pixels.pixels.think() 
	if conti == 1 and str(data).upper() != 'ĐƯỢC RỒI':
		try:
			jarvis(data)
		except Exception as e:
			print(e)
	giophut= str(strftime("%H"))+':'+str(strftime("%M"))
	ai_data = (data,giophut,"")
	try:
		with hehe:
			haha=hehe.cursor()
			haha.execute("INSERT INTO ai_data VALUES(?,?,?)",ai_data)
	except:
		print('writing ai_data ee')
		pass
	if spotify == 0:
		try:
			player_volume=dem.radio.lay_am_luong()
			dem.player.audio_set_volume(player_volume - 35)
			time.sleep(0.1)
			dem.player.audio_set_volume(player_volume - 20)
			time.sleep(0.1)
			dem.player.audio_set_volume(player_volume)
		except:
			pass		
	if spotify ==1:
		try:
			volume=dem.spotipy[1].devices(dem.spotipy[0])
			volume=volume[2]
#			print('volume sau khi giam: ' + str(volume))
			spotipy.volume(volume-35)
			time.sleep(0.1)
			spotipy.volume(volume-20)
			time.sleep(0.1)
			spotipy.volume(volume)
		except Exception as e:
			print('spotify: '+str(e))
	if seed ==1:
		pixels.pixels.off()
	print(colored('*****************SẴN SÀNG CHỜ GỌI****************','green'))

speaking.speak('Xin chào, tôi là Jarvis, trợ lý ảo cho ngôi nhà thông minh.')
print('------------------------------------------------------------------------------')
print('')
time.sleep(0.1)
print(colored('[MAIN]: THIẾT LẬP - Home Assistant tại địa chỉ: '+ domain,'yellow'))
print('')
time.sleep(0.1)
t = gih.getinfo(domain,password,con1)

if t==True:
	speaking.speak('Kết nối thành công với trung tâm điều khiển nhà. Sẵn sàng chờ lệnh của bạn.')
	
elif t ==False:
	speaking.speak("không kết nối được với trung tâm điều khiển Home Assistant")
	
	check = gih.check_internet()
	if check == False:
		speaking.speak('Không kết nối được với internet')
def maintain():
	time.sleep(0.1)
	print('[MAIN]')
	print('')
	trial_times=0
	print(colored('*****************SẴN SÀNG CHỜ GỌI****************','green'))
	if api_boolean != 1111:
		detector.start(detected_callback=xuly,interrupt_check=interrupt_callback,sleep_time=0.01)
		detector.terminate()
