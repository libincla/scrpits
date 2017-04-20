#!/usr/bin/env python
#coding:utf-8

valid = False

count = 3
passwordlist = ['caiqin']
while  count > 0 :
	input = raw_input('输入你的密码: ')
	#检查合法的密码
	for  i in passwordlist:
		if input == i :
			valid = True
			break
	if not valid:
		print "非法输入"
		continue
	else:
		break
