# import socket module
from socket import *
import threading


def web_process(connectionSocket):
    try:
        message = connectionSocket.recv(
            2048).decode()  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()  # Fill in start #Fill in end
        f.close()
        # Send one HTTP header line into socket
        # Fill in start
        outputdata.insert(0, 'HTTP/1.1 200 OK\r\n\r\n')
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(outputdata.encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 4567
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    thread = threading.Thread(target=web_process, args=(connectionSocket,))
    thread.start()
