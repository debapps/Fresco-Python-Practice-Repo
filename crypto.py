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
    mainList =[]
    
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

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    file = open('key.key', 'rb')
    key = file.read()  # The key will be type bytes
    file.close()
    
    keyval = key

    textencr = str(input()).encode()

    textdecr = str(input()).encode()


    result = encrdecr(keyval, textencr, textdecr)
    bk=[]
    f = Fernet(key)
    val = f.decrypt(result[0])
    bk.append(val.decode())
    bk.append(result[1])

    fptr.write(str(bk) + '\n')

    fptr.close()
