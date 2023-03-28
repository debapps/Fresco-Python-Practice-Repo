#!/bin/python3

import math
import os
import random
import re
import sys


from cryptography.fernet import Fernet
#
# Complete the 'encrdecr' function below.
#
# The function is expected to return a LIST.
# The function accepts following parameters:
#  1. STRING keyval
#  2. STRING textencr
#  3. Byte-code textdecr
#


def encrdecr(keyval, textencr, textdecr):
    # Declare mainList.
    mainList = []

    # value of key is assigned to a variable
    f = Fernet(keyval)

    # the plaintext is converted to ciphertext and append it in mainList.

    cipherText = f.encrypt(textencr)
    mainList.append(cipherText)

    # Decrypt the byte-code in 'textdecr' and append it into mainList.

    plainText = f.decrypt(textdecr)
    mainList.append(plainText.decode())

    return mainList


if __name__ == '__main__':

    keyfile = open('file/key.txt', 'rb')
    keyval = keyfile.read()
    keyfile.close()

    textencr = b'Welcome to Cryptography.'
    textdecr = b'gAAAAABkItff7iJ6QuGYP5MXtNPgyA1W5h2yU2voO0wtq96jR98M6CxrCrvl0XCO1s4HBl2ArZo9mEm_nn2Zsw9OmmIkIUa8sz1FUiwTNsEKgS06gBZPKv8Mcy1OH835428s5BoW3hCca7yMtwvoKgNlll9bnjaYrBrVKSP0BnKGhAaFv8G3HxE='
    result = encrdecr(keyval, textencr, textdecr)
    print(result)
