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

while True:
    s = f.readline()

    if len(s) == 0:
        break

    print s

f.close()

