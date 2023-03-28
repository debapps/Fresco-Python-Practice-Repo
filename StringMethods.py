#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):

    # Remove all special characters from para specified in special1 and save them
    # in the variable word1.

    word1 = para
    for spch in special1:
        word1 = word1.replace(spch, '')

    # Get the first 70 character from word1, reverse the string, save it in variable rword2,
    # and print it.

    first70charSTR = word1[0:70]
    rword2 = first70charSTR[::-1]
    print(rword2)

    # Remove all the Wide spaces from rword2, join the characters using the special character specified
    # in special2, and print the joint string.

    print(special2.join(rword2.replace(' ', '')))

    # If every string from list1 present in para, then format the print statement as follows:
    stringFound = True

    for item in list1:
        if item not in para:
            stringFound = False
            break

    if stringFound:
        print(f'Every string in {list1} were present')
    else:
        print(f'Every string in {list1} were not present')

    # Split every word from word1 and print the first 20 strings as a list.

    wordList = word1.split(' ')
    print(wordList[0:20])

    # Calculate the less frequestly used words whose count < 3 and print the last 20 less frequent words as
    # a list.

    lessfreqWord = []

    for word in wordList:
        if wordList.count(word) < 3 and word not in lessfreqWord and word != '':
            lessfreqWord.append(word)

    print(lessfreqWord[-20:])

    # Print the last index in word1, where the substring strfind is found.

    print(word1.rfind(strfind))


if __name__ == '__main__':

    para = "The same year Gandhi adopted the Indian loincloth, or short dhoti and, in the winter, a shawl, both woven with +yarn hand-spun on a traditional Indian spinning wheel, or charkha, as a mark of identification with India's rural poor. Thereafter, he lived modestly in a self-sufficient residential community, ate simple vegetarian food, and! undertook long fasts as a means of self-purification and political protest. Bringing anti-colonial nationalism to the common Indians, Gandhi led them in challenging the British-imposed salt tax with the 400 km (250 mi) Dandi Salt March in 1930, and later in calling for the British to Quit India in 1942. He was imprisoned for many years, upon many occasions, in both@ South Africa and India."

    spch1 = ',_!@*%#+'

    spch2 = '*'

    qw1 = ['undertook', 'later', 'martin']

    strf = 'salt'

    stringmethod(para, spch1, spch2, qw1, strf)
