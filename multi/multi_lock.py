#!/usr/bin/env python
#coding:utf-8

from multiprocessing  import Lock,Process

def f_exam(l,i):
	l.acquire()
	print 'hi!',i
	l.release()

if __name__ == '__main__':
	lock = Lock()

	for  i in range(10):
		Process(target=f_exam,args=(lock,i)).start()
