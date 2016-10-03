import socket


server = '192.168.1.1'
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

for x in range(1,81):  #<--- Type port range to scan...
    if pscan(x):
        print('Port',x,'is open!!!    *****')
    else:
        print('Port',x,'is closed')






#Super easy port scanner by Ak47, don't laugh...


