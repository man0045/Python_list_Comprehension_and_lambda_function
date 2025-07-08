# walkthrough this it consist of each varient and variable process of python list comprehension

# list comprehension: it is concise way of creating list using single line of code
# it consist of three parts: expression, for loop and if condition
# expression: it is the value that we want to assign to the new list
# for loop: it is used to iterate over the list
# if condition: it is used to filter the list
# example of list comprehension

# 1: without condition
# to find the square of each number in the list
squares = [x for x in range(5)]
print(squares)  # output: [0, 1, 4, 9,16]


# with condition if
# filter item using if condition
# example 2: # to find the square of each number in the list that is greater than 3
events = [x*x for x in range (5) if x>3]
print(events)  # output: [9, 16]


# example 3: # to find the square of each number in the list that is divisible by 2
preevents = [x*x for x in range(5) if x%2 == 0]
print(preevents)  # output: [0, 4]

#with if else condition
# //the syntax is like
# ['jo print krna hoga whi likh do' if what ever operation u want to perform else 'jo print nhi krna hoga' for x in range(jo bhi value dalni hai)]
# choose the value based oon condition
#example 4 find the number in the list that is even or odd

check = ['even' if x%2 == 0 else 'odd' for x in range(5)]
print(check)  # output: ['even', 'odd', 'even', 'odd', '
# example 5: find the number in the list that is greater than 3 or less than
labels = ['gtrater than 3' if x > 3 else 'less than 3' for x in range(5)]
print(labels)  # output: ['less than 3', 'less than 3', '......]

# when we work with multiple if condition the syntax is bit of change
# example 6: find the number in the list that is no is divisible by 2 and 3
nums = [x for x in range(10) if x%2==0 and x%3 ==0]
print(nums)
# Nested list comprehension
# 2d matrix flattening or building
# flattening of matrix
matrix = [[1,2],[3,4],[5,6]]
flat = [item for row in matrix for item in row]
print(flat)  # output: [1, 2, 3, 4, 5, 6]
# how it is working let deeply dive
# it is working like this
# matrix is like  this --> [[1,2],[3,4],[5,6]] so it contains 3 orows
# row[0] = [1,2]
# row[1] = [3,4]
# row[2] = [5,6]
# so it is iterating over each row and then each item in the row and then it is assigning
# meaning[item for row in matrix for item in row] is like
# flat = []
# for row in matrix:
#     for item in row:
#         flat.append(item)
# so coclusion comes 
# [jise print krna hai than for row in matrix for item in row] is like
# suppose if we reverse the order of the list
# like this [row for item in row for item in matrix] is like to throw error NameError, row used before being defined

# another example
# Rectangular matrix 
matrix = [[10, 20, 30], [40,50], [60,70,80]]
new = [item for row in matrix for item in row]
print(new)
# output: [10, 20, 30, 40, 50, 60]
# so it is working like this
# lets start with empty matrix
matrix = [[1,2], [], [2, 4], [], [5, 6]]
acc= [item for row in matrix for item in row]
print(acc)
# lets start work with string in  matrix
matrix = [['a', 'b', 'c'], ['d', 'e', 'f'],
          ['g', 'h', 'i'], ['j', 'k', 'l'],
          ['m', 'n', 'o']]
ret = [item for row in matrix for item in row]
print(ret)


# Moving with advanced part of list comprehension
# Using Function Inside 
# lets say we have a list of numbers and we want to square each number in the list

def square(x): x*x
result = [square(x) for x in range(5)]
print(result)
# output: [0, 1, 4, 9, 16]

# List comprehension with strings
# lets say we have a list of strings and we want to convert each string to uppercase
chars = [ch.upper() for ch in 'mannu' if ch not in "aeiou"]
print(chars)
# output: ['M', 'N', 'N', 'U']
# lets say we have a list of strings and we want to convert each string to lowercase
chars = [ch.lower() for ch in 'mannu' if ch not in "aeiou"]
print(chars)
# output: ['m', 'n', 'n']
# lets say we have a list of strings and we want to only vowels from string
chars = [ch for ch in 'mannu' if ch in "aeiou"]
print(chars)
# output: ['a', 'u']

# lets say we have a list of strings and we want to get the ascii consonants from string
chars = [ord(ch) for ch in 'mannu' if ch not in "aeiou"]
print(chars)
# output: [77, 78, 78, 85]
#replace vowel with * , consonenst remain uppercase
char = [ch.upper() if ch not in "aeiou"  else '*' for ch in 'mannu']
print(char)

# filter charecter that are not vowels and not repeated
s = "mannu"
dent = [ch for ch in s if ch not in 'aeiou' and s.count(ch) >=1]
print(dent)

# get index and charecter for consonents
trem = [(i, ch) for i, ch in enumerate("mannu") if ch not in "aeiou"]
print(trem)

# list comprehension with zip() or enumerate()
names = ['a', 'b', 'c']
scores = [90, 80, 70]
combined = [(name, score) for name, score in zip (names, scores)]
print(combined)

# set and dictionary comprehension
# set comprehension
unique = {x%3 for x in range(10)}
print(unique)
# dictionary comprehension
square = {x: x*x for x in range(5)}
print(square)





