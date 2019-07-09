import sqlite3 as lite
import xlgag
from fuzzywuzzy import fuzz
con2 = lite.connect('hassdata.db')
with con2:
	cur =con2.cursor()
	cur.execute("SELECT * FROM HASSINFO")
	rows1 = cur.fetchall()


def export_e_d(friendly_name):
	entity_id_ex=[]
	domain_ex=[]
	
	for row in rows1:
		i = 0
		while i < len(friendly_name):
			if row[2].upper()== friendly_name[i].upper():
				entity_id_ex.append(row[0])
				domain_ex.append(row[1])
				break
			i += 1
	return domain_ex, entity_id_ex
			


def check_fr(data):
	device_arr = []
	for row in rows1:
		if row[2].upper() in data.upper():
			device_arr.append(row[2])
	print(device_arr)
	x=0

	while True:
		y=0
		while True:
			if y==x:
				pass
			else:
				try:
					if device_arr[y].upper() in device_arr[x].upper():
						print('xoa phan tu y')
						device_arr.pop(y)
						y-=1
						if x==0:
							x=0
						else:
							x-=1
				except:
					break
			y += 1
			if y> len(device_arr):
				break
		x+=1
		if x > len(device_arr):
			break
	print(device_arr)
	if int(len(device_arr))==0:
		print('tiến hành xử lý gần giống')
		entity_name = xlgag.xu_ly_gan_giong(data)
		print('xử lý ra được: '+ entity_name)
		b=0
		a=0
		for row in rows1:
			a=fuzz.ratio(str(entity_name).upper(),row[2].upper())
			print(str(entity_name).upper()+" so với "+row[2].upper() +" a có giá trị : "+  str(a))
			if a>b: 
				b=a
				entity_name1=row[2]
			else:
				pass
		print('tỷ lệ cao nhất là: '+ entity_name1+ ' '+ str(b))
		print(entity_name1)
		device_arr.append(entity_name1)
	return device_arr

			
		


