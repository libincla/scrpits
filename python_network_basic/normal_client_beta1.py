#!/usr/bin/env python

import socket,sys

port = 80
host  = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	s.connect((host,port))
except socket.gaierror,e:
	print 'could not connecting to server: %s ' % e
	sys.exit(1)

s.sendall(filename + '\n')

while True:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)

