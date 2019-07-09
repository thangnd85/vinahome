import os
import pyAesCrypt
#def save_login_info():
serial = input('Nhập serial để tạo key: ')
bufferSize = 64 * 1024
password = "5pdDixSUM3qPmho4HZ8G1670-lbminh"
path = './'+ serial
os.mkdir(path)
print(path)
path_file = path+'/data.aex'
path_file1= path +'/data.aes'
file_info=open(path_file,"w")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines(serial+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.writelines('000000002165JUT3'+ "\n")
file_info.writelines('0000000089ỌIUI65'+ "\n")
file_info.writelines('0000000000231234'+ "\n")
file_info.close()
pyAesCrypt.encryptFile(path_file, path_file1, password, bufferSize)
os.remove(path_file)
print('Key created: '+ path_file1)


