#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import the json library
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
	audioString = audioString.replace('-',' ').replace('_',' ')
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
				while True:
					me = path.exists('tmp/google/'+text[:150]+'.mp3')
					if me ==False:
						tts = gTTS(text,lang = 'vi')
						tts.save('tmp/google/'+text[:150]+'.mp3')
						time_sleep = 1
						time_wait = 20
						tcount = 0
						while (me ==False and tcount < time_wait):
							time.sleep(time_sleep)
							tts.save('tmp/google/'+text[:150]+'.mp3')
							tcount += 1
					else:	
						if seed == 1:
							pixels.pixels.speak()
						audio = MP3('tmp/google/'+text[:150]+'.mp3')
						t = float (audio.info.length)							
						mixer.music.load('tmp/google/'+text[:150]+'.mp3')
						mixer.music.play()
						time.sleep(t)
						break
#FPT	
	elif tts_ == 'fpt': 
		import random, requests
		for i in range (0,l):
			text = str(sentence[i])
			if len(text.strip()) < 1 or text.strip() == '.':
				pass
			else:
				print ('Nội dung: '+text)
				import os.path
				from os import path
				while True:
					me = path.exists('tmp/fpt/'+text[:150]+'.mp3')
					if me==False:
						api_fpt_key = random.choice(api_fpt)
						url = 'https://api.fpt.ai/hmi/tts/v5'
						headers = {'api_key': api_fpt_key ,'speed':'0','prosody':'1', 'voice':voice}
						payload = text.encode('utf-8')
						url_return = requests.post(url, data=payload, headers=headers).json()['async']
						res_response = requests.get(url_return)
						res_status = res_response.status_code
#						print (url_return)
						time_sleep = 0.5
						time_wait = 20
						tcount = 0
						while (res_status == 404 and tcount < time_wait):
							time.sleep(time_sleep)
							res_response = requests.get(url_return)
							res_status = res_response.status_code
							tcount += 1
						if tcount == time_wait:
							print('error tts')
						with open('tmp/fpt/'+text[:150]+'.mp3', 'wb') as f:
							f.write(res_response.content)
							f.close()
					else:	
						mixer.music.load('tmp/fpt/'+text[:150]+'.mp3')
						mixer.music.play()
						audio = MP3('tmp/fpt/'+text[:150]+'.mp3')
						t = float (audio.info.length)
						print ('Time delay :'+str(t))
						time.sleep(t)
						break
#TTS VIETTEL
	elif tts_ == 'viettel': 
		token = gih.get_config('token')
		import json, requests, os.path
		from playsound import playsound
		from pathlib import Path
		from pygame import mixer
		url = "https://vtcc.ai/voice/api/tts/v1/rest/syn"
		for i in range (0,l):
			text = str(sentence[i])
			if len(text.strip()) < 1 or text.strip() == '.':
				pass
			else:
				print ('Nội dung: '+text)
				import os.path
				from os import path
				while True:
					from pydub import AudioSegment
					from pydub.playback import play
					me = path.exists('tmp/vtcc/'+text[:150]+'.wav')
					if me ==False:
						data = {"text": text, "voice": "hn-quynhanh", "id": "2", "without_filter": False, "speed": 1.0, "tts_return_option": 2}
						headers = {'Content-type': 'application/json', 'token': token}
						s = requests.Session()
						dirname = os.path.dirname(os.path.abspath('_file_'))
						cert_path = (dirname+'/wwwvtccai.crt')
						response = requests.post(url, data=json.dumps(data), headers=headers, verify=cert_path)
						print(response.headers)
						print(response.status_code)
						res_status = response.status_code
						time_sleep = 0.5
						time_wait = 20
						tcount = 0
						while (res_status != 200 and tcount < time_wait):
							time.sleep(time_sleep)
							response = requests.post(url, data=json.dumps(data), headers=headers, verify=cert_path)
							res_status = res_response.status_code
							tcount += 1
						if tcount == time_wait:
							print('error tts') 
						data = response.content
						with open('tmp/vtcc/'+text[:150]+'.wav', "wb") as f:
							f.write(data)
							f.close()
					else:
						if seed == 1:	
							pixels.pixels.speak() 
						sound = AudioSegment.from_wav('tmp/vtcc/'+text[:150]+'.wav')
						play(sound)
						break
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
				mp3_fp = BytesIO()
				tts.write_to_fp(mp3_fp)
				t = mp3_fp.truncate()/5400
				t = float(t)
				mp3_fp.seek(0)
				mixer.init()
				pixels.pixels.speak() 
				mixer.music.load(mp3_fp)
				mixer.music.play()
				mp3_fp.flush()
				mp3_fp.seek(0)
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
	sentence = sent(audioString)
	l = len(sentence)
	from pygame import mixer
	mixer.init(54000, -16, 1, 4096)
	from io import BytesIO
	print('[MAIN] - NÓI')
	print('')
	print ('TTS: Google')
	for i in range (0,l):
		text = str(sentence[i])
		print (text)
		count = count_chars(text)
		print (count)
		if count > 0:
			print ('Nội dung: '+text)
			tts = gTTS(text,lang = 'vi')
			mp3_fp = BytesIO()
			tts.write_to_fp(mp3_fp)
			t = mp3_fp.truncate()/5400
			t = float(t)
			print ('Time delay: '+str(t))
			mp3_fp.seek(0)
			mixer.init(54000, -16, 1, 4096)
			if seed==1:	
				pixels.pixels.speak() 
			mixer.music.load(mp3_fp)
			mixer.music.play()
			mp3_fp.flush()
			time.sleep(t)
		else:
			pass