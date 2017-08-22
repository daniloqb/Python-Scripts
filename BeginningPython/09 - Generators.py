__author__ = 'daniloqb'


def recgen(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in recgen(sublist):
                yield element

    except TypeError:
        yield nested

nested = [[1, 2], [3, 4], [5], [6, [7, 8]]]

for num in recgen(nested):
    print num
