# encoding=utf-8

import io

__author__ = 'daniloqb'


f = io.open("abc.txt",'wt',encoding='utf-8')

u = u'ônibus'



print u

f.write(u)
f.close()


text = io.open("abc.txt",'r').read()

print text


