from socket import *
import ssl
host = 'i0.hdslb.com'
filepath = 'https://i0.hdslb.com/bfs/face/8185cc2d3a7f9f69491e2009f9b987e7de37e9be.jpg@25w_25h.jpg'
c = socket(AF_INET, SOCK_STREAM)  # Fill in start. # Fill in end.
ctx = ssl.create_default_context()
sslclientSocket = ctx.wrap_socket(c, server_hostname=host)
sslclientSocket.connect((host, 443))
fileobj = sslclientSocket.makefile('rwb', 0)
requestMsg = f"GET {filepath} HTTP/1.0\r\nHost: {host}\r\n\r\n"
print(requestMsg)
fileobj.write(requestMsg.encode())
serverResponse = fileobj.read()
head = serverResponse.split(b'\r\n\r\n')[0].decode()
serverResponse = serverResponse.split(b'\r\n\r\n')[1]
print(head)
type = ''
for line in head.splitlines():
    if 'Content-Type: ' in line:
        type = line[14:].split('/')[1]
file = open(f'tt.{type}', 'wb')
print(serverResponse)
file.write(serverResponse)
file.close()
c.close()
