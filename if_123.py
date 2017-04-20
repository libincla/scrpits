#!/usr/bin/env python
#coding:utf-8

		
from random import randint

your_choice = randint(1,6)
pc_choice =  randint(2,6)

if your_choice > pc_choice:
	print 'player point %d' % your_choice
	print 'PC     point %d' % pc_choice
	print 'player win!'
elif your_choice == pc_choice:
	print 'player point %d' % your_choice
	print 'PC     point %d' % pc_choice
	print 'draw'
else:
	print 'player point %d' % your_choice
	print 'PC     point %d' % pc_choice
	print 'PC win!'
