#!/usr/bin/python

import sys

l = [x for x in range(2,int(sys.argv[1])+1)]

for i,v in enumerate(l):
	for x,y in enumerate(l):
		if(v!=y and y%v ==0):
			l.remove(y)

print l
