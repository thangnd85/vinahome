import os
import pulsectl
import time
#os.system('sudo killall pulseaudio')
#os.system('killall pulseaudio')
#os.system('pulseaudio --start')
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
	print ('KHÔNG RÕ LOẠI MIC BẠN ĐANG SỬ DỤNG HOẶC BẠN QUÊN CHƯA GẮN MIC')
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
	elif 'bcm2835 ALSA Analog Stereo' in slist[j].description and 'output' in slist[j].name and 'fallback' not in slist[j].name:
		sink = slist[j].index
		print ('ĐẦU RA 3.5 PI')
	elif 'output' in slist[j].name and 'alsa_output.platform-soc_audio.analog-stereo' in slist[j].name and 'seed' in slist[j].description:
		sink = slist[j].index
		print ('ĐẦU RA RESPEAKER')
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
#print(colored('BẮT ĐẦU KHỞI ĐỘNG BOT...','green'))
