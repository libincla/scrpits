#!/usr/bin/env python

from multiprocessing import Process
import os  

def run_bar(name):
	print 'Run child process %s (%s) ...'% (name, os.getpid())

if __name__ == '__main__':
	print 'Parent process is %s...' % os.getpid()
	pro = Process(target=run_bar,args=('test',))
	print 'new process will start'
	pro.start()
	pro.join()
	print 'new process end..'
