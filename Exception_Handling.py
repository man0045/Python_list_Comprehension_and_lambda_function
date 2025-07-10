# exception handling theory and each and 
# every possible intution idea of understanding variation of exception handling and its types

# Exception handling : Exception handling is a way to manage an event, which occurs 
# during the execution of a program , that disrupts the normal flow of the program’s instructions.
# Exception handling in a python is a way to manage errors and
# unexpected events in our program gracefully. without crashing the applications. 
# instead of stopping the execution when an error occurs , we can catch it and respond it 

# Basic syntax of exception handling in python is as follows:
try:
 # code that might raise an exception
except ExceptionType:
 # code to handle the exception:
else:
 # code to be executed if no exception occurs
finally:
 # code to be executed regardless of the exception

# Types of Error
# 1: ZeroDivivsionError --> Divided by zero
# 2: TypeError --> When we try to perform an operation on a wrong type of data
# 3: ValueError --> When a function receives an argument with an incorrect value
# 4: IndexError --> When we try to access an index that does not exist in a list
# 5: KeyError --> When we try to access a key that does not exist in a dictionary
# 6: NameError --> When we try to use a variable that has not been defined
# 7: SyntaxError --> When there is an error in the syntax of the code
# 8: AttributeError --> When we try to access an attribute that does not exist in an object
# 9: ImportError --> When we try to import a module that does not exist
# 10: ModuleNotFoundError --> When we try to import a module that does not exist
# 11: Run TimeError --> When there is an error in the code that occurs during the execution of the code
# 12: MemoryError --> When the program runs out of memory
# 13: RecursionError --> When a function calls itself too many times and exceeds the maximum


# Types or Varient
# 1. Single Exception
try:
 x = 5/0
except ZeroDivisionError:
 print("Error: Division by zero is not allowed")

#2.  Multiple Specific Exception
try:
 a = int('abc')
 b=[1 , 2, 3, 4]
 print(b[5])
except ValueError:
 print("Invalid input")
except IndexError:
 print("Index out of range")

 # Catching  All Exception
def risky_code(a):
  print(a/0)
try:

 risky_code(5)
except Exception as e:
  print("Error Occured", e)

# 4. Using else Block
try:
 print("No error")
except ZeroDivisionError:
 print("Error")
else:
 print('code ran successfully')
# Using finally Block
try:
 x = 5/1
except ZeroDivisionError:
 print('Error')
finally:
 print("this always run")


# raising your own exception
def validate_age(age):
 if age < 0:
  raise ValueError('Age cant be negative')
validate_age(-2)

# Custom Exception Class
class myError(Exception):
 pass
try:
 raise myError("this is custom Erorr")
except myError as e:
 print(e)
# Use-Cases Based Questions (Interview-Oriented)
# Q1. What is the difference between try-except and try-finally?
# try-except handles the error.

# finally runs regardless of error.

# Q2. How do you catch multiple exceptions in one block?

# try:
#     risky_code()
# except (ValueError, IndexError) as e:
#     print(e)
# Q3. What is the purpose of the else block in exception handling?
# It runs if the try block does not raise any exception.

# Q4. How can you define a custom exception?
# By creating a class that inherits from Exception.

# Q5. What's the difference between raise and assert?
# raise is used to throw exceptions.

# assert is used to validate conditions (and throws AssertionError if False).

# assert 2 + 2 == 4  # Passes
# assert 2 + 2 == 5  # Raises AssertionError
# 🧪 Practice-Oriented Examples
# ✅ Basic
# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
# except ValueError:
#     print("Not a valid number")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# ✅ File Handling

# try:
#     with open('file.txt', 'r') as f:
#         data = f.read()
# except FileNotFoundError:
#     print("File not found!")
# 📌 Summary
# Component	Description
# try	Code that might raise an error
# except	Handles specific error
# else	Runs if no error occurred 
# finally	Always runs