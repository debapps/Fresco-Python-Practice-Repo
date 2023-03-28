import collections
import string
from typing import Counter

#
# Complete the 'collectionfunc' function below.
#
# The function accepts following parameters:
#  1. STRING text1
#  2. DICTIONARY dictionary1
#  3. LIST key1
#  4. LIST val1
#  5. DICTIONARY deduct
#  6. LIST list1
#

def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):

    # Create a dictionary with the count of the words in text1.
    # - The words must be the key, and the count must be the value.
    # - Print the dictionary sorted by the key.

    wordList = sorted(text1.split(' '))
    wordCounter = dict()

    for word in wordList:
        wordCounter.update({word : wordList.count(word)})

    print(wordCounter)

    # Create a Counter object using dictionary1.
    # Substract the values of the counter object from the respective values
    # specified in the 'deduct' dictionary.
    # Convert the counter object into a dictionary and print the same.

    countObj1 = Counter(dictionary1)
    countObj2 = Counter(deduct)

    countObj1.subtract(countObj2)
    print(dict(countObj1))

    # Create a ordered dictionary with key1 values as key and val1 values as value.
    # - Delete the key in the ordered dictionary using the second value from key1.

    tempdict = Counter()
    idx = 0
    while idx < len(key1):
        tempdict.update({key1[idx]: val1[idx]})
        idx += 1

    del tempdict[key1[1]]

    # Reinsert the second values from key1 as key and val1 as value into the ordered dictionary.
    # - Convert the ordered dictionary into normal dictionary and print the same.

    tempdict.update({key1[1]: val1[1]}) 
    print(dict(tempdict))

    # Create a default dictionary that has 'even' and 'odd' keys.
    # - The keys must have the list1 as their respective values.
    # - Extract the even and odd numbers from the list.
    # - Print the default dictionary as a normal dictionary.

    evenOddDict = {}
    evenList = []
    oddList = []

    for item in list1:
        if item % 2 == 0:
            evenList.append(item)
        else:
            oddList.append(item)
    
    if len(oddList) > 0:
        evenOddDict.update({'odd': oddList})
    
    if len(evenList) > 0:
        evenOddDict.update({'even': evenList})

    print(evenOddDict)

    

if __name__ == '__main__':
    collectionfunc("how many times does each word show up in this sentence word times each each word", 
                   {1: 3, 2: 4, 12: 2, 14: 6},
                   ['a', 'b', 'c'],
                   [1, 2, 3],
                   {1: 0, 14: 2},
                   [1, 3, 5, 7, 9, 10])
