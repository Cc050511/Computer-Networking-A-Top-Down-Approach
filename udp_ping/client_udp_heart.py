from socket import *
from time import time, sleep
serverPort = 12000
servername = '172.17.87.202'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
timestamps = time()
while True:
    try:
        timestamps = time()
        clientSocket.sendto(('HEARTBEAT' + str(timestamps)).encode(),
                            (servername, serverPort))
        clientSocket.recvfrom(1024)
        print('server is running.')
        break
    except OSError:
        print("Request timed out.")
        if time() - timestamps > 15:
            print('server is not running.')
            break

clientSocket.close()
