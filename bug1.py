#!/usr/bin/env python

num_str =  raw_input('Enter a  number: ')

num_num =  int(num_str)

a_list  =  range(1,num_num+1)

print a_list
print 'BEFORE:', 'a_list'

i = 0

while i < len(a_list):
	
	if num_num % a_list[i] == 0:
		a_list.insert(i,'dot')		
#		del a_list[i]

	i = i + 1
	if len(a_list) >= 50:
		
		break
	

print 'AFTER:',a_list
