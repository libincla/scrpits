#!/usr/bin/env python
#coding:utf-8
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
	doprob()

if __name__ == '__main__':
	main()
