#!/usr/bin/env python
#coding:utf-8
#more details
import argparse

#t1 = ("add_arg",help="add sth to script")
parser =  argparse.ArgumentParser()
parser.add_argument("square",help="num square ",type=int)
args = parser.parse_args()

print args.square ** 2
