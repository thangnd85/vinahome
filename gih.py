from helper import *
import requests
import json
import sqlite3 as lite
import os
import yaml
import time
from termcolor import colored
import pyximport
pyximport.install(build_dir=”./build”)
def get_config(request):

    stream = open('config.yaml','r')
    a = yaml.load(stream,Loader=yaml.SafeLoader)
    stream.close()
    a = a[request]
    return a
version = get_config('version_above084')
reminder = get_config('reminder')

def set_config(topic,state):
    file_name = "config.yaml"
    with open(file_name) as f:
        doc = yaml.safe_load(f)
    doc[topic] = state
    with open(file_name, 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)


def info_user():
    if os.path.exists('usin.db'):
        os.remove('usin.db')
    usin = lite.connect('usin.db',check_same_thread=False)
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS link_music_youtube (
                                            link1 text,
                                            link2 text,
                                            link3 text,
                                            link4 text,
                                            link5 text,
                                            link6 text,
                                            link7 text,
                                            link8 text,
                                            link9 text,
                                            link10 text,
                                            link11 text
                                            ); """
    if usin is not None: 
        cur2 = usin.cursor()
        cur2.execute(sql_create_projects_table)

    return usin
def data_init():
    if os.path.exists('hassdata.db'):
        os.remove('hassdata.db')
    con1 = lite.connect('hassdata.db',check_same_thread=False)
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS HASSINFO (
                                            entity_id_ex text,
                                            domain_ex text,
                                            friendly_name_ex text
                                            ); """
    if con1 is not None: 
        cur = con1.cursor()
        cur.execute(sql_create_projects_table)

    return con1
def data_command_init():
    con2 = lite.connect('command.db',check_same_thread=False)
    sql_command_table = """ CREATE TABLE IF NOT EXISTS customcommand (
                                            Command text,
                                            entity_id text,
                                            service text
                                            ); """
    if con2 is not None: 
        cur = con2.cursor()
        cur.execute(sql_command_table)
    return con2


def getinfo(domain, password, con1):
    r=''
    if version == 'right':
        url = domain+ '/api/states'
        headers = {
    'Authorization': 'Bearer '+ password,
    'content-type': 'application/json',
}

    else:

        url = domain+ '/api/states?api_password=' + password
        headers = {'content-type': 'application/json'}
    try:
        r = requests.get(url,headers = headers)
    except:
        print(colored('[MAIN]: ERROR - Không kết nối được Home Assistant tại địa chỉ '+ domain,'red'))
        time.sleep(0.5)
        print('')
        print(colored('[MAIN]: PASS - Hoạt động ở chế độ không link Home Assistant','green'))
        print('')
        return False
    if str(r)=='<Response [200]>':
        r = r.json()
        i = 0
        while i < len(r)-1 :
            i += 1
            x = r[i]
            y = x['entity_id']
            y = y.split('.')
            entity_id_ex = y[1]
            domain_ex = y[0]
            y = x['attributes']
            try:
                friendly_name_ex = y['friendly_name'].strip()
            except:
                friendly_name_ex =""
                pass
            if domain_ex == 'script' or domain_ex == 'light' or domain_ex == 'switch' or domain_ex=='sensor' or domain_ex =='binary_sensor' or domain_ex =='media_player' or domain_ex =='cover' or domain_ex =='input_select' or domain_ex =='alarm_control_panel' or domain_ex =='climate' or domain_ex =='device_tracker' :
                pre_write_data = (entity_id_ex, domain_ex, friendly_name_ex)
                
                with con1:
                    cur = con1.cursor()
                    cur.execute("INSERT INTO HASSINFO VALUES(?,?,?)",pre_write_data)
        print(colored('[MAIN]: LINKING - Tiến hành link Home Assistant.....', 'yellow'))
        print('')
        time.sleep(0.5)
        print(colored('[MAIN]: SUCCEEDED - Link thành công Home Assistant.','green'))
        print('')
        time.sleep(0.5)
        return True
    else:
        print(colored('[MAIN]: ERROR - Không kết nối được Home Assistant tại địa chỉ '+ domain,'red'))
        print('')
        time.sleep(0.5)
        print(colored('[MAIN]: PASS - Hoạt động ở chế độ không link Home Assistant','green'))
        print('')
        return False


def check_internet(url='http://www.google.com/', timeout=5):
    try:
        t = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False







        

