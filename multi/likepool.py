#!/usr/bin/env python

from multiprocessing import Pool

def exam(x):
	return x * x

if __name__ == '__main__':
	p = Pool()
	print (p.map(exam,[1,2,3]))
