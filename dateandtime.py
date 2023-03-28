#
# Complete the 'dateandtime' function below.
#
import datetime

# The function accepts INTEGER val as parameter.
# The return type must be LIST.
#


def dateandtime(val, tup):

    # Declare a empty list.
    resultList = []

    # Checks the value of the val and based on it return the resultList.

    if val == 1:
        # Convert the tuple into date in dd/mm/yyyy format.
        d = datetime.date(tup[0], tup[1], tup[2])
        resultList.append(d)
        resultList.append(d.strftime('%d/%m/%Y'))
    elif val == 2:
        # Convert the tuple into date from timestamp.
        d = datetime.date.fromtimestamp(tup[0])
        resultList.append(d)
    elif val == 3:
        # Convert the tuple into time.
        t = datetime.time(tup[0], tup[1], tup[2])
        resultList.append(t)
        resultList.append(t.strftime('%I'))
    elif val == 4:
        # Convert the tuple into the weekday, month and day number of the year.
        d = datetime.date(tup[0], tup[1], tup[2])
        resultList.append(d.strftime('%A'))
        resultList.append(d.strftime('%B'))
        resultList.append(d.strftime('%j'))
    elif val == 5:
        # Convert the tuple into datetime.
        dt = datetime.datetime(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])
        resultList.append(dt)

    return resultList


if __name__ == '__main__':
    val = int(input('\nEnter val: ').strip())

    if val == 1 or val == 4 or val == 3:
        qw1_count = 3
    if val == 2:
        qw1_count = 1
    if val == 5:
        qw1_count = 6
    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input('\nEnter Tuple Item: ').strip())
        qw1.append(qw1_item)

    tup = tuple(qw1)

    ans = dateandtime(val, tup)

    print(f'\nResult: {ans}')
