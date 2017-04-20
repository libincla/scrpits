#!/usr/bin/env python
#coding:utf-8

import os
filename =  raw_input('请输入一个名字: ')

filejb = open(filename,'w')

while True:
	writeline = raw_input("请键入一行 ('.' to Quit): ")
	if writeline != '.':
		filejb.write('%s%s' % (writeline,os.linesep))
	else:
		break
filejb.close()
