#!/usr/bin/env python
#coding:utf-8


from multiprocessing import Process,Queue
import os,time,random


def write(q):
	for i in ['a','b','c']:
		print 'Put %s to queue....' % i
		q.put(i)
		time.sleep(random.random())

def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue.' % value

if __name__ == '__main__':
	#�����̴���queue,�����������ӽ���
	q = Queue()
	pw = Process(target=write,args=(q,))
	print q
	pr = Process(target=read,args=(q,))
	#�����ӽ���pw,д��
	pw.start()
	#�����ӽ���pr,����
	pr.start()
	#�ȴ�pw����
	pw.join()
	#pr������������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ
	pr.terminate()

	
