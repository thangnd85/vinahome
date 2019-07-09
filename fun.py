from helper import *
import pyximport
pyximport.install(build_dir=”./build”)
def truyen():
	headers = requests.utils.default_headers()
	headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

	link = requests.get("https://cuoibebung.com", headers=headers)
	soup =BeautifulSoup(link.content,"lxml")
	#print(soup)
	t = soup.find_all("h2")
	c = soup.find_all("div")
	s = len (c)
	tr = []
	for i in range (0,s):
    
		text = "entry-content"
		if '<div class="entry-content">' in str(c[i]) and 'Minoom – Game hay:' not in str(c[i]) and 'Game hay, có thể chơi thư giãn' not in str(c[i]):
			st = str(c[i])
#        print (str(i))
#        print (st)
			stt = re.sub(r'<.+?>','',st)
			stt = stt.replace('Chia sẻTweet','')
			stt = stt.replace('cuoi.xitrum.net','')
#        print (stt)
			tr.append(stt)
	truyen = random.choice(tr)
	print (truyen)
	return truyen
    
        
