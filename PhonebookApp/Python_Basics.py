# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:18:18 2022

@author: Sharek Khan
"""

# This script shows the fundamental Python programming concepts discussed in
# "Starting Out with Python - 4th Edition", By: Tony Gaddis.

# ---------------------------- TABLE OF CONTENTS ---------------------------- #

# CHAPTER 01 - Introduction to Computers and Programming ............ Line:  26 
# CHAPTER 02 - Input, Processing, and Output ........................ Line:  33
# CHAPTER 03 - Decision Structures and Boolean Logic ................ Line:  88
# CHAPTER 04 - Repetition Structures ................................ Line: 104
# CHAPTER 05 - Functions ............................................ Line: 132
# CHAPTER 06 - Files and Exceptions ................................. Line: 212
# CHAPTER 07 - Lists and Tuples ..................................... Line: 300
# CHAPTER 08 - More About Strings ................................... Line: 430
# CHAPTER 09 - Dictionaries and Sets ................................ Line: 519
# CHAPTER 10 - Classes and Object-Oriented Programming .............. Line: 730
# CHAPTER 11 - Inheritance .......................................... Line: 790
# CHAPTER 12 - Recursion ............................................ Line: 826

# -------------------------------- CHAPTER 1 -------------------------------- #

# This is a comment.

# Displays a message with a \n character at the end in the console.
print("Hello World!")

# -------------------------------- CHAPTER 2 -------------------------------- #

# Display a message specifying the ending character.
print("Hello", end='')
print("World!")

# Display a message specifying the separation character.
print("Hello", "World!", sep='')

# Display a message with string concatenation.
print("Hello" + "World!")

# The following showcase escape characters in Python.
newline = "\n"  # Advances to next line
tab = "\t"      # Advances to the next tab position
s_quote = "\'"  # Displays a single quotation
d_quote = "\""  # Displays a double quotation
b_slash = "\\"  # Displays a backslash

# This built-in Python function formats a numerical value.
format(1.2345, '.2f')   # Formats a precision decimal float
format(123456, 'd')     # Formats the number as an integer
format(1234.5678, 'e')  # Formats the number in scientific notation
format(1234.56, ',.2f') # Formats the number with comma separator
format(1234.56, '9.2f') # Formats the number by specifying a minimum field width
format(0.5, '%')        # Formats the number as a percentage

# The following showcases a named constant in Python.
HELLO_WORLD = 1

# The following showcase data types in Python.
integer = 64            # Integer
float_p = 64.0          # Floating point
boolean = True          # Boolean
string = "Hello World!" # String

# This built-in Python function returns the data type of a value/variable.
type(string)

# This built-in Python function reads the input from the keyboard.
user_input = input("Enter a string? ")

# These built-in Python functions convert a string to a numeric type.
int("1")
float("1.0")

# The following showcase mathematical operations in Python.
add = 1 + 1         # Addition
sub = 1 - 1         # Subtraction
mul = 1 * 1         # Multiplication
div = 1 / 1         # Division
int_div = 1 // 1    # Integer division
rem = 1 % 1         # Remainder
exp = 1 ** 1        # Exponent

# -------------------------------- CHAPTER 3 -------------------------------- #

# Conditional statement can check >, >=, <, <=, !=, ==.
if integer < 10:
    # Conditional statement operations can be grouped with 'and', 'or', 'not'.
    if integer < 10 and integer < 10:
        print("True")
    # 'else' condition acts as the opposite resultant condition.
    else:
        print("False")
# 'elif' condition acts a mid tier condition, but NOT the last condition.
elif integer > 10:
    print("False")
else:
    print("-")

# -------------------------------- CHAPTER 4 -------------------------------- #

# A condition controlled loop iterates until a boolean condition has met.
while integer < 10:
    print("Hello World!")
    
# A count controlled loop iterates a specified number of times.
for i in [1, 2, 3, 4, 5]:
    print("Hello World!")
    
# A count controlled loop using the built-in Python function that creates an
# iterable.
for i in range(5):          # 5 iterations
    print("Hello World!")
    
for i in range(0, 5):       # 5 iterations, starting at index 0
    print("Hello World!")
    
for i in range(0, 5, 1):    # 5 iterations, starting at index 0, incrementing by 1
    print("Hello World!")
    
# The following showcases augmented assignment operators in Python.
add += 1    # add = add + 1
sub -= 1    # sub = sub - 1
mul *= 1    # mul = mul * 1
div /= 1    # div = div / 1
rem %= 1    # rem = rem % 1

# -------------------------------- CHAPTER 5 -------------------------------- #

# Function definition with no return type and no parameters specified.
def first_test_function():
    print("Hello World!")
    
# Function call with no arguments specified.
first_test_function()

# Function definition with no return type and a parameter specified.
def second_test_function(message):
    print(message)
    
# Function call with an argument specified.
message = "Hello World!"
second_test_function(message)

# Function definition with no return type and parameters specified.
def third_test_function(message, number):
    print(message)
    print(number)
    
# Function call with a keyword argument specified.
third_test_function(numbe=64, message='Hello World!')

# Function definition with many return types and no parameters specified.
def fourth_test_function():
    message = "Hello World!"
    number = 10
    flag = True
    return message, number, flag  

# Function call with no argument specified.
message, number, flag = fourth_test_function()

# The following is global variable declaration outside a function.
global_variable = "Hello World!"

# Global variable used in a function through built-in Python keyword.
def global_variable_test_function():
    global global_variable
    print(global_variable)
    
# A global constant declaration outside of function.
GLOBAL_CONSTANT = "Hello World!"

# A global constant use inside a function.
def global_constant_test_function():
    print(GLOBAL_CONSTANT)  # Because constants are unique, no keyword required.
    
# This built-in Python keyword imports modules from the Standard Library or
# custom made modules.
import math    # Imports the math module of functions into memory
import random  # Imports the random module of functions into memory

# This random module function returns a random integer.
randint = random.randint(1, 100)    # Parameters specify range of integers.

# This random module function returns a random integer within a specified range.
randrange = random.randrange(100)       # 0-99
randrange = random.randrange(1, 100)    # 1-99
randrange = random.randrange(1, 100, 2) # 1-99 in increments of 2 (1, 3, 5, ... , 99)

# This random module function returns a random floating-point number between
# (0.0 - 1.0).
randfloat = random.random()

# This random module function returns a random floating-point within a
# specified range.
randfloat = random.uniform(1.0, 10.0)

# This random module function specifies the number of seed values to be generated
# with the use of the random module.
random.seed(10)
random.randint(1, 100)  # Returns 10 specific numbers from a range of 1 - 100

# This math module function returns the square root of a number.
sqrt = math.sqrt(16)    # Many more math functions part of math module, see
                        # Chapter 5.9 - The Math Module.

# -------------------------------- CHAPTER 6 -------------------------------- #

# This built-in Python function will open a file for reading only.
in_file = open('textfile.txt', 'r')

# To specify an absolute path use the string literal prefix.
absolute_file = open(r'C:\Users\textfile.txt', 'r')

# This method allows a file object to read all contents of a file.
file_contents = in_file.read()

# This method allows a file object to read a line of a file.
file_line = in_file.readline()

# This method allows a file object to be closed.
in_file.close()
absolute_file.close()

# This built-in Python function will open/create/override a file for writing.
out_file = open('textfile.txt', 'w')

# This method allows a file object to write to a file.
out_file.write("Hello World!\n")

# This method removes/strips a specific characters from the end of the string.
message = "Hello World!\n"
message = message.rstrip('\n')

# This method allows a file object to be closed.
out_file.close()

# This built-in Python function will open/create/append a file for writing.
append_file = open('textfile.txt')

# This method will write to the end of the file (since appended).
append_file.write("Hello World!\n")

# This method allows a file object to be closed.
append_file.close()

# This built-in Python function converts numeric data to a string.
number = "64"
number = str(number)    # Useful to write to files, can NOT write numeric values.

# The following shows a conditional controlled loop reading a file line by line.
loop_file = open("textfile.txt", "r")

while loop_file.readline() != "":
    print(loop_file.readline().rstrip('\n')) # Displays the line of the file
                                             # without the new line character.
loop_file.close()

# The following shows a count controlled loop reading a file line by line.
loop_file = open("textfile.txt", "r")

for line in loop_file:
    print(line.rstrip('\n'))
    
loop_file.close()

import os # Imports the os module of functions into memory

# This os module function deletes a file on disk.
os.remove("textfile.txt")

# This os module function renames an existing file on disk.
os.rename("textfile.txt")

# The following shows exception handling using built-in Python keywords.
try:
    out_file = open("textfile.txt", "w")
    number = int("sixty-four")
except ValueError:
    print("This handles string to numeric conversion errors.")
except IOError:
    print("This handles IO errors with opening non-existent files.")
except ZeroDivisionError as error:
    print(error) # Displays the errors default message.
except:
    print("This handles all exceptions!")
else:
    # 'else' processes logic if NO exceptions are caught.
    out_file.write(str(number) + '\n')
finally:
    # Performs cleanup operations, such as closing files or other resources.
    # Executes whether an exception occurs or NOT.
    out_file.close()

# -------------------------------- CHAPTER 7 -------------------------------- #

# The following creates a list of integers.
numbers = [2, 4, 6, 8, 10]  # Can be list of any data type or object.

# The following creates a list of different data types.
data = ['Hello World!', 64, 1.0]

# This built-in Python function creates a list of multiple objects.
numbers = list(range(5))

# The following shows the reptition operator that makes copies of a list.
numbers = [0] * 5

# The following shows iteration over a list using a count controlled loop.
for n in numbers:
    print(n)
    
# The following shows indexing through elements in a list.
for i in range(len(numbers)):
    print(numbers[i])       # Can use negative indices to reverse through list.

# This built-in Python function returns the length of a sequence.
numbers_len = len(numbers)

# The following shows concatenating lists.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2   # list3 will reference the values of list1 + list2.

list1 += list2          # Augmenteted concatenation appends list2 to list1.

# The following show slicing a list to return a range of values between indexes.
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(days[2:5])        # Returns values from index 2 upto 5.
print(days[:5])         # Returns values from index 0 upto 5.
print(days[2:])         # Returns values from index 2 upto length of list.
print(days[:])          # Returns all the values in list, same as print(days).
print(days[::2])        # Returns all the values from list with index stepped by 2.
print(days[-4:])        # Returns values -4 indexes from length of list upto length of list.

# NOTE: If END index is > scope, Python will use length of list.
# NOTE: If START index is < scope, Python will use 0.
# NOTE: If START index > END index, returns empty list.

# This built-in Python keyword finds an item in a list.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

if 'Mon' in months:     # 'in' operator searches a list for an item and returns a boolean condition.
    print(True)
else:
    print(False)

if 'Mon' not in months: # 'not in' operator searches a list to NOT find an item and returns a boolean condition.
    print(False)
else:
    print(True)
    
# The following shows List methods that allows to modify items in a list.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)       # Adds item to the end of the list.
numbers.index(3)        # Returns index of first element which matches item.
numbers.insert(0, 0)    # Inserts item into list at specified index.
numbers.sort()          # Sorts the list of items in ascending order.
numbers.remove(6)       # Remove first occurence of item from the list.
numbers.reverse()       # Reverses the order of the items in the list.

# This built-in Python function deletes an item from an index.
numbers = [1, 2, 3, 4, 5, 6]
del numbers[4]          # Deletes the element from the specified index.

# These built-in Python functions return the min/max value in a sequence.
numbers = [1, 2, 3, 4, 5]
print(max(numbers))
print(min(numbers))

# The following shows creating a copy of a list.
list1 = [1, 2, 3, 4]
list2 = list1           # list2 now references the list of values as list1.

list1[0] = 99           # This change will also be reflected in list2.

# The following shows creating a unique copy of a list.
list1 = [1, 2, 3, 4]
list2 = []

for item in list1:
    list2.append(item)  # Adds list1 item to list2 per index.
    
list2 = [] + list1      # Can concatenate and empty list with values of list1.

# The following shows creating a multi-dimensional list.
departments = [['Tom', 'Brian'], ['Sue', 'Laura'], ['Max', 'Yvonne']]

# NOTE: 2 dimensional arrays operate having rows & columns.
#       Column 0    Column 1
# Row 0 'Tom'       'Brian'
# Row 1 'Sue'       'Laura'
# Row 2 'Max'       'Yvonne'

# The following shows iterating through a multi-dimensional list.
for row in range(len(departments)):
    for col in range(len(departments[row])):
        print(departments[row][col])

# The following shows creating a Tuple, an immutable sequence.
my_tuple = (1, 2, 3, 4) # Unlike lists, tuples CANNOT be changed.
print(my_tuple)

# NOTE: Working with Tuples == Lists, however the values CANNOT be modified.
# DO SUPPORT iteration, indexing, index() method, len(), min() and max()
# functions, slicing expressions, 'in' and 'not in' operator, and '+' and
# '*' operators.
# DO NOT SUPPORT methods such as append(), remove(), insert(), reverse(),
# and sort().

# The following creates a Tuple with a single element.
my_tuple = (1,)         # my_tuple = (1) creates an integer NOT a Tuple.

# NOTE: Why use tuples, performance (processing tuples is faster), tuples are
#       free of unwanted modification (immutable), certain Python operations
#       require use of tuples over lists.

# These built-in Python functions convert between lists and tuples.
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

my_list = ('a', 'b', 'c')
my_tuple = tuple(my_list)

# -------------------------------- CHAPTER 8 -------------------------------- #

# The following shows iteration on a string.
for char in "Hello World!":
    print(char)
    
# The following shows indexing on a string.
my_string = "Hello World!"
print(my_string[3])     # Returns the 'l' character.
print(my_string[-2])    # Returns the 'd' character.
print(my_string[12])    # Returns an IndexError Exception, valid range 0-11.
print(my_string[-13])   # Returns an INdexError Exception, valid range (-1)-(-12).

# This built-in Python function can return the length of a string.
my_string = "Hello World!"
print(len(my_string))   # Returns the length of 12 characters.

# The following shows string concatenation.
red_string = "red"
green_string = "green"
blue_string = "blue"

pixel_colors = red_string + green_string
pixel_colors += blue_string

# NOTE: Strings are immutable, their value CANNOT change or be modified, however
# when assigning a new value the variable simply references a different memory
# location for the value and Python removes the previous reference from memory.

# The following shows string slicing.
my_string = "Hello World!"
print(my_string[2:5])        # Returns characters from index 2 upto 5.
print(my_string[:5])         # Returns characters from index 0 upto 5.
print(my_string[2:])         # Returns characters from index 2 upto length of string.
print(my_string[:])          # Returns all characters in the string, same as print(my_string).
print(my_string[::2])        # Returns all characters from string with index stepped by 2.
print(my_string[-4:])        # Returns characters -4 indexes from length of string upto length of string.

# NOTE: If END index is > scope, Python will use length of string.
# NOTE: If START index is < scope, Python will use 0.
# NOTE: If START index > END index, returns empty string.

# This built-in Python keyword finds an item in a string.
my_string = "Hello World!"

if 'Hello' in my_string:    # 'in' operator searches a string for the item.
    print(True)             # Returns a boolean condition.
else:
    print(False)

if 'Ace' not in my_string:  # 'not in' operator searches a string to NOT find an item.
    print(False)            # Returns a boolean condition.
else:
    print(True)
    
# The following shows String methods that perform various operations.
my_string = "Hello World!"
my_string.isalnum()         # Returns True if string consists of alphanumeric characters.
my_string.isalpha()         # Returns True if string ONLY consists of alphabetic characters.
my_string.isdigit()         # Returns True if string ONLY consists of numeric characters.
my_string.islower()         # Returns True if string ONLY consists of lowercase characters.
my_string.isspace()         # Returns True if string ONLY consists of white space.
my_string.isupper()         # Returns True is string ONLY consists of uppercase characters.

my_string.lower()           # Returns a copy of the string with all lowercase characters.
my_string.lstrip()          # Returns a copy of the string with all leading whitespace characters removed.
my_string.lstrip('')        # Returns a copy of the string with all leading instances of the specified character removed.
my_string.rstrip()          # Returns a copy of the string with all trailing whitespace characters removed.
my_string.rstrip('')        # Returns a copy of the string with all trailing instances of the specified character removed.
my_string.strip()           # Returns a copy of the string with all leading and trailing whitespace characters removed.
my_string.strip('')         # Returns a copy of the string with all leading and trailing instances of the specified character removed.
my_string.upper()           # Returns a copy of the string withh all uppercase characters.

my_string.endswith("")      # Returns True if the string ends with specified substring.
my_string.find("")          # Returns the lowest index in the string where the specified substring is found.
my_string.repace("", "")    # Returns a copy of the string with all previous instances of substring replaced with the new substring.
my_string.startswith("")    # Returns True is the string starts with specified substring.

# The following shows modifying a string using the repitition operator.
my_string = "Hello World!" * 5
print(my_string)            # Displays the string by the multiple specified.

# The following shows String method that splits a string into a List.
my_string = "The quick brown fox jumps over the lazy dog."
my_list = my_string.split() # By default separator is an empty space.

date = "MM/DD/YYYY"
my_list = date.split('/')   # Returns a list of substrings split by '/' character.

# -------------------------------- CHAPTER 9 -------------------------------- #

# The following shows the creation of a Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

# NOTE: Dictionary objects are divided into a (key:value) pair. The key must be
# immutable objects (unique, unchaged), values can be objects of any type.

# NOTE: Elements in Dictionary objects are not stored in any particular order.
# Hence Dictionary objects are not sequences that implement sequential order.

# The following shows retrieving a value from a Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
print(phonebook['Chris'])   # Returns the value paired with the key.
print(phonebook['Katie'])
print(phonebook['Katie'])
print(phonebook['Kathryn']) # Returns an error, since key doesn't exist.

# NOTE: You CANNOT use numeric index to reference an element in a Dictionary
# object, MUST use a key.
# NOTE: String comparisons are case sensitive, phonebook['katie'] and
# phonebook['Katie'] are not the same.

# These built-in Python keywords find key's in a Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

if 'Chris' in phonebook:    # 'in' operator searches a dictionary for the key.
    print(phonebook['Chris'])
else:
    print('Not found.')
    
if 'Chris' not in phonebook:# 'not in' operator searches a dictionary to NOT find the key.
    print('Not found.')
else:
    print(phonebook['Chris'])
    
# The following shows adding elements to an existing Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
phonebook['Kathryn'] = '555-4444'   # Adds a new element to Dictionary object.
phonebook['Chris'] = '555-5555'     # Modifies existing element in Dictionary object.

# NOTE: You CANNOT have duplicate keys in a Dictionary object, assigning a new
# value to an existing key overrides the previous value.

# This built-in Python keyword helps delete elements in an existing Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
del phonebook['Chris']      # Delete's the key and its value from the Dictionary object.
del phonebook['Tom']        # Returns an error, since key doesn't exist.

# NOTE: Always check if a key exists within the Dictionary object before adding/
# modifying/deleting it.

# This built-in Python function returns the number of elements in a Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
print(len(phonebook))

# The following shows mixing data types in Dictionary objects.
test_scores = {'Chris':[88, 92, 97], 'Katie':[89, 95, 98], 'Joanne':[78,75,82]}
print(test_scores['Chris'])

mixed_data = {'abc':123, 313:'yadda yadda', (6,1,9):[0,0,7]}

# The following shows an empty Dictionary object being created.
phonebook = {}
phonebook['Chris'] = '555-1111'
phonebook['Katie'] = '555-2222'
phonebook['Joanne'] = '555-3333'

# This built-in Python function will also create an empty Dictionary object.
phonebook = dict()

# The following shows iteration over a Dictionary object.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

for key in phonebook:
    print(key)              # Displays the active key in the Dictionary object.
    print(phonebook[key])   # Displays the value paired with the active key in 
                            # the Dictionary object.

# The following shows Dictionary methods that perform various operations.
phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
phonebook.clear()           # Clears the contents of a Dictionary.
phonebook.get('','default') # Returns the value associated with the specified key,
                            # if NOT found; returns the default value specified.
phonebook.items()           # Returns all the keys in a Dictionary and their
                            # associated values as a sequence of Tuples.
phonebook.keys()            # Returns all the keys in a Dictionary as a type of
                            # sequence.
phonebook.pop('','default') # Returns the value associated with the specified
                            # key and removes that key-value pair from the Dictionary,
                            # if NOT found; returns the default value specified.
k,v = phonebook.popitem()   # Returns a randomly selected key-value pair from
                            # the Dictionary and removes that pair. Can utilize
                            # multiple assignment for pair.
                            # NOTE: Returns error if Dictionary is empty.
phonebook.values()          # Returns all the values in the Dictionary as a type
                            # of sequence.

# This built-in Python function creates an empty set.
my_set = set()
my_set = set(['a','b','c']) # Sets only accept iterable elements such as lists,
my_set = set(('a','b','c')) # tuples, or a string.
my_set = set('abc')

# NOTE: All elements in a set must be unique, no two elements can have the same
# value.
# NOTE: Sets are unordered.
# NOTE: Elements stored in a set can be of different data types.

# This built-in Python function returns the number of elements in a set.
my_set = set([1, 2, 3, 4, 5])
print(len(my_set))

# The following shows set methods that perform modifying operations.
my_set = set()
my_set.add(1)               # Adds a specified element to a set.
my_set.add(2)
my_set.add(3)
my_set.add(2)               # WON'T add duplicate element.
my_set.update([4, 5, 6])    # Adds a group of elements to a set as an iterable.
my_set.remove(2)            # Removes an element from the set. Returns an error
                            # if element is NOT found.
my_set.remove(2)            # Removes an element from the set. Returns no error.
my_set.clear()              # Clears all the elements in a set.

# The following shows iteration over sets.
my_set = set([1, 2, 3, 4, 5])

for val in my_set:
    print(val)
    
# These built-in Python keywords find elements in a set.
my_set = set([1, 2, 3, 4, 5])

if 2 in my_set:         # 'in' operator searches for the element in the set.
    print(True)
else:
    print(False)

if 2 not in my_set:     # 'not in' operator searches to whether element DOESN'T exist in set.
    print(False)
else:
    print(True)
    
# The following shows a Set method that creates a union of 2 sets.
set1 = set([1, 2, 3])
set2 = set([4, 5, 6])
set3 = set1.union(set2)     # Unifies both sets in a new set.

set3 = set1 | set2          # Alternate approach to unify sets using '|'.

# The following shows a Set method that creates an intersection of 2 sets.
set1 = set([1, 2, 3])
set2 = set([4, 5, 6])
set3 = set1.intersection(set2)  # Intersects boths sets in a new set.

set3 = set1 & set2              # Alternate approach to intersecting sets using '&'.

# The following shows a Set method that finds the difference between two sets.
set1 = set([1, 2, 3])
set2 = set([4, 5, 6])
set3 = set1.difference(set2)    # New set is the difference of two different sets.

set3 = set1 - set2              # Alterate approach to finding the difference
                                # between sets using '-'.

# The following shows a Set method that finds the symmetric difference of sets.
set1 = set([1, 2, 3])
set2 = set([4, 5, 6])
set3 = set1.symmetric_difference(set2)  # Finds the symmetric difference of two sets.

set3 = set1 ^ set2                      # Alternate approach to finding the symmetric
                                        # difference of sets using '^'.

# The following shows a Set method that finds subsets and supersets.
set1 = set([1, 2, 3, 4])
set2 = set([2, 3])
print(set2.issubset(set1))      # Returns whether the called set is subset to the
                                # passed set as a boolean value.
print(set2 <= set1)             # Alternate approach to finding subset using '<='.

print(set1.issuperset(set2))    # Returns whether the called set is super to the
                                # passed set as a boolean value.
print(set1 >= set2)             # Alternate approach to finding superset using '>='.

# The following shows object serialization in Python using the 'pickle' module.
import pickle

# The following shows pickle module functions opening a file for binary writing.
outfile = open('phonebook.dat', 'wb')
phonebook = {'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}

# NOTE: You can serialize/pickle any type of object, including lists, tuples,
# dictionaries, sets, strings, integers, and floating-point numbers.

pickle.dump(phonebook, outfile) # Serializes the object into the file as stream of bytes.
outfile.close()                 # Closes the file.

# The following shows pickle module functions opening a file for binary reading.
infile = open('phonebook.dat', 'rb')

# NOTE: You can unserialize/unpickle any type of object from the file.

phonebook = pickle.load(infile) # Unserializes the object from the file into a
                                # dictionary object.
print(phonebook)                # Display the elements of the dictionary object.
infile.close()                  # Closes the file.

# NOTE: Reading past the end of the file will cause the load() function to raise
# an EOFError.

# -------------------------------- CHAPTER 10 -------------------------------- #

# This built-in Python keyword defines a class.
class Coin:
    # The initializer method is a special Python class method that initializes
    # the data attributes of the class on an object instantiation.
    def __init__(self):
        self.sideup = "Heads"
        
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
    
    # This defined method will act as an accessor method for hidden data attributes.
    def get_sideup(self):
        return self.sideup
    
# NOTE: The 'self' parameter is required in every method of a class. This will
# reference the specific object that the method is supposed to operate on.
# NOTE: It's NOT requried to call the parameter 'self', though it is done to
# conform to standard practice.

# NOTE: The '__init__' method is usually the first method inside a class
# definition.

# The following shows object instantiation using a custom class.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()
    
    # Display the side of the coin.
    print(my_coin.get_sideup())
    
    # Toss the coin.
    my_coin.toss()
    
    # Display the side of the coin.
    print(my_coin.get_sideup())

# Call the main function.
main()

# The following shows defining a private data attribute.
class Coin:
    def __init__(self):
        self.__sideup = "Heads" # Using '__' as prefix to data attribute makes
                                # them hidden to code outside the class.

# NOTE: It's good practice to store classes in their own modules, then simply
# import the module when operation of that specific class is needed.

# The following shows the Python special method defined in classes.
class Coin:
    def __str__(self):
        return  ""      # The '__str__' method returns a string indicating the
                        # object's state. Is executed when the object is passed
                        # into Python's built-in IO function 'print()'.

# -------------------------------- CHAPTER 11 -------------------------------- #

# The following shows inheritance within Python.
# Defining a super class.
class Automobile:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        
# Defining a sub class.
class Car(Automobile):
    def __init__(self, make, model):
        Automobile.__init__(self, make, model)

# The following shows polymorphism within Python.
# Define a super class.
class Mammal:
    def __init__(self, species):
        self.__species = species
        
    def make_sound(self):
        print("Grrr...")

# Define a sub class.
class Dog(Mammal):
    def __init__(self, species):
        Mammal.__init__(self, "Dog")
    
    def make_sound(self):
        print("Woof! Woof!")    # Overrides the super class method.

# This built-in Python function accepts an object and a class type. Returns a
# boolean value if the object is an instance of the class type.
print(isinstance("Bear", Mammal))   # Would return false as a String is NOT an
                                    # instance of class type.

# -------------------------------- CHAPTER 12 -------------------------------- #

# The following shows recursion within Python.
def message():
    print("This is a recursion function.")
    message()

# The folowing shows recursion for problem solving within Python.   
def factorial(n):
    # Factorial of a number is...
    # n = 0 then n! = 1
    # n > 0 then n! = 1 x 2 x 3 x ... x n - 1
    
    if n == 0:          # Considered base case, NO recursion required.
        return 1
    else:               # Considered recursive case, recurses until base case is reached.
        return n * factorial(n - 1)

# The following shows an indirect recursive function call, previous were direct
# recursive function calls.
def functionA():
    functionB()

def functionB():
    functionA()
    
# NOTE: Any algorithm can be coded with recursion or a loop.
# NOTE: Recursive functions are less efficient and creates system overhead.
# NOTE: Recursion is best used for solving smaller problems that can be broken down.
