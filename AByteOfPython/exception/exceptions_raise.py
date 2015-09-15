__author__ = 'daniloqb'


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast



try:
    text = raw_input('Some text: ')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except (EOFError,KeyboardInterrupt):
    print 'error occurred'
except ShortInputException as ex:
    print 'ShortInputException: The input was {0} long, expected at least {1}'.format(ex.length, ex.atleast)
else:
    print text
