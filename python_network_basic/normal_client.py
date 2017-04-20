#!/usr/bin/env python

import socket,sys

port = 80
host  = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(filename + '\r\n')

while True:
	buf = s.recv(1024)
	if not len(buf):
		break
	sys.stdout.write(buf)
