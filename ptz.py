from requests.auth import HTTPDigestAuth
import requests
import json
import time

class control():
    def __init__(self,ip,user,password):
        self.ip=ip
        self.user=user
        self.password=password
    def set_preset(self,preset_number):
        url = self.ip+'/cgi-bin/ptz.cgi?action=start&channel=1&code=GotoPreset&arg1=0&arg2='+preset_number+'&arg3=0'
        r=requests.get(url, auth=HTTPDigestAuth(self.user,self.password))

    def len(self):
        url = self.ip+'/cgi-bin/ptz.cgi?action=start&channel=1&code=Up&arg1=0&arg2=5&arg3=0'
        print(url)
        r=requests.get(url, auth=HTTPDigestAuth(self.user,self.password))
        print(r.text)

    def xuong(self):
        url = self.ip+'/cgi-bin/ptz.cgi?action=start&channel=1&code=Down&arg1=0&arg2=5&arg3=0'
        r=requests.get(url, auth=HTTPDigestAuth(self.user,self.password))
        print(r)
    def trai(self):
        url = self.ip+'/cgi-bin/ptz.cgi?action=start&channel=1&code=Left&arg1=0&arg2=5&arg3=0'
        r=requests.get(url, auth=HTTPDigestAuth(self.user,self.password))
        print(r)
    def phai(self):
        url = self.ip+'/cgi-bin/ptz.cgi?action=start&channel=1&code=Right&arg1=0&arg2=5&arg3=0'
        r=requests.get(url, auth=HTTPDigestAuth(self.user,self.password))
        print(r)
