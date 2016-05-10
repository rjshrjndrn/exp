#!/usr/bin/python
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect(('192.168.1.103',port))
print s.recv(1024)
s.close()
