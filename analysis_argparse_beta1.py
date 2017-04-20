#!/usr/bin/env python
#coding:utf-8
#more details
import argparse

parser =  argparse.ArgumentParser()
parser.add_argument("echo",help="echo sth to the cccccc")

args = parser.parse_args()

print args.echo
