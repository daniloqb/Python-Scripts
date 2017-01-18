#!/usr/bin/python


f = open("pi_billion.txt","r");
f.read(2)

txt = raw_input("Texto a ser procurado: ")
t = len(txt)
index = 0
i = 0
while True:
  c = f.read(2)
  i +=2
  if c == '':
    break
  p = chr(int(c))
  if p == txt[index]:
    index += 1
    print p,
  else:
    if index > 0:
      print
    index = 0
  if index >=t:
    print
    print "O texto ",txt, " doi encontrado na posicao: ",i
    break


f.close()
