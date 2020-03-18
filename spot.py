import gih
import tsm
import sys
import spotipy
import spotipy.util as util
import time
import random
import speaking
import os
from pygame import mixer
api_boolean= gih.get_config('api_active')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
def re_ask():
	print('[MAIN] - HỎI LẠI')
	print('')
	mixer.music.load('resources/ding.wav')
	mixer.music.play()
# if api_boolean==1:
	more_data = tsm.main()
	return more_data
	# elif api_boolean ==0:
	#	 more_data = dem.recordAudio()
	#	 return more_data
class spo():
	def __init__(self,username,client_id,client_secret,redirect_uri):
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri=redirect_uri
		self.username=username
		self.scope='user-read-currently-playing,app-remote-control,user-read-playback-state,user-modify-playback-state,playlist-read-collaborative,user-library-read'
	def assign(self):
		token=util.prompt_for_user_token(username=self.username,client_id=self.client_id,client_secret=self.client_secret,redirect_uri=self.redirect_uri,scope=self.scope)
		if token:
			sp = spotipy.Spotify(auth=token)
		else:
			print("Can't get token for", self.username)
			sp=0
		return sp 
	def play_spotify_artist(self,sp,id=None):
		a=input("nhap ten nghe si muon tim di nao: ")
		results = sp.search(q=a, type='artist')
		items = results['artists']['items']
		if len(items) > 0:
			artist = items[0]
			print(artist['name'], artist['uri'])
		sp.start_playback(id,artist['uri'])
	def play_spotify_track(self,sp,id=None):
		a=input("nhap ten bai hat muon tim di nao: ")
		results = sp.search(q=a, type='track',limit=1)
		items = results['tracks']['items']
		if len(items) > 0:
			artist = items
			print(artist)
		# sp.start_playback(id,artist['uri'])
	# def pause_spotity(self,sp):
	def devices(self,sp):
		a=sp.devices()
		a=a['devices']
		device_list=[]
		i=1
		for ass in a:
			name=ass['name']
			id=ass['id']
			volume_cur=ass['volume_percent']
			ee=[i,name,id,volume_cur]
			device_list.append(ee)
			print(device_list) 
			i+=1
		if len(device_list)>1:
			speaking.speak('em tìm thấy '+str(len(device_list))+ ' thiết bị đang chạy Spotify, anh cần chạy trên thiết bị nào')
			for ii in device_list:
				speaking.speak('Thiết bị số '+ str(ii[0])+ ' là '+str(ii[1]) )
			hoi_lai=re_ask()
			print(hoi_lai)
			for iis in device_list:
				if str(iis[0]).upper() in str(hoi_lai).upper() or str(iis[1]).upper() in str(hoi_lai).upper():
					id=iis[2]
					namen=iis[1]
					volume_cur=iis[3]
					print(str(id))
					break
				else:
					id=device_list[0][2]
					namen=device_list[0][1]
					volume_cur=device_list[0][3]
					print(str(id))
			return id,namen,volume_cur
		elif len(device_list)==1:
			id=device_list[0][2]
			namen=device_list[0][1]
			volume_cur=device_list[0][3]
			return id,namen,volume_cur
		else:
			sai='no'
			return sai
	def pause(self,sp,id=None):
		sp.pause_playback(id)
	def next_track(self,sp,id=None):
		sp.next_track(id)
	def previous_track(self,sp,id=None):
		sp.previous_track(id)
	def shuffle(self,sp,state,id=None):
		sp.shuffle(state,id)
	def play_spotify_playlist(self,sp,id=None):
		aaa=sp.current_user_playlists()
		ofsset=aaa['items'][0]['tracks']['total']
		aaa=aaa['items'][0]['uri']
		offset={'position':random.randint(0,offset)}
		print(offset)
		sp.start_playback(id,aaa,offset=offset)
		print(aaa)
	def current_track(self,sp):
		b=sp.current_user_playing_track()
		c=b['item']['name']
		d=b['item']['artists'][0]['name']
		resu=str(c) + " "+ str(d)
		print(resu)
		speaking.speak("đang phát bài "+str(c) + " trong playlist mặc định do ca sĩ " + str(d) +" trình bày.")
		return resu
def play_current_playlist(username,client_id,client_secret,redirect_uri,data):
	if 'SPOTIFY' in str(data).upper():
		a=spo(username,client_id,client_secret,redirect_uri)
		sp=a.assign()
		id=a.devices(sp)
		print('id='+str(id[0]))
	   # sp.shuffle(True, id[0])
		try:
			# id = id[random.randint(0,len(id)-1)]
			print(str(id[0]))
			# a.play_spotify_artist(sp,str(id[1]).strip("'[]'"))
			# time.sleep(3)
			a.play_spotify_playlist(sp,id[0])
			resu=a.current_track(sp)
			speaking.speak(" nhạc đang được phát trên "+ id[1])
		except Exception as e:
			print(e)
			print('không thấy spotify trên thiết bị nào cả')
			speaking.speak('em không tìm thấy thiết bị Spotify nào đang được mở')
			time.sleep(3)
		return sp,a
	else:
		sp=False
		a=False
		return sp,a
# sp=play_current_playlist('drlbminh','d6881de9093040d8b9c18d669224b559','8f233b0f5037456b9c5e084f3f069efd','http://localhost:9999/','spotify')
# time.sleep(3)
# sp[0].volume(40)