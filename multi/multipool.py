#!/usr/bin/env python

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print 'Run task %s (%s)....' % (name,os.getpid())
	start = time.time()
	time.sleep(random.random() * 2)
	end = time.time()
	print 'Task %s already runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
	print 'Parent process is %s' % os.getpid()
	pro  =  Pool()
	for i in range(10):
		pro.apply_async(long_time_task,args=(i,))
	print 'waiting for all subprocess done'
	pro.close()
	pro.join()
	print 'All subprocess done'


