#!/usr/bin/python

f = open("pi_million.txt","r");

state = 0
l = []
i = 0
while True:
  c = f.read(2)
  print i
  if c == '':
    break
  p = chr(int(c))
  i = i+2
  if state == 0:
    if p =='K':
      l.append(p)
      state = 1
  elif state == 1:
    if p == 'E':
      l.append(p)
      state = 2
    else:
      print l
      l = []
      state = 0
  elif state == 2:
    if p == 'T':
      l.append(p)
      state = 3
    else:
      print l
      l = []
      state = 0
  elif state == 3:
      txt = "".join(l)
      print 'Found ', txt, 'in position ',i
      break
f.close()
