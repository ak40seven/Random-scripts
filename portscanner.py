print ('Hello and welcome to Ak47s very awesome program forked by PPW21.')
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '192.168.1.1'
#Insert an URL or an IP Adress to scan above...


def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

#Type port range to scan...
for x in range(1,81):
    if pscan(x):
        print('Port',x,'is open!!!    *****')
    else:
        print('Port',x,'is closed')






#Super easy port scanner by Ak47, don't laugh...
# :D


