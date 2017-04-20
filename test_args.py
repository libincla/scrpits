#!/usr/bin/env python

def testit(func,*List,**Dict):
	
	try:
		rev = func(*List,**Dict)
		res = (True,rev)
	except Exception,diag:
		res = (False,str(diag))

	return res

def test():
	funcs = (int,long,float)
	vals =  (1234,12.34,'1234','12.34')
	
	for eachFunc in funcs:
		print '_' * 20
		for i  in vals:
			rev = testit(eachFunc,i)
			
			if rev[0]:
				print '%s(%s) = '%\
				(eachFunc.__name__,'eachval'),i[1]
			else:
				print '%s(%s) = FAILED:' %\
				(eachFunc.__name__,'eachval'),i[1]

if __name__ == '__main__':
	test()
