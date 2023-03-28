# This program calculate the key entry time.
# Story: Each day, employees from an e-commerce company have to type a string of number
# into a console using a 3 x 3 numeric keypad to enter their building. Every day the numbers
# on the keypad are mixed up.
# Use the following rules to calculate total amount of time it takes to type a string:
# 1. It takes 0 second to move their finger to the first key and it takes 0 second to press
#    the key where the finger is located any number of times.
# 2. They can move their finger to one location to any adjacent key in 1 second. Adjacent keys
#    include those on a diagonal.
# 3. Moving to a non-adjacent key is done as a series of moves to adjacent keys.
#    It takes 2 seconds.

MATRIX_SIZE = (3, 3)

# This function returns the indices of an item in a matrix (2D list).


def getMatrixIdx(matrix, item):
    for row in matrix:
        rowIdx = matrix.index(row)
        if item in row:
            colIdx = row.index(item)
            return (rowIdx, colIdx)

# This function returns the adjacent indices of a matrix indice.


def getAdjacentIdices(itemIdx, matSize):

    i, j = itemIdx
    m, n = matSize
    adjIdx = []

    # Get the adjacent indices in straight lines.
    if i > 0:
        adjIdx.append((i-1, j))

    if i+1 < m:
        adjIdx.append((i+1, j))

    if j > 0:
        adjIdx.append((i, j-1))

    if j+1 < n:
        adjIdx.append((i, j+1))

    # Get the adjacent indices in diagonal lines.
    diaIdx = (i+1, j-1)
    if checkValidIdx(diaIdx, matSize):
        adjIdx.append(diaIdx)

    diaIdx = (i+1, j+1)
    if checkValidIdx(diaIdx, matSize):
        adjIdx.append(diaIdx)

    diaIdx = (i-1, j+1)
    if checkValidIdx(diaIdx, matSize):
        adjIdx.append(diaIdx)

    diaIdx = (i-1, j-1)
    if checkValidIdx(diaIdx, matSize):
        adjIdx.append(diaIdx)

    return adjIdx


# Check if valid indices of a mXn matrix.


def checkValidIdx(indx, matSize):
    i, j = indx
    m, n = matSize

    if i < 0 or j < 0 or i >= m or j >= n:
        return False
    else:
        return True

# This function gets the adjacent elements of an element of a matrix.


def getAdjacentItems(matrix, item, matSize):
    itemIdx = getMatrixIdx(matrix, item)
    adjIndx = getAdjacentIdices(itemIdx, matSize)
    adjItems = []

    for indx in adjIndx:
        adjItems.append(matrix[indx[0]][indx[1]])

    return adjItems

# This fuction returns the keypad matrix from the string.


def createKeyMatrix(keypad):
    keyMatrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    i = 0

    for row in range(0, 3):
        for col in range(0, 3):
            keyMatrix[row][col] = int(keypad[i])
            i += 1

    return keyMatrix

# This function takes two inputs:
# s: string to type.
# keypad: a string of 9 digits where each group of 3 digits represents a row on the keypad of
# the day, in order.
# This function returns an integer denoting minimum amount of time (in seconds) it takes
# to type the string s.


def entryTime(s, keypad):
    keyAccessTime = 0
    keyMatrix = createKeyMatrix(keypad)

    firstKey = True
    prevKey = -1

    for item in s:
        key = int(item)

        if firstKey or prevKey == key:
            keyAccessTime += 0
            firstKey = False
        else:
            if key in adjItems:
                keyAccessTime += 1
            else:
                keyAccessTime += 2

        adjItems = getAdjacentItems(keyMatrix, key, MATRIX_SIZE)
        prevKey = key

    return keyAccessTime


def main():

    keypad = input("\nEnter the keypad keys: ")
    s = input("\nThe User Key in value: ")
    print(f"\nThe time for key press: {entryTime(s, keypad)} sec.")


if __name__ == "__main__":
    main()
