from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
# Create socket called clientSocket and establish a TCP connection with mailserver
mailport = 587
hostname = 'chenzm39@gmail.com'
password = 'q1615029259'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


starttls_command = 'STARTTLS\r\n'
clientSocket.send(starttls_command.encode())
tls_rev = clientSocket.recv(1024).decode()
print(tls_rev)
if tls_rev[:3] != '220':
    print('220 reply not received from server.')

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
sslclientSocket = ctx.wrap_socket(clientSocket)
auth = 'AUTH LOGIN\r\n'
sslclientSocket.write(auth.encode())
auth_rev = sslclientSocket.read(1024).decode()
print(auth_rev)
if auth_rev[:3] != '334':
    print('334 reply not received from server.')

user = base64.b64encode(hostname.encode()).decode()+'\r\n'
sslclientSocket.write(user.encode())
user_rev = sslclientSocket.read(1024).decode()
print(user_rev)
if user_rev[:3] != '334':
    print('334 reply not received from server.')

p = base64.b64encode(password.encode()).decode()+'\r\n'
sslclientSocket.write(p.encode())
p_rev = sslclientSocket.read(1024).decode()
print(p_rev)
if p_rev[:3] != '235':
    print('235 reply not received from server.')


# Send MAIL FROM command and print server response.
sslclientSocket.send("Mail from:<chenzm39@gmail.com>\r\n".encode())
recv1 = sslclientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send RCPT TO command and print server response.

sslclientSocket.send('RCPT TO:<chenzm39@qq.com>\r\n'.encode())
recv1 = sslclientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send DATA command and print server response.
sslclientSocket.send('DATA\r\n'.encode())
recv1 = sslclientSocket.recv(1024)
print(recv1)
if recv1[:3] != '354':
    print('354 reply not received from server.')
# Send message data.
sslclientSocket.send('\r\n'.encode())
sslclientSocket.send(msg.encode())
sslclientSocket.send(endmsg.encode())

# Message ends with a single period.

recv1 = sslclientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send QUIT command and get server response.
sslclientSocket.send('QUIT\r\n'.encode())
clientSocket.close()
