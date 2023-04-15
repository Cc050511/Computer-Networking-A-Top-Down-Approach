# SMTP Lab
文件结构

    smtp.py
    smtp_1.py
    test.py

`smtp.py`实现使用qq邮箱发送邮件，服务器和端口号分别为`smtp.qq.com`和`25`

    在4.13日成功实现，能够正确运行
    4.14日再次运行，运行失败，失败提示代码如下

`220 reply not received from server.
Traceback (most recent call last):
File "d:\study\math\计算机网络\code\smtp.py", line 33, in <module>
f(heloCommand, 250)
File "d:\study\math\计算机网络\code\smtp.py", line 21, in f
recv = clientSocket.recv(1024).decode()
ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。`

`smtp_1.py`试图实现gmail发送邮件，未能实现出来。

    1. 可能需要vpn
    2. 需要启用TLS/SSL并且使用ssl库的wrap_socket()函数
    3. 失败原因如下

`Traceback (most recent call last):
File "d:\study\math\计算机网络\code\smtp\smtp_1.py", line 16, in <module>
clientSocket.connect((mailserver, 587))
TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。`

`test.py`是网上找到的代码，用谷歌邮箱通过ssl发送文件,源文件去掉不必要的代码后报错ssl.wrap_socket已弃用，需修改为`ctx = ssl.SSLContext()` `ctx.wrap_socket`。修改后报错与`smtp_1.py`一致。

### 未知原因导致无法与邮件服务器建立TCP连接
目前所学无法得知具体原因，猜测为**网络状况差**

# 4.15更新，`smtp_1.py`运行成功
1. 不需要vpn就可以连接到smtp.gmail.com
2. 在STARTTLS命令后为socket套上ssl加密
3. 开启谷歌两步验证，并获取一个app password替换密码登录
4. gmail可以不包含FROM和TO首部，仅需主体与结束语句独占一行的`.`

```
\r\n I love computer networks!\r\n 
.\r\n
```

一些关于登录命令的讲解[click here](https://www.samlogic.net/articles/smtp-commands-reference-auth.htm)

对于解决`Username and Password not accepted`有很好帮助的[回答](https://stackoverflow.com/questions/75021886/gmail-smtp-send-535-5-7-8-username-and-password-not-accepted)