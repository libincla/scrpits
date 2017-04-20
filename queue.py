#!/usr/bin/env python
#coding:utf-8

queue = []

def pushit():
	queue.append(raw_input('Enter a new choice: ').strip())

def popit():
	if len(queue) == 0:
		print 'queue cann\'t be empty'
	else:
		queue.pop(0);print 'pop it from the first'

def viewqueue():
	print queue

CMD = {'u': pushit, 'o': popit,'v': viewqueue }

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
