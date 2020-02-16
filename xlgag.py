
import sqlite3 as lite
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
con = lite.connect('data.db',check_same_thread=False)
def hamcat_control(data):

    data1=data
    print('-------------Thực hiện xử lý ngôn ngữ---------------')
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM hamcat")
        rows=cur.fetchall()
        for row in rows:
            for i in range(0,2):
                if row[i].upper() in data1.upper():
                    print('tìm thấy '+ row[i])
                    data1=data1.replace(str(row[i]),"")
                    data1=data1.strip()
    return data1
def xu_ly_gan_giong(data):
    data=str(data).upper()
    if 'MỞ' in data:
        print(data)
        locamo=data.find('MỞ')
        data=data[locamo+3:len(data)]
    elif 'TẮT' in data:
        locatat=data.find('TẮT')
        data=data[locatat+4:len(data)]
    data=hamcat_control(data)
    entity_name=data.strip()
    print(entity_name)
    a=fuzz.ratio(entity_name,'ĐÈN PHÒNG KHÁCH')
    print(a)
    return entity_name

if __name__=='__main__':
    data=input("nhap lenh di dai ca: ")
    xu_ly_gan_giong(data)