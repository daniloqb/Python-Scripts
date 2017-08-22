__author__ = 'daniloqb'


def checkIndex(key):
    if not isinstance(key,(int,long)):
        raise TypeError

    if key < 0:
        raise IndexError

    print key

class ArithmeticSequence():
    def __init__(self, start=0, step=1):

        self.start = start
        self.step = step
        self.change = {}

    
    def __getitem__(self, key):

        checkIndex(key)

        try: return self.change[key]
        except KeyError:
            return self.start + key *self.step

    def __setitem__(self, key, value):

        checkIndex(key)

        self.change[key] = value



s = ArithmeticSequence(0,5)


print s[6]

s[6]='four'
print s[6]
