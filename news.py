from helper import *
import pyximport
pyximport.install(build_dir=”./build”)
from bs4 import BeautifulSoup as bs
headers = requests.utils.default_headers()
headers.update({
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
def getlink(data):
	if 'HÀI' in data:
		link = requests.get("http://netnews.vn/audio-hai.html", headers=headers)
	elif 'THỜI SỰ' in data:
		link = requests.get("http://netnews.vn/audio-thoi-su.html", headers=headers)
	elif 'THỂ THAO' in data:
		link = requests.get("http://netnews.vn/audio-the-thao.html", headers=headers)
	elif 'TRUYỆN LẠ' in data:
		link = requests.get("http://netnews.vn/audio-do-day.html", headers=headers)
	elif 'SƯC KHỎE' in data:
		link = requests.get("http://netnews.vn/audio-song-khoe.html", headers=headers)
	else:
		link = requests.get("http://netnews.vn/audio-thoi-su.html", headers=headers)		
	soup = bs(link.content,"lxml")
#	print(soup)
	c = soup.find_all("script")
	s = len (c)
	for i in range (0,s):
		if '.mp3' in str(c[i]):
			m = str(c[i])
#			link = re.sub(r'id[.+?] = ','',link)
#			l = re.match(r'http://.*?\.mp3',link)
#			print (link)
			start = m.find('http://')
			kk = m[start:]
			end = kk.find('.mp3')
			me = kk[0:end+4]
#			print (me)
	
	t = soup.find_all("a")
	ss = len(t)
	ll = []
	for i in range (0,ss):
		if ('http://' in str(t[i]) and '.html' in str(t[i]) and 'audio' in str(t[i])):
			l = str(t[i])
			ll.append(l)
#			print (str(i))
#			print (l)
#			l = bs(l,"lxml")
	qu = [me]
	sss = len(ll)
	for i in range (0,sss):
		h1 = str(ll[i])
		start = h1.find('href="')
		kk = h1[start:]
		end = kk.find('.html')
		h1l = kk[6:end+5]
#		print (h1l)
		url = 'http://netnews.vn/'+h1l
		link = requests.get(url, headers=headers)
		soup = bs(link.content,"lxml")
		c = soup.find_all("script")
		s = len (c)

		for j in range (0,s):
			if '.mp3' in str(c[j]):
				m = str(c[j])
#			link = re.sub(r'id[.+?] = ','',link)
#			l = re.match(r'http://.*?\.mp3',link)
#			print (link)
				start = m.find('http://')
				kk = m[start:]
				end = kk.find('.mp3')
				me = kk[0:end+4]
			
#				print (me)
				qu.append(me)
#	print (qu)
	return qu