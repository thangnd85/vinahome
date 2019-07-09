TOP100 = {'pop':'ZWZB96AB', 'country': 'ZWZB96AE', 'rock': 'ZWZB96AC', 'dance': 'ZWZB96C7', 'r&b': 'ZWZB96C8', 'rap': 'ZWZB96AD', 'soundtrack': 'ZWZB96C9',
          'nhac tre':'ZWZB969E', 'tru tinh': 'ZWZB969F', 'que huong': 'ZWZB96AU', 'cach mang': 'ZWZB96AO', 'rock viet': 'ZWZB96A0', 'rap viet': 'ZWZB96AI', 'dance viet': 'ZWZB96AW'}
url_list = 'https://mp3.zing.vn/xhr/media/get-list?op=top100&start=0&length=20&id='
url_audio = 'https://mp3.zing.vn/xhr/media/get-source?type=audio&key='
prefix_url = 'https:'
import requests, time, random, vlc, threading
def get_codes(type_TOP):
	type_TOP = type_TOP.lower()
	uri = url_list + TOP100.get(type_TOP)
	re = requests.get(uri).json()
	items = re['data']['items']
	audio_codes = []
	for item in items:
		code = item['code']
		audio_codes.append(code)
	return audio_codes

def get_audio_links(type_TOP):
	alink = []
	audio_links = {}
	codes = get_codes(type_TOP)
	for code in codes:
		uri = url_audio + code
		re = requests.get(uri).json()['data']
		link = prefix_url + re['source']['128']
		duration =  int(re['duration'])
		audio_links[link] = duration
		alink.append(link)
	return alink
def zing_song(data):
	if 'TRỮ TÌNH' in data.upper():
		type_TOP = 'tru tinh'
	elif 'NHẠC TRẺ' in data.upper():
		type_TOP = 'nhac tre'
	elif 'QUÊ HƯƠNG' in data.upper():
		type_TOP = 'que huong'
	elif 'CÁCH MẠNG' in data.upper():
		type_TOP = 'cach mang'
	elif 'ROCK VIỆT' in data.upper():
		type_TOP = 'rock viet'
	elif 'RAP VIỆT' in data.upper():
		type_TOP = 'rap viet'
	elif 'DANCE VIỆT' in data.upper():
		type_TOP = 'dance viet'
	if 'POP' in data.upper():
		type_TOP = 'pop'
	elif 'ROCK' in data.upper():
		type_TOP = 'rock'
	elif 'COUNTRY' in data.upper():
		type_TOP = 'country'
	elif 'DANCE' in data.upper():
		type_TOP = 'dance'
	elif 'SOUNDTRACK' in data.upper():
		type_TOP = 'soundtrack'
	else:
		type_TOP = 'nhac tre'
	print (type_TOP)
	mp3_links = get_audio_links(type_TOP)
	return mp3_links
def phat_zing(playlist):
	inst = vlc.Instance()
	player = inst.media_list_player_new()
	mediaList = inst.media_list_new(playlist)
	player.set_media_list(mediaList)
	playing = set([1,2,3,4])
	return player
#	print (mp3_links)
