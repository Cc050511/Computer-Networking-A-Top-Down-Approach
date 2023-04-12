from socket import *
name = "Yun of client"
serverName = '172.17.87.202'
serverPort = 6789
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
value = input('input a integer values between 1 and 100 :')
clientSocket.send(name.encode())
clientSocket.send(value.encode())
name_recv = clientSocket.recv(2048).decode()
value_recv = clientSocket.recv(2048).decode()
print("From server: ", name_recv, "\tvalue: ", value_recv)
clientSocket.close()
