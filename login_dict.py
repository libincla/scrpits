#!/usr/bin/env python
#coding:utf-8

#初始化一个字典用来存储账号密码
login_db = {}


def newuser():
	hint = 'login design: '
	#这里判断字典中是否有输出的名字
	while True:
		login_name = raw_input(hint)
		if login_db.has_key(login_name):
			hint = 'name already exist, try another'
			continue
		else:
			break
	#获取密码
	passwd = raw_input('input your password: ')
	login_db[login_name] = passwd

def  olduser():
	name =  raw_input('login: ')
	passwd = raw_input('password: ')
	pwd = login_db.get(name)
	
	if pwd == passwd:
		print 'welcome back!', name
	else:
		print 'login incorrect!'

def showmenu():
	hint = '''
	(N)ew Useri
	(E)xisting User
	(Q)uit
	Enter your choice: '''

	done = False
	while not done:
		
		chosen = False
		while not chosen:
			try:
				choice = raw_input(hint).strip()[0].lower()
			except (EOFError,KeyboardInterrupt):
				choice = 'q'
				
			print '\n you have picked: [%s] '% choice
			
			if choice not in 'neq':
				print 'not valid option, try again'
			else:
				chosen =  True

		if choice == 'q':
			done = True
			print login_db
			print 'over'
		if choice == 'n':
			newuser()
		if choice == 'e':
			olduser()

if  __name__ == '__main__':
	showmenu()
			
