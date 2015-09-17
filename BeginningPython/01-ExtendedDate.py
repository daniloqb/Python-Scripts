__author__ = 'daniloqb'





wrong_date = False

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
          'september', 'october', 'november', 'december']

months_with_31_days = [1,3,5,7,8,10,12]

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
        if day > 0 and day <=31:
            break

    if day > 30 and month not in months_with_31_days:
        wrong_date = True

    if month == 2:
        if day > 29:
            wrong_date = True

        if day == 29:
            if  year % 2 !=0 or year % 4 !=0:
                wrong_date = True


    if wrong_date:
        print 'Wrong date!'
        wrong_date = False
    else:
        print '{} {}{}, {}'.format(months[month - 1], day, endings[day - 1], year)



