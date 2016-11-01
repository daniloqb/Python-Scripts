#!/usr/bin/python

from  math_funcs import *
import sys

def list_param():
    list = []
    for p in sys.argv:
        list.append(p)
    list.remove(list[0])
    list.remove(list[0])
    return list

function = sys.argv[1]

if function == 'primeFactors':
    print primeFactors(sys.argv[2])

elif function == 'listOfPrimes':
    print listOfPrimes(sys.argv[2])

elif function == 'mmc2':
    list = []
    for p in sys.argv:
        list.append(p)

    list.remove(list[0])
    list.remove(list[0])
    print mmc2(list)

elif function == 'mdc2':
    list = []
    for p in sys.argv:
        list.append(p)

    list.remove(list[0])
    list.remove(list[0])
    
    print mdc2(list)

elif function == 'mdc':
    list = []
    for p in sys.argv:
        list.append(p)
    list.remove(list[0])
    list.remove(list[0])
    res = list[0]
    list.remove(list[0])

    for m in list:
        res = mdc(int(res),int(m))

    print res

elif function == 'mmc':
    list = []
    for p in sys.argv:
        list.append(p)
    list.remove(list[0])
    list.remove(list[0])
    res = list[0]
    list.remove(list[0])

    for m in list:
        res = mmc(int(res),int(m))

    print res
    
elif function == 'addFractions':
    list = list_param()
    f1 = list[0]
    list.remove(list[0])

    for f in list:
        t = addFractions(f1,f)
        f1 = str(t[0])+'/'+str(t[1])

    print f1
