#!/usr/bin/env python
#coding:utf-8
#第一个while 循环只是检测三次做题是否正确，无论如何都是会退出循环的
#第一个while循环包含到第二个循环中，第二个循环主要处理是否继续




from operator import add,sub
from random import randint,choice


ops = {'+':add,'-':sub}
MAXTRIES = 2


def doprob():
	op = choice('+-')
	nums = [randint(1,10) for i in range(2)] #type is list
	answer = ops[op](*nums)#这里*表示传列表或者元组进去,**表示传字典进去
	try_time = 0
	express = '%d %s %d = ' %(nums[0],op,nums[1])

	while True:
		try:
			if int(raw_input(express)) == answer:
				print 'correct'
				break
			if try_time == MAXTRIES:
				print 'the Answer is %d' %(answer)
				break #it means one is good
			else:
				print 'try again'
				try_time += 1
		except (KeyboardInterrupt,EOFError,ValueError):
			print  'invalid input .... try again'


def main():
	while True:
		doprob()
		try:
			operate = raw_input('Again? [y/n]').lower()
			if operate and operate[0] == 'n':
				break

		except (KeyboardInterrupt,EOFError):
			break

if __name__ == '__main__':
	main()
