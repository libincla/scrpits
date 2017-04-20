#!/usr/bin/env python
#coding:utf-8

filen = raw_input('请输入一个文件名称: ')


fname = open(filen,'r')
for eachline in fname:
	print eachline,

#except:
#	print '也许是文件不存在'

