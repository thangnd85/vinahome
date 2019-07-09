import pyAesCrypt
import os
import gser
serial = gser.getserial()
exists = os.path.isfile('./data.aes')

if exists:
    size = os.path.getsize('./data.aes')
    size = int(size)
    print('Tồn tại file key')
    if size != 871:
        print ('File không hợp lệ, đang xóa')
        os.remove('./data.aes')

else:
    os.system('wget -O data.aes http://34.83.28.247/'+serial+'/data.aes')
    size = os.path.getsize('./data.aes')
    size = int(size)
    if size != 871:
        os.remove('./data.aes')
def check_legal():
    bufferSize = 64 * 1024
    password = "5pdDixSUM3qPmho4HZ8G1670-lbminh"
    ok = 0
    # decrypt

    if os.path.exists('./data.aes'):
        pyAesCrypt.decryptFile("data.aes", "data.aex", password, bufferSize)
        with open("data.aex") as file:
            readfile=file.read().splitlines()
            serial_dangky = readfile[10]
        file.close()
        os.remove("data.aex")
        return serial_dangky
    else:
        return ok