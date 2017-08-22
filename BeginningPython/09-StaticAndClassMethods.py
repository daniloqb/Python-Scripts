__author__ = 'daniloqb'

__metaclass__ = type


class OldMyClass:
    def smeth():
        print 'This is a static method.'

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'This is a class method of', cls

    cmeth = classmethod(cmeth)


class NewMyClass:
    @staticmethod
    def smeth():
        print 'This is a static method.'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls


OldMyClass.smeth()

print '\n'

OldMyClass.cmeth()

print '\n'

NewMyClass.smeth()
print '\n'
NewMyClass.cmeth()