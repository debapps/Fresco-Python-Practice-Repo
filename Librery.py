#
# Complete the 'Library' function below.
#

import math


def Library(memberfee, installment, book):

    # print(memberfee,installment,book)

    if installment > 3:
        raise ValueError('Maximum Permitted Number of Installments is 3')

    if installment == 0:
        raise ZeroDivisionError('Number of Installments cannot be Zero.')
    else:
        installmentAmount = float(math.ceil(memberfee / installment))
        # print(installmentAmount)
        print('Amount per Installment is  {}'.format(
            round(installmentAmount, 1)))

    HarryPotterNovels = [
        'Philosophers Stone',
        'Chamber of Secrects',
        'Prisoner of Azkaban',
        'Goblet of Fire',
        'Order of Phoenix',
        'Half Blood Prince',
        'Deathly Hallows 1',
        'Deathly Hallows 2'
    ]
    BookTitleList = []
    for booktitle in HarryPotterNovels:
        BookTitleList.append(booktitle.upper())

    # print(BookTitleList)
    if book.upper() not in BookTitleList:
        raise NameError('No such book exists in this section')
    else:
        print('It is available in this section')
