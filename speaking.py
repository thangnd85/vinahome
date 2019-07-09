from helper import *
import pyximport
pyximport.install(build_dir=”./build”)
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols
tts_= gih.get_config('tts')
api_fpt = gih.get_config('api_fpt')
voice = gih.get_config('voice')
mixer.init(48000, -16, 2, 4096)
def count_chars(text):
	txt = ''
	result = 0
	for char in text:
		if char.isalpha() or char.isdigit():
			result += 1
			txt += char
	return result

def speak(audioString):

	audioString = audioString.replace('?','?.')
	audioString = audioString.replace('!','!.')
	audioString = audioString.replace(':',':.')
	consequitivedots = re.compile(r'\.{2,}')
	audioString = consequitivedots.sub('.', audioString)
	sentence = sent(audioString)
	l = len(sentence)
#	mixer.init()
	if tts_ == 'google':
		mixer.init(48000, -16, 2, 4096)
		from io import BytesIO
		print('[MAIN] - NÓI')
		print('')
		print ('TTS: Google')
		for i in range (0,l):
			text = str(sentence[i])

			print (text)
			count = count_chars(text)
			if count > 0 :
				print ('Nội dung: '+text)
				tts = gTTS(text,lang = 'vi',slow=False, lang_check=True, pre_processor_funcs=[pre_processors.tone_marks, pre_processors.end_of_line, pre_processors.abbreviations])
#	tts.tokenizer.pre_procesNsors.end_of_line(audioString)
				mp3_fp = BytesIO()
				tts.write_to_fp(mp3_fp)
				t = mp3_fp.truncate()/5280+0.1
				t = float(t)
				print ('Time delay: '+str(t))
				mp3_fp.seek(0)
#				mixer.init()
				mixer.music.load(mp3_fp)
				mixer.music.play()
				mp3_fp.flush()
#				mp3_fp.seek(0)
#			mixer.init()
				time.sleep(t)
			else:
				pass

#FPT
	elif tts_ == 'fpt': 
		url = 'http://api.openfpt.vn/text2speech/v4'
		headers = {'api_key': api_fpt ,'speed':'1','prosody':'1', 'voice':voice}
		print ('TTS: FPT')
		mixer.init()		
		for i in range (0,l):
			text = str(sentence[i])
			if len(text.strip()) < 1 or text.strip() == '.':
				pass
			else:
				print ('Nội dung: '+text)			
				payload = text.encode('utf-8')
				try:
					r = requests.post(url, data=payload, headers=headers)
					print (r)
					datajson = r.json()
					datajson=datajson['async']
					urltts = datajson
					r = requests.get(urltts)
					with open('audio.mp3', 'wb') as f:
						f.write(r.content)
						f.close()
					mixer.music.load('audio.mp3')
					mixer.music.play()
					audio = MP3('audio.mp3')
					t = float (audio.info.length)
					print ('Time delay :'+str(t))
					time.sleep(t)
					os.remove('audio.mp3')
				except:
					print('error tts')
					pass


# Speak English
def speaken(audioString):
	tts = gTTS(audioString,lang = 'en')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
# Speak Korean
def speakko(audioString):
	tts = gTTS(audioString,lang = 'ko')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
# Speak Japanese
def speakja(audioString):
	tts = gTTS(audioString,lang = 'ja')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
# Speak Chinese
def speakzh(audioString):
	tts = gTTS(audioString,lang = 'zh-cn')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
