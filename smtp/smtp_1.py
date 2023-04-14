from socket import *
import base64
import ssl
# msg = 'FROM: chenzm39@qq.com\r\n'
# msg += 'TO: chenzm39@gmail.com\r\n'
# msg += 'Subject: ' + 'test' +  '\r\n'
# msg += "\r\n I love computer networks!"
# endmsg = "\r\n.\r\n"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
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

# heloCommand = 'STARTTLS\r\n'
# f(heloCommand, 334)
f("STARTTLS\r\n",334)
sslclientSocket = ssl.wrap_socket(clientSocket)

def g(message, flag):
    sslclientSocket.write(message.encode())
    recv = sslclientSocket.read(1024).decode()
    print(recv)
    if recv[:3] == flag:
        print('{flag} reply not received from server.')
        

heloCommand = 'AUTH LOGIN\r\n'
g(heloCommand, 334)


g((base64.b64encode(("chenzm39@gmail.com").encode()) + b'\r\n').decode(), 334)

g((base64.b64encode(("q1615029259").encode()) + b'\r\n').decode(), 334)

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
# 发送数据格式为邮件报文格式，包含首部行(from,to,可选subject)
# 不同于上述SMTP命令，首部行是自身的一部分，不能省略。
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

clientSocket.close
# Fill in end
