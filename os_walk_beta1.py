#!/usr/bin/env python
#coding:utf-8

import os

def main():
	for root,dirs,files in os.walk('/Users/libin/test'):
		print  root
		print  dirs
		#print  '!!!!!!!'
		#print  'time to file'
		print  files

if __name__ == '__main__':
	main()
