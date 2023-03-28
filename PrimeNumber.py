#
# Complete the 'primegenerator' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER val
#

def primegenerator(num, val):

    # The num is the inclusive range of the prime number list.

    primeList = []
    for number in range(2, num + 1):
        isPrime = True
        for i in range(1, number):
            if number % i == 0 and i != 1:
                isPrime = False

        if isPrime:
            primeList.append(number)

    # if the val = 1, return the odd indices of the prime number list,
    # else if the val = 0, return the even indices of the prime number list.

    if val:
        for index in range(len(primeList)):
            if index % 2 == 0:
                yield primeList[index]
    else:
        for index in range(len(primeList)):
            if index % 2 != 0:
                yield primeList[index]


for number in primegenerator(21, 0):
    print(number, end=' ')
