#!/usr/bin/env python

from multiprocessing import Process


def sayhi(i):
	print 'hi!',i

if __name__ == '__main__':
	for i in range(10):
		Process(target=sayhi,args=([i]))
