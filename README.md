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

- `tuplevalues`: It is a tuple. It always contains 4 tuples.

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

### CalendarView.py

Import the **calendar** module. Define a function called **'usingcalendar'** which takes following paramerer:

- `datetuple` - a tuple of (year, month, date)

Generate the code based on following conditions:

1. Use the calendar module to build the code.
2. Check whether the given year from the tuple is a leap year.

   - If it is a leap year, assign the month's value as 2 throughout the whole function.

3. Print the monthly calendar for the specified year and month.
4. Use _itermonthdates_ module from the calendar to iterate through date of the specified month and year in the calendar.

   - Print the last 7 days that appear on the calendar of that month as a list.

5. Print the day of the week, which appears the most frequent in the specified month and year as a string.
   - The string can be `Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday`.
   - If there is more than one frequent day, then consider the one that comes first.
     - For example, if there are same number of Mondays and Tuesdays, then consider Monday.

**Input Constraints**

All the values must be integer.

---

### Collection.py

Import the **collections** module. Define a function called **collectionfunc** which takes following six parameters:

- `text1`: A string of sentence.
- `dictionary1`: A dictionary.
- `key1`: A list of keys.
- `val1`: A list of values.
- `deduct`: A distionary.
- `list1`: A list of keys.

Generate print statements based on following conditions:

1. Create a dictionary with the count of words in **text1**.

   - The words must be the keys and the counts must be the values.
   - Print the dictionary sorted by key.

2. Create a counter object using **dictionary1**.

   - Subtract the values of the counter object from the respective values specified in the **deduct** dictionary.
   - Convert the counter object into a dictionary and print it.

3. Create an ordered dictionary with **key1** values as key and **val1** values as value.

   - Delete the key in the ordered dictionary using the second value from **key1**.

4. Reinsert the second values from **key1** as key and **val1** as value into the ordered dictionary.

   - Convert the ordered dictionary into a normal dictionary and print the same.

5. Create a default dictionary that has 'even' and 'odd' keys.
   - The keys must have in the list as their respective values.
   - Extract the 'even' and 'odd' numbers from the **list1**.
   - Print the default dictionary as a normal dictionary.

---

### EncodeDecode.py

Import **fernet** from **cryptography** module. Define a function called **encrdecr** which takes 3 parameters as follows:

- `keyval`: key for encoding and decoding data.
- `textencr`: Text to be encrypted.
- `textdecr`: The byte-code to be decrypted.

Write code based on the following conditions:

1. Declare an empty main list.
2. Encrypt the text in **textencr** and append it to the list.
3. Decrypt the byte-code in **textdecr** and append it to the list.
4. Return the list.

---

### DateAndTime.py

Import **datetime** module. Define a function called **dateandtime** which takes 2 parameters:

- `val`: An Integer value ranges from 1 to 5.
- `tup`: A Tuple, whose values change based on the value of **val**.

**Input Constraints**

- When the value of **val** is 1 or 4, the tuple **tup** will contain three values in the order of (year, month, date) in the form of integers.
- When the value of **val** is 2, the tuple **tup** will contain one single integer value of timestamp.
- When the value of **val** is 3, the tuple **tup** will contain three values in the order of (hours, minutes, seconds) in the form of integers.
- When the value of **val** is 5, the tuple **tup** will contain six values in the order of (year, month, date hours, minutes, seconds) in the form of integers.

Develop the function based on following conditions:

1. Declare an empty list.
2. When the value of **val** is 1:

   - Convert the tuple **tup** into date and append it into the list.
   - Format the date in `%d/%m/%Y` format and append it into the list.

3. When the value of **val** is 2:

   - Convert the tuple **tup** into date and append it into the list.

4. When the value of **val** is 3:

   - Convert the tuple **tup** into time and append it into the list.
   - Extract the hour in 00-12 format and append it into the list.

5. When the value of **val** is 4:

   - Convert the tuple **tup** into date.
   - From the date, extract the weekday (full version) and append it into the list.
   - From the date, extract the month (full version) and append it into the list.
   - From the date, extract the day number of the year (001 - 366) and append it into the list.

6. When the value of **val** is 5:

   - Convert the tuple **tup** into datetime and append it into the list.

7. Return the list.
