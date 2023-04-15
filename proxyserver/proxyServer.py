from socket import *
import sys, ssl
# if len(sys.argv) <= 1:
#     print(
#         'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
#     sys.exit(2)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
# serverPort = sys.argv[1]
tcpSerSock.bind(('', 8888))
tcpSerSock.listen(10)
# Fill in end.
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()  # Fill in start. # Fill in end.
    print(message)
    # Extract the filename from the given message
    if (message == ''):
        continue
    filename = message.split()[1].partition("/")[2]
    if('favicon.ico' in filename):
        continue
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        for line in outputdata:
            tcpCliSock.send(line.encode() + b"\r\n")
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            if 'http://' in message.split()[1]:
                hostn = message.split()[1][7:].split('/')[0]
            elif 'https://' in message.split()[1]:
                hostn = message.split()[1][8:].split('/')[0]
            else:
                hostn = message.split()[1].split('/')[1]
            for line in message.splitlines():
                if "Referer: " in line:
                    hostn = line[9:].partition('8888/')[2]
            print("hostn:", hostn)
            ctx = ssl.create_default_context()
            sslc = ctx.wrap_socket(c, server_hostname=hostn)

            # try:
            # Connect to the socket to port 80
            # Fill in start.
            sslc.connect((hostn, 443))
            # Fill in end.
            # Create a temporary file on this socket and ask port 80 for the file requested by the client
            print("运行到这里1？")
            fileobj = sslc.makefile('rwb', 0)
            print("运行到这里2？")
            requestMsg = f"GET https://{hostn} HTTP/1.1\r\nHost: {hostn}\r\n\r\n"
            print(requestMsg)
            fileobj.write(requestMsg.encode())
            # Read the response into buffer
            # Fill in start.
            serverResponse = fileobj.read()
            print("运行到这里3？")
            # print(serverResponse)
            # Fill in end.
            # Create a new file in the cache for the requested file.
            # Also send the response in the buffer to client socket and the corresponding file in the cache
            if b'<!DOCTYPE html>' in serverResponse:
                tmpFile = open(f'{filename}.html', "wb")
            else:
                tmpFile = open(f'{filename}', "wb")
                
            # Fill in start.
            print(serverResponse.split(b'\r\n\r\n')[0].decode())
            # tmpFile.write(serverResponse)
            tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
            tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
            tcpCliSock.send(serverResponse.split(b'\r\n\r\n')[1])
            tmpFile.close()
            # Fill in end.
            # except:
            #     print("Illegal request")
            c.close()
        else:
            # HTTP response message for file not found
            # Fill in start.
            print("404 NOT FOUND")
            # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
    # break
# Fill in start.
tcpSerSock.close()
# Fill in end.
