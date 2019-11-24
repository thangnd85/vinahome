
import speaking
import urllib.request
from bs4 import BeautifulSoup
def tintucmoi():
    url =  'https://vnexpress.net'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    new_feeds = soup.find('section', class_='featured container clearfix').find_all('a')
    i=0
    tintuc_candoc=""
    for feed in new_feeds:
        i+=1
        title = feed.get('title')
        if len(str(title))>10 and i> 1:
            tintuc_candoc =str(tintuc_candoc)+ " . " +str(title)

        if i>15:

            break
           
    print(tintuc_candoc)
    speaking.speak(tintuc_candoc)
    
        # try:
        #     if len(title)>10:
        #         speaking.speak('Một số tin tức mới')
        #         print(title)
        #         speaking.speak(title)
        # except:
        #     pass
