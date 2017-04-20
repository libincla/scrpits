#!/usr/bin/env python
#coding:utf-8
#more details
import argparse

#t1 = ("add_arg",help="add sth to script")
parser =  argparse.ArgumentParser()
parser.add_argument("echo",help="echo sth to the cccccc")
parser.add_argument("add_arg",help="add sth args to script")
args = parser.parse_args()

print args.echo
print args.add_arg
