# Fresco Practice

This repository is created for the solution of Fresco Play Practice questions for Python.

Now, lets have problem statements component wise in the following sections.

## Problem Statement

### KeyEntryTime.py

This program calculate the key entry time.

**Story:** Each day, employees from an e-commerce company have to type a string of number into a console using a 3 x 3 numeric keypad to enter their building. Every day the numbers on the keypad are mixed up.

Use the following rules to calculate total amount of time it takes to type a string:

- It takes 0 second to move their finger to the first key and it takes 0 second to press the key where the finger is located any number of times.
- They can move their finger to one location to any adjacent key in 1 second. Adjacent keys include those on a diagonal.
- Moving to a non-adjacent key is done as a series of moves to adjacent keys. It takes 2 seconds.

---

### PrimeNumber.py

The program generates list of prime numbers for specific range.

The function is expected to return an INTEGER. The function accepts following parameters:

1. INTEGER num - Range of prime number.
2. INTEGER val - if the val = 1, return the odd indices of the prime number list, else if the val = 0, return the even indices of the prime number list.

---

### StringMethods.py

This program implement a string method that takes five input parameters as follows:

- para: A long strings of text.
- special1: A string of special characters.
- special2: A single character.
- list1: A list of string.
- strfind: A single word to find

The string method are implemented as follows:

1. Remove all special characters from para specified in special1 and save them in the variable word1.
2. Get the first 70 character from word1, reverse the string, save it in variable rword2, and print it.
3. Remove all the Wide spaces from rword2, join the characters using the special character specified in special2, and print the joint string.
4. If every string from list1 present in para, then format the print statement as follows:

   - "Every string in {list1} were present"

   **Else**

   - "Every string in {list1} were not present"

5. Split every word from word1 and print the first 20 strings as a list.
6. Calculate the less frequestly used words whose count < 3 and print the last 20 less frequent words as a list.
7. Print the last index in word1, where the substring strfind is found.

---

### PerformIterator.py

Import the **'itertools'** module. Define a function called **'performIterator'**, which takes one parameter.

- tuplevalues: It is a tuple. It always contains 4 tuples.

Generate the code based on following conditions:

1. Declare an emplty main list.
2. Declare another list. Use the _cycle_ module of the itertools to cycle through the first tuple and append the values to the list.

   - Convert the list into tuple and append it to the main list.

3. Use the _repeat_ module in the itertools to repeat the first value from the second tuple.

   - Create a tuple with the values and append it to the main list.

4. Use the _accumulate_ module in the itertools to get the product after each iteration from the third tuple.

   - Create a tuple with the values and append it to the main list.

5. Use the _chain_ module in the itertools to chain all the values of the tuple.

   - Create a tuple with the values and append it to the main list.

6. Use the _filterfalse_ module in the itertools to extract the odd number from the chainned tuple.

   - Create a tuple with the values and append it to the main list.

7. Convert the main list into a tuple and return it.

---

### CalenderView.py

Import the **calender** module. Define a function called **'usingcalender'** which takes following paramerer:

- `datetuple` - a tuple of (year, month, date)

Generate the code based on following conditions:

1. Use the calender module to build the code.
