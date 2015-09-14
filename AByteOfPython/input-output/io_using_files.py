__author__ = 'daniloqb'

poem = '''\
Programing is fun
When the work is done
if you wanna make your work also fun:
    use Python!

'''


f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt')

s = f.readline()

while s:
    print s
    s = f.readline()
