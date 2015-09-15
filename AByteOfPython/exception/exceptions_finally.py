import sys
import time

__author__ = 'daniloqb'

f = None

try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, sys.stdout.flush()
        print 'press crtl+c now.'
        time.sleep(2)

except IOError:
    print 'File not found'
except KeyboardInterrupt:
    print 'Operation canceled'
finally:
    if f:
        f.close()


