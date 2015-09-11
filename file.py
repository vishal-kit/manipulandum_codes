#!/usr/bin/env python

f=open("out.txt",'r')
if (f.closed):
	print '-1'	
print f.read()

