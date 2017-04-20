#!/usr/bin/env python
#coding:utf-8

import getopt
import sys


optlist,args = getopt.getopt(sys.argv[1:],'abcd:')

print optlist

print 'here are all arguments:======>'
print args
