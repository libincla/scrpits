#!/usr/bin/env python
#coding:utf-8

def mysum(x,y):
	return x + y

allNums = range(5)
t = 0

for i in allNums:
	t = mysum(t,i)
	print t


