
try:
	import pulsectl
except:
	print("THIẾU MỘT GÓI CẦN THIẾT. XIN CHẠY LẠI python3 setupLBMINHBOT.py")
import os
import time
from termcolor import colored
print('-------------------------------------------------------------------')
print("[SETUP_MIC_SPEAKER] - THIẾT LẬP MICROPHONE VÀ MIC")

pulse = pulsectl.Pulse('my-client')
blist = pulse.source_list()
ee=len(blist)
slist=pulse.sink_list()
ss=len(slist)
#	print(blist)
print('')
print(colored('ĐANG NHẬN DIỆN MICROPHONE...','green'))
print('')
#time.sleep(0.7)
for i in range(0, ee):
	print ('MIC '+str(i)+' :'+blist[i].name)
	if 'OmniVision' in blist[i].name:
		source = blist[i].name
		print ('------------------->>>MIC ARRAY SONY PS3<<<--------------------------')
	elif 'mono' in blist[i].name:
		source = blist[i].name
		print('------------------------->>>MIC USB<<<-----------------------------')
	else:
		pass
#	time.sleep(0.7)
#			print ('KHÔNG RÕ LOẠI MIC BẠN ĐANG SỬ DỤNG HOẶC BẠN QUÊN CHƯA GẮN MIC')
#		iii = input('NHẬP TÊN MIC BẠN SỬ DỤNG (TỐT NHẤT LÀ BÔI ĐEN ĐOẠN TÊN BÊN TRÊN): ')
#		source = str(iii)
print(colored('--->>>XONG','green'))
print('')
#time.sleep(1)
print(colored('THIẾT LẬP MẶC ĐỊNH CỔNG RA 3.5 PI...','green'))
print('')
# time.sleep(0.7)
# for j in range(0, ss):
# 	print ('OUTPUT LIST: '+str(j)+' LÀ THIẾT BỊ '+slist[j].description)
# 	if 'USB' in slist[j].description:
# 		sink = slist[j].index
# 		print ('ĐẦU RA USB SOUND')
# 	elif 'Analog Stereo' in slist[j].description:
# 		sink = slist[j].index
# 		print ('ĐẦU RA 3.5 PI')
# 	else:
# 		pass
#			print('CÁC ĐẦU RA KHÁC VUI LÒNG QUAN SÁT VÀ CÀI ĐẶT THỦ CÔNG')
#			sss = input('NHẬP SỐ THỨ TỰ OUTPUT LIST: ')
#			sink = int(sss)
	# time.sleep(0.7)
time.sleep(0.7)
#os.system('amixer cset numid=3 1')

print(colored('--->>>XONG','green'))
#time.sleep(0.7)
print(colored('THIẾT LẬP ÂM LƯỢNG MỨC 80%','green'))
#time.sleep(0.7)
#os.system("amixer sset 'Master' 80%")
#time.sleep(0.7)
print(colored('--->>>XONG','green'))
print('')
#time.sleep(1)
print('')
#time.sleep(1)
print(colored('BẮT ĐẦU KHỞI ĐỘNG BOT...','green'))
