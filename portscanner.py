print ('Hello and welcome to Ak47s very awesome program forked by PPW21.')
import socket


server =raw_input 'IP/URL to scan'
#Insert an URL or an IP Adress to scan above...


#Or, you could prompt the user for IP if you prefer
#server=raw_input("Which IP do you want to scan?:")

def pscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server,port))
        s.close()
        return True
    except:
        return False
#Type port range to scan...
for x in range(1,81):
    if pscan(x):
        print('Port',x,'is open!!!    *****')
    else:
        print('Port',x,'is closed')
