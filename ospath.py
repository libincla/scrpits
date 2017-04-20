#!/usr/bin/env python
#coding:utf-8


import os
for dire in ('/tmp',r'c: \temp'):
	if os.path.isdir(dire):
		print '%s already exists' % dire
		break
else:
	print 'no temp directory available'
	dire = ''

if dire:
	os.chdir(dire)
	cwd = os.getcwd()
	print '当前目录在',cwd

	print '创建指定目录'

	os.mkdir('/Users/libin/tmp')
	os.chdir('/Users/libin/tmp')
	cwd = os.getcwd()
	print 'new working directory'
	print cwd

	print os.listdir(cwd)

	print 'creating test file'
	fobj = open('test1.txt','w+')
	fobj.write('foo\n')
	fobj.write('bar\n')
	fobj.close()
	
	print 'update current directory'
	print os.listdir(cwd)



	print 'now renaming testfile to newfilename'
	os.rename('test1.txt','test.txt')

	print 'update directory listing:'
	print os.listdir(cwd)

	path = os.path.join(cwd,os.listdir(cwd)[0])
	
	print ' full file pathname'
	print path

	print os.path.split(path)
	
	print '(filename,extension)'

	print os.path.splitext(os.path.basename(path))

	print  'display file contents'
	fobj1 = open(path)
	for eachline in fobj1:
		print eachline,
	fobj1.close()

	print 'now delete test file'
	os.remove(path)
	print 'update now directory listing:'
	print os.listdir(cwd)

	print  'Done'
