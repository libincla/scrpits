#!/usr/bin/env python

from multiprocessing import Process

def  exam(name):
	print 'hello!',name

if __name__ == '__main__':
	P = Process(target=exam,args=(['lilei']))
	P.start()
	P.join()
