__author__ = 'daniloqb'


try:
    text = raw_input('Enter some text: ')
except EOFError:
    print 'Why did you do an EOF on me?'
except KeyboardInterrupt:
    print 'You canceled the operation'
else:
    print text

