import random


__author__ = 'daniloqb'

class Fibs():
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a

    def __iter__(self):
        return self


class Rannum():

    def __init__(self,num=10):
        self.num = num
        self.count = 1

    def next(self):
        if self.count > self.num: raise StopIteration
        else:
            self.count +=1
            return random.randint(0,100)
    def __iter__(self):
        return self



r = Rannum(2)


for n in r:
    print n

print

r = Rannum(3)

print list(r)

f = Fibs()
for i in range(1,5):
    print f.next()
