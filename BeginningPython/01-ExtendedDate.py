__author__ = 'daniloqb'


class WrongDateException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def printMsg(self):
        print self.msg


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
while True:
    year = raw_input('Year: ')
    if not year: exit()

    year = int(year)

    while True:
        month = int(raw_input('Month (1-12): '))
        if month > 0 and month <= 12:
            break

    while True:
        day = int(raw_input('day (1-31: '))
        if day > 0 and day <= 31:
            break

    try:
        if day > 30 and month not in months_with_31_days:
            raise WrongDateException(months[month - 1] + ' has less than 31 days.')

        if month == 2:
            if day > 29:
                raise WrongDateException(months[month - 1] + ' has less than 30 days.')

            if day == 29:
                if year % 2 != 0 or year % 4 != 0:
                    raise WrongDateException(str(year) + ' is not a bisect year, so February has less than 29 days.')
    except WrongDateException as e:
        e.printMsg()
        print
    else:
        print '{} {}{}, {}'.format(months[month - 1], day, endings[day - 1], year)
