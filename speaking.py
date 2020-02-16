from helper import *
import gih
import os
import time
from pygame import mixer
seed = gih.get_config('seed')
if seed == 1:
	import pixels
tts_= gih.get_config('tts')
api_fpt = gih.get_config('api_fpt')
voice = gih.get_config('voice')
import wget

def count_chars(text):
	txt = ''
	result = 0
	for char in text:
		if char.isalpha() or char.isdigit():
			result += 1
			txt += char
	return result
def speak(audioString):
	audioString = audioString.replace('-','').replace('_','')
	consequitivedots = re.compile(r'\.{2,}')
	audioString = consequitivedots.sub('.', audioString)
	sentence = sent(audioString)
	l = len(sentence)
#	mixer.init()
	if tts_ == 'google1':
		mixer.init(54000, -16, 1, 4096)
		from io import BytesIO
		print('[MAIN] - NÓI')
		print('')
		print ('TTS: Google')
		for i in range (0,l):
			text = str(sentence[i])
			# text = text[:]
			print (text)
			count = count_chars(text)
			print (count)
			if count > 0:
				print ('Nội dung: '+text)
#Kiểm tra tồn tại file
				import os.path
				from os import path
				me = path.exists('tmp/google/'+text[:150]+'.mp3')
				if me ==True:
					if seed == 1:
						pixels.pixels.speak() 
					mixer.music.load('tmp/google/'+text[:150]+'.mp3')
					mixer.music.play()
					audio = MP3('tmp/google/'+text[:150]+'.mp3')
					t = float (audio.info.length)
					print ('Time delay :'+str(t))
					time.sleep(t)
				else:
					tts = gTTS(text,lang = 'vi')
#	tts.tokenizer.pre_procesNsors.end_of_line(audioString)
#				mp3_fp = BytesIO()
#				tts.write_to_fp(mp3_fp)
#				t = mp3_fp.truncate()/6800
#				t = float(t)
#				print ('Time delay: '+str(t))
#				mp3_fp.seek(0)
#				mixer.init()
					tts.save('tmp/google/'+text[:150]+'.mp3')
					time.sleep(3)
					if seed == 1:
						pixels.pixels.speak() 
#				mixer.music.load(mp3_fp)
					mixer.music.load('tmp/google/'+text[:150]+'.mp3')
					mixer.music.play()
#				mp3_fp.flush()
#				mp3_fp.seek(0)
#			mixer.init()
					audio = MP3('tmp/google/'+text[:150]+'.mp3')
					t = float (audio.info.length)
					print ('Time delay :'+str(t))
					time.sleep(t)				
			else:
#				mixer.init(48000, -16, 1, 4096)
				pass

#FPT	
	elif tts_ == 'fpt': 
		import random, requests
		mixer.init()
		keys = ['Os1MlynwG2W7eNFecfME0EOHZ9hCcobk','hFewll7iiYesYsc5TQO9RyPWogvYGXff','1E9dz9Oyax0WFbqVxIsBQSTuCf04yA6I']
		api_fpt_key = random.choice(keys)
		url = 'https://api.fpt.ai/hmi/tts/v5'
		headers = {'api_key': api_fpt_key ,'speed':'0','prosody':'1', 'voice':voice}
		for i in range (0,l):
			text = str(sentence[i])
			if len(text.strip()) < 1 or text.strip() == '.':
				pass
			else:
				print ('Nội dung: '+text)
				import os.path
				from os import path
				me = path.exists('tmp/'+text[:150]+'.mp3')
				if me ==True:
					if seed == 1:
						pixels.pixels.speak() 
					mixer.music.load('tmp/'+text[:150]+'.mp3')
					mixer.music.play()
					audio = MP3('tmp/'+text[:150]+'.mp3')
					t = float (audio.info.length)
					print ('Time delay :'+str(t))
					time.sleep(t)
				else:
					payload = text.encode('utf-8')
					
					try:
						r = requests.post(url, data=payload, headers=headers)
#						print (r)
						datajson = r.json()
						datajson=datajson['async']
						urltts = datajson
						print (urltts)
#						wget.download(urltts,'tmp/'+text+'.mp3')
						time.sleep(3)
						r = requests.get(urltts)
						with open('tmp/'+text[:150]+'.mp3', 'wb') as f:
							f.write(r.content)
							f.close()
						if seed == 1:	
							pixels.pixels.speak() 
						mixer.music.load('tmp/'+text[:150]+'.mp3')
						mixer.music.play()
						audio = MP3('tmp/'+text[:150]+'.mp3')
						t = float (audio.info.length)
						print ('Time delay :'+str(t))
						time.sleep(t)
#						os.remove('audio.mp3')
					except:
						print('error tts')
						pass
#TTS VIETTEL
	elif tts_ == 'viettel': 
		import json, requests, os.path
		from playsound import playsound
		from pathlib import Path
		mixer.init(44100, -16, 1, 4096)
		url = "https://vtcc.ai/voice/api/tts/v1/rest/syn"
		for i in range (0,l):
			text = str(sentence[i])
			if len(text.strip()) < 1 or text.strip() == '.':
				pass
			else:
				print ('Nội dung: '+text)
				import os.path
				from os import path
				from pydub import AudioSegment
				from pydub.playback import play
				me = path.exists('tmp/vtcc/'+text[:150]+'.wav')
				if me ==True:
					if seed == 1:
						pixels.pixels.speak() 
					sound = AudioSegment.from_wav('tmp/vtcc/'+text[:150]+'.wav')
					play(sound)
#					mixer.music.play()
#					audio = wav('tmp/vtcc/'+text+'.wav')
#					t = float (audio.info.length)
#					print ('Time delay :'+str(t))
#					time.sleep(t)
				else:
					data = {"text": text, "voice": "doanngocle", "id": "2", "without_filter": False, "speed": 1.0, "tts_return_option": 2}
#add your token to authenticate
					headers = {'Content-type': 'application/json', 'token': 'OOGW-uNFk3vFBoZ3T9BDp9OZLWeFmPcxxGHkqMHpjqXXF9oIuExGs5pSbsWv7jMM'}
					s = requests.Session()
					dirname = os.path.dirname(os.path.abspath('_file_'))
					cert_path = (dirname+'/wwwvtccai.crt')
					response = requests.post(url, data=json.dumps(data), headers=headers, verify=cert_path)
# Headers is a dictionary
					print(response.headers)

# Get status_code.
					print(response.status_code)

# Get the response data as a python object.
					data = response.content
# generated wav file is ./python-example.wav
					with open('tmp/vtcc/'+text[:150]+'.wav', "wb") as f:
						f.write(data)
						f.close()
					time.sleep(3)
					if seed == 1:	
						pixels.pixels.speak() 
					sound = AudioSegment.from_wav('tmp/vtcc/'+text[:150]+'.wav')
					play(sound)					
# TTS Google1
	elif tts_ == 'google':
		from pygame import mixer
		mixer.init(54000, -16, 1, 4096)
		from io import BytesIO
		print('[MAIN] - NÓI')
		print('')
		print ('TTS: Google')
		for i in range (0,l):
			text = str(sentence[i])
			# text = text[:]
			print (text)
			count = count_chars(text)
			print (count)
			if count > 0:
				print ('Nội dung: '+text)
				tts = gTTS(text,lang = 'vi')
#	tts.tokenizer.pre_procesNsors.end_of_line(audioString)
				mp3_fp = BytesIO()
				tts.write_to_fp(mp3_fp)
				t = mp3_fp.truncate()/5000
				t = float(t)
				print ('Time delay: '+str(t))
				mp3_fp.seek(0)
				mixer.init()
				if seed == 1:
					pixels.pixels.speak() 
				mixer.music.load(mp3_fp)
				mixer.music.play()
				mp3_fp.flush()
				mp3_fp.seek(0)
#			mixer.init()
				time.sleep(t)
			else:
				pass

					
					
		
# Speak English
def speaken(audioString):
	mixer.init(54000, -16, 1, 4096)
	tts = gTTS(audioString,lang = 'en')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	if seed == 1:
		pixels.pixels.speak() 
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
# Speak Korean
def speakko(audioString):
	mixer.init(54000, -16, 1, 4096)
	tts = gTTS(audioString,lang = 'ko')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init(
	if seed == 1:
		pixels.pixels.speak() 
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
# Speak Japanese
def speakja(audioString):
	mixer.init(54000, -16, 1, 4096)
	tts = gTTS(audioString,lang = 'ja')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	if seed == 1:
		pixels.pixels.speak() 
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
# Speak Chinese
def speakzh(audioString):
	mixer.init(54000, -16, 1, 4096)
	tts = gTTS(audioString,lang = 'zh-cn')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	if seed == 1:
		pixels.pixels.speak() 
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)
def speakvn(audioString):
	mixer.init(54000, -16, 1, 4096)
	tts = gTTS(audioString,lang = 'vi')
	mp3_fp = BytesIO()
	tts.write_to_fp(mp3_fp)
	mp3_fp.seek(0)
#	mixer.init()
	if seed == 1:
		pixels.pixels.speak() 
	mixer.music.load(mp3_fp)
	mixer.music.play()
	mp3_fp.seek(0)