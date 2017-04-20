#!/usr/bin/env python

from multiprocessing import Process,Manager

def f(d,l):
	d['x'] = 1
	d['2'] = 2
	d[0.3] = None
	l.reverse()

if __name__ == '__main__':
	manager = Manager()
	
	d =  manager.dict()
	l =  manager.list(range(20))
	
	p =  Process(target=f,args=(d,l))
	p.start()
	p.join()

	print d
	print l
