from socket import *
serverPort = 6789
name = "Yun of server"
value = 5
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    clientName = connectionSocket.recv(2048).decode()
    clientValue = int(connectionSocket.recv(2048).decode())
    if clientValue <= 0 or clientValue > 100:
        print("client'value out of range.connection close.")
        connectionSocket.close()
    else:
        print("client'name: ", clientName, "\tserver'name: ", name)
        print("client value: ", clientValue, "\tserver value: ",
              value, "\tsum of two integer: ", clientValue+value)
        connectionSocket.send(name.encode())
        connectionSocket.send(str(value).encode())
        connectionSocket.close()
