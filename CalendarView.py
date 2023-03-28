import calendar
import datetime
#
# Complete the 'calen' function below.
#
# The function accepts TUPLE datetuple as parameter.
#


def usingcalendar(datetuple):
    # Get the year, month, date.
    year = datetuple[0]
    month = datetuple[1]
    date = datetuple[2]

    # check if year is leap year, then assign month = 2.
    if calendar.isleap(year):
        month = 2

    # Get the monthly calender.
    calObj = calendar.TextCalendar()
    calStr = calObj.formatmonth(year, month)
    print('\nThe monthly calender:')
    print(calStr)

    # Iterate through the dates of the calendar for a month. Get the last seven dates.
    dateList = []
    for date in calObj.itermonthdates(year, month):
        dateList.append(date)
    print('\nThe last seven dates:')
    print(dateList[-7:])

    # Get the most frequent day name in a month of a year.

    days = []
    for daynum in range(29, 32):
        try:
            days.append(datetime.date(year, month, daynum).strftime('%A'))
        except ValueError:
            break
    print('\nThe most frequent day name:')
    print(days[0])


if __name__ == '__main__':
    usingcalendar(tuple([1730, 7, 1]))
    usingcalendar(tuple([2050, 10, 1]))
