import os
import sys
import time
import platform
c=[]
d=[]
path = os.path.dirname(os.path.abspath('_file_'))
path = path
try:
	os.chdir(path)
	os.system('sudo chmod -R 0777 '+ path)
except:
	print('chmod ee')
print('-------------------------------------------------------------------')
print("[SETUP] - KHỞI ĐỘNG BỘ CÀI ĐẶT")
print('-------------------------------------------------------------------')
print ('BẮT ĐẦU CÀI ĐẶT ........')


def install_app():
	os.system('sudo apt-get -y -qq install curl apt-transport-https >> /dev/null')
	os.system('sudo curl -sSL https://dtcooper.github.io/raspotify/key.asc | sudo apt-key add -v -')
	os.system("echo 'deb https://dtcooper.github.io/raspotify raspotify main' | sudo tee /etc/apt/sources.list.d/raspotify.list")
	c=[]
	d=[]
	a=['sox','libsdl-mixer1.2','swig','libatlas-base-dev','python3-pyaudio','vlc','python3-setuptools','build-essential', 'libsdl1.2-dev', 'libfreetype6-dev', 'libsdl-dev', 'libsdl-image1.2-dev', 'libsdl-mixer1.2-dev', 'libsdl-ttf2.0-dev', 'libsmpeg-dev', 'libportmidi-dev', 'libavformat-dev', 'libswscale-dev', 'python3-dev', 'python3-numpy', 'python3-cffi','python3-scipy', 'python-matplotlib', 'ipython', 'python-pandas', 'python-sympy', 'python-nose','libffi-dev','libcurl4-openssl-dev','libssl1.0-dev','libsoup2.4-dev','git','libgcrypt20-dev','libgstreamer-plugins-bad1.0-dev','gstreamer1.0-plugins-good','libasound2-dev', 'flac','curl','apt-transport-https','libportaudio0','libportaudio2','libportaudiocpp0','portaudio19-dev','raspotify','python3-pip','python3-venv','ffmpeg','pulseaudio','pavucontrol']
	print('')
	time.sleep(1)
	print('[SETUP] - TRONG QUÁ TRÌNH CÀI ĐẶT VUI LÒNG TRẢ LỜI CÁC YÊU CẦU Y/N: ')
	print('')
	print('QUÁ TRÌNH CÀI ĐẶT CÓ THỂ LÂU HƠN 10 PHÚT. HÃY CHUẨN BỊ CAFE HOẶC ĐỔI NHÀ MẠNG :)')
	print('--------------------------------------------------------------------------------')
	i=0
	print('---------------------ĐANG KIỂM TRA CẬP NHẬT HỆ THỐNG ---------------------------')
	up=os.system('sudo apt-get update >> /dev/null')
	if up==0 or up==1:
#		print('ĐANG GỠ BỎ PYTHON2 RA KHỎI HỆ THỐNG')
#		os.system('sudo apt-get remove  --purge -y -qq python >> /dev/null')
#		print('CÀI ĐẶT LẠI PULSEAUDIO: ')
#		os.system('sudo apt-get remove --purge -y -qq pulseaudio >>/dev/null')
		print('ĐANG NÂNG CẤP HỆ THỐNG. VUI LÒNG PHA THÊM SỮA  .....')
		os.system('sudo apt-get -y -qq upgrade  >> /dev/null')

		print('ĐANG CÀI ĐẶT CÁC ỨNG DỤNG CẦN THIẾT. HÃY KIÊN NHẪN ....')
		print('Tổng số ứng dụng: '+str(len(a)))
	print ("ĐANG CÀI ĐẶT ỨNG DỤNG: ") 
	while i <len(a) -1:
		i+=1
		print('ĐANG CÀI '+str(i)+'/'+str(len(a)))
#		sys.stdout.write(">>>")
		b=os.system('sudo apt-get -y -qq install ' + a[i] +'>>/dev/null')
		if b==0:
			pass
		else:
			c.append('- '+ a[i]+ ' lỗi')
	p=0
	if len(c) > 0:
		while p < len(c):
			print(str(c[p]))
			p+=1
	else:
		print ('')
		print('-------------------------------------------------------------------')
		print('[CÀI ĐẶT BƯỚC 1]: OK')
		print('-------------------------------------------------------------------')
		
def install_pip():	
	print ('-----------------ĐANG NÂNG CẤP PYTHON3 EASY INSTALL----------------------------')
	os.system('env/bin/python -m pip install --default-timeout=1000 --upgrade --quiet -I pip')

	time.sleep(1)
	os.system('pip config --user set global.progress_bar off')
	os.system('sudo rm '+path+'/env/bin/python3')
	os.system('sudo rm '+path+'/env/bin/activate.fish')
	os.system('sudo rm '+path+'/env/bin/activate.csh')
	os.system('sudo chmod 777 -R env')
	os.system('python3 -m venv env')
#	time.sleep(5)
	os.system('. env/bin/activate')
	pip = ['PySDL2', 'wheel','requests', 'regex', 'pya20','pygame', 'termcolor','pyAesCrypt', 'cffi', 'google-cloud-speech', 'six', 'googletrans' ,'wikipedia' ,'forecastiopy', 'click', 'pyyaml','datetime','bs4','datefinder','pafy','youtube_dl','pyalsaaudio', 'gTTS', 'python-vlc', 'SpeechRecognition','underthesea','numpy','feedparser','lxml','mutagen','pyaudio','pulsectl','google-assistant-library','google-assistant-sdk[samples]','google-auth-oauthlib[tool]','google-assistant-grpc','spidev','spotipy','git+https://github.com/plamere/spotipy.git --upgrade','fuzzywuzzy','python-Levenshtein','playsound','wget','pydub','pulsemixer']
	i=0
	print ('SỐ MODULE CẦN CÀI ĐẶT: '+str(len(pip)))
	print ('Có thể có module cần thời gian dài để xây dựng. Xin hãy kiên nhẫn')
#	up=os.system('sudo apt-get update')
#	if up==0 or up==1:
#		os.system('sudo apt-get upgrade')
	print('ĐANG CÀI ĐẶT MODULE')
	while i < len(pip) - 1:
		i+=1
		print ('MODULE '+str(i)+'/'+str(len(pip)))
#		sys.stdout.write ('>>>')
		b=os.system('env/bin/python -m pip install --upgrade --no-cache-dir --default-timeout=1000 --quiet ' + pip[i])
		if b==0:
			pass
		else:
			d.append('- '+ pip[i]+ ' lỗi')
	j=0
	if len(d) > 0:
		while j < len(d):
			print(str(d[j]))
			j+=1

	else:
		print ('')
		print('-------------------------------------------------------------------')
		print('[CÀI ĐẶT BƯỚC 2]: OK')
	print('------------------------------------------------------------------------------------------')
	time.sleep(1)
def build_snowboy():	
	os.system('rm '+ path+'/swig/Python3/_snowboydetect.so') 
	os.system('rm '+ path+'/swig/Python3/snowboy-detect-swig.cc')
	os.system('rm '+ path+'/swig/Python3/snowboy-detect-swig.o') 
	os.system('rm '+ path+'/swig/Python3/snowboydetect.py')  	
	time.sleep(1)
	os.chdir(path+'/swig/Python3')
	time.sleep(1)
	res= os.system('make')
	if res == 0:
		os.chdir('..')
		os.chdir('..')
		os.system('sudo cp '+ path+'/swig/Python3/_snowboydetect.so ./')
		time.sleep(2)
		os.system('sudo cp '+ path+'/swig/Python3/snowboydetect.py ./')
		time.sleep(2)
	os.system('sudo chmod -R 0777 /etc/pulse/default.pa')
	os.system('sudo touch /lib/systemd/system/bot.service')
	time.sleep(1)
	os.system('sudo rm /lib/systemd/system/bot.service')
	time.sleep(1)	
	os.system('sudo touch /lib/systemd/system/bot.service')
	time.sleep(1)
	os.system('mkdir ~/.config')
	os.system('mkdir ~/.config/systemd')
	os.system('mkdir ~/.config/systemd/user')
	os.system('cp bot.service ~/.config/systemd/user/bot.service')
	os.system('systemctl --user daemon-reload')
	os.system('sudo usermod -aG pulse-access pi')
	time.sleep(1)
	time.sleep(1)
def config_bot():
	import gih
	from termcolor import colored
	print("HỖ TRỢ CẤU HÌNH BOT")
	print("")
	time.sleep(0.7)
	print(colored("VUI LÒNG NHẬP DOMAIN HOME ASSISTANT MÀ BẠN MUỐN KẾT NỐI",'yellow') + "- NHẬP DẠNG HTTPS://DOMAIN.DUCKDNS.ORG HOẶC HTTP://IP:8123")
	print("")
	print("CẤU HÌNH HIỆN TẠI CỦA DOMAIN ĐANG LÀ: "+ colored(gih.get_config('domain'),'red'))
	domain=input("BẠN HÃY NHẬP VÀ DOMAIN MỚI HOẶC NHẬP "+colored('K','yellow') +" ĐỂ BỎ QUA: ")
	if str(domain).upper() == 'K':
		pass
	else:
		try:
			gih.set_config('domain',domain)
			print("THIẾT LẬP THÀNH CÔNG DOMAIN LÀ: "+ colored(str(domain),'green'))
		except:
			print("Có lỗi thiết lập, vui lòng thiết lập thủ công phần domain")

	
	print("")
	time.sleep(0.7)
	print(colored("VUI LÒNG NHẬP TOKEN CỦA HOME ASSISTANT","yellow")+ "- NẾU CHƯA BIẾT CÁCH TẠO TOKEN XIN VUI LÒNG XEM TRÊN YOUTUBE HƯỚNG DẪN CỦA LBMINH")
	print("CẤU HÌNH HIỆN TẠI CỦA TOKEN ĐANG LÀ: "+ colored(gih.get_config('longlived-token'),'red'))
	token=input("BẠN HÃY NHẬP VÀO TOKEN MỚI HOẶC NHẬP "+colored('K','yellow') +" ĐỂ BỎ QUA: ")
	if str(token).upper()=='K':
		pass
	else:
		try:
			gih.set_config('longlived-token',token)
			print("------>THIẾT LẬP THÀNH CÔNG TOKEN LÀ: "+ colored(str(token),'green'))
		except:
			print(colored("Có lỗi thiết lập, vui lòng thiết lập thủ công phần token","red"))
	print("")
	time.sleep(0.7)
	print(colored("BẠN CÓ MUỐN DÙNG API NHẬN GIỌNG KHÔNG","yellow")+" - NẾU KHÔNG DÙNG NHẬN GIỌNG SẼ CHẬM - NẾU DÙNG NHẬN GIỌNG SẼ NHANH HƠN - BẠN PHẢI ĐĂNG KÝ NẾU MUỐN DÙNG")
	time.sleep(0.5)
	print("CẤU HÌNH HIỆN TẠI CỦA API ĐANG LÀ: "+ colored(gih.get_config('api_active'),'red'))
	api=input("BẠN HÃY NHẬP VÀO "+ colored("0","yellow")+" (KHÔNG DÙNG) HOẶC "+ colored("1","yellow")+" (CÓ DÙNG) HOẶC " + colored("K","yellow")+ " ĐỂ BỎ QUA: ")
	if str(api) =="1" or str(api) == "0" or str(api) =="1111":
		gih.set_config('api_active',int(api))
		print("------>THIẾT LẬP API: "+ colored(str(api),'green'))
	elif str(api).upper()=='K':
		print("GIỮ NGUYÊN THIẾT LẬP API CÓ SẴN")
	else:
		print(colored("BẠN NHẬP SAI GIÁ TRỊ RỒI, TIẾN HÀNH SET MẶC ĐỊNH LÀ API: 0","red"))
		gih.set_config('api_active',0)

	if api=='1':
		print("")
		time.sleep(0.7)
		print("TÊN HIỆN TẠI CỦA API ĐANG LÀ: "+ colored(gih.get_config('google_application_credentials'),'red'))
		jsonapi=input("VUI LÒNG NHẬP TÊN MỚI CỦA JSON API - NHẬP DẠNG 'ABCD.JSON' " + " - HOẶC ẤN K ĐỂ BỎ QUA: ")
		if str(jsonapi).upper() != "K":
			try:
				gih.set_config('google_application_credentials',jsonapi)
				print(colored('THIẾT LẬP THÀNH CÔNG JSON','red'))
			except:
				print('Lỗi trong quá trình thiết lập tên api. Vui lòng config thủ công')
#CHỌN TTS
	print("")
	time.sleep(0.7)
	print(colored("BẠN CÓ MUỐN DÙNG LỰA CHỌN GIỌNG ĐỌC GOOGLE HOẶC FPT","yellow")+" FPT NẾU TRẢ PHÍ GIỌNG RẤT TRUYỀN CẢM")
	time.sleep(0.5)
	print("CẤU HÌNH HIỆN TẠI CỦA TTS ĐANG LÀ: "+ colored(gih.get_config('tts'),'red'))
	tts=input("BẠN HÃY NHẬP VÀO "+ colored("google","yellow")+" (GOOGLE TTS) HOẶC "+ colored("fpt","yellow")+" (FPT TTS) HOẶC " + colored("K","yellow")+ " ĐỂ BỎ QUA: ")
	if str(tts) =="google" or str(tts) == "fpt":
		gih.set_config('tts',str(tts))
		print("------>THIẾT LẬP TTS: "+ colored(str(tts),'green'))
	elif str(tts).upper()=='K':
		print("GIỮ NGUYÊN THIẾT LẬP TTS CÓ SẴN")
	else:
		print(colored("BẠN NHẬP SAI GIÁ TRỊ RỒI, TIẾN HÀNH SET MẶC ĐỊNH LÀ API: google","red"))
		gih.set_config('tts','google')
#TTS FPT
	if tts=='fpt':
		print("")
		time.sleep(0.7)
		print("API HIỆN TẠI CỦA FPT LÀ: "+ colored(gih.get_config('api_fpt'),'red'))
		api_fpt=input("NHẬP API CỦA FPT TTS " + " - HOẶC ẤN K ĐỂ BỎ QUA: ")
		if str(api_fpt).upper() != "K":
			try:
				gih.set_config('api_fpt',str(api_fpt))
				print(colored('THIẾT LẬP THÀNH CÔNG FPT TTS','red'))
			except:
				print('Lỗi trong quá trình thiết lập tên api. Vui lòng config thủ công')
#DARSKY	
	print("")
	time.sleep(0.7)
	print(colored("BẠN CÓ MUỐN KIỂM TRA THỜI TIẾT","yellow")+" THÔNG QUA DARSKY")
	time.sleep(0.5)
	print("CẤU HÌNH HIỆN TẠI CỦA DARKSKY ĐANG LÀ: "+ colored(gih.get_config('api_darksky'),'red'))
	darksky=input("BẠN HÃY NHẬP VÀO "+colored("google","yellow")+" API DARSKY HOẶC " + colored("K","yellow")+ " ĐỂ BỎ QUA: ")
	if str(darksky) != '':
		gih.set_config('api_darksky',darksky)
		print("------>THIẾT LẬP DARKSKY: "+colored(str(darksky),'green'))
	elif str(darksky).upper()=='K':
		print("GIỮ NGUYÊN THIẾT LẬP TTS CÓ SẴN")
	else:
		print(colored("BẠN NHẬP SAI GIÁ TRỊ RỒI, TIẾN HÀNH SET MẶC ĐỊNH LÀ API: null","red"))
		gih.set_config('api_darksky','null')
				
def mic_set():
	print('-------------------------------------------------------------------')
	print("[SETUP_MIC_SPEAKER] - THIẾT LẬP MICROPHONE VÀ MIC")
	try:
		os.system('sudo apt-get install -y -qq python3-pip >> /dev/null')
	except:
		pass
	if platform.machine() == 'x86':	
		m=os.system('sudo apt-get install -y -qq libpulse0:i386 >> /dev/null')
	elif platform.machine() == 'armv7l':
		n=os.system('sudo apt-get install -y -qq  libpulse0>> /dev/null')
	try: 
		import pulsectl
	except:
		pass
	import pulsectl
	os.system('killall pulseaudio')
	os.system('sudo killall pulseaudio')
	os.system('pulseaudio --start')
	time.sleep(1)
	pulse = pulsectl.Pulse('my-client')
	blist = pulse.source_list()
	ee=len(blist)
	slist=pulse.sink_list()
	ss=len(slist)
#	print(blist)
	print('')
	print("ĐANG NHẬN DIỆN MICROPHONE...")
	print('')
	time.sleep(0.7)
	for i in range(0, ee):
		print ('MIC '+str(i)+' :'+blist[i].name)
		if 'OmniVision' in blist[i].name:
			source = blist[i].name
			print ('------------------->>>MIC ARRAY SONY PS3<<<--------------------------')
		elif 'mono' in blist[i].name and 'input' in blist[i].name and 'monitor' not in blist[i].name:
			source = blist[i].name
			print('------------------------->>>MIC USB<<<-----------------------------')
		elif 'input' in blist[i].name and 'monitor' not in blist[i].name:
			source = blist[i].name
			print('------------------------->>>MIC KHÁC<<<-----------------------------')
		else:
			source = blist[0].name
		time.sleep(0.7)
#			print ('KHÔNG RÕ LOẠI MIC BẠN ĐANG SỬ DỤNG HOẶC BẠN QUÊN CHƯA GẮN MIC')
#		iii = input('NHẬP TÊN MIC BẠN SỬ DỤNG (TỐT NHẤT LÀ BÔI ĐEN ĐOẠN TÊN BÊN TRÊN): ')
#		source = str(iii)
	print("--->>>XONG")
	print('')
	time.sleep(1)
	print("THIẾT LẬP MẶC ĐỊNH CỔNG RA 3.5 PI...")
	print('')
	# time.sleep(0.7)
	for j in range(0, ss):
		print ('OUTPUT LIST: '+str(j)+' LÀ THIẾT BỊ '+slist[j].description)
		if 'USB' in slist[j].description and 'output' in slist[j].name:
			sink = slist[j].index
			print ('ĐẦU RA USB SOUND')
		elif 'Analog Stereo' in slist[j].description and 'output' in slist[j].name and 'fallback' not in slist[j].name:
			sink = slist[j].index
			print ('ĐẦU RA 3.5 PI')
		else:
			sink = slist[0].index
		print('CÁC ĐẦU RA KHÁC VUI LÒNG QUAN SÁT VÀ CÀI ĐẶT THỦ CÔNG')
#			sss = input('NHẬP SỐ THỨ TỰ OUTPUT LIST: ')
#			sink = int(sss)
		# time.sleep(0.7)
#	os.system('amixer cset numid=3 1')
	print("--->>>XONG")
	print('')
	time.sleep(1)
	if str(source) != '':
		os.system('pacmd set-default-source '+str(source))
		os.system('pactl set-source-volume 0 80%')
	if str(sink) != '':
		os.system('pacmd set-default-sink '+str(sink))
		os.system('pactl set-sink-volume 0 80%')
	print('')
	print('NẾU MIC KHÔNG HOẠT ĐỘNG HÃY DÙNG LỆNH DƯỚI ĐÂY. LƯU Ý ĐÚNG TÊN MIC')
	print('')
	print ('pacmd set-default-source tên_mic, ví dụ: pacmd set-default-source '+str(source))
	print('')
	print ('NẾU KHÔNG CÓ ÂM THANH PHÁT RA LOA. HÃY CÀI ĐẶT LẠI OUTPUT VỚI LỆNH: ')
	print ('pacmd set-default-sink + số_thứ_tự_sinklist, ví dụ:  pacmd set-default-sink ' + str(sink))
	print('')
#	i=0
#	while i<5:
#		try:
#			i+=1 
#			if 'OmniVision' in blist[i].name:
#				source_ps3 = blist[i].name
#				with open('/etc/pulse/default.pa','a+') as pulsewrite:
#					pulsewrite.writelines('set-default-source '+ str(source_ps3))
#					print("Cài đặt mic PS3 làm mic mặc định")
#				break
#			elif 'mono' in blist[i].name:
#				source_mono = blist[i].name
#				with open('/etc/pulse/default.pa','a+') as pulsewrite:
#					pulsewrite.writelines('set-default-source '+ str(source_mono))
#					print("Cài đặt mic USB làm mic mặc định")
#				break
#		except:
#			pass

	time.sleep(1)
	os.system('pacmd set-source-volume 1 120000')
	time.sleep(1)
	print('[SETUP] - KẾT THÚC SETUP BOT LBMINH')
	try:
		print('SỐ MODULE LỖI BƯỚC 1: '+ str(len(c)))
		print('SỐ MODULE LỖI BƯỚC 2: '+ str(len(d)))
		time.sleep(1)
		if len(c)==0 and len(d)==0:
			print('CHÚC MỪNG BẠN. CÀI ĐẶT THÀNH CÔNG')
			print('VUI LÒNG THIẾT LẬP CẤU HÌNH TRONG FILE CONFIG.YAML TRƯỚC KHI DÙNG')
			print(" ")
			print("GÕ: 'python3 main.py' ĐỂ CHẠY THỦ CÔNG SAU KHI ĐÃ CẤU HÌNH XONG")
			print("GÕ: 'sudo systemctl start bot.service' ĐỂ KHỞI ĐỘNG BOT SAU 4 PHÚT")
		else:
			print('VUI LÒNG CÀI LẠI CÁC MODULE LỖI')

	except:
		pass
import time
try:
	os.chdir(path)
	os.system('sudo chmod -R 0777 '+path)
except:
	print('chmod ee')
print("CHƯƠNG TRÌNH CÀI ĐẶT BAO GỒM 5 PHẦN: ")
print("1/ CÀI ĐẶT APT  ")
print("2/ CÀI ĐẶT PACKAGE  ")
print("3/ CÀI ĐẶT SNOWBOY VÀ SERVICE  ")
print("4/ CẤU HÌNH MICROPHONE VÀ LOA ")
print("5/ HỖ TRỢ CẤU HÌNH BOT")
print('--------------------------------------------------------------------')
time.sleep(0.7)
a=input('Bạn có muốn chạy PHẦN 1 - CÀI ĐẶT GÓI không? - Xin trả lời (Y/N): ')
if str(a).upper() == 'Y':
	install_app()
else:
	time.sleep(0.7)
	print('Bỏ qua phần cài đặt gói - chuyển sang phần tiếp theo...')
	time.sleep(0.7)
time.sleep(0.7)
az=input('Bạn có muốn chạy PHẦN 2 - CÀI ĐẶT GÓI không? - Xin trả lời (Y/N): ')
if str(az).upper() == 'Y':
	install_pip()
else:
	time.sleep(0.7)
	print('Bỏ qua phần cài đặt gói - chuyển sang phần tiếp theo...')
	time.sleep(0.7)
azz=input('Bạn có muốn chạy PHẦN 3 - BUILD SNOWBOY VÀ SERVICE? - Xin trả lời (Y/N): ')
if str(azz).upper() == 'Y':
	build_snowboy()
else:
	time.sleep(0.7)
	print('Bỏ qua phần cài đặt gói - chuyển sang phần tiếp theo...')
	time.sleep(0.7)

b=input('Bạn có muốn chạy PHẦN 4 - CẤU HÌNH MICROPHONE VÀ LOA không? - Xin trả lời (Y/N): ')
time.sleep(0.7)
if str(b).upper() == 'Y':
	mic_set()
else:
	time.sleep(0.7)
	print('Bỏ qua phần cài đặt microphone và loa')
	time.sleep(0.7)
c=input('Bạn có muốn chạy PHẦN 5- HỖ TRỢ CẤU HÌNH BOT không? - Xin trả lời (Y/N): ')
time.sleep(0.7)
if str(c).upper() == 'Y':
	from termcolor import colored
	import gih
	config_bot()
	print("CẤU HÌNH HIỆN TẠI CỦA BOT LÀ: ")
	print('DOMAIN: '+ colored(gih.get_config('domain'),'green'))
	print('TOKEN: '+ colored(gih.get_config('longlived-token'),'green'))
	print('API: '+ colored(gih.get_config('api_active'),'green'))
	print('TTS: '+ colored(gih.get_config('tts'),'green'))
	print('QUÁ TRÌNH CÀI ĐẶT ĐÃ HOÀN TẤT. KẾT THÚC TRÌNH HỖ TRỢ CÀI ĐẶT SAU 3 GIÂY')
	time.sleep(3)
else:
	time.sleep(0.7)
	print('Bỏ qua phần cấu hình')
	time.sleep(0.7)
	print('QUÁ TRÌNH CÀI ĐẶT ĐÃ HOÀN TẤT. KẾT THÚC TRÌNH HỖ TRỢ CÀI ĐẶT SAU 3 GIÂY')
	time.sleep(3)

