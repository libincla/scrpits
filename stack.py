#!/usr/bin/env python
#coding:utf-8

stack = []

def pushit():
	stack.append(raw_input('Enter a new choice: ').strip())

def popit():
	if len(stack) == 0:
		print 'stack cann\'t be empty'
	else:
		stack.pop();print 'pop it from the buttom'

def viewstack():
	print stack

CMD = {'u': pushit, 'o': popit,'v': viewstack }

def  showmenu():
	pr = """ p(U)sh p(O)p (V)iew (Q)uit 
	Enter Choice:  """
	
	#main
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			
			print ' you picked: [%s] ' % choice
			if  choice not in 'uovq':
				print 'invalid option, try again'
			else:
				break

		if choice == 'q':
			break
		CMD[choice]()

if __name__ == '__main__':
	showmenu() 
