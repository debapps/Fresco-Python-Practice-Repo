#!/bin/python3

import math
import os
import random
import re
import sys


import itertools
#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#


def performIterator(tuplevalues):
    # Declare an emplty main list.
    mainList = []

    # Scenario 1: Declare another list. Use the _cycle_ module of the itertools
    # to cycle through the first tuple and append the values to the list.
    cycleList = []
    firstTup = tuplevalues[0]

    LoopCount = 0
    for item in itertools.cycle(firstTup):
        LoopCount += 1
        if LoopCount <= 4:
            cycleList.append(item)
        else:
            break

    mainList.append(tuple(cycleList))

    # Scenario 2: Use the _repeat_ module in the itertools to repeat the first value
    # from the second tuple.
    secondTup = tuplevalues[1]
    repeatList = []
    for item in itertools.repeat(secondTup[0], len(secondTup)):
        repeatList.append(item)

    mainList.append(tuple(repeatList))

    # Scenario 3: Use the _accumulate_ module in the itertools to get the product after
    # each iteration from the third tuple.
    thirdTup = tuplevalues[2]
    accumList = []
    for item in itertools.accumulate(thirdTup):
        accumList.append(item)
    mainList.append(tuple(accumList))

    # Scenario 4: Use the _chain_ module in the itertools to chain all the values of the tuple.
    chainList = []
    for item in itertools.chain(tuplevalues[0], tuplevalues[1], tuplevalues[2], tuplevalues[3]):
        chainList.append(item)
    mainList.append(tuple(chainList))

    # Scenario 5: Use the _filterfalse_ module in the itertools to extract the odd number
    # from the chainned tuple.
    oddList = []
    for item in itertools.filterfalse(lambda x: x % 2 == 0, chainList):
        oddList.append(item)
    mainList.append(tuple(oddList))

    # Convert the main list into a tuple and return it.
    return tuple(mainList)


if __name__ == '__main__':
    tuplevalues = ((1, 10, 5, 2), (8, 48, 14, 63),
                   (59, 47, 49, 22), (19, 60, 1, 40))
    print(performIterator(tuplevalues))
