# Cài thêm 
# pip install bing_tr requests fuzzywuzzy pytest jmespath coloredlogs ratelimit
import requests
from requests import get
import datetime
from datetime import timedelta
#from bing_tr import bing_tr as translate
#from google_tr import google_tr as translate
from googletrans import Translator
translator = Translator()
import gih
latlong=gih.get_config('toado')
g_ip = 0    # Global Variable of IP Address
g_lat = latlong[0]   # Global Variable of Latitude
g_lon = latlong[1]   # Global Variable of Longnitude
def ip_finder():
    global g_ip  # Global Variable of IP Address
    global g_lat # Global Variable of Latitude
    global g_lon # Global Variable of Longnitude
    if(g_ip==0):
        ip = get('https://api.ipify.org')  # Fetching Current Device Public IP address
        if ip.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(ip.status_code))
        else:
            ip = ip.text
            g_ip = ip
    yourapi = '128979ae3de728602f249354a85ac508' # Your API key
    ip_url = 'http://api.ipstack.com/'+g_ip+'?access_key='+yourapi
    jsn_ip = requests.get(ip_url)
    if jsn_ip.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(jsn_ip.status_code))
    else:
        ip_result = jsn_ip.json()
        g_lat = ip_result['latitude']      # Set the Latitude
        g_lon = ip_result['longitude']     # Set the Longitude
def weather_json(mode,arr):
    global g_ip  # Global Variable of IP Address
    global g_lat # Global Variable of Latitude
    global g_lon # Global Variable of Longnitude
    if (mode=='ip' or mode=='IP'):
        if(arr==0):
            if(g_ip==0):
                ip_finder()  # For Collecting IP,Lat,Lon
            else:
                g_ip = arr
                ip_finder()  # For Collecing the Lat Lon
        else:
                g_ip = arr
                ip_finder()  # For Collecing the Lat Lon
    elif (mode=='LATLON' or mode=='latlon'):
        if(arr[0]!=0 and arr[1]!=0  ):
            g_lat = arr[0]
            g_lon = arr[1]
        else:
            g_ip = 0
            g_lat = latlong[0]
            g_lon = latlong[1]
            ip_finder()
    else:
        g_lat = latlong[0]
        g_lon = latlong[1]
        ip_finder()
    if(g_lat==0 or g_lon==0):
        return('Error Input')
    else:
        your_darksky_api=gih.get_config('api_darksky')
        #url = 'https://api.darksky.net/forecast/'+your_darksky_api+'/'+str(g_lat)+','+str(g_lon)+'?lang=vi'
        url = 'https://api.darksky.net/forecast/'+your_darksky_api+'/'+str(g_lat)+','+str(g_lon)+'?lang=vi'
        jsn = requests.get(url)
        if jsn.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(jsn.status_code))
        else:
            result = jsn.json()
            return(result)
def current(mod,arr):
    result = weather_json(mod,arr)
    dic={} # Result Dictionary
    fer = result['currently']['temperature']
    cel = (fer-32)*(5/9) # Fahrenheit to Celsius conversion 
    hum = int(result['currently']['humidity'] * 100) # Humidity on percentage
    dic["overal"]=result['currently']['summary']
    dic["temp"]="%.1f" % cel
#    dic["Current Temperature in F"]="%.1f" %fer
    dic["hum"]=hum
    dic["wind"]=result['currently']['windSpeed']
#    dic["Current Wind Pressure"]=result['currently']['pressure']
    return(dic)
def hourly(mod,arr):
    result = weather_json(mod,arr)
    dic={'today':{"%.1f"%i:{} for i in range(25)},'tomorrow':{"%.1f"%i:{} for i in range(25)}}
    for i in range (1,49):
        fer = result['hourly']['data'][i]['temperature']
        cel = (fer-32)*(5/9)                 # Fahrenheit to Celsius conversion 
        hum = int(result['hourly']['data'][i]['humidity'] * 100)  # Humidity on percentage
        if(i<=24):
            dic['today']["%.1f" %i]["overal"]= result['hourly']['data'][i]['summary']
            dic['today']["%.1f" %i]["temp"]="%.1f" % cel
#            dic['today']["%.1f" %i]["Temperature in F"]="%.1f" %fer
            dic['today']["%.1f" %i]["hum"]=hum
            dic['today']["%.1f" %i]["wind"]=result['hourly']['data'][i]['windSpeed']
#            dic['today']["%.1f" %i]["Wind Pressure"]=result['hourly']['data'][i]['pressure']
        else:
            tm  = i - 24
            dic['tomorrow']["%.1f" %tm]["overal"]= result['hourly']['data'][i]['summary']
            dic['tomorrow']["%.1f" %tm]["temp"]="%.1f" % cel
#            dic['tomorrow']["%.1f" %tm]["Temperature in F"]="%.1f" %fer
            dic['tomorrow']["%.1f" %tm]["hum"]=hum
            dic['tomorrow']["%.1f" %tm]["wind"]=result['hourly']['data'][i]['windSpeed']
#            dic['tomorrow']["%.1f"%tm]["Wind Pressure"]=result['hourly']['data'][i]['pressure']
    return(dic)
def weekly(mod,arr):
    result = weather_json(mod,arr)
    x = datetime.datetime.now()
    dic = {}
    for i in range (1,7):
        r_date = x+datetime.timedelta(i)
        dic[r_date.strftime("%d")]={}
    for i in range (1,7):
        r_date = x+datetime.timedelta(i)
        s = []
        mfer = result['daily']['data'][i]['temperatureMax']
        mcel = (mfer-32)*(5/9)                # Fahrenheit to Celsius conversion
        Mfer = result['daily']['data'][i]['temperatureMin']
        Mcel = (Mfer-32)*(5/9)              # Fahrenheit to Celsius conversion
        hum = int(result['daily']['data'][i]['humidity'] * 100) # Humidity on percentage
        dic[r_date.strftime("%d")]["overal"]=result['daily']['data'][i]['summary']
        dic[r_date.strftime("%d")]["mintemp"]="%.1f" % Mcel
#        dic[r_date.strftime("%d")]["Max Temperature in F"]="%.1f" %Mfer
        dic[r_date.strftime("%d")]["maxtemp"]= "%.1f" % mcel
#        dic[r_date.strftime("%d")]["Min Temperature in F"]="%.1f" %mfer
        dic[r_date.strftime("%d")]["hum"]=hum
        dic[r_date.strftime("%d")]["wind"]=result['daily']['data'][i]['windSpeed']
#        dic[r_date.strftime("%d")]["Wind Pressure"]=result['daily']['data'][i]['pressure']
    return(dic)

