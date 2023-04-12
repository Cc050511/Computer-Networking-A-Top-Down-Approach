from socket import *
from time import time
serverPort = 12000
servername = '172.17.87.202'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
message = "this is ping of "
rtts = []
for n in range(1, 11):
    try:
        round_trip_time = time()
        clientSocket.sendto((message + str(n)).encode(),
                            (servername, serverPort))
        recvdata, serverAddress = clientSocket.recvfrom(1024)
        rtts.append(time() - round_trip_time)
        if recvdata:
            print(f'Ping: {n}\t round trip time(RTT): {rtts[-1]}')
    except OSError:
        print("Request timed out")

print(f'RTT\tmin: {min(rtts)}\tmax: {max(rtts)}\t average: {sum(rtts) / len(rtts)}\t loss rate: {len(rtts) / 10}')
clientSocket.close()
