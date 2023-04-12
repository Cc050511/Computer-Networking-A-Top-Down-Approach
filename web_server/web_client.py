from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)
server_name = sys.argv[1]
server_port = sys.argv[2]
server_filepath = sys.argv[3]
print(f'{server_name} {server_port} {server_filepath}')
message = f'GET /{server_filepath} HTTP/1.1\t\nHost: {server_name}\t\n\t\n'
clientSocket.connect((server_name, int(server_port)))
clientSocket.send(message.encode())
recv_response = clientSocket.recv(1024).decode()
print(recv_response)
