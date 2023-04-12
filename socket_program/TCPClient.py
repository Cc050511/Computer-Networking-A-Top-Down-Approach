from socket import *
serverName = '172.17.87.202'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedMessage = clientSocket.recv(1024)
print("From Server: ", modifiedMessage.decode())
clientSocket.close()
