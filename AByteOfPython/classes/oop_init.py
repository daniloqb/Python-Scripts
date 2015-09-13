__author__ = 'daniloqb'

class Person():

    # init e o construtor da classe, como em outras linguagens
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name

Person('Swaroop').say_hi()

