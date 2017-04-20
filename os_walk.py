#!/usr/bin/python
#coding:utf-8

import os

for rootpath,dirs,files in os.walk("/Users/libin/scripts",topdown=False):
	for i in files:
		print (os.path.join(rootpath,i))
	for  i in dirs:
		print (os.path.join(rootpath,i))
