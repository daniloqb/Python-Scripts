#!/usr/bin/python

import sys

def BaseStringToValue(digitString, base):
    print digitString
    output = 0
    if digitString =='':
        output = 0
    else:
        output = int(digitString[len(digitString)-1])
        rs = ''
        for i in range(len(digitString)-1):
            rs += digitString[i]        
       
        vs = BaseStringToValue(rs,base)
        output += int(base) * int(vs)
    return output



digitString = sys.argv[1]
base = sys.argv[2]

print BaseStringToValue(digitString,base)


        
