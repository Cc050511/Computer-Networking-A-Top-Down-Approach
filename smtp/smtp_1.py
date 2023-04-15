from socket import *
import base64
import ssl

msg = "\r\n I love math!\nI love computer networks!"
endmsg = "\r\n.\r\n"
account = 'chenzm39@gmail.com'
password = 'wcsqnvuiifrvuyqs'  # app password
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'  # Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
# Fill in end


def f(message, flag):
    clientSocket.send(message.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] == flag:
        print('{flag} reply not received from server.')


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
f(heloCommand, 250)

f("STARTTLS\r\n", 334)
ctx = ssl.create_default_context()
sslclientSocket = ctx.wrap_socket(clientSocket, server_hostname=mailserver)


def g(message, flag):
    sslclientSocket.write(message.encode())
    recv = sslclientSocket.read(1024).decode()
    print(recv)
    if recv[:3] == flag:
        print('{flag} reply not received from server.')


heloCommand = 'AUTH LOGIN\r\n'
g(heloCommand, 334)


g((base64.b64encode((account).encode()) + b'\r\n').decode(), 334)

g((base64.b64encode(password.encode()) + b'\r\n').decode(), 334)

# Send RCPT TO command and print server response.
# Fill in start
toCommand = 'MAIL FROM: <chenzm39@gmail.com>\r\n'
g(toCommand, 250)
toCommand = 'RCPT TO: <chenzm39@qq.com>\r\n'
g(toCommand, 250)
# Fill in end
# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
g(dataCommand, 354)
# Fill in end
# Send message data.
# Fill in start
# clientSocket.send('FROM: chenzm39@qq.com\r\n'.encode())
sslclientSocket.write(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
g(endmsg, 250)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
g(quitCommand, 221)

clientSocket.close()
# Fill in end
